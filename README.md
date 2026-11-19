[![make.fun](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/ASEP9929/makefun-gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/ASEP9929/makefun-gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

# Waited 13 Years for This Day

A GTA 6 launch-week meme for make.fun's `gta6-meme-x-01` bounty: after 13
years since GTA V, GTA VI is finally out — and the make.fun ghost is
standing in the middle of a Vice City synthwave sunset, holding up its
magenta star coin like it just won the wait.

The picture (`meme.png`, 1080x1080) is drawn from scratch in this session
with `gen_meme.py` (Python + PIL, no downloaded assets, no Rockstar
artwork): a purple-to-orange sunset, a slatted synthwave sun, a lit
skyline, palm silhouettes, and the white make.fun ghost — thick black
outline, black sparkle eyes, round little hand — holding its magenta coin
with a white star. The banner reads "GTA VI IS FINALLY OUT — now win real
money on make.fun".

## The post (draft caption for X)

The meme is posted on X from @Mahesa3u with this text (the play code is
filled in from the bounty page right before posting):

> Waited 13 years for GTA VI. Worth every second. 👻 My agent and I win
> real money on make.fun — you can too:
> https://make.fun/bounty/gta6-meme-x-01 @makefunai {{PLAY_CODE}}

## How the entry works

`POST.json` at the repo root holds the post's address
(`{"url": "https://x.com/<handle>/status/<id>"}`); `main.ts` copies it to
`/output/POST.json`, where the gate reads it. The house reads the post
itself from X — its first picture and its text — and hands them to the
judge. Verify locally with:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

make.fun is a site where people and their AI agents build things, enter
them in paid competitions (bounties) and earn real money when they win.
