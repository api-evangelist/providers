---
aid: electronic-arts
name: Electronic Arts
description: Electronic Arts (EA) is a global leader in digital interactive entertainment, developing and delivering games, content, and online services for internet-connected consoles, mobile devices, and personal computers. EA's portfolio includes franchises such as EA SPORTS FC, Madden NFL, Battlefield, The Sims, Apex Legends, and Need for Speed, supported by online services like EA app, EA Play, and Origin. EA does not currently publish a public developer API portal; integrations and data exchanges are handled through partner programs and the EA Help support and account surfaces.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Gaming
  - Video Games
  - Entertainment
  - Consumer
  - Player Services
created: '2026-03-21'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/electronic-arts/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: electronic-arts:electronic-arts
    name: Electronic Arts
    description: Public-facing presence of Electronic Arts. Covers EA's corporate site, consumer game services, EA app, EA Play subscription, and EA Help support surfaces. EA does not publicly publish a developer API portal at this time, so this entry is tracked as a Contract-position reference rather than a producer of public APIs.
    humanURL: https://www.ea.com
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Gaming
      - Video Games
      - Entertainment
      - Consumer
    properties:
      - type: Website
        url: https://www.ea.com
      - type: Support
        url: https://help.ea.com
      - type: Careers
        url: https://www.ea.com/careers
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - name: Electronic Arts Website
    url: https://www.ea.com
    type: Website
  - name: EA Help
    url: https://help.ea.com
    type: Support
  - name: EA Play
    url: https://www.ea.com/ea-play
    type: Subscription
  - name: EA Investor Relations
    url: https://ir.ea.com
    type: InvestorRelations
  - name: EA Careers
    url: https://www.ea.com/careers
    type: Careers
  - name: EA GitHub Organization
    url: https://github.com/electronicarts
    type: GitHub
---
