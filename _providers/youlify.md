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
- group: auth
  href: https://artifacts.apis.io/youlify/well-known/youlify-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/youlify-help-security.txt
- group: agent
  href: https://artifacts.apis.io/youlify/well-known/youlify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/youlify-well-known.yml
- group: other
  href: https://artifacts.apis.io/youlify/hosts/youlify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/youlify-hosts.yml
- group: other
  href: https://artifacts.apis.io/youlify/vendors/youlify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/youlify-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.youlify.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.youlify.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.youlify.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://webflow.youlify.ai/resources/news
- group: company
  title: ''
  type: Blog
  url: https://www.youlify.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.youlify.ai/en/collections/17787387-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.youlify.ai/
- group: auth
  href: https://artifacts.apis.io/youlify/security/youlify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/youlify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://youlify.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://pay.youlify.ai/mcp
  - status: 403
    url: https://practice.youlify.ai/mcp
  - status: 200
    url: https://youlify.ai
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Youlify provides an AI-driven revenue cycle management platform tailored for U.S. healthcare organizations. Its solution automates medical billing, maximizes revenue, reduces claim denials, and offers transparent analytics. Leveraging advanced machine learning, Youlify streamlines billing workflows, improves cash flow, and supports compliance with healthcare regulations, positioning itself as a modern fintech partner for providers and payers.
layout: provider
modified: '2026-10-21'
name: Youlify
nav: Providers
network: true
overview: 'Youlify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Fintech, Artificial Intelligence, and Revenue Cycle.


  Youlify''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 45.5
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/youlify/youlify-2026-11-03T150342.png
security:
- kind: domain-security
  name: Youlify Domain Security
  slug: youlify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: youlify
tags:
- Company
- Healthcare
- Fintech
- Artificial Intelligence
- Revenue Cycle
website: https://youlify.ai
---
