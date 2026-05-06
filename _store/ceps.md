---
aid: ceps
url: https://raw.githubusercontent.com/api-evangelist/ceps/refs/heads/main/apis.yml
name: CEPS (Centre for European Policy Studies)
tags:
  - Brussels
  - Data Governance
  - EU Policy
  - European Union
  - Policy Research
  - Publications
  - RSS
  - Research
  - Think Tank
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Founded in Brussels in 1983, the Centre for European Policy Studies (CEPS) is a leading independent think tank and forum for debate on EU affairs, with an exceptionally strong in-house research capacity and an extensive network of partner institutes. CEPS conducts rigorous, evidence-based policy research on European and global issues (Data Governance Act, Data Act, AI Act, climate, migration, financial markets) and disseminates its findings primarily through publications, events, and podcasts rather than a commercial API; programmatic access to CEPS output is primarily via public RSS, OPML feeds, and structured publication pages on ceps.eu.
apis:
  - aid: ceps:ceps-publications-feed
    name: CEPS Publications RSS / Content Feeds
    tags:
      - Atom
      - Content
      - Publications
      - RSS
    humanURL: https://www.ceps.eu/ceps-publications/
    properties:
      - url: https://www.ceps.eu/ceps-publications/
        type: Website
      - url: https://www.ceps.eu/feed/
        type: RSS
      - url: https://www.ceps.eu/news/
        type: News
    description: CEPS exposes its publications and news stream as RSS/Atom feeds that aggregators, knowledge management tools, and policy-monitoring platforms can consume to track CEPS working papers, policy insights, reports, and commentaries as they are released.
  - aid: ceps:ceps-events
    name: CEPS Events Listings
    tags:
      - Calendar
      - Events
      - Policy Forum
      - Webinars
    humanURL: https://www.ceps.eu/events/
    properties:
      - url: https://www.ceps.eu/events/
        type: Website
      - url: https://www.ceps.eu/feed/
        type: Feed
    description: CEPS maintains a calendar of policy events, conferences, task force meetings, and webinars that can be embedded or syndicated via the public events listing pages.
common:
  - type: Website
    url: https://www.ceps.eu/
  - type: About
    url: https://www.ceps.eu/about-ceps/
  - type: Publications
    url: https://www.ceps.eu/ceps-publications/
  - type: News
    url: https://www.ceps.eu/news/
  - type: Events
    url: https://www.ceps.eu/events/
  - type: RSS
    url: https://www.ceps.eu/feed/
  - type: Knowledge4Policy
    url: https://knowledge4policy.ec.europa.eu/organisation/ceps-centre-european-policy-studies_en
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Centre_for_European_Policy_Studies
  - type: Privacy Policy
    url: https://www.ceps.eu/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
