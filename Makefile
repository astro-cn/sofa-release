# Build sofa c sources into a static library using LLVM (clang/clang-cl)

ifeq ($(OS),Windows_NT)
	CC       = clang-cl
	AR       = lib
	LIBNAME  = sofa.lib
	OBJEXT   = obj
	CFLAGS   = /c /O2 /nologo
	ARFLAGS  = /OUT:
else
	UNAME_S  := $(shell uname -s)
	CC       = clang
	AR       = ar
	LIBNAME  = libsofa.a
	OBJEXT   = o
	CFLAGS   = -c -O2 -Wall
	ARFLAGS  = rcs
endif

SOURCES   = $(wildcard *.c)
OBJECTS   = $(SOURCES:.c=.$(OBJEXT))

all: $(LIBNAME)

$(LIBNAME): $(OBJECTS)
ifeq ($(OS),Windows_NT)
	$(AR) $(ARFLAGS)$@ $(OBJECTS)
else
	$(AR) $(ARFLAGS) $@ $(OBJECTS)
endif

%.$(OBJEXT): %.c
	$(CC) $(CFLAGS) $<

clean:
	rm -f $(OBJECTS) $(LIBNAME)