---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: Jam.gg never shipped an HTTP API, and the company is now listed Inactive by Y Combinator — its own web property cannot complete a TLS handshake on either host (jam.gg answers the ClientHello with TLS alert 80 internal_error from Netlify/AWS Global Accelerator, www.jam.gg answers with alert 40 handshake_failure from the Webflow proxy), piepacker.com has left DNS, and no api/docs/developers subdomain resolves, so the only reachable artifacts are the first-party SDK repositories on GitHub.
  evidence:
  - status: 301
    url: http://jam.gg/
  - status: 0
    url: https://jam.gg/
  - status: 0
    url: https://www.jam.gg/
  - status: 200
    url: https://www.ycombinator.com/companies/jam-gg
  - status: 200
    url: https://github.com/piepacker
  - status: 200
    url: https://repo1.maven.org/maven2/io/github/piepacker/jampadcompose/maven-metadata.xml
  reason: defunct
  state: none
created: '2026-08-17'
description: 'Jam.gg, founded in Paris in 2020 as Piepacker and rebranded in 2022, built a browser-based social cloud gaming platform for playing retro and indie multiplayer games with friends with no download or install, on patented streaming technology the company said cut bandwidth requirements by roughly 15x. It passed 8 million users before pivoting to selling its cloud gaming technology B2B to game developers and publishers. Backed by Makers Fund, Serena Capital, LEGO Ventures, Kima Ventures and Kickstarter (~$15.4M raised) and a Y Combinator W20 company. Jam.gg never published an HTTP API: its developer surface was a native game-integration SDK plus a Compose Multiplatform virtual gamepad library, both shipped from the GitHub organization still named piepacker. Y Combinator''s company directory now lists Jam.gg as Inactive, noting the business split into two entities in 2023 with Onibi emerging separately; the jam.gg web property no longer completes a TLS handshake and piepacker.com
  has left DNS.'
image: https://avatars.githubusercontent.com/u/51542573?v=4
layout: provider
modified: '2026-08-17'
name: Jam.gg
nav: Providers
network: true
random_paper: 116
slug: jam-gg
tags:
- Company
- Gaming
- Cloud Gaming
- Games
- Game Development
- Emulation
- SDK
- WebRTC
- France
---
