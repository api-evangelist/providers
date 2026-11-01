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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.pearly.co/security
- group: other
  href: https://artifacts.apis.io/pearly/hosts/pearly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pearly-hosts.yml
- group: other
  href: https://artifacts.apis.io/pearly/vendors/pearly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pearly-vendors.yml
- group: auth
  href: https://artifacts.apis.io/pearly/security/pearly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pearly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pearly/security/pearly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pearly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pearly.co/
- group: start
  title: ''
  type: Login
  url: https://app.pearly.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pearly.co/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pearly.co/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.pearly.co/security
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pearly.co/status
- group: operate
  title: ''
  type: Support
  url: https://www.pearly.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pearly.co/legal/terms
coverage:
  checked: '2026-10-25'
  detail: The provider's website offers human‑readable pricing and policy pages but publishes no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://www.pearly.co/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Pearly provides dental practice billing and revenue cycle management automation software. Its platform streamlines patient billing, accounts receivable, payment plans, letter automation, and integrates with practice management systems. Pearly serves DSOs, group practices, and private dental offices, offering online payments, reporting, and AI‑driven insights to improve cash flow and reduce administrative overhead.
image: https://cdn.prod.website-files.com/6271f4e0a1e7c31d31ac990a/667b4ac23b6ba346e80dc84d_Pearly_Dental_RCM_Home.png
layout: provider
modified: '2026-10-25'
name: Pearly
nav: Providers
network: true
overview: 'Pearly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Billing, RCM, SaaS, and Healthcare.


  Pearly''s developer surface includes pricing, support, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pearly Domain Security
  slug: pearly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pearly Trust Center
  slug: pearly-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: pearly
tags:
- Dental
- Billing
- RCM
- SaaS
- Healthcare
website: https://www.pearly.co/
---
