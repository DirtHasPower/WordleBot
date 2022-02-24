# WordleBot by DirtHasPower
An algorithm to beat Wordle. No packages/libraries necessary.

Feel free to use/change but please credit me.

Credit to https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93 for list of valid wordle words.

If you have questions, contact me at dirthaspower@gmail.com


WordleBotV2 Change Log:

• FindBestWord() now prioritizes words with letters earlier in the alphabet. This makes it slightly more accurate.

• The way the program handles multiple of the same character has been made significantly more efficient.

• The win rate is now ~88%. 26% increase from WordleBotV1.py


WordleBotV3 Change Log:

• Added secondary word choosing method to stop WordleBot from getting 4 greens and then cycling through one letter at a time.

• Changed main loop slightly

• Win Rate has not been tested yet
