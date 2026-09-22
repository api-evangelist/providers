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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aetherbio/refs/heads/main/security/aetherbio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aetherbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aetherbio.com/
- group: company
  title: ''
  type: About
  url: https://aetherbio.com/about
- group: operate
  title: ''
  type: Contact
  url: mailto:info@aetherbio.com
- group: company
  title: ''
  type: Careers
  url: https://careers.kula.ai/aetherbio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aetherbiomachines
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aetherbio
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AetherMachines
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aetherbio.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aetherbio.com/terms-and-conditions
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aetherbio
coverage:
  checked: '2026-09-12'
  detail: Aether Biomachines sells physical goods — RapidPrint and Ultra reinforced 3D printing filaments, and protein-based critical mineral processing — and its entire public surface is a 15-page Webflow marketing site (home, technology, products, about, two TDS download forms, three news posts, privacy, terms) whose nav and footer contain no developer, docs, portal, API or integration link at all; its Protein Function Model and "Platform + ML" team are internal, with no external access mechanism described anywhere on the site. Every REST/OpenAPI, GraphQL, MCP, agent-card, /llms.txt, /agents.md and /.well-known/ path probed on aetherbio.com and www.aetherbio.com returned a hard 404 (verified against a control path returning the identical 52,431-byte 404 body), api./developer./developers./app./platform./portal./mcp..aetherbio.com do not resolve in DNS, docs.aetherbio.com is an internal Google Drive alias that 302s to drive.google.com, and both company GitHub organizations (aetherbio, aetherbiomachines)
    contain only an abandoned 2020 static website repo, an empty placeholder and four forks of third-party ML/bio tools — no first-party SDK, contract or spec.
  evidence:
  - status: 200
    url: https://aetherbio.com/
  - status: 404
    url: https://aetherbio.com/openapi.json
  - status: 404
    url: https://aetherbio.com/swagger.json
  - status: 404
    url: https://aetherbio.com/api-docs
  - status: 404
    url: https://aetherbio.com/graphql
  - status: 404
    url: https://aetherbio.com/llms.txt
  - status: 404
    url: https://aetherbio.com/agents.md
  - status: 404
    url: https://aetherbio.com/developers
  - status: 404
    url: https://aetherbio.com/.well-known/agent-card.json
  - status: 404
    url: https://aetherbio.com/.well-known/agent.json
  - status: 404
    url: https://aetherbio.com/.well-known/api-catalog
  - status: 404
    url: https://www.aetherbio.com/.well-known/security.txt
  - status: 404
    url: https://aetherbio.com/zz-api-evangelist-control-9f3a
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'Aether Biomachines, Inc. (trading as Aether Bio) is a Menlo Park, California protein engineering and advanced materials company founded in 2017 by Pavle Jeremic, which operates a proprietary robotic high-throughput screening laboratory and trains a Protein Function Model on millions of micro-scale enzyme experiments in order to discover novel proteins with novel functions. The company converts that discovery platform into physical products rather than software: the RapidPrint series of reinforced nylon 3D printing filaments and the Ultra series of carbon fiber-loaded filaments for aerospace and defense additive manufacturing, with aluminum-replacing super materials and AI-designed proteins for selective extraction of lithium, nickel and rare earth elements from low-concentration brines in development. It raised a $49M Series A in 2023 and a $15M round led by Tribe Capital in December 2025. Aether Bio runs no developer program and publishes no public API, SDK, webhook surface
  or machine-readable API contract on any host it operates; its platform and machine learning work is internal to the company.'
image: https://cdn.prod.website-files.com/693839bb65b9bdaa8d3db9d2/693839bb65b9bdaa8d3dba14_Aether%20Bio_Webclip.png
layout: provider
modified: '2026-09-12'
name: Aether Biomachines
nav: Providers
network: true
overview: Aether Biomachines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Protein Engineering, Synthetic Biology, and Advanced Materials.
random_paper: 1
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 2.6
  previous_composite: 9.6
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aetherbio Domain Security
  slug: aetherbio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aetherbio
tags:
- Company
- Biotechnology
- Protein Engineering
- Synthetic Biology
- Advanced Materials
- Advanced Manufacturing
- Additive Manufacturing
- Critical Minerals
- Machine-Learning
- Aerospace and Defense
website: https://aetherbio.com/
---
