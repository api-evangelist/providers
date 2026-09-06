---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Revelator Agentic Access
  operation_count: 32
  slug: revelator-agentic-access
  summary_line: 32 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Partner account signup, login, switching, and permissions.
  name: Revelator Account API
  slug: revelator-account-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Rights contracts and payee management.
  name: Revelator Accounting API
  slug: revelator-accounting-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Revenue, consumption, engagement, playlist, and artificial-streaming analytics.
  name: Revelator Analytics API
  slug: revelator-analytics-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Release validation, distribution options, queueing, status, takedown.
  name: Revelator Distribution API
  slug: revelator-distribution-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Payment-provider (Tipalti) integration.
  name: Revelator Integrations API
  slug: revelator-integrations-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Common reference/lookup data.
  name: Revelator Lookup API
  slug: revelator-lookup-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Financial sale reports and user statements.
  name: Revelator Revenue API
  slug: revelator-revenue-api
- baseURL: https://api.revelator.com
  baseurl_source: declared
  description: Minting and retrieving ERC1155 royalty tokens.
  name: Revelator Royalty Tokens API
  slug: revelator-royalty-tokens-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Revelator Account API
  slug: open-revelator-account-api
- collection_type: open
  name: Revelator Account Accounting API
  slug: open-revelator-accounting-api
- collection_type: open
  name: Revelator Account Analytics API
  slug: open-revelator-analytics-api
- collection_type: open
  name: Revelator Account Distribution API
  slug: open-revelator-distribution-api
- collection_type: open
  name: Revelator Account Integrations API
  slug: open-revelator-integrations-api
- collection_type: open
  name: Revelator Account Lookup API
  slug: open-revelator-lookup-api
- collection_type: open
  name: Revelator Account Revenue API
  slug: open-revelator-revenue-api
- collection_type: open
  name: Revelator Account Royalty Tokens API
  slug: open-revelator-royalty-tokens-api
- collection_type: open
  name: Revelator API
  slug: open-revelator
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/revelator-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revelator-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revelator-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revelator-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revelator
- group: company
  title: ''
  type: Website
  url: https://www.revelator.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.revelator.com
- group: commercial
  title: ''
  type: Plans
  url: plans/revelator-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revelator-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revelator-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.revelator.com/blog
created: '2026-06-21'
description: Revelator is a music distribution and rights, royalties, and payments infrastructure platform for labels, distributors, and music businesses. Its REST API exposes the digital supply chain - distribution, catalog, analytics and trends, royalty accounting, and payments - behind a single OAuth2 Bearer-token interface using a child-account model.
finops:
- name: Revelator Finops
  service_category: Media and Entertainment
  slug: revelator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revelator.png
layout: provider
modified: '2026-06-21'
name: Revelator
nav: Providers
network: true
overview: 'Revelator publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounting API, Analytics API, and 5 more. Tagged areas include Music, Distribution, Rights, Royalties, and Payments.


  Revelator''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Revelator Plans Pricing
  plan_count: 4
  slug: revelator-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Revelator Rate Limits
  slug: revelator-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revelator/refs/heads/main/screenshots/revelator-2026-09-02T153702.png
security:
- kind: authentication
  name: Revelator Authentication
  slug: revelator-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Revelator Domain Security
  slug: revelator-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revelator
tags:
- Music
- Distribution
- Rights
- Royalties
- Payments
- Analytics
website: https://www.revelator.com
---
