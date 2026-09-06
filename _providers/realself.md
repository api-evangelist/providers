---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.realself.com/v1
  baseurl_source: declared
  description: 'RealSelf Lead Sharing publishes a notification to a partner-owned HTTPS endpoint every time a new patient lead is created on the platform. Delivery is over an Amazon SNS topic subscription: the subscr'
  name: RealSelf Lead Sharing
  slug: realself-lead-sharing
artifact_total: 12
asyncapis:
- description: Event surface RealSelf exposes to partner practices, practice-management systems and lead-routing vendors. When a consumer submits a consultation request on realself.com, RealSelf publishes a New Lead
  name: RealSelf Lead Sharing
  slug: realself-lead-sharing-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.realself.com/
- group: company
  title: ''
  type: Blog
  url: https://www.realself.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/RealSelf/rs-lead-sharing-subscriber-example
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RealSelf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realself.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.realself.com/security/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/realself-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/realself-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/realself-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realself-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realself-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/realself-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/realself-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/realself-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/realself-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/realself-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/realself-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/realself-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/realself-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/realself-llms.txt
created: '2026-08-26'
description: 'RealSelf is a Seattle-based consumer healthcare marketplace for elective aesthetic treatments — plastic surgery, cosmetic dermatology, injectables, cosmetic dentistry, hair restoration and vision correction. Consumers research procedures through community reviews, before-and-after photo galleries, doctor Q&A and the Worth It rating, then request consultations from the roughly 30,000 registered doctors and practices on the platform. RealSelf does not operate a general-purpose public developer program: its machine-readable surface is a partner Lead Sharing integration that publishes new patient leads to a subscriber over Amazon SNS, plus a publicly served JSON Schema registry at api.realself.com/v1/schemas covering the new-lead webhook payload and the internal event/page-analytics envelopes.'
image: https://avatars.githubusercontent.com/u/991957?v=4
json_schemas:
- name: Realself Event 1 0 0
  property_count: 8
  slug: realself-event-1-0-0
- name: New Lead Webhook
  property_count: 3
  slug: realself-new-lead-webhook-1-0-0
- name: Realself Pages Interaction 1 0 0
  property_count: 3
  slug: realself-pages-interaction-1-0-0
- name: Realself Pages Page 1 0 0
  property_count: 2
  slug: realself-pages-page-1-0-0
- name: Realself Pages View 1 0 0
  property_count: 6
  slug: realself-pages-view-1-0-0
layout: provider
modified: '2026-08-26'
name: RealSelf
nav: Providers
network: true
overview: 'RealSelf publishes 1 API on the [APIs.io](https://apis.io/) network: Lead Sharing. Tagged areas include Company, Healthcare, Aesthetics, Marketplace, and Reviews.


  The RealSelf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RealSelf''s developer surface includes engineering blog, documentation, authentication, and 17 more developer resources.'
plans:
- name: Realself Plans Pricing
  plan_count: 0
  slug: realself-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Realself Rate Limits
  slug: realself-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 55.2
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Realself Authentication
  slug: realself-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Realself Domain Security
  slug: realself-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Realself Vulnerability Disclosure
  slug: realself-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: realself
tags:
- Company
- Healthcare
- Aesthetics
- Marketplace
- Reviews
- Lead Generation
- Consumer Health
- Webhook
- JSON-Schema
website: https://www.realself.com/
---
