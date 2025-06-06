import subprocess
import struct
import os

# File names
source_file = "fibonacci.s"
object_file = "program.o"
elf_file = "program.elf"
bin_file = "program.bin"
hex_file = "program.hex"

# Toolchain commands 
AS = "riscv64-elf-as"
LD = "riscv64-elf-ld"
OBJCOPY = "riscv64-elf-objcopy"

# Clean up old files
for f in [object_file, elf_file, bin_file, hex_file]:
    if os.path.exists(f):
        os.remove(f)

try:
    # Step 1: Assemble .s → .o
    subprocess.run([AS, "-o", object_file, source_file], check=True)
    print("✅ Assembled:", object_file)

    # Step 2: Link .o → .elf
    subprocess.run([LD, "-Ttext=0x0", "-o", elf_file, object_file], check=True)
    print("✅ Linked:", elf_file)

    # Step 3: Convert .elf → .bin
    subprocess.run([OBJCOPY, "-O", "binary", elf_file, bin_file], check=True)
    print("✅ Binary created:", bin_file)

    # Step 4: Convert .bin → .hex (v2.0 raw format)
    with open(bin_file, "rb") as f:
        data = f.read()

    hex_lines = []
    for i in range(0, len(data), 4):
        word = data[i:i+4]
        if len(word) < 4:
            word = word.ljust(4, b'\x00')
        value = struct.unpack("<I", word)[0]
        hex_lines.append(f"{value:08x}")

    with open(hex_file, "w") as f:
        f.write("v2.0 raw\n")
        for line in hex_lines:
            f.write(line + "\n")

    print(f"✅ Hex file ready: {hex_file}")

except subprocess.CalledProcessError as e:
    print("❌ Error during build:", e)
except Exception as e:
    print("❌ General error:", e)
