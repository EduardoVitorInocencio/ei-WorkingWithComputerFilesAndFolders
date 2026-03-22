from pathlib import Path

root_dir = Path('destination')

for path in root_dir.rglob('*.txt'):
    with open(path,'wb') as f:
        f.write(b'')
    path.unlink()