# RISC-V CPU Project - Usage Guide

This README explains how to use the custom-built RISC-V processor designed in [Hneemann's Digital](https://github.com/hneemann/Digital).

---

## 🛠 Requirements

* **Digital (Logic Simulator)**: Download from [GitHub](https://github.com/hneemann/Digital)
* **Python 3**: To convert ELF to HEX
* **RISC-V GNU Toolchain**: For assembling programs

### Install Toolchain on Arch Linux

```bash
sudo pacman -S riscv64-elf-gcc
```
Alternatively, convert instructions word by word, and load them onto memory using [this](https://luplab.gitlab.io/rvcodecjs/#q=jal+x0,+-12&abi=false&isa=RV32I)

---

## 📝 Step 1: Write RISC-V Assembly

Create a file named `program.s`:

```assembly
.text
.global _start

_start:
    addi x5, x0, 0    # x5 = 0
    addi x6, x0, 1    # x6 = 1

loop:
    add  x7, x5, x6   # x7 = x5 + x6
    addi x5, x6, 0    # x5 = x6
    addi x6, x7, 0    # x6 = x7
    jal  x0, loop     # jump back to loop
```

---

## ⚙️ Step 2: Convert Assembly to HEX

Use the provided Python script `build_riscv_hex.py` to convert the code to HEX:

```bash
python3 build_riscv_hex.py
```

This will generate `program.hex` with contents like:

```
v2.0 raw
XXXXXXXX
XXXXXXXX
...
```

---

## 🧠 Step 3: Load Instructions in Digital

1. Open your CPU circuit in **Digital**
2. Navigate to the `Files/` folder and open your `.dig` circuit
3. Click on the **Instruction Memory** block
4. Go to edit->load file
5. Load the generated `program.hex`
6. Confirm and close

---

## 🕹️ Step 4: Simulate the CPU

* Start the simulation
* Provide clock signals using a **clock generator** or manual pulses
* Monitor changes in register values (e.g., x5, x6, x7)

---

## 🔍 Optional Debugging Tools

* Connect **register outputs** to 7-segment displays or LEDs
* Use **step-by-step clocking** to observe internal operations
* Add a **reset circuit** if needed

---

## 📁 Project Structure

```
project/
├── Files/                # Contains all .dig circuit files
│   └── riscv_cpu.dig     # Your Digital circuit
├── Notes/                # Documentation, logs, or design notes
├── program.s             # RISC-V assembly source
├── program.hex           # Compiled HEX file for instruction memory
└── build_riscv_hex.py    # Python script to convert to HEX
```

---

## 📬 Questions?

If you're stuck, feel free to reach out or explore the [RISC-V spec](https://riscv.org/technical/specifications/) for more insight.
