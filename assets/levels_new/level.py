Skip to content
Search or jump to…
Pulls
Issues
Marketplace
Explore
 
@sofiane-wattiez 
ShadowRZ
/
PySokoban
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
PySokoban/level/Default.pysl
@ShadowRZ
ShadowRZ Map blit.
Latest commit b52c1b1 on 29 Jan 2017
 History
 1 contributor
3492 lines (3084 sloc)  54.4 KB
   
; Star Pusher (Sokoban clone)
; http://inventwithpython.com/blog
; By Al Sweigart al@inventwithpython.com
;
; Everything after the ; is a comment and will be ignored by the game that
; reads in this file.
;
; The format is described at:
; http://sokobano.de/wiki/index.php?title=Level_format
;   @ - The starting position of the player.
;   * - The starting position for a pushable star.
;   . - A goal where a star needs to be pushed.
;   + - Player & goal
;   * - Star & goal
;  (space) - an empty open space.
;   X - A wall.
;
; Level maps are separated by a blank line (I like to use a ; at the start
; of the line since it is more visible.)
;
; I tried to use the same format as other people use for their Sokoban games,
; so that loading new levels is easy. Just place the levels in a text file
; and name it "starPusherLevels.txt" (after renaming this file, of course).


; Starting demo level:
 XXXXXXXX
XX      X
X   .   X
X   *   X
X .*@*. X
XXXX*   X
   X.   X
   X   XX
   XXXXX
;
;
;
; These Sokoban levels come from David W. Skinner, who has many more puzzles at:
; http://users.bentonrea.com/~sasquatch/sokoban/

; Sasquatch Set I

; 1

   XXX
  XX X XXXX
 XX  XXX  X
XX *      X
X   @* X  X
XXX *XXX  X
  X  X..  X
 XX XX.X XX
 X      XX
 X     XX
 XXXXXXX

; 2

 XX XXXXX
XX XX . X
X XX *. X
 XX *   X
XX *@ XXX
X *  XX
X.. XX XX
X   X XX
XXXXX X

; 3

           XXXXX
          XX   X
          X    X
    XXXX  X * XX
    X  XXXX* *X
    X     * * X
   XX XX * * *X
   X  .X  * * X
   X  .X      X
XXXXX XXXXXXXXX
X.... @  X
X....    X
XX  XXXXXX
 XXXX

; 4

  XXXXXXXXXXX
 XX     X  @X
XXX * **X   X
X XX*    ** X
X  X  * X   X
XXXXXX XXXXXX
X.. ..* X*XX
X ..    XXX
X  ..XXXXX
XXXXXXXXX

; 5

  XXXXXXXXXXX
 XX    X    XX
XXX * *X* * XXX
X X* * X * *X X
X *  ..X..  * X
X  *...X...*  X
X * .. * .. * X
XXXXXX @ XXXXXX
X * ..   .. * X
X  *...X...*  X
X *  ..X..  * X
X X* * X * *X X
XXX * *X* * XXX
 XX    X    XX
  XXXXXXXXXXX

; 6

  XXXXXXXXXXX
XXX.  .*.  .XXX
 XX *  *  * XX
  XX ..*.. XX
   XX*X*X*XX
    X.* *.X
    X  @  X
    XXX XXX
   XX * * XX
   X.  *  .X
   XXX . XXX
     XXXXX

; 7

           XXXXXX
    XXXX  XX    X
  XXX  X  X  XX XXX
XXX    XXXX X   * X
X  * @ ...*..  *  X
X * *  XX XXX   XXX
XXX XXX   X XXXXX
 X      XXX
 X   XXXX
 XXXXX

; 8

    XXXXXXX
    X     XX
XXXXX XXX  XX
X       X  XX
X@****. XX* X
X  X    XX .X
XX  XX  X * X
 XX  XXXX.*.X
  XX        X
   XXXXXX  XX
        XXXX

; 9

XXXXXXXXX
X. .    X
X.*. .  X
XX XXX@ X
 X  *  XX
 X ** XX
 X  * X
 X  XXX
 XXXX

; 10

      XXXXXX
      X    X
      X @  XXX
XXXX  X      X
X  XXXX..X.X*XXXXX
X * * XX...      X
X     .....X**   X
XXXXXX XX*XX XXXXX
     X  *    X
     XXXX XXXX
       X  X
       X  XXXXX
     XXX *    X
     X  * *   X
     X X*X XXXX
     X     X
     XXXXXXX

; 11

  XXXX
XXX  XXXX
X   @   XX
X X. .X.XXX
X *** *** X
XXX.X.X.X X
 XX       X
  XXXX  XXX
     XXXX

; 12

              XXXXX
              X   X
    XXXXX     X   XXXXXXX
    X   XXXXX X   ..... X
XXXXX X XX  X X     X X X
X * * * * * X XX   XX * X
X X XX......XXXX XXX ** XXX
X      XX * X    X X  **  X
XXXXXXXXXX+**   XX X      X
         X.* *X X  XXXXXXXX
         X.XX   X
         XXXXXXXX

; 13

   XXXXXXX
 XXX     XX
 X   XXX  X
 X      X X
XXX*X@  X X
X   XXXXX X
X   X  *. X
XX**X  *.XX
 X     *..X
 XXXX X...XX
    X X*** X
    X   *  X
    XXXXX  X
        XXXX

; 14

 XXXXXXX
XX     X X
X  *.*.X
X  *.X.XXX
X X*@**  X
X   XX X X
XXXXXX   X
     XXXXX

; 15

   XXXX
   X@ X
  XX  X
  X .*X
  X*. X
XXX..*XXX
X  ..*  X
X * * X X
XXXXX X X
    X   X
    XXXXX

; 16

  XXXXXX
 XX X  XXX
XX X   X XX
X X   *.X X
XX  * *.X X
X XXXXX. XX
X     *. @X
X     *. XXXX
XXX X X*X X XXX
  XXXX .*     X
    X  .*     X
    XX .XXXXX X
    X X.* *  XX
    X X.*   X X
    XX X   X XX
     XXX  X XX
       XXXXXX

; 17

    XXXXXXXXXXX
   XX . . . . XXX
   X  ** * * *  X
   X   XXXXXXXX X XXXXX
 XXXX XX  *     X X   X
 X    X  * * X  XXX X X
XX  X X   XXXX     *  X
X...  XXXXX *  XXXX XXX
X... @     *     X    X
X...XXXXXXXXXXXX *  * X
XXXXX          XXXXX  X
                   XXXX

; 18

    XXXX
XXXXX  X
X      X
X* * * X
X.*.*.*X
X*.*.*.X
X * * *X
X......X
X.*.*.*X
X* * * X
X * * *X
X* * * X
X      X
X@ XXXXX
XXXX

; 19

XXXXX
X   XXXXXXX
X  *      XX
XX XXXXXX  XX
 X X    X X XXXXXXXX
 X X XX    *       XX
 X X.   X@XXXXXX *  XX
 X X.X  XXX    XX *  XX
 X X.    X      XX *  XX
 X X.X   X  XX   XX *  XX
XX X.X  XX  XXX   XX *  X
X  X.X   X  X*XX   XX   X
X   .X X X  XX*XX   XXXXX
XXXXXX   X  XXXXXX
     XXXXX

; 20

     XXXX
     X  X
XXXXXX*.X
X   * *.X
X *@*...X
X ***..XX
X  * ..X
XXXXXXXX

; 21

XXXXX XXXXXXXX
X   XXX . *  X
X   * *.. X* XX
XX *X ..* *  @X
 X  * . XXX   X
 XXXXXXXX XXXXX

; 22

   XXXXX XXXX
   X@ .XXX  XXX
XXXX  ** *    X
X   X . . XX  X
X  * X . . XX X
XX .  * **  X X
 X X  XXX.  X X
 X XXXX XXXXX X
 X       X    X
 XXXXXXX X XXXX
       X .* X
     XXXX   X
     XX XXXXX
      XXX

; 23

     XXXXXXX
XXXXXX     XXXXXX
X  . ..*X*.. .  X
X  * *  .  * *  X
XXX*XXXX@XXXX*XXX
X  * *  .  * *  X
X  . ..*X*.. .  X
XXXXXX     XXXXXX
     XXXXXXX

; 24

        XXXXXX
        X   XX
  XXXXXXX *  X
  X * * * X* X
  X   X. *   X
 XXXX.X.X *XXX
 X   ..... X
 X  * ..XX*X
XXX XX ..  X
X  *.X* X *X
X   *   X  X
XX@  X  XXXX
 XX  XXXX
  XXXX

; 25

         XXXXX
     XXXXX  XXXXX
     X  .X*   * X
     X X. *** @ XX
     X  .X*   *  X
     XXX.X  * *  X
       X.  XX* XXX
 XXXXXXX*XXX.* X
 X *    ....XXXX
XX X*X**....X
X  * *   X..X
X     *  X..X
X  XXXXXXXXXX
XXXXX

; 26

           XXXX
 XXXXXXXXXXX  X
 X  * * * *   XX
 X  X X X X X*XX
 XX. . . . . .X
  X*X X X X X*XXXX
XXX. . . . . .   X
XXX*X X X X X @  X
  X   * * * *  XXX
  X  XXXXXXXXXXX
  XXXX

; 27

      XXXXXXXX
 XXXXXX      XXXXXXXXXX
XX *     XXX          XX
X * * XX X  XXXXXXXXX  X
X  *  X              X X
X * * X X  XXXXXXXXX X X
X  *  X  X X. . . .  X X
X * * X X    . . . .XX X
X  *  X X X . . . . X  X
XX* *XX X  XXXX X X   XX
 X   X@ X       X  XXXX
 XXXXXX  XXXXX  X  X
      XX     X  X  X
       XXXXX  XX  XX
           XX    XX
            XXXXXX

; 28

       XXXXXX
       X    XXX
   XXXXX * *  X
XXXX   X.X    XX
X  * X*X.XX*XXXXX
X **. .X.*      XX
X  *.X.X.XXXXX  XXXX
XX  ....... @X     X
 XXXX* X.XXX X*XXX*XX
  XX *  .  X  * * * X
   X * XXX          X
   X   X XXXXXXXXXXXX
   XXXXX

; 29

XXXX
X  X              XXXX
X  XXXXXXXX XXXXXXX  X
X         XXX  XX  * X
XX.XXXXXX ...     X. X
 X.X      X .X   X * X
 X****X*** X.X   XX. X
 X.X *   * X..      XX
 X.X  *  *   X X   XX
 X  X   ** X   XXXXX
 X.  XX*  XXXXXX
 X.   X  *.  X
XX. @ XXX.X* X
X     X X    X
X    XX XXXXXX
XXXXXX

; 30

     XXXXX
     X   X
     X   X        XXXXXX
   XXX  XX XXXXX  X    XXX
   X    X        XX X**  X
  XX*   XXXXXXXXXX *  *  X
XXX  XX ..........*  X**@X
X    X **X XXXXXXX *     X
X   *  X...X     XXX  XXXX
X   X   * XXX XX   XXXX
XXXXXXXX    X
       X    X
       X    X
       XXXXXX

; 31

       XXXXXXXXX
       XXX    XX  XXXX
