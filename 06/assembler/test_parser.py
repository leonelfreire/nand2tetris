# Tests the parser.

import unittest
import parser

class TestParser(unittest.TestCase):
    def testShouldClean(self):
        self.assertEqual('', parser.clean(''))

        self.assertEqual('', parser.clean('//'))
        self.assertEqual('', parser.clean('//comment'))
        self.assertEqual('', parser.clean('// comment'))
        self.assertEqual('', parser.clean(' //comment'))
        self.assertEqual('', parser.clean('// comment '))
        self.assertEqual('', parser.clean('//   comment'))
        self.assertEqual('', parser.clean('   //comment'))
        self.assertEqual('', parser.clean('//   comment   '))

        self.assertEqual('', parser.clean('//'))
        self.assertEqual('', parser.clean('//comment'))
        self.assertEqual('', parser.clean('// comment'))
        self.assertEqual('', parser.clean(' //comment'))
        self.assertEqual('', parser.clean('// comment '))
        self.assertEqual('', parser.clean('//   comment'))
        self.assertEqual('', parser.clean('   //comment'))
        self.assertEqual('', parser.clean('//   comment   '))

        self.assertEqual('@var', parser.clean('@var'))
        self.assertEqual('@var', parser.clean('@var//'))
        self.assertEqual('@var', parser.clean('@var//comment'))
        self.assertEqual('@var', parser.clean('@var// comment'))
        self.assertEqual('@var', parser.clean('@var //comment'))
        self.assertEqual('@var', parser.clean('@var// comment '))
        self.assertEqual('@var', parser.clean('@var//   comment'))
        self.assertEqual('@var', parser.clean('@var   //comment'))
        self.assertEqual('@var', parser.clean('@var//   comment   '))

        self.assertEqual('@var', parser.clean(' @var '))
        self.assertEqual('@var', parser.clean('   @var          //   '))
        self.assertEqual('@var', parser.clean('    @var          //comment    '))
        self.assertEqual('@var', parser.clean('     @var          // comment     '))
        self.assertEqual('@var', parser.clean('      @var           //comment      '))
        self.assertEqual('@var', parser.clean('       @var          // comment       '))
        self.assertEqual('@var', parser.clean('        @var          //   comment        '))
        self.assertEqual('@var', parser.clean('         @var             //comment         '))
        self.assertEqual('@var', parser.clean('          @var          //   comment          '))

        self.assertEqual('!D', parser.clean('!D'))
        self.assertEqual('!D', parser.clean('!D//'))
        self.assertEqual('!D', parser.clean('!D//comment'))
        self.assertEqual('!D', parser.clean('!D// comment'))
        self.assertEqual('!D', parser.clean('!D //comment'))
        self.assertEqual('!D', parser.clean('!D// comment '))
        self.assertEqual('!D', parser.clean('!D//   comment'))
        self.assertEqual('!D', parser.clean('!D   //comment'))
        self.assertEqual('!D', parser.clean('!D//   comment   '))

        self.assertEqual('!D', parser.clean(' !D '))
        self.assertEqual('!D', parser.clean('   !D          //   '))
        self.assertEqual('!D', parser.clean('    !D          //comment    '))
        self.assertEqual('!D', parser.clean('     !D          // comment     '))
        self.assertEqual('!D', parser.clean('      !D           //comment      '))
        self.assertEqual('!D', parser.clean('       !D          // comment       '))
        self.assertEqual('!D', parser.clean('        !D          //   comment        '))
        self.assertEqual('!D', parser.clean('         !D             //comment         '))
        self.assertEqual('!D', parser.clean('          !D          //   comment          '))

        self.assertEqual('D=D|A', parser.clean('D  = D  |  A'))
        self.assertEqual('D=D|A', parser.clean('D  =  D |  A//'))
        self.assertEqual('D=D|A', parser.clean('D  =  D  | A//comment'))
        self.assertEqual('D=D|A', parser.clean('D  =  D  |A// comment'))
        self.assertEqual('D=D|A', parser.clean('D  =  D|  A //comment'))
        self.assertEqual('D=D|A', parser.clean('D=D|A// comment '))
        self.assertEqual('D=D|A', parser.clean('D =  D  |  A//   comment'))
        self.assertEqual('D=D|A', parser.clean('D  = D  |  A   //comment'))
        self.assertEqual('D=D|A', parser.clean('D  =  D | A//   comment   '))

        self.assertEqual('D=D|A', parser.clean(' D =  D  |  A '))
        self.assertEqual('D=D|A', parser.clean('   D  = D  |  A          //   '))
        self.assertEqual('D=D|A', parser.clean('    D  =  D |  A          //comment    '))
        self.assertEqual('D=D|A', parser.clean('     D  =  D  | A          // comment     '))
        self.assertEqual('D=D|A', parser.clean('      D  =  D |  A           //comment      '))
        self.assertEqual('D=D|A', parser.clean('       D=D|A          // comment       '))
        self.assertEqual('D=D|A', parser.clean('        D  =  D |  A          //   comment        '))
        self.assertEqual('D=D|A', parser.clean('         D  = D  |  A             //comment         '))
        self.assertEqual('D=D|A', parser.clean('          D  =  D |  A          //   comment          '))

        self.assertEqual('D;JMP', parser.clean('D; JMP'))
        self.assertEqual('D;JMP', parser.clean('D ;JMP//'))
        self.assertEqual('D;JMP', parser.clean('D  ;JMP//comment'))
        self.assertEqual('D;JMP', parser.clean('D ;JMP// comment'))
        self.assertEqual('D;JMP', parser.clean('D;   JMP //comment'))
        self.assertEqual('D;JMP', parser.clean('D ;     JMP// comment '))
        self.assertEqual('D;JMP', parser.clean('D ; JMP//   comment'))
        self.assertEqual('D;JMP', parser.clean('D ;  JMP   //comment'))
        self.assertEqual('D;JMP', parser.clean('D ;   JMP//   comment   '))

        self.assertEqual('D;JMP', parser.clean(' D; JMP '))
        self.assertEqual('D;JMP', parser.clean('   D ;JMP          //   '))
        self.assertEqual('D;JMP', parser.clean('    D  ;JMP          //comment    '))
        self.assertEqual('D;JMP', parser.clean('     D;  JMP          // comment     '))
        self.assertEqual('D;JMP', parser.clean('      D      ; JMP           //comment      '))
        self.assertEqual('D;JMP', parser.clean('       D;   JMP          // comment       '))
        self.assertEqual('D;JMP', parser.clean('        D ;      JMP          //   comment        '))
        self.assertEqual('D;JMP', parser.clean('         D  ; JMP             //comment         '))
        self.assertEqual('D;JMP', parser.clean('          D   ;       JMP          //   comment          '))

        self.assertEqual('D=A+1;JMP', parser.clean('D =A+1;JMP'))
        self.assertEqual('D=A+1;JMP', parser.clean('D= A + 1 ;JMP//'))
        self.assertEqual('D=A+1;JMP', parser.clean('D=A+ 1; JMP//comment'))
        self.assertEqual('D=A+1;JMP', parser.clean('D= A+1;JMP// comment'))
        self.assertEqual('D=A+1;JMP', parser.clean('D= A+ 1;  JMP //comment'))
        self.assertEqual('D=A+1;JMP', parser.clean('D=A+1; JMP// comment '))
        self.assertEqual('D=A+1;JMP', parser.clean('D=A+ 1;JMP//   comment'))
        self.assertEqual('D=A+1;JMP', parser.clean('D=A    +1;JMP   //comment'))
        self.assertEqual('D=A+1;JMP', parser.clean('D=A+     1;JMP//   comment   '))

        self.assertEqual('D=A+1;JMP', parser.clean(' D=A+1;JMP '))
        self.assertEqual('D=A+1;JMP', parser.clean('   D = A + 1 ; JMP          //   '))
        self.assertEqual('D=A+1;JMP', parser.clean('    D =A +1; JMP          //comment    '))
        self.assertEqual('D=A+1;JMP', parser.clean('     D  =A+ 1;   JMP          // comment     '))
        self.assertEqual('D=A+1;JMP', parser.clean('      D   =A+1; JMP           //comment      '))
        self.assertEqual('D=A+1;JMP', parser.clean('       D=A+1; JMP          // comment       '))
        self.assertEqual('D=A+1;JMP', parser.clean('        D =A  +1; JMP          //   comment        '))
        self.assertEqual('D=A+1;JMP', parser.clean('         D   =A    +1; JMP             //comment         '))
        self.assertEqual('D=A+1;JMP', parser.clean('          D =A+  1;  JMP          //   comment          '))

    def testShouldParseAInstruction(self):
        i = parser.parseInstruction('@var')
        self.assertEqual('A', i['type'])
        self.assertEqual('var', i['value'])

        i = parser.parseInstruction('@12345')
        self.assertEqual('A', i['type'])
        self.assertEqual('12345', i['value'])

        i = parser.parseInstruction('@other_var')
        self.assertEqual('A', i['type'])
        self.assertEqual('other_var', i['value'])

    def testShouldNotParseAInstruction1(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('@')

        self.assertEqual(parser._MSG_INVALID_A, str(cm.exception))

    def testShouldNotParseAInstruction2(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('@-var')

        self.assertEqual(parser._MSG_INVALID_A, str(cm.exception))

    def testShouldNotParseAInstruction3(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('@-12345')

        self.assertEqual(parser._MSG_INVALID_A, str(cm.exception))

    def testShouldNotParseAInstruction4(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('@32768')

        self.assertEqual(parser._MSG_INVALID_A_VALUE, str(cm.exception))

    def testShouldParseCInstructionComputation(self):
        i = parser.parseInstruction('0')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('!D')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('!A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('!M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-D')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

    def testShouldParseCInstructionDestination(self):
        # M
        i = parser.parseInstruction('M=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        # D
        i = parser.parseInstruction('D=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('D', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        # MD
        i = parser.parseInstruction('MD=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('MD=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('MD', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        # A
        i = parser.parseInstruction('A=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('A', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        # AM
        i = parser.parseInstruction('AM=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AM=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AM', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        # AD
        i = parser.parseInstruction('AD=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AD=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AD', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        # AMD
        i = parser.parseInstruction('AMD=0')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=!D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=!A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=!M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=A+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=M+1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=A-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=M-1')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D+A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D+M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D-A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D-M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=A-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=M-D')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D&A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D&M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D|A')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('AMD=D|M')
        self.assertEqual('C', i['type'])
        self.assertEqual('AMD', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

    def testShouldParseCInstructionJump(self):
        # Without destination
        i = parser.parseInstruction('M;JGT')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JGT', i['jump'])

        i = parser.parseInstruction('M;JEQ')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JEQ', i['jump'])

        i = parser.parseInstruction('M;JGE')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JGE', i['jump'])

        i = parser.parseInstruction('M;JLT')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JLT', i['jump'])

        i = parser.parseInstruction('M;JNE')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JNE', i['jump'])

        i = parser.parseInstruction('M;JLE')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JLE', i['jump'])

        i = parser.parseInstruction('M;JMP')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JMP', i['jump'])

        # With destination
        i = parser.parseInstruction('M=0;JGT')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual('JGT', i['jump'])

        i = parser.parseInstruction('M=1;JEQ')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual('JEQ', i['jump'])

        i = parser.parseInstruction('M=-1;JGE')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual('JGE', i['jump'])

        i = parser.parseInstruction('M=D;JLT')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual('JLT', i['jump'])

        i = parser.parseInstruction('M=A;JNE')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual('JNE', i['jump'])

        i = parser.parseInstruction('M=M;JLE')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual('JLE', i['jump'])

        i = parser.parseInstruction('M=!D;JMP')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual('JMP', i['jump'])

    def testShouldParseCInstructionOptionalSemicolon(self):
        i = parser.parseInstruction('0;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('!D;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('!A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('!M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-D;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('-M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D+1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A+1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M+1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D+A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D+M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D-A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D-M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('A-D;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M-D;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D&A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D&M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D|A;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('D|M;')
        self.assertEqual('C', i['type'])
        self.assertEqual(None, i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=0;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('0', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=!D;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=!A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=!M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('!M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-D;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=-M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D+1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A+1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M+1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M+1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M-1;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M-1', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D+A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D+A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D+M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D+M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D-A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D-A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D-M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D-M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=A-D;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('A-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=M-D;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('M-D', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D&A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D&A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D&M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D&M', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D|A;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D|A', i['comp'])
        self.assertEqual(None, i['jump'])

        i = parser.parseInstruction('M=D|M;')
        self.assertEqual('C', i['type'])
        self.assertEqual('M', i['dest'])
        self.assertEqual('D|M', i['comp'])
        self.assertEqual(None, i['jump'])

    def testShouldNotParseCInstruction1(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('X')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction2(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('X=1')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction3(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('X=Z')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction4(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('X=X+1;JMP')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction5(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('D;JOO')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction6(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('M+A')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction7(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('M-A')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction8(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('M&A')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction9(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('M|A')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction10(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('A+M')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction11(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('A-M')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction12(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('A&M')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldNotParseCInstruction13(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseInstruction('A|M')

        self.assertEqual(parser._MSG_INVALID_C, str(cm.exception))

    def testShouldParseLabel(self):
        l = parser.parseLabel('(label)')
        self.assertEqual('label', l['value'])

        l = parser.parseLabel('(_label)')
        self.assertEqual('_label', l['value'])

        l = parser.parseLabel('(label_)')
        self.assertEqual('label_', l['value'])

        l = parser.parseLabel('(_123)')
        self.assertEqual('_123', l['value'])

        l = parser.parseLabel('(_123_label)')
        self.assertEqual('_123_label', l['value'])

        l = parser.parseLabel('(label_end)')
        self.assertEqual('label_end', l['value'])

    def testShouldNotParseLabelInstruction1(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseLabel('(label')

        self.assertEqual(parser._MSG_INVALID_LABEL, str(cm.exception))

    def testShouldNotParseLabelInstruction4(self):
        with self.assertRaises(parser.ParserException) as cm:
            parser.parseLabel('(label)(label)')

        self.assertEqual(parser._MSG_INVALID_LABEL, str(cm.exception))

if __name__ == '__main__':
    unittest.main()
