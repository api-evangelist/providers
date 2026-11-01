---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/vishwa/plans/vishwa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vishwa-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.vishwa.ai/security
- group: auth
  href: https://artifacts.apis.io/vishwa/authentication/vishwa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vishwa-authentication.yml
- group: agent
  href: https://artifacts.apis.io/vishwa/llms/vishwa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vishwa-llms.txt
- group: agent
  href: https://artifacts.apis.io/vishwa/well-known/vishwa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vishwa-well-known.yml
- group: other
  href: https://artifacts.apis.io/vishwa/hosts/vishwa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vishwa-hosts.yml
- group: other
  href: https://artifacts.apis.io/vishwa/vendors/vishwa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vishwa-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vishwa.ai/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.vishwa.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vishwa.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://vishwa.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://vishwa.ai/news
- group: docs
  title: ''
  type: Documentation
  url: https://www.vishwa.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.vishwa.ai/docs/quickstart/automate-invoice-processing
- group: docs
  title: ''
  type: APIReference
  url: https://www.vishwa.ai/api-reference
- group: auth
  href: https://artifacts.apis.io/vishwa/security/vishwa-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vishwa-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vishwa/security/vishwa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vishwa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vishwa.ai/
coverage:
  checked: '2026-10-26'
  detail: Home page and docs are served as a JavaScript-rendered Next.js application with no machine-readable spec.
  evidence:
  - status: 200
    url: https://www.vishwa.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Vishwa AI is an AI underwriting platform for credit teams, enabling screening, diligence, underwriting, and monitoring of deals across private credit, commercial real estate, private equity, and institutional lending. The platform extracts data, verifies with experts, and provides a 100% audit trail, tying every output back to source documents for comprehensive compliance and risk analytics.
image: https://vishwa.ai/og/default.png
layout: provider
modified: '2026-10-26'
name: Vishwa
nav: Providers
network: true
overview: 'Vishwa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, FinTech, Underwriting, and Credit.


  Vishwa''s developer surface includes authentication, pricing, documentation, getting-started guide, API reference, and 13 more developer resources.'
plans:
- name: Vishwa Plans Pricing
  plan_count: 1
  slug: vishwa-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 20.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vishwa Authentication
  slug: vishwa-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vishwa Domain Security
  slug: vishwa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vishwa Trust Center
  slug: vishwa-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, FIPS 140
slug: vishwa
tags:
- Company
- AI
- FinTech
- Underwriting
- Credit
website: https://www.vishwa.ai/
---