XXXXX  X    * XX  X  X
X   XXXX ****  XXXX*.XX
X .*      *@*      *. X
XX.*XXXX  **** XXXX   X
 X  X  XX *    X  XXXXX
 XXXX  XX    XXX
       XXXXXXXXX

; 32

                   XXXXX
                   X   X
           XXXXXXXXX * X
    XXXXXX X   X   X   X
    X    X X *     * X@X
  XXX XX XXXX XXX XX XXX
  X   *  *     X   X   X
  X  *  * X X* X ** ** X
 XXXXXX  *  X  X   X   X
XX    XX XXXXXXXXXXXXXXX
X  .X   * X    X
X..    X  XXXXXX
X...XXXX  X
X....X XXXX
X....X
XXXXXX

; 33

   XXXXXXX
  XX     XX
  X  XXX  X
  X XX *  XXXX
  X X .X   *.XXXX
  X X * *XXX.*  X
  X X *X   XXX XXXXX
  X X @ * *  X X   X
  X X  XXX X*X  *  X
  X XX X  * *.X X XXXXXXX
  X X  X     ....*  *   X
  X X XX *X *XXXX*      X
XXX*   *     X    XXXXXXX
X   XXXXXXXXXX XXXX
X              X
XX  XXXXXXXXXXXX
 XXXX

; 34

            XXXXX
            X ..XXXXXXXX
            X ......X  X
            X.. XX**  *X
         XXXXX.XX   *  X
         X  ....X *  **X
XXXXX XX X  .. .X*  *  X
X   X    X XX.XXX  ** *XXX
X   XXX  X XX X  *  X    X
X @   XXXX X  X X XXX* X X
X             X  *    *  X
X   XXXX      XXX XXXX**XX
X  XX  XXXX     X       X
X  X      XX    XXXXXX  X
XXXX       XX     X X * X
            XX    X X   X
             XXXXXX XXXXX

; 35

 XXXXX
 X   X
XX X XXXXX
X    XX  XXXXXXX
X X     *      XXXX
X   XXXX *  ** X  X
XXXXX  X *** * X* X
       X *  * * * XXXXXX
     XXX*   X* *  *    X
     X * **      XXX @ XX
     X  * ****XXXX...   X
     X  *     * X. .X...X
     XXX ****   ......  X
       X      XX..X.....X
       XXXXXX XX.....XXXX
            X   .....X   X
            XXXXXXXXXX

; 36

               XXXXX
   XXXX        X   XXXXXX
   X  X        X *    * X
   X  XXXX     X  *XX*  XXX
   X     XXXXXXXXX  X * * X
   X      ..........X   * X
 XXXXXX XX....@XXX  X **  X
 X    X XXXXX.XX X XX   * X
 X            X  X*  ** * X
XXXX X  XXXXX X  X  *  X  X
X    X X      X  XXX   XXXX
X      X  X   X    XXXXX
X   X     XXXXX
XXXXX     X
    XXXXXXX

; 37

  XXXXX       XXXXXXXXX
  X   X       X       X
XXX X*XXX XXXXX X X X XXXXX
X *. .  X X    . . . .    X
X X X X*XXX X X X X X X X*X
X  . . . .  * * * *  . .  X
XXX*X X X*XXXXXXXXXXX*X X*X
  X  . .  XX        X  .  X
  XXX*X X*XXXXXXX X X*X X*XXX
    X  . .* * * X   X  . .  X
    X*X X X X X XXXXX*X X X X
    X  . . . . .  *  . . .  X
    XXX X X X X X X X X X X X
      X * *. . .* * * * * * X
      XXXXX X X XXXXXXXXXXXXX
          X  @  X
          XXXXXXX

; 38

                      XXXX
  XXXX         XXXXXXXX  X
XXX@ XX        X      X  X
X     X        X XXX * * X
X ....XXXXXXXXXX   X  X..X
X . X  XX *   * *X X  X..X
XXX X     *  *** X X * * X
  X ...X *  **   X X  X  X
  X  ..X *   * * X X XX  X
  XX...X  * ** * X*X XXXXX
   X   XX *  * *   X X
   XXX XXXXXX  XXX X XXX
   X .   XX XXXX .   . X
  XX   . X     X X.X.X X
  X  .   X X X X   X   X
  X . XXXX     XXXXXXXXX
  X  XX
  XXXX

; 39

   XXXX           XXXXX
   X  XXXXXXX  XXXX   X
   X @  *   XXXX   *  X
   X  XXX.X    X  **  X
 XXX.XX * X* X    X  XX
 X  ..X * ...X XXX  XX
 X * ...*XX.XX     XX
 XX.XXX* *..   ** XX
  X.  X. .XXX * * X
  X  *...XX XX X  X
 XX XXXXXX   X   XX
XX   XX      XXXXX
X **  X
X   * X
XXX * X
  X  XX
  XXXX

; 40

     XXXXXXX
XXXX X     X
X  XXX *** X
X  ....*  XXXXX
X  ..X *  X  @X
XXX*XX*XXXX X XXXXXX
 X.*....*  *  XXX  XXXXX
 X ..XXXXX  XX   * *   X
 X....*.... X  **  X * X
 XXXXXXXXXX X** XX X   X
    X *.XXX        *  XX
    X       *XXX*X X  X
    XXXXX   *    * XXXX
        XXXX    XXXX
           XXXXXX

; 41

   XXXXX
   X   X
 XXX   XXXXXXXX
XX  ***    X X X
 X  * *    XX X XXXXX
XX  ***   XX X XX   XX
 XXX   XXXX X X X   X
   X   X X X XXXX* *XXX
  XX   XX X XX  *...* XX
   XXXXX X XX    .@.  X
        X X X   *...* XX
         XXXXXXXX* *XXX
                X   X
                XXXXX

; 42

XXXX
X  XXXXXX
X       XXXX
X * *   X  XXXXX
XXXXX XXX    * X
 X  X   *  X   X
 X      XX*XXXXXX
 X *XXX  X ...X X
 XX X@X* XX.X.X X
 X    X   X...X X
 X * XX* *X...XXXXX
 XXX XX   X...    X
  X  X  * * * X X X
  X *XXX XXXXXX X X
  X             X X
  XXXXXXXXXXXXX   X
              XXXXX

; 43

   XXXX
  XX  XXXXXXXXXXXXX
 XX    .......... X
XX    X  XXXX*XXX XX
X      X X      X  XX
X     X  X ***  X X XXXXX
XXXXX  X . .X XXX . . . XX
    X   *. .X  X ** * * @X
   XXXXXXX XXX X   XXXXXXX
   X *   *   X XX XXX
   X    *  * X  X XX X XXXX
   X *XXX XXXX  X X X XX  XXXX
   X  * ***  X XX X  XX      X
   XX        X XX XXXX ***   X
    XX XXXXXXX .....     XXXXX
    X  *         XXXXXX  X
    X   XXXXXX  XX    XXXX
    XXXXX    XXXX

; 44

 XXXXXXXXXXXXX
XX       X   XXX
X  * *****     X
XXX *   *  XXX X
  X * * *XXX X X
  XX   * XX  X XXX
   XXXX   XXXX   X
     XXX       X XXX
   XXXX   XXXX     X
   X@ *   XXX  X.X XXXXX
   X * * XX X  ....    X
   X ** XX  XXXX.....  X
  XX *  X     X..X.XX  X
  X * * XX    X......  X
  X  * * X    X . ..X XX
  XX  *  X    XX XX.X X
   X    XX     X      X
   XXXXXX      XXXXXXXX

; 45

  XXXX      XXXXXXXX
  X  XXXXX XX   X  X
  X    * XXX *  *  X
  X  * X XX    *   XXXX
  XXX  X    X XXX*XX  X
XXXXX  XXX  XXXX   *  X
X   X *  **XX .. XX*  X
X  **   X *          XX
XX  X *XX  XXXX X XXXX
XXX X  XX* XXX..X..X
X   XXX..  X  .....XXX
X   X  *.XXX X  X..  X
XX**X  *.XX@ X  X    X
 X     *. XXXX  XXX  X
 XXXXXX   X  X       X
      XXXXX  XX    XXX
              X  XXX
              XXXX

; 46

      XXXX XXXXXXXXXXXXXXXXXXX
  XXXXX  XXX            .*   X
XXX  *.       XXXXX*XXXX   X X
X    *.  XXXX X     .   XXX .X
X  * *.XXX XX X XXXX X  *.X *X
XXX  *.XX X X X X  X  X * X  X
  XXXXXX X XX X* * XX   X. X X
        XXXXX X.X.  X  XXX X X
 XXXXX  X   X XXX XXX   X    X
 XX*XX  X     .X  X   X***  XX
 X*XXX XXX XX XX XX X  .X. XX
 XXX*X X  .* .X *.*.XX XXX X
 XX*XX X X.XXXX     X *.   XX
 X*XXX X **   XXX XXX   XX  XX
 XXX*X X X   . *@*  XXXXXXX. X
 XXXXX X XXX XXXX.X        * X
       X     X  XXXXXXXXXXX  X
       XXXXXXX            XXXX

; 47

XXXXXXXXX
X       X    XXXXXX
X   *   XXXXXX    XXX
X X*X* * *  X *     X
X *   *@*  * * * ** X
X * *X * X     ***  X
X  * * XXXXXXX   XXXXX
XX    XXX....XXXXX ..X
 XXX**X **** X...* ..X
  X         XX   X.. X
  X  X  X*XXX....XX*XX
  X   XX..*. ....    X
  XXX .*   .X....X   X
    XXXXXXXXXXXXXXXXXX

; 48

   XXXX XXXX
  XX  X X  X  XXXXXXX
XXX   XXX* XX X     XXX
X  *      * XXX       X
X * * XXX*   X  X     X
XXX XXX X    X   X    X
X  * X  XX XXX    X XXX
X    *   X X@        XX
X *X X XXX XXX   X   X
X  * X X * * X  X  X X
XX   X    *  X X.    X
 XX  X X   XX X..  XXX
  XX X X  XX X... XX
 XXX X XXXX X....XX
 X          *.*.XX
 XXXXXXXXXXXX..XX
            XXXX

; 49 'Parallel Logic'

XXXXXXXXXXXXXXXXXXXXXXXXX
X  X  X  X  X  X  X  X  X
X *X* X *X* X *X* X *X* X
X  X  X  X  X  X  X  X  X
XX X XXX X XXX X XXX X XX
X  X  X  X  X  X  X  X  X
X     X     X     X     X
X XXX X XXX X XXX X XXX X
X  X  X  X  X  X  X  X  X
X  X     X  *  X     X  X
X  X XXX X XXX X XXX X  X
X  . . .  . + .  . . .  X
XXXXXXXXXXXXXXXXXXXXXXXXX

; 50 'Particle Theory'

  X X X X X X X X X X X X
 X X X X X X X X X X X X X
X   .*    . *.  . *   .*  X
 X *X X*X X X X*X X X X  X
X  .  .    *.  .  .* .  . X
 X X*X X X X X*X* *X X*X X
X .     .* .*    . *.  .  X
 X *X X X X X@X X X X X* X
X  .  .* .    *. *.     . X
 X X*X X* *X*X X X X X*X X
X .  . *.  .  .*    .  .  X
 X  X X X X*X X X X*X X* X
