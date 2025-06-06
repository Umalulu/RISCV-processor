.text
.global _start

_start:
    addi x5, x0, 0    # x5 = 0
    addi x6, x0, 1    # x6 = 1

loop:
    add  x7, x5, x6   # x7 = x5 + x6
    addi x5, x6, 0    # x5 = x6
    addi x6, x7, 0    # x6 = x7
    jal  x0, loop     # jump to loop (negative offset automatically handled)

