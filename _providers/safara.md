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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/safara/hosts/safara-hosts.yml
  title: ''
  type: Hosts
  url: hosts/safara-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.godrift.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.godrift.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.godrift.com/auth/login/email
- group: auth
  href: https://artifacts.apis.io/safara/security/safara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.safara.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.safara.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: 'Safara is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by sequoia-capital) and added to the network as a stub for full-pipeline profiling.'
image: https://www.godrift.com/static/meta_image.jpg
layout: provider
modified: '2026-10-23'
name: Safara
nav: Providers
network: true
overview: Safara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 22
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Safara Domain Security
  slug: safara-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: safara
tags:
- Company
website: https://www.safara.com/
---
