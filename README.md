spotify-puzzles
===============

Solutions for https://www.spotify.com/se/jobs/tech/, written for Python 2.6.

Reverse Binary
==============

Confirmed working on submission to puzzle@spotify.com

Zipf's Song
===========

Currently works for all provided test cases on the puzzle page, however it seems there are some additional edge cases as it does not work on submissions. So far I've confirmed the following edge cases work:

- Default edge case provided by Spotify where two songs have the same quality value, the first to appear on the album is selected.
- Edge case where multiple songs on the album have the same quality value, they are sorted by their position on the album.
- Incorrect input from user in text file where an extra line is present, this is stripped to avoid errors.
- Edge case where user has x songs, and wants to sort the top x songs (this can include any of the edge cases above).
