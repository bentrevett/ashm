# ashm

* A toy assembly-like language called a-sham-bly (ashm).
* __All arithmetic is integer arithmetic only.__
* __All comparisons are done on comparison between registers only.__

## Instructions

#### MOV A, B

- Moves B into A. 
- B can be either another register or a literal number.

#### ADD A, B

- Performs A = A+B. 
- B can be either another register or a literal number.

#### SUB A, B

- Performs A = A-B. 
- B can be either another register or a literal number.

#### MUL A, B

- Performs A = A*B. 
- B can be either another register or a literal number.

#### DIV A, B

- Performs A = A/B.
- B can be either another register or a literal number.

#### MOD A, B

- Performs A = A % B.
- B can be either another register or a literal number.

#### LBL A

- Creates a label that can be jumped to.

#### JMP A

- Unconditional jump to label A.

#### JEQ A B C

- Jumps to label C if the values in registers A and B are equal.

#### JGT A B C

- Jumps to label C if the value in register A is greater than the value in register B.

#### JLT A B C

- Jumps to label C if the value in register A is less than the value in register B.

#### JGZ A B

- Jumps to label B if the value in register A is greater than zero.

#### JLZ A B

- Jumps to label B if the value in register A is less than zero.

#### JEZ A B

- Jumps to label B if the value in register A is equal to zero.

