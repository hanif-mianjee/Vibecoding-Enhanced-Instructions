#!/usr/bin/env sh
# Vibecoding-Enhanced-Instructions installer
# This script clones the repo into the current directory, prunes some files/folders, and deletes itself.

set -eu

# Config
REPO_URL="${REPO_URL:-https://github.com/hanif-mianjee/Vibecoding-Enhanced-Instructions.git}"
TARGET_DIR="."
TMP_DIR=".repo_tmp_$$"

# Hardcoded list of files/folders to remove after cloning.
# Can be overridden by setting the PRUNE_LIST environment variable to a newline-separated list.
if [ -z "${PRUNE_LIST-}" ]; then
PRUNE_LIST=$(cat <<'EOF'
.git
.gitignore
README.md
milestones.md
feedback-checklist.md
features
milestones
VERSION
EOF
)
fi

echo "==> Starting installation"

# Requirements check
if ! command -v git >/dev/null 2>&1; then
  echo "Error: git is required but not found in PATH." >&2
  exit 1
fi

# Determine script name if available (not set when piped)
SCRIPT_NAME=""
if [ "${0-}" != "" ]; then
  # When executed via a file, $0 is that file; with a pipe it might be 'sh' or 'bash'
  # We'll exclude this name in the emptiness check if it exists in the directory
  # shellcheck disable=SC2039 # POSIX 'basename' is fine
  SCRIPT_NAME=`basename "$0" 2>/dev/null || echo ""`
fi

# Safety checks on target directory
if [ ! -w "$TARGET_DIR" ]; then
  echo "Error: current directory is not writable: $TARGET_DIR" >&2
  exit 1
fi

if [ -d "$TARGET_DIR/.git" ]; then
  echo "Error: current directory already contains a Git repository (.git). Aborting to avoid conflicts." >&2
  exit 1
fi

# Ensure directory is empty (allow the installer script itself if present)
non_empty=0
for entry in "$TARGET_DIR"/* "$TARGET_DIR"/.[!.]* "$TARGET_DIR"/..?*; do
  [ -e "$entry" ] || continue
  base=`basename "$entry"`
  # ignore the installer itself if present
  if [ -n "$SCRIPT_NAME" ] && [ "$base" = "$SCRIPT_NAME" ]; then
    continue
  fi
  if [ "$base" = "." ] || [ "$base" = ".." ]; then
    continue
  fi
  non_empty=1
  break
done
if [ "$non_empty" -eq 1 ]; then
  echo "Error: current directory is not empty. Please run this in an empty folder." >&2
  echo "Hint: You can create a new directory and run the installer there." >&2
  exit 1
fi

echo "==> Cloning repository into a temporary directory"
git clone --depth=1 "$REPO_URL" "$TMP_DIR" 1>/dev/null

echo "==> Moving files into the current directory"
# Move normal files
for item in "$TMP_DIR"/* "$TMP_DIR"/.[!.]* "$TMP_DIR"/..?*; do
  # Skip if the glob didn't match anything
  [ -e "$item" ] || continue
  # Extra safety: don't move '.' or '..'
  base=`basename "$item"`
  if [ "$base" = "." ] || [ "$base" = ".." ]; then
    continue
  fi
  mv -f "$item" "$TARGET_DIR/"
done

echo "==> Cleaning up temporary directory"
rm -rf "$TMP_DIR"

echo "==> Pruning files/folders from hardcoded list"
printf '%s\n' "$PRUNE_LIST" | while IFS= read -r path; do
  # Normalize line endings (strip any trailing CR from CRLF) and trim whitespace
  p=`printf '%s' "$path" | tr -d '\r' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'`
  # Skip empty lines and comments
  [ -n "$p" ] || continue
  case "$p" in
    \#*) continue ;;
  esac
  case "$p" in
    "/"|"."|"..")
      echo "Skipping dangerous path entry: $p"
      continue
      ;;
  esac
  if [ -e "$TARGET_DIR/$p" ]; then
    rm -rf -- "$TARGET_DIR/$p"
    echo "Removed: $p"
  else
    echo "Not found (skip): $p"
  fi
done

echo "==> Finalizing"
# Attempt to self-delete the installer in the repository root
if [ -f "$TARGET_DIR/install.sh" ]; then
  rm -f -- "$TARGET_DIR/install.sh" || true
fi

echo "✅ Installation complete."
exit 0
