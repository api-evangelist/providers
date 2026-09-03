---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unrivaled-sports-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unrivaledsports.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unrivaledsports.com/privacy-policy/
- group: other
  title: ''
  type: Team
  url: https://unrivaledsports.com/team/
- group: company
  title: ''
  type: Careers
  url: https://www.teamworkonline.com/baseball-jobs/unrivaledsports/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unrivaled-sports/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/unrivaled-sports-stock
coverage:
  checked: '2026-09-02'
  detail: Unrivaled Sports is a youth sports venue and tournament operator — its whole corporate site is a four-page WordPress brochure (home, team, privacy policy, consumer health data notice) whose own sitemap lists no developer, docs, or API page, and STEP 0b contract discovery came back empty across unrivaledsports.com and the ripkenbaseball.com, cooperstown.com, unrivaledbaseball.com and baseballfactory.com brand hosts.
  evidence:
  - status: 200
    url: https://unrivaledsports.com/page-sitemap.xml
  - status: 404
    url: https://unrivaledsports.com/developers
  - status: 404
    url: https://unrivaledsports.com/openapi.json
  - status: 404
    url: https://unrivaledsports.com/llms.txt
  - status: 404
    url: https://unrivaledsports.com/.well-known/agent-card.json
  - status: 404
    url: https://ripkenbaseball.com/openapi.json
  - status: 404
    url: https://cooperstown.com/openapi.json
  - status: 404
    url: https://unrivaledbaseball.com/graphql
  - status: 404
    url: https://api.github.com/orgs/unrivaledsports
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'Unrivaled Sports is a youth sports platform and experience operator founded in March 2024 by Josh Harris and David Blitzer (Harris Blitzer Sports & Entertainment) with a strategic investment from The Chernin Group, later joined by DICK''S Sporting Goods and Under Armour as strategic investors. The company owns and operates a portfolio of youth sports destinations, tournaments and camps across baseball, softball, flag football and action sports — including Ripken Baseball, Cooperstown All Star Village, Baseball Factory, Softball Factory, Diamond Nation, Big League Dreams, Sports Force Parks, ForeverLawn Sports Complex at the Pro Football Hall of Fame Village, Rocker B Ranch, Unrivaled Flag, Under the Lights Flag Football and the We Are Camp action-sports properties (High Cascade, Windells, Snöbahn, Seek Skate Camp, Milepost 35). It reports 15 venues, 2 million annual visitors and 800,000 athletes served. It is a venue and event operator rather than a software company: as of
  2026-09-02 it publishes no developer program, no public API, and no machine-readable API contract on any of its own or its portfolio brands'' hosts.'
image: https://unrivaledsports.com/wp-content/uploads/2026/07/US-OG-Image.png
layout: provider
modified: '2026-09-02'
name: Unrivaled Sports
nav: Providers
network: true
overview: Unrivaled Sports is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Youth Sports, Baseball, and Softball.
random_paper: 18
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Unrivaled Sports Domain Security
  slug: unrivaled-sports-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unrivaled-sports
tags:
- Company
- Sports
- Youth Sports
- Baseball
- Softball
- Flag Football
- Events
- Tournaments
- Venues
- Camps
- Recreation
- Private Equity Backed
website: https://unrivaledsports.com/
---
