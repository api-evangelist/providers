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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquishair/refs/heads/main/hosts/aquishair-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquishair-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquishair/refs/heads/main/vendors/aquishair-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquishair-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aquishair.co.uk/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aquishair.co.uk/pages/privacy-policy-1
- group: company
  title: ''
  type: Newsroom
  url: https://aquishair.co.uk/pages/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquishair/refs/heads/main/security/aquishair-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquishair-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aquishair.co.uk
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/aquishair
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Aquishair is a UK‑based brand that designs and sells premium hair towels, turbans and related hair‑care accessories. Their products focus on quick drying, softness and style, marketed toward women seeking convenient, high‑quality hair solutions. The company emphasizes natural materials and scientific formulation, offering a range that includes the popular Lisse Dair hair turban and other innovative hair‑care items. Aquishair operates an online store and provides detailed product information, brand story, and support through its website.
layout: provider
modified: '2026-09-25'
name: Aquishair
nav: Providers
network: true
overview: Aquishair is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hair Care, E-Commerce, United Kingdom, and Consumer Goods.
random_paper: 21
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquishair Domain Security
  slug: aquishair-domain-security
  summary_line: TLSv1.3
slug: aquishair
tags:
- Company
- Hair Care
- E-Commerce
- United Kingdom
- Consumer Goods
website: https://aquishair.co.uk
---
