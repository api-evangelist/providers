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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/vat-it/llms/vat-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vat-it-llms.txt
- group: agent
  href: https://artifacts.apis.io/vat-it/well-known/vat-it-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vat-it-well-known.yml
- group: other
  href: https://artifacts.apis.io/vat-it/hosts/vat-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vat-it-hosts.yml
- group: other
  href: https://artifacts.apis.io/vat-it/vendors/vat-it-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vat-it-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://vatit.com/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vatit.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://vatit.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vatit.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://vatit.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vatit.com/
- group: auth
  href: https://artifacts.apis.io/vat-it/security/vat-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vat-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vatit.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://vatit.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: VAT IT provides global indirect tax solutions, leveraging AI-driven technology to streamline e‑invoicing, VAT compliance, US sales tax, and VAT reclaim for businesses. Their platform offers tools such as VAT potential calculators, e‑invoicing mandate tools, and industry‑specific guides, aiming to maximize tax recovery and simplify compliance across multiple jurisdictions.
layout: provider
modified: '2026-10-26'
name: VAT IT
nav: Providers
network: true
overview: 'VAT IT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Compliance, Artificial Intelligence, and Finance.


  VAT IT''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 51.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vat-it/vat-it-2026-11-03T145815.png
security:
- kind: domain-security
  name: Vat It Domain Security
  slug: vat-it-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vat-it
tags:
- Company
- Tax
- Compliance
- Artificial Intelligence
- Finance
- Software-as-a-Service
website: https://vatit.com/
---