X  *.   * .  .* .    *.   X
 X X X X X X X X X X X X X
  X X X X X X X X X X X X

; Sasquatch Set II


; 1

XXXXX
X   XXXXX
X * * * X
XXX X X X
  X X   X
 XX XXX XX
 X .....@X
 X * *   X
 X XXX XXX
 X     X
 XXXXXXX

; 2

     XXXX
XXXXXX..X
X     . X
X  X  ..X
X  XX XXX
X    *  XX
X  X X* @X
X  X * * X
X  XX * XX
XXXXX   X
    XXXXX

; 3

          XXXXX
         XX   XX
         X     XX
         X    @ X
XXXXXXXXXXXX X. X
X            X.XX
X XXXXXXXXXXXX.X
X             .X
XX*X*X*X*X*X*X.X
 X            .X
 XXXXXXXXXXXXXXX

; 4

       XXXXX
     XXX   X
XXXX X  ** XXXX
X  XXX  *  X  X
X    XXX**  * X
X *X  @  XX X X
XX XXXXX X..X XX
 X    XX X..X  X
 XX  * X X..   X
X XX * X  ..XXXX
 X XX    X  X
  X XXXX   XX
   X   XXXXX

; 5

     XXXXX
  XXXX   X
  X  . X XXX
  X *. * * X
  X X.XX * X
XXX@X..X*  X
X   XX.X  XX
X * * .X *X
XX XXX.XX X
 X        X
 XXXXX  XXX
     XXXX

; 6

    XXXXX
   XX   XXXXXX
   X  @   X  X
   X  X  * * X
XXXX  XXX*X. X
X.....X    .XX
X.....X X*X. XXX
XXX     . XX   X
 X  XX XX* XXX XXXX
 X   X  X  *  *   X
 X   ***X X  *  * X
 XXXXX  X XXXXXX  X
     X*    X   XXXX
    XX * X X
    X *    X
    X    XXX
    XXXXXX

; 7

         XXXXX
XXXXXXXXXX   X
X. ........ .XX
X  XXXX    X  XX
XX *   X    X  XX
 X *  X X    X  XX
 X * * X X    X  X
 X *  *   X    @ X
 X * **  X       X
 X *XX XXXXXXXXXXX
 X  X  X
 X    XX
 XXXXXX

; 8

     XXXXXXXXX
 XXXXX       X
XX      XXXX X
X * X  @ *..*XXX
X  X  X X....  X
X  X*X  X....  X
X *X X XX*XXX  X
X    X*       XX
XX  *  *X  XXXX
 XX  *  XXXX
  XXX ** X   X
    X    X XXX
    XXXXXX

; 9

              XXXX
           XXXX  XX XXX
        XXXX  *   X X*X XXXX
 XXXXXXXX  *   *  X XXX X  X
 X  * * *   * XX  X     X  XX
XX *     * XXXX * XXXXXXX   X
X   ** XXXXX *   XX      X  X
X  XX XX  *   *  X          X
X.X  * X * *  XXXX  XX XX   X
X.X  * * * XXXX        X    X
X.X.X   *  X           X    X
X.X.  XXX  X     XXXXXXXX   X
X.X.XXX@XXXX XX  X         XX
X.............   X XXXXXX  X
X  .XXXXXXXXXXX XX X    XXXX
XXXXX         X    X
              XXXXXX

; 10

             XXXX
   XXXXX XXXXX  XX
  XX   XXX       XX
 XX   * * . * X @ XX
 X  XX * XX XXX X  X
 X XX *  X  X *  X X
 X X *  X  X     X X
XX X   XX X X XXX  X
X  XX X X. * .XX  XX
X X.X XX XX X.X  XX
X X  *  X. * .* XX
X   X*  *.X  . XX
XXXXX XX XX X XX
    X X *  X  X
    X X    X XX
    X  X*XX  X
    XX      XX
     XXXXXXXX

; 11

    XXXX
    X  XXXX
    X *   XXXXXXXXX
    X .X    * XX  X
    X *X .XX *    XX
 XXXX .XXX   X**   X
XX  XX X  .. X **  X
X  *      ...X   * X
X *  XXXXX... X   XX
X  *X   X  .**@XXXX
XXX   X X    X X
  XXXXX  XXXX  X X
      XX      XX
       XXXXXXXX

; 12

X  XXX
 XX   XX
 X*.*  X
X .*.* .XX
X *.*.*  X
X  *.@.*  X
 X  *.*.* X
 XX. *.*. X
   X  *.*X
   XX   XX
     XXX  X

; 13

    XXXXX
    X   XXXXX
    X X X   X
    X     X X
 XXXXX.X ...XXXXX
 X  .** XXX*X   X
 X X.X     *. X X
 X  .X ***  X   X
XXX  X *@* X  XXX
X   X  *** X.  X
X X .*     X.X X
X   X*XXX **.  X
XXXXX... X.XXXXX
    X X     X
    X   X X X
    XXXXX   X
        XXXXX

; 14

    XXXXXXX
    X     XXX
    X XXX*  XX
    X....*   X
  XXX XX X   X
XXX@.*  X X XX
X .*.*   XX X
X  *.*  X.**X
X  XX XX    X
XXXXX   X XXX
    XXX  * X
      XX   X
       XXXXX

; 15

  XXXXX
  X   XXXXX
  X **X   XXXXX
  X   . * X   XXXXX
 XXX XX   . * X   XXXXX
 X   XX.XXX ....* X   XXXXX
 X **X   XXX.XX.  X * X   X
 X   X * X  .XX.XXX   .** X
XXX XX   .***X   XXX.XX   X
X   XX.XXX   X***.   XX XXX
X **.   XXX.XX.  X * X   X
X   X * X  .XX.XXX   X** X
XXXXX   X *.... XXX.XX   X
    XXXXX   X * .   XX XXX
        XXXXX   X * .   X
            XXXXX   X** X
                XXXXX  @X
                    XXXXX

; 16

XXXXXXXXXXXXX
X           X
X .*.*.*.*. X
X *.*.*.*.* X
X .*.*.*.*. X
X *.*.*.*.* X
X .*.*@*.*. X
X *.*.*.*.* X
X .*.*.*.*. X
X *.*.*.*.* X
X .*.*.*.*. X
X           X
XXXXXXXXXXXXX

; 17

XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                           X
X .*.*.*.*.*.*.*.*.*.*.*.*. X
X *.*.*.*.*.*.*.*.*.*.*.*.* X
X .*.*.*.*.*.*.*.*.*.*.*.*. X
X *.*.*.*.*.*.*.*.*.*.*.*.* X
X .*.*.*.*.*.*.*.*.*.*.*.*. X
X *.*.*.*.*.*.*.*.*.*.*.*.* X
X .*.*.*.*.*.*@*.*.*.*.*.*. X
X *.*.*.*.*.*.*.*.*.*.*.*.* X
X .*.*.*.*.*.*.*.*.*.*.*.*. X
X *.*.*.*.*.*.*.*.*.*.*.*.* X
X .*.*.*.*.*.*.*.*.*.*.*.*. X
X *.*.*.*.*.*.*.*.*.*.*.*.* X
X .*.*.*.*.*.*.*.*.*.*.*.*. X
X                           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; 18

  XXXXXXXXXXXXXXXXXXXXX
 XX        X     X    X
 X  * * *  X* * * *  *XXX
 X *XXXXX **  *XX XX *  X
 X  X  ..X   X X    X   X
 XX*   ... X X   ...X* XX
XX   * ... X* X  ...*  XX
X  *XXXX..X    XX...XX* X
X    *.*..**@**..*.*    X
X *XX...XX    X..XXXX*  X
XX  *...  X *X ... *   XX
XX *X...   X X ...   *XX
X   X    X X   X..  X  X
X  * XX XX*  ** XXXXX* X
XXX*  * * * *X  * * *  X
  X    X     X        XX
  XXXXXXXXXXXXXXXXXXXXX

; 19

       XXXXX  XXXXX
       X   X  X   X
       X X.XXXX.X X
       X ..    .. X
XXXXX  XXX XXXX XXX
X   X    X X    X
X X XX   X X@XX X
X  * XX  X X  X XXX
XX  * XX X *  *.. X
 XX  * XXX X  X.X X
  XX  * XX XX X   X
   XX  * X X  XXXXX
    XX  *  * XX
     XXXXX  XX
         XXXX

; 20

          XXXXXXXXX
     XXXX X       X
  XXXX  X X *     X
  X  X  XXXX.X    X
  X   * *   .XXXX X
  X  *X*XX X.X....X
XXX X *  X X.X....X
X  * *  X X..*....X
X X XX *  X XXXX  X
X  * X X *X      XX
XX  *  X    XXXXXX
 XX  * X ***X
  XX **@XX  X
   XX      XX
    XXXXXXXX

; 21

   XXXXXXXXXXXXX
   X     X     X
   X * * * * * X
   XXX XXXXX XXX
XXXX.*   *   *.XXXX
X ...X * X * X... X
X  *XX*X.X.X*XX*  X
XX   . . @ . .   XX
X  *XX*X.X.X*XX*  X
X ...X * X * X... X
XXXX.*   *   *.XXXX
   XXX XXXXX XXX
   X * * * * * X
   X     X     X
   XXXXXXXXXXXXX

; 22

   XXXXXXXXXX
  XX        X
 XX    XXX  XXXXXXX
 X ** X    *X  X  X
 X  XXX  X**      X
 X    ** X     X**X
 X  X   XXXX X*   X
 XX X XXX.*. X XX X
XX *.*.X..*.XX    XXX
X  ***...**.XXX **  X
X X....X...X  X   X X
X  XX XX.*. * X XXX X
XX  X * ..XX   *  X X
 XX X **XXX *X**  X X
  X  @  X   *    X  X
  XXXXX   XX*XXXX  XX
      XXXXXX      XX
           XXXXXXXX

; 23

XXXXXXXXXXXXXX XXXXXXX
X             X       X
X.XXXXXXXXXX  X*XXXXX  X
X           X        X  X
X*XXXXXXXX  X XXXXXX  X  X
X         X         X  X  X
X*XXXXXX  X XXXXXXX  X  X  X
X       X          X  X  X  X
X*XXXX  X XXXXXXXX  X  X  X  X
X     X           X  X  X  X X
X*XX  X XXXXXXXXX  X  X  X X X
X   X            X  X  X X X X
X*  X XXXXXXXXXX  X  X X X X X
X X             X  X X X X X X
X X XXXXXXXXXXX  X X X X X X X
X. @           * * * * * * . X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; 24

                    XXXX
              XXXXXXX  X
              X      * XX
    XXXXXXXX  X ..XX *  X
           XX XX.X  X   X
   XXXXXXX     X.X * *XXX
 XXX     XXXXXXX.X  X XX
 X   XX    X   *.  **  X
 X XX  X.X X@X X.X  XX X
 X  **  .*   X    XX   X
 XX X  X.XXXXXXX     XXX
XXX* * X.X     XXXXXXX
X   X  X.XX XX
X  * XX.. X  XXXXXXXX
XX *      X
 X  XXXXXXX
 XXXX

