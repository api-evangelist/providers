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
api_count: 1
apis:
- description: The AI Agent API provides endpoints for interacting with the GoodbyeMatrix platform, including asset management, residency assistance, and investment services. It is described in the technical referen
  name: GoodbyeMatrix AI Agent API
  slug: ai-agent-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/goodbyematrix-com/llms/goodbyematrix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goodbyematrix-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/goodbyematrix-com/well-known/goodbyematrix-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goodbyematrix-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/goodbyematrix-com/well-known/goodbyematrix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/goodbyematrix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/goodbyematrix-com/hosts/goodbyematrix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goodbyematrix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/goodbyematrix-com/vendors/goodbyematrix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goodbyematrix-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/goodbyematrix-com/security/goodbyematrix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goodbyematrix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goodbyematrix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://goodbyematrix.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://ai.goodbyematrix.com/cbi/api/agent/v1/docs
- group: company
  title: ''
  type: Blog
  url: https://goodbyematrix.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goodbyematrix.com/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goodbyematrix.com/en/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://goodbyematrix.com/en/pricing-api/
coverage:
  checked: '2026-10-30'
  detail: Docs at https://ai.goodbyematrix.com are behind a Cloudflare Access login page.
  evidence:
  - status: 302
    url: https://ai.goodbyematrix.com
  reason: partner-login
  state: gated
created: '2026-10-30'
description: GoodbyeMatrix helps entrepreneurs, investors and digital nomads grow and protect wealth, reduce taxes legally, obtain second residencies and citizenships, and access offshore banking and investment services worldwide. It offers strategic offshore solutions, gold storage, and global lifestyle guidance.
image: https://mlbgycir5pim.i.optimole.com/cb:rsPN~537d5/w:auto/h:auto/q:mauto/g:sm/https://goodbyematrix.com/wp-content/uploads/2022/07/schweiz-1-scaled.jpg
layout: provider
modified: '2026-10-30'
name: goodbyematrix-com
nav: Providers
network: true
overview: 'goodbyematrix-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wealth, Offshore, Tax-Reduction, Citizenship, and Investment.


  goodbyematrix-com''s developer surface includes documentation, API reference, engineering blog, pricing, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 73.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goodbyematrix-com/goodbyematrix-com-2026-11-03T132931.png
security:
- kind: domain-security
  name: Goodbyematrix Com Domain Security
  slug: goodbyematrix-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: goodbyematrix-com
tags:
- Wealth
- Offshore
- Tax-Reduction
- Citizenship
- Investment
website: https://goodbyematrix.com/
---
