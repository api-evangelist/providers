---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fantasy-akhada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affiliate.fantasyakhada.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.supersixsports.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FantasyAkhada
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/fantasyakhada
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/FantasyAkhada/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/fantasyakhada/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCtkKN933dPJN9dA74U3KC_w
coverage:
  checked: '2026-08-12'
  detail: Fantasy Akhada shipped only a consumer fantasy-sports app (iOS, sideloaded Android APK, React web lobby) and never published a developer portal, API, SDK or webhook surface - and its canonical host www.fantasyakhada.com no longer resolves at all, being a dangling CNAME to a deleted AWS ap-south-1 load balancer, with every backend service host named in the company's own JavaScript bundles likewise withdrawn from DNS.
  evidence:
  - note: DNS NXDOMAIN - CNAME to dualstack.supersix-alb-76454354.ap-south-1.elb.amazonaws.com, which is itself NXDOMAIN (deleted load balancer)
    status: 0
    url: https://www.fantasyakhada.com/
  - note: DNS NXDOMAIN
    status: 0
    url: https://api.fantasyakhada.com/
  - note: soft 200 - returns the site's 23,915-byte marketing HTML catch-all, not a document
    status: 200
    url: https://affiliate.fantasyakhada.com/.well-known/security.txt
  - note: soft 200 - returns the SPA's 6,110-byte HTML shell, not a spec
    status: 200
    url: https://app.fantasyakhada.com/openapi.json
  - note: soft 200 - HTML shell, rejected as an agent card; nothing written to a2a/
    status: 200
    url: https://app.fantasyakhada.com/.well-known/agent-card.json
  - status: 404
    url: https://play.google.com/store/apps/details?id=com.fantasyakhada.akhada
  - status: 404
    url: https://apps.apple.com/in/app/fantasy-akhada/id1555409649
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Fantasy Akhada is an Indian daily-fantasy-sports platform operated by Super Six Sports Gaming Private Limited (CIN U72900HR2019PTC083570) of Gurugram, Haryana, founded in 2020 by Amit Purohit, Sumit Kumar Jha, Sahil Ahuja, Amit Bhardwaj and Ankit Upreti, with cricket commentator Harsha Bhogle as brand ambassador. Users build virtual teams for real cricket, football, kabaddi, basketball and hockey fixtures and enter free and cash contests, with the platform taking a commission on entry fees; it marketed itself on the lowest commission rates in the category and claimed 3.5 to 4 million registered users. The product shipped only as a consumer iOS app and a sideloaded Android APK plus a React single-page web lobby - there is no developer program, public API, SDK, webhook surface or developer portal of any kind, and none has ever been published. As of the August 2026 probe the brand''s own web presence is broken: www.fantasyakhada.com is a dangling CNAME to a deleted AWS ap-south-1
  load balancer, the apex carries no address record, every backend service host referenced by the company''s own JavaScript bundles has been withdrawn from DNS, and only stale static CloudFront/S3 builds remain. India''s Promotion and Regulation of Online Gaming Act 2025 banned real-money online games nationwide in August 2025.'
layout: provider
modified: '2026-08-12'
name: Fantasy Akhada
nav: Providers
network: true
overview: 'Fantasy Akhada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fantasy Sports, Sports, Online Gaming, and Consumer Mobile.


  Fantasy Akhada''s developer surface includes YouTube channel and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Fantasy Akhada Domain Security
  slug: fantasy-akhada-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fantasy-akhada
tags:
- Company
- Fantasy Sports
- Sports
- Online Gaming
- Consumer Mobile
- Cricket
- India
- Entertainment
website: https://affiliate.fantasyakhada.com/
---