; 25

  XXXXXX
  XX   XXXXXXXXXXX
  X * *  *  X *  XXXXXX
  X .*.X..*.X .*     XX
  X *  X * *  * *X*.* X
 XX XXXX    X .  X *  X
 X  * XXXXXXXXX.XX .* X
 X.*.. *        XXXX XX
 X* * X*X.**.*X X    X
 X    X X*.**.X*X * *X
XX XXXX        * ..*.X
X *. XX.XXXXXXXXX *  X
X  * X  . X    XXXX XX
X *.*X* *  * * X .* X
XX     *. X.*..X * @X
XXXXXX  * X  *  *.* X
     XXXXXXXXXXX   XX
               XXXXXX

; 26

XXXXXX    XXXXXXX
X  ..X    X  X  X
X  ..XXXXXX *X  X
XX X.  * XX  *  X
 X  ***   X XX*XX
 X.X. X* *  X  X
 X.X.XX XX  *  X
 X.X   *  X X  X
 X. XX   @X XX*X
 X.   XXXX     X
 X.      *  *X X
 X. XXXXXXXX   X
 XXXX      XXXXX

; 27

XXXXXXXXXXXXXXXX
X   X   XX  X  X
X .*. *  X . . X
XX XXX X  * X* X
X . X  XXX XX.XX
X  * .*  X. X  X
XXX XX X  *  * X
XX  X  XXX XX  X
X  XX XXX  X  XX
X *  *  X XX XXX
X  X .X  *. *  X
XX.XX XXX  X . X
X *X *  X XXX XX
X . . X@ * .*. X
X  X  XX   X   X
XXXXXXXXXXXXXXXX

; 28

 XXXXXXXXXX
 X    X   X
 X *  X   X     XXXX  XXXXX
 XXX **   XXXXXXX  XXXX   X
XX *  *  XXX   XX  *      X
X *   XXX  X X XX  XXXXX XXX
X  X*X       ..XXX XX  X   X
X    X  X.X X.. X   X *  * X
XXX * * X.X X.. X   X  XX XX
  X  X  X.X  XXXX XXXX XX  X
 XXXXXXXX.X         X *  * X
 X  ..  X.X XXXXXX  X   X  X
 X.****.X.X X   X  XXXX XXXX
 X.* @*.X.X X X X  *      X
 X.****.X.X X   X  XXXX   X
 X  ..   .  X   XXXX  XXXXX
 XXXXXXXXXXXX

; 29

                XXXXX
          XXXXXXX   X XXXXX
     XXXXXX       X.XXX   X
    XX      X XXX X.    * X
    X  XXXXXX XX  X  XXX XX
    X XX * ..* X *   XX  X
    X X  * *.*@XXXXX X  XX
    X X    ..* X *   X XX
XXXXX*XXXXXXX*XX X .   X
X *            . XXXX XXXX
X **X XXXXXXXXX*XX   .   X
X X . .X      .  X ***** X
X   .  X *.*.X   X... ...X
XXXXX * X XX XXXXX ***** X
    X.X    X         .   X
    XXXXXXXXXXXXXXXXXXXXXX

; 30

    XXXX
XXXXX  XXXXXXXXXX
X      X  X     X
X X  ..   XX   *XXX
X X XX.X.  X ***@ X
X      X.  X *  X X
X   XXXXXXXX *  X X
XXX    *       XX X
  X.XXXXXXXXXXXX  X
  X.             XX
  XXXXXXXXXXXXXXXX

; 31

 XXXXX
XX   X XXXX
X    XXX  X
X  X @X   X
XX*XXXX   XXXXXX
X ...    XX    XX
X ...  X    XX  X
XXXX X XXXXX  X XX
   X X       *X  X
   X X * * **  X X
   X  XXXXX    X X
   XX      X   X X
    XXXXXX  XXX  X
         XX     XX
          XXXXXXX

; 32

      X
    XX XX
    X   X
   X .*. X
 XX  *.*  XX
 X .*.*.*. X
X  *.*+*.*  X
 X .*.*.*. X
 XX  *.** XX
   X .*.    X
    X   X X X
    XX XX   X
      X  XXX

; 33

XXXXX
X   XX
X  * XXXXX
XX  * X  X
 XX * X *XXXXXXXXXXX
  XX      * * * *  X
   XXXXX* X X X  X X
       X      X    X
       X XXXXXXX*XXXXXXX
      XX         X@X   X
      X  X X XX  X     X
      X..*.*.*......   X
      XXXXXXXXXX    X XX
               XXXX   X
                  XXXXX

; 34

 XXXXX  XXXXX
 X   XXXX   X
XX X*.*.* X X
X   *.@.*   X
X X *.*.*X XX
X   XXXX   X
XXXXX  XXXXX

; 35

         XXXXX
XXXXXXXXXX   X
X      * *** X
X *XX X  X X X
X *    X X X X
XX*XX .X.    X
 X   ..... X X
 X* XX.@.XX *X
 X X .....   X
 X    .X. XX*XX
 X X X X    * X
 X X X  X XX* X
 X *** *      X
 X   XXXXXXXXXX
 XXXXX

; 36

 XXXXXXX XXXXXXX
XX  .  XXX     XX
X **.** X .*.*. X
X * . * X *.*.* X
X...X...  .*@*. X
X * . * X *.*.* X
X **.** X .*.*. X
XX  .  XXX     XX
 XXX XXX XXX XXX
XX     XXX     XX
X .*.*. X .***. X
X *.*.* X *...* X
X .* *.   *.X.* X
X *.*.* X *...* X
X .*.*. X .***. X
XX     XXX     XX
 XXXXXXX XXXXXXX

; 37

            XXXXX
        XXXXX   XXXXX
    XXXXX   X * X   XXXXX
XXXXX   X **     ** X   XXXXX
X   X** .   XX*XX   . **X   X
X **.   XXXXX . XXXXX   .** X
X   XXXXX   XX.XX   XXXXX   X
XX* X   X.... . ....X   X *XX
 X  . * .   X @ X   . * .  X
XX* X   X.... . ....X   X *XX
X   XXXXX   XX.XX   XXXXX   X
X **.   XXXXX . XXXXX   .** X
X   X** .   XX*XX   . **X   X
XXXXX   X **     ** X   XXXXX
    XXXXX   X * X   XXXXX
        XXXXX   XXXXX
            XXXXX

; 38

XXXXX                 XXXXX
X   XXXXXXXXXXXXXXXXXXX   X
X X * * * * * * * * * * X X
X * X     X     X     X * X
XX  X.XXX.X.XXX.X.XXX.X  XX
 X* X  .  X  *  X  .  X *X
 X  .  X  .  X  .  X  .  X
 X*XXX.X.XXX.@.XXX.X.XXX*X
 X  .  X  .  X  .  X  .  X
 X* X  .  X  *  X  .  X *X
XX  X.XXX.X.XXX.X.XXX.X  XX
X * X     X     X     X * X
X X * * * * * * * * * * X X
X   XXXXXXXXXXXXXXXXXXX   X
XXXXX                 XXXXX

; 39

 XXXXXXXXXXXXXXXXX
 X               X
XX*X.X.X.X.X.X.X*XX
X  *.*.*.*.*.*.*  X
X  X*X* *@* *X*X  X
X  *.*.*.*.*.*.*  X
XX*X.X.X.X.X.X.X*XX
 X               X
 XXXXXXXXXXXXXXXXX

; 40

                XXXXX
  XXXXXXXXXXXXXXX   XXXXXXXX
 XX * * * * *    * * * * * XX
XXX     X         X        XXX
X  X.XX.X.XX.X.XX.X.XX.X.XX  X
X *X  .* *  *X  .* *  *X  .* X
X  .  X*  * *.  X*  * *.  X  X
X *XX.X.XX.X.XX.X.XX.X.XX.X* X
XX      .  X   @  .  X      XX
XX      X  .      X  .      XX
X *X.XX.X.XX.X.XX.X.XX.X.XX* X
X  X  .* *  *X  .* *  *X  .  X
X *.  X*  * *.  X*  * *.  X* X
X  XX.X.XX.X.XX.X.XX.X.XX.X  X
XXX        X         X     XXX
 XX * * * * *    * * * * * XX
  XXXXXXXX   XXXXXXXXXXXXXXX
         XXXXX

; 41

 XXXXXXXXXXX
XX    X    XX
X ***.*.*** X
X...     ...X
X ***.*.*** X
XX    *    XX
X ***.*.*** X
X...  @  ...X
X ***.*.*** X
XX    X    XX
 XXXXXXXXXXX

; 42

XXXXXXXXXXX
X         X
X *XX XXX XX   XXXXX
X  X * * * XXXXX   XXX
X *    X     X *. .  X
X  XX*XXX*XX X X...X X
X *    X     X X. .X XX
XX X * * *XX X X...X  X
X  XX XXX X. X X. . X X
X *       X    X    X X
X @XXXXXXXX XXX     X X
XXXX     X       XXX  X
         X XXXX  X   XX
         X     XX  XXX
         XXXXX    XX
             XXXXXX

; 43

         XXXXXXX
  XXXXXXXX  X. X
  X        * * XXXXX
  X XX XX   X. X   X      XXXX
XXX X * **X*X. X X XXXXXXXX  X
X  *X   X  * * X......       X
X *    XXX *X.  X  XXXX      X
XX X X** X * .X X  X  XX     X
 X X   *   @XX  X XX   XX   XX
 X  XX  *** X  XX XXX   XXXXX
 XX  X.XX.XXX       X
  XX X**.*...  XX   X
   X   X   XX  XX  XX
   XXX   XXXXXXXXXXX
     XXXXX

; 44

     XXXXXXX
     X  @  X
XXXXXX XXX XXXXXX
X   X   *   X   X
X   *   X   *   X
XX*XXX*XXX*XXX*XX
X   *   X   *   X
X   X   *   X   X
XX*XXX*XXX*XXX*XX
X   X   *   X   X
X ..*...X...*.. X
XXXXXX XXX XXXXXX
     X     X
     XXXXXXX

; 45

              XXXX
           XXXX .X
     XXXX  X    .XXXX
   XXX  XXXX  XX..  XX
   X  * X  X* X...   X
   X X  X  X  X...   X
   X X* X * * X      X
XXXX  *    X  X    @XX
X     X X**XXXXX   XX
X   * * X  X   XXXXX
XXXXXX  X  X
     XXXX  X
        XXXX

; 46

         XXXX XXXX
         X  XXX  X
      XXXX * *   XXXXXXX
      X   *   X*   XX  XXXX
      X XXX XXX        X  X
     XX  *   XXXXXX X     X
     X  * X XX    XXXXX   X
     X X X  X  X ** X XX XXX
     X X    X*.XX *        X
     X XXXXXX   *  X XXX   XX
     X....*.**.X X   X X   XX
     XXXX      X XXXXX XXXXX
       XX*XX XXX*X
      XX  X   *  X
XXXXXXX   X *    XXXXXXXXXXXXX
X *      XXXXXX XX         @ X
X        .........           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; 47

      XXXXX
      X . X
  XXXXX . XXXXX
  X   * . *   X
  X * XX.XX * X
  X   X * X   X
XXX*XX     XX*XXX
X   X  ***  X   X
X....* *@* *....X
X   X  ***  X   X
XXX*XX     XX*XXX
  X   X * X   X
  X * XX.XX * X
  X   * . *   X
  XXXXX . XXXXX
      X . X
      XXXXX

