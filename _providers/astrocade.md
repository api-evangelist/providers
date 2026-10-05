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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Developer portal for Astrocade offering API documentation and integration details.
  name: Astrocade API
  slug: astrocade-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/astrocade/refs/heads/main/llms/astrocade-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astrocade-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astrocade/refs/heads/main/hosts/astrocade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astrocade-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astrocade/refs/heads/main/vendors/astrocade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astrocade-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.astrocade.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.astrocade.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrocade/refs/heads/main/security/astrocade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astrocade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astrocade.com/
coverage:
  checked: 2026-09-26
  detail: Developer portal returns HTML pages but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://dev.astrocade.com/openapi.json
  - status: 404
    url: https://dev.astrocade.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Astrocade is an online gaming platform that leverages artificial intelligence to let users play and create free games. It offers a community-driven experience where players can discover, share, and develop AI-powered games, fostering creativity and social interaction across its web-based service.
image: https://d16qq0o35va7kz.cloudfront.net/images/Astrocade_Share_Thumbnail_1200x630.jpg
layout: provider
modified: '2026-09-26'
name: Astrocade
nav: Providers
network: true
overview: 'Astrocade publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Artificial Intelligence, Online, Community, and Platform.


  Astrocade''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astrocade Domain Security
  slug: astrocade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astrocade
tags:
- Gaming
- Artificial Intelligence
- Online
- Community
- Platform
website: https://www.astrocade.com/
---
