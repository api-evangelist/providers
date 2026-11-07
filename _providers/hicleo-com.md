---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://hicleo.com/wahhh/
- group: agent
  href: https://artifacts.apis.io/hicleo-com/llms/hicleo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hicleo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/hicleo-com/well-known/hicleo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hicleo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hicleo-com/hosts/hicleo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hicleo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hicleo-com/vendors/hicleo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hicleo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hicleo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hicleo.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://hicleo.com/press/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.hicleo.com/
- group: auth
  href: https://artifacts.apis.io/hicleo-com/security/hicleo-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hicleo-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hicleo-com/security/hicleo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hicleo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hicleo.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://hicleo.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Cleo provides a holistic, cost‑saving caregiving support platform for working parents, caregivers, employers, health plans, and consultants. It offers proactive family care solutions that claim up to 3× ROI, improving workforce productivity, employee retention, and mental health while reducing healthcare costs across the globe.
layout: provider
modified: '2026-10-25'
name: Cleo
nav: Providers
network: true
overview: 'Cleo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Caregiving, Health, Employer, and Family.


  Cleo''s developer surface includes documentation and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 52.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hicleo-com/hicleo-com-2026-11-03T133359.png
security:
- kind: domain-security
  name: Hicleo Com Domain Security
  slug: hicleo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Hicleo Com Trust Center
  slug: hicleo-com-trust-center
  summary_line: SOC 2, GDPR
slug: hicleo-com
tags:
- Company
- Caregiving
- Health
- Employer
- Family
- Platform
website: https://hicleo.com/
---
