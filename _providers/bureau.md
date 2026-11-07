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
api_count: 1
apis:
- description: Bureau provides AI‑powered real‑time fraud prevention and identity decisioning platform.
  name: Bureau API
  slug: bureau-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bureau/vendors/bureau-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bureau-vendors.yml
- group: design
  href: https://artifacts.apis.io/bureau/conformance/bureau-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bureau-conformance.yml
- group: other
  href: https://artifacts.apis.io/bureau/hosts/bureau-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bureau-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bureau.id/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.bureau.id/support/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bureau.id/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://bureau.id/solutions/onboarding
- group: auth
  href: https://artifacts.apis.io/bureau/security/bureau-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bureau-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bureau.id
- group: docs
  title: ''
  type: Documentation
  url: https://bureau.id/resources/blog
- group: company
  title: ''
  type: Blog
  url: https://bureau.id/resources/blog
- group: operate
  title: ''
  type: Contact
  url: https://bureau.id/contact-us
coverage:
  checked: '2026-10-06'
  detail: Docs redirect to a login page at accounts.prism.bureau.id requiring authentication.
  evidence:
  - status: 302
    url: https://docs.bureau.id
  reason: partner-login
  state: gated
created: '2026-10-06'
description: Bureau provides AI‑powered real‑time fraud prevention and identity decisioning platform. It unifies risk data across the customer lifecycle, offering KYC, KYB, AML compliance, credit underwriting, and fraud detection for fintech, e‑commerce, and other digital businesses. The service combines device, behavior, identity, network, and transaction signals to deliver instant decisions across onboarding, authentication, and payments.
image: https://framerusercontent.com/images/KO6tYrHXwBCv8FqbOHdVaMMpXsY.png
layout: provider
modified: '2026-10-06'
name: Bureau
nav: Providers
network: true
overview: 'Bureau is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Prevention, Identity Verification, KYC, AML, and Fintech.


  Bureau''s developer surface includes support, getting-started guide, documentation, engineering blog, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bureau/bureau-2026-11-03T122759.png
security:
- kind: domain-security
  name: Bureau Domain Security
  slug: bureau-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bureau
tags:
- Fraud Prevention
- Identity Verification
- KYC
- AML
- Fintech
website: https://bureau.id
---
