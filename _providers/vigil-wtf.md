---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vigil-wtf/refs/heads/main/plans/vigil-wtf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vigil-wtf-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vigil-wtf/refs/heads/main/authentication/vigil-wtf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vigil-wtf-authentication.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vigil-wtf/refs/heads/main/hosts/vigil-wtf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vigil-wtf-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vigil-wtf/refs/heads/main/vendors/vigil-wtf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vigil-wtf-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vigil.wtf/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vigil.wtf/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vigil.wtf/pricing
- group: start
  title: ''
  type: Login
  url: https://www.vigil.wtf/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.vigil.wtf/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vigil-wtf/refs/heads/main/security/vigil-wtf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vigil-wtf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vigil.wtf
coverage:
  checked: '2026-10-02'
  detail: API root returns 400 errors and no OpenAPI or docs are available.
  evidence:
  - status: 400
    url: https://api.vigil.wtf
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Vigil offers a token‑optimisation and cost‑monitoring proxy for large‑language‑model APIs. It aggregates calls to frontier models, providing per‑call latency, error tracking, and token‑usage analytics, enabling developers to manage expenses and performance across multiple providers.
image: https://www.vigil.wtf/opengraph-image
layout: provider
modified: '2026-10-02'
name: Vigil
nav: Providers
network: true
overview: 'Vigil is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, AI Middleware, Security, and Analytics.


  Vigil''s developer surface includes authentication, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Vigil Wtf Plans Pricing
  plan_count: 1
  slug: vigil-wtf-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vigil Wtf Authentication
  slug: vigil-wtf-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Vigil Wtf Domain Security
  slug: vigil-wtf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vigil-wtf
tags:
- Monitoring
- AI Middleware
- Security
- Analytics
website: https://www.vigil.wtf
---
