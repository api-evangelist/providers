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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/probablymonsters-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.probablymonsters.com/
- group: operate
  title: ''
  type: Support
  url: https://support.probablymonsters.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.probablymonsters.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.probablymonsters.com/en/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProbablyMonsters
coverage:
  checked: '2026-08-26'
  detail: ProbablyMonsters ships finished console and PC games to players and nothing else — its entire public site is About, Careers, News and four game pages, its GitHub organization has zero public repositories, api/developer/docs subdomains do not resolve, and every contract-discovery path (/openapi.json, /swagger.json, /graphql, /llms.txt, /.well-known/*) returns a real 404 on the corporate host.
  evidence:
  - status: 404
    url: https://www.probablymonsters.com/openapi.json
  - status: 404
    url: https://www.probablymonsters.com/llms.txt
  - status: 404
    url: https://www.probablymonsters.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/ProbablyMonsters/repos
  - status: 200
    url: https://www.probablymonsters.com/en/about/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'ProbablyMonsters Inc. is an independent video game company headquartered in Bellevue, Washington, with a second location in Fort Worth, Texas. Founded in 2016 by former Bungie CEO Harold Ryan, it operates as a parent company that founds, funds and incubates development teams building AAA and AA interactive entertainment — publishing titles including Crimson Moon, Storm Lancers, IRE: A Prologue and Nekome. ProbablyMonsters sells finished games to players through console and PC storefronts; it is not a platform or developer-tools business. It publishes no developer program, no public API, no SDK and no machine-readable API description, and its GitHub organization carries zero public repositories. This profile records that absence with the probes behind it.'
image: https://www.probablymonsters.com/probablymonsters-meta-primary.jpg
layout: provider
modified: '2026-08-26'
name: ProbablyMonsters
nav: Providers
network: true
overview: 'ProbablyMonsters is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video Games, Game Development, Game Studios, and Interactive Entertainment.


  ProbablyMonsters'' developer surface includes support and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Probablymonsters Domain Security
  slug: probablymonsters-domain-security
  summary_line: TLSv1.3 · DMARC
slug: probablymonsters
tags:
- Company
- Video Games
- Game Development
- Game Studios
- Interactive Entertainment
- Entertainment
- Media
website: https://www.probablymonsters.com/
---
