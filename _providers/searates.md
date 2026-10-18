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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/searates/refs/heads/main/llms/searates-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/searates-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/searates/refs/heads/main/hosts/searates-hosts.yml
  title: ''
  type: Hosts
  url: hosts/searates-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/searates/refs/heads/main/vendors/searates-vendors.yml
  title: ''
  type: Vendors
  url: vendors/searates-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dpworld.com/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dpworld.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.dpworld.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.dpworld.com/about-us/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.dpworld.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://dev.dpworld.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/searates/refs/heads/main/security/searates-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/searates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dpworld.com/en
coverage:
  checked: '2026-10-14'
  detail: Developer portal pages are static HTML with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://dev.dpworld.com/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: SeaRates provides global freight forwarding and logistics solutions, offering online tools for shipping quotes, tracking, and customs documentation. The company operates a digital platform that connects shippers with carriers, supporting air, sea, and road freight. SeaRates was acquired by DP World, integrating its services into a broader supply chain network, but continues to offer its branded portal for freight management and rate calculations.
image: https://dpw-p-001.sitecorecontenthub.cloud/api/public/content/og-7324d2a8316b4a8da223e7b2559a1905?v=365923f6
layout: provider
modified: '2026-10-14'
name: SeaRates
nav: Providers
network: true
overview: 'SeaRates is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight, Shipping, and Supply Chain.


  SeaRates'' developer surface includes documentation and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Searates Domain Security
  slug: searates-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: searates
tags:
- Company
- Logistics
- Freight
- Shipping
- Supply Chain
website: https://www.dpworld.com/en
---
