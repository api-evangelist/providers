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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://runontabz.com/company/security
- group: auth
  href: https://artifacts.apis.io/tabz/well-known/tabz-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tabz-help-security.txt
- group: agent
  href: https://artifacts.apis.io/tabz/well-known/tabz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tabz-well-known.yml
- group: other
  href: https://artifacts.apis.io/tabz/hosts/tabz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tabz-hosts.yml
- group: other
  href: https://artifacts.apis.io/tabz/vendors/tabz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tabz-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.runontabz.com/en/
- group: auth
  title: ''
  type: Security
  url: https://runontabz.com/company/security
- group: start
  title: ''
  type: Login
  url: https://pharmacy.runontabz.com/login/?returnUrl=%2F
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runontabz.com/
- group: auth
  href: https://artifacts.apis.io/tabz/security/tabz-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tabz-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tabz/security/tabz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tabz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runontabz.com
- group: company
  title: ''
  type: Blog
  url: https://runontabz.com/company/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runontabz.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runontabz.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runontabz.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://docs.runontabz.com/mcp
  - status: 200
    url: https://runontabz.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Tabz is a pharmacy commerce platform that provides payments, checkout, and invoicing solutions for manufacturers, mail‑order, compounding, specialty, and retail pharmacies. It enables seamless patient payment collection, integrates with pharmacy management systems, and offers APIs for building custom commerce experiences. Tabz aims to simplify the complex pharmacy payment ecosystem, supporting high‑cost medication workflows and improving checkout efficiency across the industry.
image: https://runontabz.com/logo.png
layout: provider
modified: '2026-10-21'
name: Tabz
nav: Providers
network: true
overview: 'Tabz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Payments, Checkout, and Commerce.


  Tabz''s developer surface includes support, documentation, engineering blog, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 11.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tabz/tabz-2026-11-03T144259.png
security:
- kind: domain-security
  name: Tabz Domain Security
  slug: tabz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tabz Trust Center
  slug: tabz-trust-center
  summary_line: PCI DSS, HIPAA
slug: tabz
tags:
- Company
- Pharmacy
- Payments
- Checkout
- Commerce
- Healthcare
website: https://runontabz.com
---
