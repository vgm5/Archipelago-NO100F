# RAM Instruction to .iso Instruction:  RAM ADDRESS - 0x8000 0000 + 0x1B000
AP_SAVE_LOAD = {
    # ignore cheats, hold L+R and press (x/y/b) for funny
    0xc73ec: 0x60000000,  # nop
    0xc73f8: 0x60000000,  # nop
    0xc7404: 0x60000000,  # nop
    0xc7410: 0x60000000,  # nop
    0xc741c: 0x60000000,  # nop
    0xc7428: 0x60000000,  # nop
    0xc7434: 0x60000000,  # nop
    0xc7440: 0x60000000,  # nop
    0xc7444: 0x60000000,  # nop
    0xc7448: 0x60000000,  # nop
    0xc744c: 0x60000000,  # nop
    0xc7450: 0x60000000,  # nop
    0xc7454: 0x60000000,  # nop
    0xc7458: 0x60000000,  # nop
    0xc745c: 0x60000000,  # nop

    # inject write function
    0xeab7c: 0x480f6089,  # bl   -> 0x801C5C04 (write function)

    # inject read function
    0xea724: 0x480f6521,  # bl   -> 0x801C5C44 (read function)

    # write function
    0x1e0c04: 0x9421ffe8,  # stwu sp, -0x0018(sp)
    0x1e0c08: 0x7c0802a6,  # mflr r0
    0x1e0c0c: 0x90010014,  # stw  r0, 0x0014 (sp)
    0x1e0c10: 0x4be74c01,  # bl   ->0x8003A810 (Write_b1__7xSerialFi)
    0x1e0c14: 0x3dc0817f,  # lis	r14, 0x817f
    0x1e0c18: 0x39e00000,  # li   r15, 0
    0x1e0c1c: 0x7fe3fb78,  # mr	r3, r31
    0x1e0c20: 0x7c8e782e,  # lwzx	r4, r14, r15
    0x1e0c24: 0x4be74afd,  # bl	->0x8003A720 (Write__7xSerialFi)
    0x1e0c28: 0x39ef0004,  # addi r15, r15, 4
    0x1e0c2c: 0x2c0f007c,  # cmp  r15, 0x7c
    0x1e0c30: 0x4081ffec,  # ble -> 0x1e0c1c
    0x1e0c34: 0x80010014,  # lwz  r0, 0x0014(sp)
    0x1e0c38: 0x7c0803a6,  # mtlr r0
    0x1e0c3c: 0x38210018,  # addi sp, sp, 0x0018
    0x1e0c40: 0x4e800020,  # blr

    # read function
    0x1e0c44: 0x9421ffe8,  # stwu sp, -0x0018(sp)
    0x1e0c48: 0x7c0802a6,  # mflr	r0
    0x1e0c4c: 0x90010014,  # stw	r0, 0x0014 (sp)
    0x1e0c50: 0x3dc0817f,  # lis	r14, 0x817F
    0x1e0c54: 0x39e00000,  # li   r15, 0
    0x1e0c58: 0x7fe3fb78,  # mr	r3, r31
    0x1e0c5c: 0x7c8e7a14,  # add  r4, r14, r15
    0x1e0c60: 0x7c9d2378,  # mr	r29, r4
    0x1e0c64: 0x4be746c9,  # bl	->0x8003A32C (Read_7xSerialFPUi)
    0x1e0c68: 0x39ef0004,  # addi r15, r15, 4
    0x1e0c6c: 0x2c0f007c,  # cmpwi r15, 0x7c
    0x1e0c70: 0x4081ffe8,  # ble -> 0x1e0c58
    0x1e0c74: 0x3c808023,  # lis  r4, 0x8023
    0x1e0c78: 0x7fe3fb78,  # mr   r3, r31
    0x1e0c7c: 0x38844ae0,  # addi r4, r4, 0x4ae0
    0x1e0c80: 0x3ba405b0,  # addi r29, r4, 0x5b0
    0x1e0c84: 0x7fa4eb78,  # mr   r4, r29
    0x1e0c88: 0x4be746a5,  # bl   -> 0x8003A32C (Read_7xSerialFPUi)
    0x1e0c8c: 0x80010014,  # lwz  r0, 0x0014(sp)
    0x1e0c90: 0x7c0803a6,  # mtlr r0
    0x1e0c94: 0x38210018,  # addi sp, sp, 0x18
    0x1e0c98: 0x4e800020,  # blr

    # nuke remaining cheats info
    0x1e0c9c: bytes([0] * 0xb0)
}

UPGRADE_REWARD_FIX = {
    0x6a2f4: 0x60000000,  # nop	#Nullifies Upgrade Collection
    0x6a2fc: 0x60000000,  # nop
    0x6a304: 0x60000000,  # nop
    0x6a5bc: 0x60000000,  # nop
    0x6a5c0: 0x60000000,  # nop
    0x6a5cc: 0x60000000,  # nop

    0x6a394: 0x60000000,  # nop # Nullifies Gum/Soap Ammo Collection
    0x6a3a8: 0x60000000,  # nop
    0x6a3b4: 0x60000000,  # nop
}

MONSTER_TOKEN_FIX = {
    0x6a420: 0x60000000,  # nop
}

SNACK_REWARD_FIX = {
    0x7538c: 0x60000000,  # nop
}
