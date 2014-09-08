Pixley's StadiumStats!
============

------------
Requires Python 3.4!  Make sure you're running 3.4, not 2.7!
------------

As a small hobby, I do a weekly commentary livestream for the Stadium 2 matches being played on Twitch Plays Pokemon between the runs of Pokemon X and Pokemon Omega Ruby.  I'm not well-versed in base stats, so I decided to build a reference program to quickly check the stats of the combatants, because I think knowing the relative stats will make for better commentary.

Since Python doesn't have set list sizes, this should easily expand to Pokemon Battle Revolution once Streamer-senpai gets that going, requiring only a swap of the input files.  I'll happily update the repo once that happens.

Twitch Plays Pokemon: http://twitch.tv/twitchplayspokemon (Runs 24/7)
  
Pixley Commentates Twitch: http://mixlr.com/pixley (Broadcasts Tuesdays at 2 PM UTC)

============
Quick Documentation
============

As of the initial release, I haven't commented it like it should be.  I literally threw this together over an evening, and that's including teaching myself some Python.  Manually building the input files took a bit longer.

stats.py
------------
The entirety of the script.  Super simple stuff.  Reads in the input files, then asks the user to type in the names of the Pokemon in the current battle.  Then it spits out a nice table, dividing between the Blue and Red Teams.  Solely for my benefit, it also lists the Pokemon types divided between Physical and Special, since it's been a very long time since the Physical-Special split back in Gen 4.  The user can get stats for as many battles as desired.

It is worth noting, however, that user and file input is very specific.  The user must type in one Pokemon name per line, first letter capitalized, no spelling errors permitted.  If the script gets an input it doesn't recognize, it'll spit out a silly error message halfway through building the table, then permit the user to start another battle.

Pokemon whose input may seem ambiguous to a user, formatted as the script accepts:
Nidoran-M
Nidoran-F
Mr. Mime
Farfetch'd
Porygon2

statlist.txt
------------
File containing the stats of each Pokemon available for rent in Stadium 2 (with lines skipped where Mewtwo and Mew would be).  Each line (counted starting with 1) lists the stats for the Pokemon whose National Dex number is that of the line.  So the first line lists the rental Bulbasaur's stats.

Stat order: HP, Attack, Defense, Sp. Atk, Sp. Def, Speed

pokelist.txt
------------
Each line is the name of the Pokemon whose National Dex number is that of the line (counted starting with 1).  Mewtwo and Mew are skipped due to not being available for rent in Stadium 2.
