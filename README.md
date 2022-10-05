# WordleBot by DirtHasPower
An algorithm to beat Wordle. No packages/libraries necessary.

Feel free to use/change but please credit me.

If you have any questions, feel free to contact me at dirthaspower@gmail.com

Credit to https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93 for list of valid wordle words.


Instructions:<br>
-Input your word(Ex. bagel)<br>
-Input a five letter string to represent the results(G for green, Y for yellow, W for white)(Ex. WGGYW)<br>
-Program will output recommend a word<br>
-Repeat<br>


WordleBotV2 Change Log:<br>
-FindBestWord() now prioritizes words with letters earlier in the alphabet. This makes it slightly more accurate.<br>
-The way the program handles multiple of the same character has been made significantly more efficient.<br>
-The win rate is now ~88%. 26% increase from WordleBotV1.py<br>


WordleBotV3 Change Log(Still in beta. Use is not recommended):<br>
-Added secondary word choosing method to stop WordleBot from getting 4 greens and then cycling through one letter at a time.<br>
-Changed main loop slightly<br>
-Win Rate has not been tested yet
