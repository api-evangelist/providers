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
artifact_total: 1
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.merchante.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.merchante.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.merchante.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.merchante.com/developer-portal
- group: agent
  href: https://artifacts.apis.io/merchante/llms/merchante-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/merchante-llms.txt
- group: agent
  href: https://artifacts.apis.io/merchante/well-known/merchante-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/merchante-well-known.yml
- group: other
  href: https://artifacts.apis.io/merchante/hosts/merchante-hosts.yml
  title: ''
  type: Hosts
  url: hosts/merchante-hosts.yml
- group: other
  href: https://artifacts.apis.io/merchante/vendors/merchante-vendors.yml
  title: ''
  type: Vendors
  url: vendors/merchante-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.merchante.com/
- group: auth
  href: https://artifacts.apis.io/merchante/security/merchante-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merchante-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.merchante.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.merchante.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: MerchantE provides modern acquiring solutions for ISVs, PayFacs, ISOs, and merchants, powered by human insight. It offers a modern payment infrastructure built for builders, enabling faster integration and trusted transaction processing across multiple channels.
image: https://www.merchante.com/og-image.jpg
layout: provider
modified: '2026-10-26'
name: MerchantE
nav: Providers
network: true
overview: 'MerchantE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, and Acquiring.


  MerchantE''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.5
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 46.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/merchante/merchante-2026-11-03T135501.png
security:
- kind: domain-security
  name: Merchante Domain Security
  slug: merchante-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: merchante
tags:
- Company
- Payments
- Fintech
- Acquiring
website: https://www.merchante.com/
---
