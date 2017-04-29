FPC=fpc
FPC_FLAGS=-O2

all: uf uf_simple uf_balanced

uf: uf.pas
	${FPC} ${FPC_FLAGS} $<
	
uf_balanced: uf_balanced.pas
	${FPC} ${FPC_FLAGS} $<
	
uf_simple: uf_simple.pas
	${FPC} ${FPC_FLAGS} $<
	
clean:
	rm -f uf uf.o uf_simple uf_simple.o uf_balanced uf_balanced.o

.PHONY: all clean
