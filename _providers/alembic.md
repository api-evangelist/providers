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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alembic/refs/heads/main/hosts/alembic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alembic-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alembic.com/terms
- group: auth
  title: ''
  type: Security
  url: https://alembic.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alembic.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://alembic.com/news
- group: company
  title: ''
  type: Blog
  url: https://alembic.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alembic/refs/heads/main/security/alembic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alembic-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alembic/refs/heads/main/security/alembic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alembic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alembic.com/
created: '2026-09-24'
description: Alembic offers an enterprise causal AI platform that models cause‑and‑effect across marketing, sales, pricing, supply and operations. It provides decision‑grade intelligence for CEOs, CFOs, COOs, CMOs and other senior leaders, enabling real‑time simulation of strategic choices and proof of what drives growth.
image: https://cdn.sanity.io/images/8dklkuhz/production/33ce3d4c505c58a645ece94772a71fea58ecad98-1200x630.png
layout: provider
modified: '2026-09-24'
name: Alembic
nav: Providers
network: true
overview: 'Alembic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Causal AI, Decision Intelligence, and Business Intelligence.


  Alembic''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 41.1
    operational_transparency: 10.5
  previous_composite: 10.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alembic Domain Security
  slug: alembic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alembic Vulnerability Disclosure
  slug: alembic-vulnerability-disclosure
  summary_line: disclosure policy published
slug: alembic
tags:
- Causal AI
- Decision Intelligence
- Business Intelligence
website: https://alembic.com/
---