; 48

        X
       X X
     XX   XX
     X *.* X
    X  . .  X
  XX *.*.*.* XX
  X  . X X .  X
 X *.*X * X*.* X
X  . . *@* . .  X
 X *.*X * X*.* X
  X  . X X .  X
  XX *.*.*.* XX
    X  . .  X
     X *.* X
     XX   XX
       X X
        X

; 49

    XXXX
    X  XXXXXX
    X  * *  XXX    XXXX
    X   *     X   XX  X
XXXXX*X*X***  X  XX * X
X     * *   * X XX    X
X  X*    * *XXXXX ** XX
XX X XXXX  .....X   XX
X      X *  **.XX XXX
X   X  X ** X.XX.   X
XX     X    X.X+* X X
 X     XXXXXX.XX..* X
 XXXXXXX X *..XX.XXXX
         X X *..*.X
         X   .X.  X
         XXXXXX*X X
              X   X
              XXXXX

; 50

XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X.      .   .   .   .      .X
X XX  X X   X X X   X X  XX X
X XX  * X * X * X * X *  XX X
X  XX***X***X***X***X***XX  X
X   *...*...*...*...*...*   X
X  **.X.*.X.*.X.*.X.*.X.**  X
X   *...*...*...*...*...*   X
X.XXX***X***X*@*X***X***XXX.X
X   *...*...*...*...*...*   X
X  **.X.*.X.*.X.*.X.*.X.**  X
X   *...*...*...*...*...*   X
X  XX***X***X***X***X***XX  X
X XX  * X * X * X * X *  XX X
X XX  X X   X X X   X X  XX X
X.      .   .   .   .      .X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; Sasquatch Set III

; 1

 XXXXXXX
 X  *  X
 X  @  X
 XX*X.XX
 X  X  X
 X *X. X
 X  X  X
XX XX XX
X  * * X
X   *  X
XXX   XX
  XXXXX

; 2

      XXXX
XXXXXXX  X
X     * .XX
X **X  *  XX
X *@ X* *  XX
XX * X * *  X
 XXX X. * * X
 X   .  X  .X
 X   X  XXXXX
 XXXXXXXX

; 3

        XXXX
XXXXXXXXX  X
X          X
X X*XXX X  X
X  *   X X X
X*X*XX  X  X
X  *  X  X X
X  *X  X X X
X  * X X X XX
XXX*. . . . X
  X@XXXXXXX X
  X         X
  XXXXXXXXXXX

; 4

   XXXXXXXXXXXXX
  XX           X
 XX  XXXXXXXXX@XXX
XX  X         *  X
X  XX XXXXXXXX*X X
X X  * * * *   X X
X X*.. . . ..*X  X
X X .XXXXXXX. X XX
X  *.XXXXXXX.*X X
XXX . . . . . X X
  X * * * * * X X
  XXXXXXXXX XX  X
          X * * X
          X     X
          XXXXXXX

; 5

 XXXXXXXXXXX
XX         X
X  XXXXXXX*XX
X X       * XXX
X X...***.*.@ X
X X       * X X
X  XXXXXXX*X  X
XX        *  XX
 XXXXXXXX   XX
        XXXXX

; 6

             XXXX
     XXXXXXXXX  XXX
     X  . .   . . X
     X **.*X X*.* X
     XX . .X X. . X
      X * *X  * * X
      X *  X* XXXXX
     XXXXX X XX
     X   @   X
    XX X XXXXX
XXXXX *X  * X
X * *  X* * X
X . .X X. . XX
X *.*X X*.** X
X . .   . .  X
XXX  XXXXXXXXX
  XXXX

; 7

  XXXXX
  X   XXXXX
XXX X     XX
X  * XXXX  X
X  * XX  X X
X  *  ** X X
X   X    X X
X@X** * XX X
XXX  X*  X X
 X .* .* X X
 X   X  X  X
 XX  X    XX
  XXXXXXXXX

; 8

       XXXX
XXXXXXXX@ X
X   ...X* X
X * * * * X
XXXXX   . X
   XX*X*. X
 XXX. X .XX
 X  .*X* X
 X  .*   X
 XXX.*X  X
   X  XXXX
   XXXX

; 9

        X
 XXXXXXXXXXX
 X   X  X  X
 X * X* *  X
 X*.*.*.X* X
 X .    *. X
 X*.*X.  .*X
XX .*   X* XX
X  .X.*XX.  X
X * *   *   X
XXX X X XXXXX
  XX@   X
   XXXXXX

; 10

           X
    X     X X
   X X  XX   XX
  X . X X .*. X
 X *.* X .* *. X
X   *  @ * * *  X
 X *.* X .* *. X
  X . X X .*. X
   X X  XX   XX
    X     X X
           X

; 11

       X
      X X
    XX   XX
    X  .  X     X
  XX *.*.* XX  X X
  X *.*.*.* X X . X
 X  .*.*.*.  X *.* X
X  .*.*@*.*.    *   X
 X  .*.*.*.  X *.* X
  X *.*.*.* X X . X
  XX *.*.* XX  X X
    X  .  X     X
    XX   XX
      X X
       X

; 12

XXXXXXXX
X  . . X
X *.*. X
XX*X*X XX
 X . .  X
 X*X*X @X
 X . .  X
XX*X*X XX
X  . . X
X *X*X XXX
XX   . . X
 XXX*X*X X
   X .   X
   X*X XXX
   X   X
   XXXXX

; 13

       XXXX
XXXXXXXX  X
X@ * * ** XXX
X  ....*.*  X
XX XXX ..*X X
 X**  X .*  X
 X X * X.*X X
 X   * X..  X
 XX  *    XXX
  XXX X*X.X
   X * *  X
   X     XX
   XXXXXXX

; 14

          XXXXX
  XXXXXXXXX   X
XXX * * * *.  X
X  .*.* *.*.X X
X X.*..@..*.X X
X X.*.* *.*.  X
X  .* * * * XXX
X   XXXXXXXXX
XXXXX

; 15

           XXXXX
XXXXXXXXXXXX   XXXXXXX
X     X X XX X X X   X
X X X*  *  X .*  * X XX
X  ..*.** *@* **.*..  X
XX X *  *. X  *  *X X X
 X   X X X XX X X     X
 XXXXXXX   XXXXXXXXXXXX
       XXXXX

; 16

 XXXXXXXXX
XX   *   XX
X  X X X  X
X X.*.*.X X
X  *.*.*  X
X*X.*@*.X*X
X  *.*.*  X
X X.*.*.X X
X  X X X  X
XX   *   XX
 XXXXXXXXX

; 17

         X
    X  XXXXX
  XXXXX    XXXX
  X   ..** X  X
  X * * .X@X* XX
 XXXX X *XX   X
 X   X  *  X*.X
XX *XX  .    . X
 X *.**.X.**.* X
 X .    .  XX* XX
  X.*X  *  X   X
  X   XX* X XXXX
 XX *X X. * * X
  X  X **..   X
  XXXX    XXXXX
     XXXXX  X
       X

; 18

 XXXXXXXXXXXXX
XX    X   X  XX
X .XX**  *  . X
X  ...X.X.X.X X
XX X * *   .X X
X *. X X X*.* X
X  X  * *  X*XX
X  .*X @ X*.  X
XX*X  * *  X  X
X *.*X X X .* X
X X.   * * X XX
X X.X.X.X...  X
X .  *  **XX. X
XX  X   X    XX
 XXXXXXXXXXXXX

; 19

 XXXXXXXXXXXXX
XX     *     XX
X  XX.X XX.X  X
X X * * * * X X
X .*. XX  .*X X
X X  X . X  . X
X X*  *.* X*X X
X*  X..@..X  *X
X X*X *.*  *X X
X .  X . X  X X
X X*.  XX .*. X
X X * * * * X X
X  X.XX X.XX  X
XX     *     XX
 XXXXXXXXXXXXX

; 20

 XXX XXX XXX
XX  X @ X  XX
X  *X* *X*  X
X . . . . . X
 XX*X* *X*XX
X . . . . . X
X  * *X* *  X
X . . . . . X
 XX*X* *X*XX
X . . . . . X
X  *X* *X*  X
XX  X   X  XX
 XXX XXX XXX

; 21

   XXX   XXX
   X  XXX  X
  X    X    X
XX  ***.***  XX
X  .X . . X.  X
X  . X * X .  X
 X .* X.X *. X
 XX* .*@*. *XX
 X .* X.X *. X
X  . X * X .  X
X  .X . . X.  X
XX  ***.***  XX
  X    X    X
   X  XXX  X
   XXX   XXX

; 22

   XXXXXXXXXXX
  X           X
 XX*XXXX.XXXX*XX
X *. * *.* * .* X
X X ...   ... X X
X X*.* *.* *.*X X
X X . *X.X* . X X
X X* *X * X* *X X
X .. ..*@*.. .. X
X X* *X * X* *X X
X X . *X.X* . X X
X X*.* *.* *.*X X
X X ...   ... X X
X *. * *.* * .* X
 XX*XXXX.XXXX*XX
  X           X
   XXXXXXXXXXX

; 23

 XXXX XXX XXXX
X    X   X    X
X X  X   X  X X
X  *********  X
X  * .   . *  X
 XX*.XX XX.*XX
X  * X   X *  X
X  *   @   *  X
X  * X   X *  X
 XX*.XX XX.*XX
X  * .   . *  X
X  *********  X
X X  X   X  X X
X    X   X    X
 XXXX XXX XXXX

; 24

 XXXXXXXXXXXXXXX
 X.  *  .  *  .X
 X XX*X X X*XX X
 X  .* .X. *.  X
 X X   ***   X X
XX***   X   ***XX
X  X. *. .* .X  X
X@   X* * *X    X
X  X. *. .* .X  X
XX***   X   ***XX
 X X   ***   X X
 X  .* .X. *.  X
 X XX*X X X*XX X
 X.  *  .  *  .X
 XXXXXXXXXXXXXXX

; 25

X XXXX  X  XXXX X
 X    X   X    X
X *.   XXX   .* X
X *X * * * * X* X
X   X .* *. X   X
X  . X  *  X .  X
 X  * XX*XX *  X
  X.* X . X *.X
X X  ..*@*..  X X
  X.* X . X *.X
 X  * XX*XX *  X
X  . X  *  X .  X
X   X .* *. X   X
X *X * * * * X* X
X *.   XXX   .* X
 X    X   X    X
X XXXX  X  XXXX X

; 26

 XXXXXXXXXXXXXXX
XX      X      XX
X ** ******* ** X
X *...*...*...* X
X  .*.*.*.*.*.  X
X *...*...*...* X
X ************* X
X *...*...*...* X
XX*.*.*.@.*.*.*XX
X *...*...*...* X
X ************* X
X *...*...*...* X
X  .*.*.*.*.*.  X
X *...*...*...* X
X ** ******* ** X
XX      X      XX
 XXXXXXXXXXXXXXX

; 27

  XXXXXXXXXXXXX
 XX .   .   . XX
XX *.* *.* *.* XX
X * * * * * * * X
X..*.*.*.*.*.*..X
X * * * * * * * X
X  *.*.*.*.*.*  X
X * * * * * * * X
X..*.*.*@*.*.*..X
X * * * * * * * X
X  *.*.*.*.*.*  X
X * * * * * * * X
X..*.*.*.*.*.*..X
X * * * * * * * X
XX *.* *.* *.* XX
 XX .   .   . XX
  XXXXXXXXXXXXX

