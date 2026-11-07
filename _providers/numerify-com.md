---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/numerify-com/authentication/numerify-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/numerify-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/numerify-com/llms/numerify-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/numerify-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/numerify-com/well-known/numerify-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/numerify-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/numerify-com/hosts/numerify-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/numerify-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/numerify-com/vendors/numerify-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/numerify-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://digital.ai/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digital.ai/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://digital.ai/leadership/
- group: company
  title: ''
  type: Blog
  url: https://digital.ai/learn/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.digital.ai/agility/docs/tags/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digital.ai/
- group: auth
  href: https://artifacts.apis.io/numerify-com/security/numerify-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numerify-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://numerify.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://numerify.com
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Numerify is a venture-backed startup originally listed in the API Evangelist harvest backlog, identified as a portfolio company of Lightspeed Venture Partners. The company appears to have been acquired or rebranded, as its primary domain numerify.com now redirects to Digital.ai, a separate enterprise software platform. No dedicated website or API documentation for Numerify could be located, and no public API specifications were found. This profile records the limited publicly available information about Numerify, noting its acquisition status and lack of active endpoints.
image: https://digital.ai/wp-content/uploads/2022/01/RC-SS-AI-2023-4-change0-risk-prediction-dashboard-updated.png
layout: provider
modified: '2026-10-29'
name: Numerify
nav: Providers
network: true
overview: 'Numerify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture, Startups, and Acquired.


  Numerify''s developer surface includes authentication, support, engineering blog, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 47.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/numerify-com/numerify-com-2026-11-03T140358.png
security:
- kind: authentication
  name: Numerify Com Authentication
  slug: numerify-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Numerify Com Domain Security
  slug: numerify-com-domain-security
  summary_line: TLSv1.2
slug: numerify-com
tags:
- Company
- Venture
- Startups
- Acquired
website: https://numerify.com
---
