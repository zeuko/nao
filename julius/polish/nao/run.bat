julius-4.3.1.exe                   ^
    -htkconf ../wav_config         ^^
    -v nao.dict                    ^^^
    -input file                    ^^^^
    -d ../PLPL-v2.61.lm            ^^^^^
    -forcedict -h ../PLPL-v2.61.am ^^^^^^
    -hlist ../PLPL-v2.61.phn       ^^^^^^^
    -smpFreq 16384                 ^^^^^^^^
    -fallback1pass                 ^^^^^^^^^
    -spmodel sp                    ^^^^^^^^^^
    -multipath                     ^^^^^^^^^^^
    -iwsp                          ^^^^^^^^^^^^
    -gprune heuristic              ^^^^^^^^^^^
    -b2 360                        ^^^^^^^^^^
    -n 40                          ^^^^^^^^^
    -s 2000                        ^^^^^^^^
    -lmp 12.0 -6.0                 ^^^^^^^
    -lmp2 12.0 -6.0                ^^^^^^
    -spsegment                     ^^^^^
    -input adinnet                 ^^^^
    -module                        ^^^
    -b 2000                        ^^
    -record recorded               ^
    -d ..\PLPL-v2.61.lm