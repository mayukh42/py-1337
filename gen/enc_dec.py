
''' 
    decoder with a state machine
    encoding scheme: n[A-Z]\\km[A-Z] means A-Z will be repeated n times, followed by k, then a repeat of A-Z m times, etc. 
    brackets can be stacked

    examples: 
    3[a]2[bc] -> aaabcbc,
    3[a]\42[bc] -> aaa4bcbc
'''

from enum import Enum
from dataclasses import dataclass

def is_digit(s):
    asc = ord(s)
    return asc >= 48 and asc <= 57

def is_alphabet(s):
    asc = ord(s)
    return asc >= 97 and asc <= 122


class State(Enum):
    REG = 1
    SQB = 2
    ESC = 3

@dataclass
class StackElem():
    state: State
    seg: str
    mult: int

def decode(enc_str) -> str:
    dec_str = ""
    # state machine
    state = State.REG
    stack = []
    end = len(enc_str)
    for i in range(end):
        if is_digit(enc_str[i]) and i+1 < end and enc_str[i+1] == "[":
            # state transition to [...] segment
            state = State.SQB
            stack.append(StackElem(
                state, "", int(enc_str[i])
            ))
            i += 1
        elif is_alphabet(enc_str[i]) and state == State.SQB:
            # stack has > 1 elms
            stack[-1].seg += enc_str[i]
        elif enc_str[i] == "\\":
            state = State.ESC
            stack.append(StackElem(
                state, "", 1
            ))
        elif is_digit(enc_str[i]) and state == State.ESC:
            last = stack.pop()
            if len(stack) > 0:
                state = stack[-1].state
                stack[-1].seg += str(enc_str[i])
            else:
                dec_str += str(enc_str[i])
                state = State.REG
        elif enc_str[i] == "]" and state == State.SQB:
            last = stack.pop()
            if len(stack) > 0:
                state = stack[-1].state
                stack[-1].seg += last.seg * last.mult
            else:
                dec_str += last.seg * last.mult
                state = State.REG
        elif is_alphabet(enc_str[i]):
            dec_str += enc_str[i]
        i += 1


    return dec_str