; 28

      XXXXX
   XXXX . XXXX
   X XX*.*XX X
 XXXX   .   XXXX
 X XX **.** XX X
 XX  XX . XX  XX
XXX *XX*.*XX* XXX
X * * *...* * * X
X.......@.......X
X * * *...* * * X
XXX *XX*.*XX* XXX
 XX  XX . XX  XX
 X XX **.** XX X
 XXXX   .   XXXX
   X XX*.*XX X
   XXXX . XXXX
      XXXXX

; 29

XXXXXXXXXXXXXXXXX
X  .    .    .  X
X XX*XXX*XXX*XX XXXXXXXXXXXXX
X.XX  XX  XX XX.X  .     .  X
X *   *   *   * X XX*XXX*XX X
X XX  X   X   X X.XX  XX XX.X
X XX*XXX*XXX*XX X *   *   * X
X X   X   X  XX X XX  X   X X
X.*   *   *   *.@ XX*XXX*XX X
X XX  X   X   X X X   X  XX X
X XX*XXX*XXX*XX X *   *   * X
X X   X   X  XX X.XX XX  XX.X
X *   *   *   * X XX*XXX*XX X
X.XX XX  XX  XX.X  .     .  X
X XX*XXX*XXX*XX XXXXXXXXXXXXX
X  .    .    .  X
XXXXXXXXXXXXXXXXX

; 30

 XXXXXXXXXXXXXXX
XX             XX
X  XXXXX XXXXX  X XXXXXXXXXXX
X X . . . . . X XXX         XX
X X* * * * * *X     XXX XXX  X
X X .X.X.X.X. X XX X . . . X X
X X* * * * * *X XX X* * * *X X
X X .X.X.X.X. X XX X .X.X. X X
X  * * *@* * *  XX  * * * *  X
X X .X.X.X.X. X XX X .X.X. X X
X X* * * * * *X XX X* * * *X X
X X .X.X.X.X. X XX X . . . X X
X X* * * * * *X     XXX XXX  X
X X . . . . . X XXX         XX
X  XXXXX XXXXX  X XXXXXXXXXXX
XX             XX
 XXXXXXXXXXXXXXX

; 31

   XXXXX XXXXX
 XXX    X  @ XXXX
XX    X *  X    XX
X   X..*.X*...X  X
X X . *X * *X .  X
X   .X    X  *.X  X
X  X.*  X*   X*   X
 X. * X  * X  .*X X
X * X* **X** *X * X
X X*.  X *  X * .X
X   *X   *X  *.X  X
X  X.*  X    X.   X
 X  . X* * X* . X X
 X  X...*X.*..X   X
 XX    X  * X    XX
  XXXX    X    XXX
     XXXXX XXXXX

; 32

   XXXXXX  XXXXX
  XX    XXXX   X
  X  XX  *   X X
  X X .X *X *  X
  X X*.*  X   XXXXXXX
  X  *. X XXX X     X
  XXX .*. . X X.*.* X
   X *. XXX*X*X XX XX
XXXX  X*        X   X
X   X * XXX@XXX.    X
X *     X  X..  X..XX
XXXXXX X    ..X .  X
    X   ** X..XX ..X
    X  * *XX     X X
    X **       X   X
    X  XXXXXXXXXXXXX
    XXXX

; 33

         XXXX
   XXXXXXX  XXXX
   X         * XX
XXXX*  XXX.XXX  XX
X   * X  X.X  X  X
X X * X   .  @ X X
X X   X..XXX   X X
X X *X....  X  X X
X X  X...X*  X X X
X X* X XX ** * X X
X X  X .*    XX  X
X X**XX X  XX   XX
X X     XXX   XXX
X  XXXX*    XXX
XX      XXXXX
 XXXXXXXX

; 34

            XXXX
    XXXXX   X  XXXXX
   XX   X   X      X
   X  X XXXXX X X  X
   X X * * * * X  XX
   X X       X  X X
   X  XXXXXX*XX X X
XXXX  X *  X  X X X
X   * X .. *  X X X
X X X X*...X X  X X
X .***X. ..X   XX XX
XX*....*.*  * X    X
 XX* XX.XXXXX X *  X
  XX  X     *  X X X
   XX@ X.X* * * *X X
    XX    * *  X   X
     XX  XXXXXXXXXXX
      XXXX

; 35

              XXXX
 XXXX       XXX  X
 X  XXXXXXXXX  ..X
 X  * @ *   * X..X
 X *X *   X X X..X
 X  XX*XX*X*X*X..X
 X * X..X.      XX
 X   X*. .XX*XX X
XX* *X..X.      X
X    XX*XXXXXXXXX
X   ** * X
XX       X
 XXXXXXXXX

; 36

           XXXXX
          XX . XX
         XX.* *.XX
         X * * * X
         X. * * .X
         X * * * X
         XX.* *.XX
 XXXXXXX  XX . XX  XXXXXXX
XX     XX  XX XX  XX     XX
X .*.*. X   X X   X *.*.* X
X *.*.* XXXXX XXXXX .*.*. X
X .* *.             *.@.* X
X *.*.* XXXXXXXXXXX .*.*. X
X .*.*. X         X *.*.* X
XX     XX  XXXXX  XX     XX
 XXXXXXX   X***X   XXXXXXX
           XXXXX

; 37

XXXXXXXXX     XXXXXXX
X   X   XXXXXXX  X  X
X .*. *       X . . X
XX XXX X X X * * X* X
X . X  X.* *.XX XX.XX
X  * .* .X X. X. X  X
XXX XX X.* *.  *  * X
XX  X  XX** .XX XX  X
X  XX XX. **XX  X  XX
X *  *  .* *.X XX XXX
X  X .X .X X. *. *  X
XX.XX XX.* *.X  X . X
X *X * * X X X XXX XX
X . . X   @   * .*. X
X  X  XXXXXXX   X   X
XXXXXXX     XXXXXXXXX

; 38

XXXXX       XXX
X  XXXXXXXXXXXXXXX
X *   * @ *  X   X
X  X * * * *     X
XX X  * . *  X XXX
 X X * * * * X X
 X X  * . *  X X
 X X * * * * X X
XX X  * . *  X XX
XX XXXXXXXXXXX  X
X *           * X
X   XXXXXXXXXX  X
XXXXX       XXXXX

; 39

   XXXX   XXXX
   X  XXXXX  XXXX
XXXX * *        XX
X   *   XXX  XX  XX
X@XXX X XXX.X..X  X
X  *  X X      .X X
X * X X X   X  .  X
XX X  X XXXXXXXXXXX
 X   XX * * * X
 XXXXXX X.X.X.XXX
    X     X X   X
    X X X.X.X.X X
    X X * * * X X
    X  X  X X X X
    XX  XXX   X X
     XX    XXX  X
      XXXX     XX
         XXXXXXX

; 40

  XXXXXXX XX XXXXXXX
  X     XXXXXX     XX
  X.XXX  XX  .  XX  XX
  X .  X  **X .X  X  X
  X X.  XXX.X  **  X XXXXXXX
  X * *    XXX  .  X       XX
 XXX*X * **  XX* .XXXXXXXX  X
XX  * X *  X  X X .   X   X X
X  **  *X. .X @ X. .X*  **  X
X X   X   . X X  X  * X *  XX
X  XXXXXXXX. *XX  ** * X*XXX
XX       X  .  XXX    * * X
 XXXXXXX X  **  X.XXX  .X X
       X  X  X. X**  X  . X
       XX  XX  .  XX  XXX.X
        XX     XXXXXX     X
         XXXXXXX XX XXXXXXX

; 41
;'MS46 v2'

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X        .........           X
X *      XXXXXX XX         @ X
XXXXXXX   X *    XXXXXXXXXXXXX
      XX  X   *  X
       XX*XX XXX*X
     XXXX    ..X XXXXX XXXXX
     X  ..*.**.X X   X X   XX
     X XXXXXX.. *  X XXX*  XX
     X X    X*. X *        X
     X X X  X  X ** X XX XXX
     X  * X XX    XXXXX   X
     XX  *   XXXXXX X     X
      X XXX XXX       *X  X
      X   *   X* * XX  XXXX
      XXXX * *    XXXXXX
         X  XXXX  X
         XXXX  XXXX

; 42

XXXXXXXXXXXXXXXXXXXXXXXXX
X   X   X   X   X   X   X
X * X X X X X X X X X * X
X  * * * * * * * * * *  X
XXX X X X X X X X X X XXX
X  * *...... ......* *  X
X X X XXXXXX XXXXXX X X X
X  * .X     *     X. *  X
XXX X* **** @ **** *X XXX
X  * .X     *     X. *  X
X X X XXXXXX XXXXXX X X X
X  * *...... ......* *  X
XXX X X X X X X X X X XXX
X  * * * * * * * * * *  X
X * X X X X X X X X X * X
X   X   X   X   X   X   X
XXXXXXXXXXXXXXXXXXXXXXXXX

; 43

    XXXX
   XX  XXXX
   X *   .XXXXXXXX
   X * X .   * * X
XXXX XXX .XXXX X X
X  ....X*.X  X X X
X X. * X .X* X X X
X  XX  ***@* X X X
XX   XX  X   X X X
 XXX   X  XX X X X
   XXX X ...     X
     X X** **X  XX
     X X ...* XXX
     X ** X   X
     X   XXXXXX
     XXXXX

; 44

      XXXXX
     XX   XX
     X  *  X
    XX *.* XX
   XX *.*.* XX
 XXX *.*.*.* XXX
XX  *.*.*.*.*  XX
X  *.*.* *.*.*  X
X *.*.*   *.*.* X
X  *.*.* *.*.*  X
XX  *.*.*.*.*  XX
 XXX *.*.*.* XXX
   XX *.*.* XX
    XX *.* XX
     X  *  X
     XX @ XX
      XXXXX

; 45

      XXXXX
      X   X
     XX * XX
   XXX *.* XXX
   X  *.*.*  X
  XX *.*.*.* XX
XXX *.*.*.*.* XXX
X  *.*.* *.*.*  X
X *.*.*   *.*.* X
X  *.*.* *.*.*  X
XXX *.*.*.*.* XXX
  XX *.*.*.* XX
   X  *.*.*  X
   XXX *.* XXX
     XX * XX
      X @ X
      XXXXX

; 46

           XXXXX
 XXXXXXXXXXX @ XXXXXXXXXXX
 X   .   .   X     .     X
 X ********* X .* ***.*. X
 X.....*.....X**.*...*.**X
XX ********* X .*.*** *. XX
X    .   .   X     .      X
X XXXXXXXXXXXXXXXXXXXXXXX X
X   .  .  .  X  . . . .   X
XX *** *** * X *.*.*.*.* XX
 X.*.* * *.*.X**** * ****X
 X * *** *** X *.*.*.*.* X
 X  .  .  .  X  . . . .  X
 XXXXXXXXXXX * XXXXXXXXXXX
           XXXXX

