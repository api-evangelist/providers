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
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bench/refs/heads/main/plans/bench-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bench-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bench.co/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bench/refs/heads/main/hosts/bench-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bench-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bench/refs/heads/main/vendors/bench-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bench-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bench.co/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.bench.co/signup
- group: auth
  title: ''
  type: Security
  url: https://www.bench.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bench.co/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bench.co/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.bench.co/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bench.co/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.bench.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.bench.co/article-category/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.bench.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bench/refs/heads/main/security/bench-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bench-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bench/refs/heads/main/security/bench-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bench-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bench.co
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or gRPC spec found despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.bench.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bench provides online bookkeeping services for small businesses, offering a proprietary technology platform that handles ongoing monthly books, catch‑up bookkeeping, tax filing, and financial advisory. The company aims to simplify accounting with automated tools, fractional bookkeepers, and a suite of calculators and resources to help businesses understand profit margins, operational metrics, and inventory costs.
image: https://cdn.prod.website-files.com/64559587fb856f82933854bf/64c085f260dc48172089af7f_Frame_14510.jpg
layout: provider
modified: '2026-09-27'
name: Bench
nav: Providers
network: true
overview: 'Bench is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Bookkeeping, Small Business, Software-as-a-Service, and Finance.


  Bench''s developer surface includes signup flow, pricing, changelog, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Bench Plans Pricing
  plan_count: 2
  slug: bench-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bench Domain Security
  slug: bench-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bench Trust Center
  slug: bench-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
slug: bench
tags:
- Accounting
- Bookkeeping
- Small Business
- Software-as-a-Service
- Finance
website: https://www.bench.co
---
