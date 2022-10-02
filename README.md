[![CMake](https://github.com/m-heim/Npc/actions/workflows/cmake.yml/badge.svg)](https://github.com/m-heim/Npc/actions/workflows/cmake.yml)

*NPC*

A compiler project written in c, the language is called np (not pascal), its supposed to be similar to c in terms of machine distance. However, it should provide features that make programming easier.
You can find multiple examples of code under ./programs


*GOALS*

|   | *Language goals:* |
| - | ----------------- |
| <ul><li>[ ]</li></ul> | Low level (C style) |
| - [ ] | Simplicity (C style) |
| - [ ] | Fast (C style) |
| - [ ] | Useful builtins (Python style) |

*Compiler goals:*
- [ ] Compiling process max. takes 100 % more than C
- [ ] Useful error messages
- [x] No external libraries
- [ ] Using selfmade lex/parse generator
- [ ] Executable process max. takes 100 % more than C
- [ ] Self hosted
- [ ] Supports Linux
- [ ] Supports Windows
- [ ] Supports ARM

*Done:*

- Scanner

*In progress:*
- Documentation
- Parser
  
*Todo:*
- Ir generation
- Code optimization
- Code generation
- (Peephole optimizations)

Any contributions in any way appreciated.

How to:
- recommended way to contribute is via vscode in windows with wsl or simply in linux. If you want to use another IDE do so as you wish though. The advantages are that the workflow is setup already.
- the settings and extensions are provided in .vscode

Would really appreciate to see a pull request from you

| Directory/File | Purpose |
| ---------------|-------- |
| /src           | All the source code and headers for the compiler |
| /programs      | Test programs to test the parser |
| /gp-parsergen  | Seperate project which provides the parser generator for the project |
| /documentation | Contains the doxygen documentation and documentation about the language itself (i.e. lexing patterns and the bnf of the syntax) |
| /build         | Contains the build output and the data generated by cmake |
| /.vscode       | Contains launch settings, extension recommendations, settings and tasks |
| /.github       | Contains all github workflows |
| /.gitmodules   | Contains the link for github to get the parser generator |