; 47

           XXXXX
 XXXXXXXXXXX @ XXXXXXXXXXX
 X  .     .  X    .*.    X
 X .*.***.*. X.*  *.*  *.X
 X.***.*.***.X*.*** ***.*X
XX .*.***.*. X.*  *.*  *.XX
X   .     .  X    .*.     X
X XXXXXXXXXXXXXXXXXXXXXXX X
X   *.   .*  X *       .  X
XX  * .*. *  X .**   *** XX
 X  *.***.*  X *  ***  * X
 X  * .*. *  X ***   **. X
 X  *.   .*  X .       * X
 XXXXXXXXXXX * XXXXXXXXXXX
           XXXXX

; 48 'Parallel Logic 2'

 XXXXXXXXXXXXXXXXXXXXXXXXX
 X  X  X  X  X  X  X  X  X
 X *X* X *X* X *X* X *X* X
 X  X  X  X  X  X  X  X  X
 X *X* X *X* X *X* X *X* X
 X  X  X  X  X  X  X  X  X
 XX X XXX X XXX X XXX X XX
 X  X  X  X  X  X  X  X  X
 X  *  X  *  X  *  X  *  X
XX XXX X XXX X XXX X XXX XX
X   X  X  X  X  X  X  X   X
X   X  *  X  *  X  *  X   X
XX  X XXX X XXX X XXX X  XX
 X...........+...........X
 XXXXXXXXX   X   XXXXXXXXX
         X  XXX  X
         XXXX XXXX

; 49

  XXXXXXXXXXXXXXXXXXXXXXXXX
  X           X           X
XXX** ** ** **.** ** ** **XXX
X *+.*..*..*..*..*..*..*..* X
X *..*..*..*..*..*..*..*..* X
X  **.**.**.**.**.**.**.**  X
X *..*..*..*..*..*..*..*..* X
X *..*..*..*..*..*..*..*..* X
XX.**.**.**.** **.**.**.**.XX
X *..*..*..*..*..*..*..*..* X
X *..*..*..*..*..*..*..*..* X
X  **.**.**.**.**.**.**.**  X
X *..*..*..*..*..*..*..*..* X
X *..*..*..*..*..*..*..*..* X
XXX** ** ** **.** ** ** **XXX
  X           X           X
  XXXXXXXXXXXXXXXXXXXXXXXXX

; 50

 XXXX                   XXXX
 X  XXXXXXXXXXXXXXXXXXXXX  X
 X    ....... @ .......    X
 X  X .XXXXXXXXXXXXXXX. X  X
XXX  X.    X  X   X   .X  XXX
 X     X   *  X   *  X     X
 X     XX*XX  XX*XX  X     X
 XXX   X  XX*XX  XXXXX   XXX
 X  X  X  *   *  *   X  X  X
 X     X  X   X  X   X     X
 X  X  XXXXX*XXXXXX*XX  X  X
 XX   XX   X  X   X  XX   XX
 XXXXXXX   *  X   *  XXXXXXX
       XX*XX  XX*XX  X
XXXXXX X  XXXXX  XX*XX XXXXXX
X    X X  *   *  *   X X    X
XXXXXX X  X   X  X   X XXXXXX
       XXXXXXXXXXXXXXX

; Sasquatch Set IV


; 1

   XXXX
XXXX  X
X     XXXX
X * X  . XX
X  X   .  X
XX X**X.  X
XX    XXXXX
X @ XXX
X   X
XXXXX

; 2

     XXXXX
XXXXXX   X
X  *     X
X  *XXX XX
XX.*. . .X
 X *X    X
 X @XXXXXX
 X  X
 XXXX

; 3

    XXXXX
 XXXX   X
 X @ *X X
 X X....X
XX* * * X
X  XXX XX
X      X
XXXXX  X
    XXXX

; 4

  XXXXXX
  X  . XX
  X X*  X
  X *.* X
  XX *. X
 XX *.@ X
XX X .* X
X  **.X X
X      XX
XXXXXXXX

; 5

 XXXX
 X  X
XX .XXX
X  .* X
X* *  XX
X *.** X
X  .   X
XXX*XXXX
  X@X
  XXX

; 6

  XXXX
XXX  X
X  ..X XXXXXXX
X X..X X     XXXX
X X. XXX   *    X
X X.   X * * ** X
X X  @ XXX *XX  X
X           XXXXX
XX  XXXXXXXXX
 XXXX

; 7

 XXXXXXXXXXXXXXX
XX *.       .* XX
X  X XXXXXXX X  X
X X           X X
X  .****X****.  X
XXX     X     XXX
  X XXXX@XXXX X
  X           X
  XXXXXXXXXXXXX

; 8

XXXXXXXXXXXXXXXXXXXXXXX
X      X   X   X      X
X *@** X *     X .. ..X
XX XX XXX XXX XXX XX XX
 X X       X       X X
 X X   X   X   X   X X
 X XXXXXXXXXXXXXXXXX X
 X                   X
 XXXXXXXXXXXXXXXXXXXXX

; 9

XXXXXXXXXXX
X@  X  X  X
X  *X*   *X
XX  X..X  X
 X  X..X  X
 X  X..X  XX
 X*   *X*  X
 X  X  X   X
 XXXXXXXXXXX

; 10

XXXXXX
X    X
X .* X
X ** X
XX*. X
 X  XXXX
 X XX  X
 X  X  X
 X     X
 X.***@X
 X  X  X
 XXXXXXX

; 11

  XXXXXXXX
 XX.... @X
 X  X .  X
XX X  X XX
X  X* X X
X *   X XX
XXX* XX  X
  X   ** X
  X   X  X
  XXXXXXXX

; 12

 XXXXXX
 X    X
 X    XXX
 XX*X   X
XX . XX X
X     X XX
X X.X  * X
X *.XXX* X
XXX XX   X
  X   **@X
 XX..XX  X
 X   XXXXX
 X   X
 XXXXX

; 13

      XXXX
  XXXXX  X
XXX.  X* XX
X  *   .*.X
X *.* X*  X
XXX XXX   X
 X   XXX XXX
 X  *X *.* X
 X.*.@  *  X
 XX *X  .XXX
  X  XXXXX
  XXXX

; 14

 XXXXXX
 X    XXXXX
 X * *X   X
 X  * * * X
XXX* . *  X
X * .@. * X
X  * . *XXX
X * * *  X
X   X* * X
XXXXX    X
    XXXXXX

; 15

XXXXXXXXXXX
X    *    X
X ** XX * X
X  *..X** X
X XX*.*.  X
X*X..@..X*X
X  .*.*XX X
X **X..*  X
X * XX ** X
X    *    X
XXXXXXXXXXX

; 16

XXXXXXXXXXXXX
X     *   . X
X.* *XXX ** X
X ** XX .*  X
X  .*X..* * X
X X .*.*XXX X
X*XX..@..XX*X
X XXX*.*. X X
X * *..X*.  X
X  *. XX ** X
X ** XXX* *.X
X .   *     X
XXXXXXXXXXXXX

; 17

XXXXXXXXXXXXXXX
X             X
X *.*.*.*.*.* X
X .*.*.X.*.*. X
X *.*.* *.*.* X
X .*.*.X.*.*. X
X *.*.* *.*.* X
X .X X @ X X. X
X *.*.* *.*.* X
X .*.*.X.*.*. X
X *.*.* *.*.* X
X .*.*.X.*.*. X
X *.*.*.*.*.* X
X             X
XXXXXXXXXXXXXXX

; 18

 XXXXXXXXXXXXXXX
XX  X   X   X  XX
X   **.. ..**   X
X  *   ***   *  X
XX* .XXX XXX. *XX
X * XX *@* XX * X
X . X       X . X
X .*X* XXX *X*. X
XX *   X X   * XX
X .*X* XXX *X*. X
X . X       X . X
X * XX * * XX * X
XX* .XXX XXX. *XX
X  *   ***   *  X
X   **.. ..**   X
XX  X   X   X  XX
 XXXXXXXXXXXXXXX

; 19

 XXXXXXXXX
 X   *   X
 X XX XX X
 X  * *  X
XXX  X  XXX
X  .*X*.  X
X X  @  X X
X  .*X*.  X
XXX  X  XXX
  XXXXXXX

; 20

XXXX
X  XXXXXXXXX
X    XX    X
X ***X     X
XX...X X***X
 X...X X...X
 X***  X...XX
 X    XX*** X
 XXXXXXX @  X
       XXXXXX

; 21

  XXXXXXXXX
 XX   X   X
XX *X X X*XXX
X   X. .X   X
X * *.@.* * X
X   X. .X   X
XXX*X X X* XX
  X   X   XX
  XXXXXXXXX

; 22

  XXXX  XXXX
  X  XXXX  XXXX
XXX     * *   X
X    X *  *...XX
X * X XXXX X.. X
XX   X         X
 X ** **@ X...XX
 X   X  XXXXXXX
 XXXX   X X
    XXXXX

; 23

       XXXX
  XXXXXX  X
 XX  *  * X
XX  * X*  X
X  * X   *X
X   X XX  XX
XXX*  ..X  X
  X  X*...@X
  X   ..XXXX
  X  XXXX
  XXXX

; 24

          XXXX
          X  XXX
          X    X
   XXXXXXXX**  X
   X       *  XX
   X XXXX ** XX
XXXX....X *  X
X   ...X **  X
X  X...X * XXX
X @XX XX * X
X         XX
X  X  XXXXX
XXXXXXX

; 25

 XXXXXXXXXXXXXXX
XX  ....X      XX
X  X X     XXX  X
X   ....X X   X X
X      X * *  X X
XX     X *@* X  X
 XXXXXXX * * X  X
  XX*X   * *  X X
   XXX XXXX   X X
    XX     XXX  X
     XXXXX     XX
         XXXXXXX

; 26

   XXXXX XXXXX
   X @ XXX   X
   X X *     X
XXXX X* * XXXX
X    X * *X
X XXX * * X
X.......X XX
XXXX XX X  X
   X    X  X
   XXXXXX  X
        XXXX

; 27

    XXXX
  XXX  XXX
XXX      XX
X **X***@ XX
X     X    X
X XXX  X***X
X    X   X X
XXXX   .XX X
   XXXX.XX XX
    XX .XX  X
    XX...   X
    X  .XXXXX
    X  .X
    XXXXX

; 28

 XXXX
 X  XXXXX
 X  * * X
 X* . . X
 X  XXXXXXXX
 X      X  X
 XXXX *    X
 X   X*XXX X
 X @*X   X XXXX
 X ** **   X  X
 X   X XX * * X
XX XXX.....X. X
X...  XXX*X . X
X * *       . X
XXXXXXXX  XXXXX
       XXXX

; 29

 X XX XXXX
XX X  X  XXX
   X XX*   X
XXXX X * X X
X    X * X X
  XXXX * X X
XXX    . X X
X@X.*****X X
X        X X
X XXXXX  X X
X      XX  X
XXXXXX    XX
     XXXXXX

; 30

      XXXXX
      X   XXXXXXX
      X    XX   XX
      X.X       XXX
  XXXXX.X  X XXXXXXX
 XX  XX.XXXX. XX   XX
XX     .....@.X  * XXX
X   XXX.X  X.X  * *  XX
X     X. X  .X * * *  X
X   X X.  XX X* * *   X
XX  X X.   X * * * XXXX
 XXX  X.   X  * * XX
   X X     X * *  X
   X X    XXXXXX*XX
   X  XXXX       X
   XX      XXXXXXX
    XXXXXXXX

