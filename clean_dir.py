from pathlib import Path

def main(args: list[str]) -> int:
    """Removes all the files that match the given glob pattern, in this
        directory and all its children.  The glob pattern is set to match
        backup files, but could be modified to match anything desired."""
    here = Path.cwd()
    print(here)
    glob_patterns = ('*.*', '**.bak', '**~')
    for pattern in glob_patterns:
        print('Globbing for', pattern)
        for f in here.glob(pattern):
            print(f)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
