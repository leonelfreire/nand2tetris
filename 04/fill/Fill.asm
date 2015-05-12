// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

@8191
D=A

@lastScreenAddress
M=D // lastScreenAddress = 8191

@i
M=D // i = lastScreenAddress (starts backwards)

@SCREEN
D=A

@screenAddress
M=D // screenAddress = @SCREEN

@color
M=0 // Color to fill (0 or -1)

@pointer
M=0 // Generic pointer

(LOOP_FILL)
    @i
    D=M

    @RESET
    D;JLT // if i < 0 goto RESET

    @screenAddress
    D=M+D // D = @SCREEN + @i

    @pointer
    M=D // Saves the current screen address

    @KBD
    D=M

    @SET_COLOR_WHITE
    D;JLE // if @KBD <= 0 goto SET_COLOR_WHITE

    @SET_COLOR_BLACK
    D;JGT // if @KBD > 0 goto SET_COLOR_BLACK

    (CONTINUE)
        @color
        D=M

        @pointer
        A=M // A = @SCREEN + @i
        M=D // M = @color

        @i
        M=M-1

    @LOOP_FILL
    0;JMP

(RESET)
    @lastScreenAddress
    D=M

    @i
    M=D // i = lastScreenAddress

    @LOOP_FILL
    0;JMP

(SET_COLOR_WHITE)
    @color
    M=0

    @CONTINUE
    0;JMP

(SET_COLOR_BLACK)
    @color
    M=-1

    @CONTINUE
    0;JMP
