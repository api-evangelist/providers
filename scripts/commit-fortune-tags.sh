#!/usr/bin/env bash
# Commit and push Fortune tag additions across all/* repos.
# Run from any directory — paths are absolute.

ALL="/Users/kinlane/GitHub/all"
DONE=0
FAILED=0
SKIPPED=0

while IFS= read -r slug; do
    DIR="$ALL/$slug"
    YML="$DIR/apis.yml"

    # Skip if no git repo or no apis.yml
    if [ ! -d "$DIR/.git" ] || [ ! -f "$YML" ]; then
        ((SKIPPED++))
        continue
    fi

    # Skip if nothing staged / no changes
    if git -C "$DIR" diff --quiet HEAD -- apis.yml 2>/dev/null; then
        ((SKIPPED++))
        continue
    fi

    git -C "$DIR" add apis.yml
    git -C "$DIR" commit -m "Add Fortune 1000 tag to apis.yml" --quiet
    if git -C "$DIR" push --quiet 2>/dev/null; then
        ((DONE++))
        echo "  pushed: $slug"
    else
        ((FAILED++))
        echo "  FAILED: $slug"
    fi

    # Pace to avoid GitHub rate limits
    sleep 1

done < "$1"

echo ""
echo "Done: $DONE  Failed: $FAILED  Skipped: $SKIPPED"
