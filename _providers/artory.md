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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artory/refs/heads/main/llms/artory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artory-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artory/refs/heads/main/hosts/artory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artory-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wag-art.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wag-art.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.wag-art.com/who-we-are/press
- group: other
  title: ''
  type: Leadership
  url: https://www.wag-art.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artory/refs/heads/main/security/artory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wag-art.com/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found at api.wag-art.com despite probing common endpoints.
  evidence:
  - status: 0
    url: https://api.wag-art.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Artory provides a secure, immutable ledger for recording and verifying the provenance of high‑value assets such as fine art, collectibles, and real estate. By combining blockchain‑based technology with data science, Artory enables collectors, dealers, and institutions to maintain a trusted record of ownership, transaction history, and valuation. The platform supports asset‑level data integration, secure document storage, and API access for partners to query and update asset records, fostering transparency and confidence in the secondary market.
image: https://framerusercontent.com/assets/iH0NXT3mQAExFaujkX72Vfn4.png
layout: provider
modified: '2026-09-26'
name: Artory
nav: Providers
network: true
overview: Artory is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Art, Marketplace, Data, and Asset Management.
random_paper: 13
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artory Domain Security
  slug: artory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artory
tags:
- Company
- Art
- Marketplace
- Data
- Asset Management
website: https://www.wag-art.com/
---
