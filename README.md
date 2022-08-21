# Jumpstart Commander Legends

Generate a deck from a prebuilt collection of halfdecks with each half helmed but a Commander Legends Uncommon Partner, and 6 common cards. (Intended for playtesting and spelltable play via Moxfield)

Halfdecks: https://archidekt.com/decks/2098253#Jumpstart_Commander_Legends

By default the script will randomly generate a partner pair. If you wish to specify one or both, just specify with their names as arguments. (Examples Below)

The result will be a generated decklist.txt in the same folder.

*Random Partners*
```console
foo@bar:~$ python deck_generator.py
```

*One Random Partner, One Specified*
```console
foo@bar:~$ python deck_generator.py Ardenn
```

*Arranged Marriage*
```console
foo@bar:~$ python deck_generator.py Ardenn Kediss
```
