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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Automate on-demand deliveries with GoGet — create, update, and cancel jobs, estimate fees, check coverage and availability, track GoGetters live, and receive job-status webhooks. Authenticated with an
  name: GoGet Delivery API
  slug: goget-delivery-api
artifact_total: 4
asyncapis:
- description: ''
  name: Goget Jobs Webhooks
  slug: goget-jobs-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://goget.my
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.goget.my/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.goget.my/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.goget.my/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.goget.my/
- group: start
  title: ''
  type: SignUp
  url: https://app.goget.my/
- group: operate
  title: ''
  type: Support
  url: https://support.goget.my/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://goget.my/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://goget.my/business/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goget.my/terms_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goget.my/privacy_policy
- group: operate
  title: ''
  type: StatusPage
  url: https://gogetmy.instatus.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/goget-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goget-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goget-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goget-jobs-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/goget-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goget-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goget-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goget-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goget-domain-security.yml
created: '2026-07-17'
description: GoGet is a Malaysian on-demand workforce and delivery technology company whose network of verified workers, called GoGetters, powers same-day delivery, dispatch, and blended-workforce staffing for more than 10,000 businesses across Klang Valley, Penang, Negeri Sembilan and Johor Bahru. Beyond its consumer and business apps, GoGet exposes the GoGet Delivery API so merchants can automate on-demand deliveries end to end — create and manage jobs, estimate delivery fees, verify coverage and availability, track GoGetters live, and receive job lifecycle events via webhooks. Integration is free and typically completed in one to two weeks. GoGet is backed by 500 Global.
image: https://web.goget.my/assets/images/og/logo_1200_630.png
layout: provider
modified: '2026-07-19'
name: GoGet
nav: Providers
network: true
overview: 'GoGet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Delivery, Logistics, On-Demand, and Gig Economy.


  The GoGet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoGet''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 36.8
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goget/refs/heads/main/screenshots/goget-2026-07-25T220015.png
security:
- kind: authentication
  name: Goget Authentication
  slug: goget-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goget Domain Security
  slug: goget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goget
tags:
- Company
- Delivery
- Logistics
- On-Demand
- Gig Economy
- Workforce
- Dispatch
- Malaysia
- Webhook
website: https://goget.my
---