; 31

 XXXXXXXXXXXXX
 X     @     X
 X**.*****.**X
 X  *     *  X
 X   X XXX   X
 XXXXX   XXXXX
XXXXXXXX XXXXXX
X             X
X**.*******.**X
X  *       *  X
X   XXXXXXX   X
XXXXX     XXXXX

; 32

           XXXX
         XXX  X
  XXXXXXXX ** XX
XXX   X   .*.* X
X  ** X X....* X
X *.. X * *    X
XX**. XX  XXXXXX
 X ..*XX XXX   X
 XX .  X    *X X
  X X*   @X  . XX
  X   XXX XX*.. X
  XXXXXX  XX .**XX
  X    * * X ..* X
  X *....X X **  X
  X *.*.   X   XXX
  XX ** XXXXXXXX
   X  XXX
   XXXX

; 33

      XXXXXXX
     XX     XX
     X  *.*  X
     X X* *X X
 XXXXX  *.*  XXXXX
XX   XX     XX   XX
X  X  XXX.XXX  X  X
X *** X *** X *** X
X . . ..*@*.. . . X
X *** X *** X *** X
X  X  XXX.XXX  X  X
XX   XX     XX   XX
 XXXXX  *.*  XXXXX
     X X* *X X
     X  *.*  X
     XX     XX
      XXXXXXX

; 34

     XXXXX
     X @ X
     X * X
     X * X
    XX * XX
XXXXX.*.*.XXXXX
X    *. .*    X
X ***. X .*** X
X    *. .*    X
XXXXX.*.*.XXXXX
    XX * XX
     X * X
     X * X
     X   X
     XXXXX

; 35

      XXXXX
      X   X
     XX * XX
    XX *.* XX
   XX * * * XX
  XX *.*.*.* XX
XXX *.*.X.*.* XXX
X  * *.X X.* *  X
X *.*.X   X.*.* X
X  * *.X X.* *  X
XXX *.*.X.*.* XXX
  XX *.*.*.* XX
   XX * * * XX
    XX *.* XX
     XX * XX
      X @ X
      XXXXX

; 36

      XXXXX
     XXX  XX
    XX *   XX
   XX *  ** XX
  XX *.X.*.* XX
 XX *.*. .*.* XX
XX *.*. . .*.* XX
X  **. * * .X *XX
X   . . @ . .   X
XX* X. * * .**  X
XX *.*. . .*.* XX
 XX *.*. .*.* XX
  XX *.*.X.* XX
   XX **  * XX
    XX   * XX
     XX  XXX
      XXXXX

; 37

   XX XX
 XX  X  XX
 XX     XX
X  **X**  X
X  *...*  X
 X X.@.X X
X  *...*  X
X  **X**  X
 XX     XX
 XX  X  XX
   XX XX

; 38

    XX XX
  XX  X  XX
 X  .* *.  X
 X  *   *  X
X .* X.X *. X
X * X * X * X
 X  .*@*.  X
X * X * X * X
X .* X.X *. X
 X  *   *  X
 X  .* *.  X
  XX  X  XX
    XX XX

; 39

  XXXXX X XXXXX
 XX X XXXXX X XX
 X  X   X   X  X
XX ** *   * ** XX
X   ..*X X*..   X
XXX*..  X  ..*XXX
 X * ** X ** * X
 X   X  *  X   X
XXX XXX* *XXX XXX
 X   X  *  X   X
 X * ** X ** * X
XXX*..  X  ..*XXX
X   ..*X@X*..   X
XX ** *   * ** XX
 X  X   X   X  X
 XX X XXXXX X XX
  XXXXX X XXXXX

; 40

             XXX
      XXXXXXXXXXXXXXXXX
  XXXXXX   XX   XX   XXXXXX
XXXX   X **   X   ** X   XXXX
X  X**     X.. ..X     **X  X
X      XXX X.XXX.X XXX      X
X* XXXXX XXX X*X XXX XXXXX *X
X           ..@..           X
X* XXXXX XXX X*X XXX XXXXX *X
X      XXX X.XXX.X XXX      X
X  X**     X.. ..X     **X  X
XXXX   X **   X   ** X   XXXX
  XXXXXX   XX   XX   XXXXXX
      XXXXXXXXXXXXXXXXX
             XXX

; 41

XXXXXXXXXXXXXXX
X  ..  .   .  X
X *XX* X **XX.X
X  X  XXX  X  X
X.XX  X X XX* X
X *   * *   * X
X.XX  X X  X  X
X.XX  X@X XXX.X
X * X XXX X X.X
X *         * X
X.XXX XXX X X X
X  X  X   XXX.X
X *X**XXX*X X X
X  .   .  . . X
XXXXXXXXXXXXXXX

; 42

XXXX   XXXXX   XXXX
X  XX  X   XXXXX  X
X *.X  X *     *  X
X  .X  X   XXXXX  X
XX .XXXX XXX  XX*XX
 X*. *     X  *   X
 X ..XXX   X  X   X
 X*..@XXXXXXX*XXXXX
 X ..XXXX   X  X
 X*. *      X  X
XX .XXXXXX*XX  X
X  .X   X  XX*XX
X *.X   X  *   X
X  XX   X  X   X
XXXX    XXXXXXXX

; 43

 XXXXXXXXXXXXXXXX
XX              XX
X  XXXXXXXXXXXX  X
X X            X X
X X *** * *   @X X
X  X   XXX   **X XX
XX * XX   X   * * X
 XX   X X  XXXX   X
  XXX..  X     X  XXX
    XX    .. X .X * XXXX
     X XXXX XX .X X.X  X
     X    X XXX* * .X  XX
     XXXX X    .X X.    X
        X   XX .XXX.XX  X
        XXXXXX          X
             X   X  X   X
             XXXXXXXXXXXX

; 44

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X  .  .  .  .  .  .  .  .  .  X
X * * X * * X * * X * * X * * X
XXX.XXXXX.XXXXX.XXXXX.XXXXX.XXX
X * * X * * X * * X * * X * * X
X     .     .   X .     .     X
XXX.XXXXX.XXXXXXXXXXX.XXXXX.XXX
X  *  X  *  . *@X X  *  *  *  X
X  *  *  *  X X * .  *  X  *  X
XXX.XXXXX.XXXXXXXXXXX.XXXXX.XXX
X     .     . X   .     .     X
X * * X * * X * * X * * X * * X
XXX.XXXXX.XXXXX.XXXXX.XXXXX.XXX
X * * X * * X * * X * * X * * X
X  .  .  .  .  .  .  .  .  .  X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; 45

 XXXXXXXXXXXXXXXXXXXXX
XX   X   X   X   X   XX
X * * * * * * * * * * X
X  X X X X X X X X X  X
X *.* *.* *.* *.* *.* X
XX. .X. .X. .X. .X. .XX
X *.* *.* *.* *.* *.* X
X  X X X X X X X X X  X
X *.* *.* *.* *.* *.* X
XX. .X. .X.@.X. .X. .XX
X *.* *.* *.* *.* *.* X
X  X X X X X X X X X  X
X * * * * * * * * * * X
XX   X   X   X   X   XX
 XXXXXXXXXXXXXXXXXXXXX

; 46

   X    X    X    X    X
   XXXXXXXXXXXXXXXXXXXXX
  XX    X    X    X    XX
XXX .**. .**. .**. .**. XXX
 X .*  *.*  *.*  *.*  *. X
 X * XX * XX * XX * XX * X
 X * XX * XX * XX * XX * X
 X .*  *.*  *.*  *.*  *. X
XXX .**. .**.@.**. .**. XXX
 X .*  *.*  *.*  *.*  *. X
 X * XX * XX * XX * XX * X
 X * XX * XX * XX * XX * X
 X .*  *.*  *.*  *.*  *. X
XXX .**. .**. .**. .**. XXX
  XX    X    X    X    XX
   XXXXXXXXXXXXXXXXXXXXX
   X    X    X    X    X

; 47

            XXXXX
 XXXXXXXXXXXX @ XXXXXXXXXXXX
 X            X            X
 X*.*  .*.*.*.X**.******.**X
 X.*.*.*.*.*.*X  *. ..*.*  X
 X*.*.*.*.*.*.X  *.*.. .*  X
XX.*.*.*.  *.*X**.******.**XX
X             X             X
X XXXXXXXXXXXXXXXXXXXXXXXXX X
X    ..  ..   X * . *. * .  X
XX ********** X  * *.*. .  XX
 X *. .. .*.* X.*.*.  *.*.*X
 X *.*. .. .* X*.*.*  .*.*.X
 X ********** X  . .*.* *  X
 X   ..  ..   X . * .* . * X
 XXXXXXXXXXXX * XXXXXXXXXXXX
            XXXXX

; 48

XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X   X   X   X   X   X   X   X
X X X   X   X   X   X   X X X
X   .***.***.***.***.***.   X
XXX.X X X X X X X X X X X.XXX
X  *  . . . . . . . . .  *  X
X  *X X*X*X*X*X*X*X*X*X X*  X
X  *  * . . . . . . . *  *  X
XXX*..* X*X*X*@*X*X*X *..*XXX
X  *  * . . . . . . . *  *  X
X  *X X*X*X*X*X*X*X*X*X X*  X
X  *  . . . . . . . . .  *  X
XXX.X X X X X X X X X X X.XXX
X   .***.***.***.***.***.   X
X X X   X   X   X   X   X X X
X   X   X   X   X   X   X   X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; 49

 XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 X         *   *   *         X
 X  * XXX *  XXXXX  * XXX *  X
 X * * XXX *  XXX  * XXX * * X
 X*X  * XXX *  X  * XXX *  X*X
 X XX .*.*.*.*.*.*.*.*.*. XX X
 X XXX* * * * *.* * * * *XXX X
XX ..*.....*...*...*.....*.. XX
XX  * * * * * *@* * * * * *  XX
XX ..*.....*...*...*.....*.. XX
 X XXX* * * * *.* * * * *XXX X
 X XX .*.*.*.*.*.*.*.*.*. XX X
 X*X  * XXX *  X  * XXX *  X*X
 X * * XXX *  XXX  * XXX * * X
 X  * XXX *  XXXXX  * XXX *  X
 X         *   *   *         X
 XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

; 50

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X .* XX *. XX .* XX *. XX .* X
X*  .  .  *XX*  .  .  *XX*  .X
X.  *XX*  .  .  *XX*  .  .  *X
X *. XX .* XX *. XX .* XX *. X
XXX X  X XX  XX X  X XX  XX XX
XXX X  X XX X  . X X XX  XX XX
X *. XX .* X   *  X .* XX *. X
X.  *XX*  . .*XX  X*  .  .  *X
X*  .  .  *X  @X*. .  *XX*  .X
X .* XX *. X  *   X *. XX .* X
XX XX  XX X X .  X XX X  X XXX
XX XX  XX X  X XX  XX X  X XXX
X .* XX *. XX .* XX *. XX .* X
X*  .  .  *XX*  .  .  *XX*  .X
X.  *XX*  .  .  *XX*  .  .  *X
X *. XX .* XX *. XX .* XX *. X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX