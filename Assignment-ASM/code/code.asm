.include "/home/sreshta/Rupa/Assembly/m328Pdef.inc"

ldi r16, 0b00001100                ;identifying output pins 2,3
out DDRD,r16
ldi r17, 0b11111100
out DDRB,r17
ldi r17, 0b11111100
out PortB,r17
ldi r19,0b00000001
ldi r20,0b00000001
AND r19,r17          ;r19=B
LSR  r17
AND r20,r17           ;r20=A
ldi r21,0b00000001
eor r21,r19           ;r21=B'

ldi r22,0b00000001
eor r22,r20           ;r22=A'
mov r0,r22                    
AND r0,r19            ;r0=A'B
mov r1,r20
AND r1,r21            ;r1=AB'
OR r0,r1              ;D=A'B+AB'   (A)
mov r1,r22
AND r1,r19            ;r1=A'B=X    (B)
mov r16,r0
mov r16,r0            
LSL r16               ;r30=000000A0
OR r16,r1            ;r30=000000ab
LSL r16
LSL r16
out PortD,r30 


Start:
rjmp Start
