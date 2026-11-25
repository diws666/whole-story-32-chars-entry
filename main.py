import os

LINE = "He left. She stayed. Rent due."  # verified count: 30 chars (30 bytes UTF-8); gate max is 32

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
