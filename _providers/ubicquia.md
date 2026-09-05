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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://config.api.ubicquia.com/api/
  baseurl_source: declared
  description: The publicly described Ubicquia configuration and provisioning API ("Ubi Api", OpenAPI 3.0.0, 39 operations) covering sales orders, fulfillment details, device serial numbers and production files, dis
  name: Ubicquia Config API
  slug: ubicquia-config-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.ubicquia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ubicquia.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ubicquia.com/info-and-manuals-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ubicquia.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ubicquia.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.ubicquia.com/book-a-demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ubicquia.com/contact-us-to-purchase
- group: auth
  title: ''
  type: Compliance
  url: https://www.ubicquia.com/insights/the-ubicquia-security-program
- group: auth
  title: ''
  type: Security
  url: https://www.ubicquia.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ubicquia-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ubicquia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubicquia-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubicquia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ubicquia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ubicquia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ubicquia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ubicquia-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ubicquia-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ubicquia-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ubicquia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ubicquia-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubicquia-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubicquia-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-01'
description: Ubicquia is a Fort Lauderdale, Florida intelligent-infrastructure company that turns streetlights, distribution transformers, and substations that cities and utilities already own into connected, AI-monitored assets. Its plug-in hardware family — UbiCell (NEMA-socket streetlight controller), UbiHub and UbiHub AI+ (streetlight gigabit switch with cameras, edge AI and LTE), UbiGrid DTM+ (distribution transformer monitoring), UbiMetro (streetlight small cell) and UbiSmart AQM+ (air quality) — feeds the UbiVu analytics and asset-management platform, which the company states analyzes 4.3 billion data points daily. Ubicquia serves cities, electric utilities, public safety agencies and enterprises across grid monitoring, intelligent streetlighting, power quality, safety and security, street audit, substation monitoring, and traffic and curb management. It publicly serves an OpenAPI 3.0 description of its device configuration, provisioning and sales-order API at config.api.ubicquia.com,
  and raised a $106M Series D in 2026.
image: https://cdn.sanity.io/images/1851a3wt/production/6092260ef60a7711ec4ef0ae4785609ee5608d86-3072x1726.webp?w=1200&h=630&fit=crop&auto=format
layout: provider
modified: '2026-09-01'
name: Ubicquia
nav: Providers
network: true
overview: 'Ubicquia publishes 1 API on the [APIs.io](https://apis.io/) network: Config API. Tagged areas include Company, Smart Cities, Internet of Things, Energy, and Utilities.


  Ubicquia''s developer surface includes engineering blog, support, signup flow, pricing, authentication, and 19 more developer resources.'
plans:
- name: Ubicquia Plans Pricing
  plan_count: 0
  slug: ubicquia-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Ubicquia Rate Limits
  slug: ubicquia-rate-limits
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 41.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 55.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubicquia/refs/heads/main/screenshots/ubicquia-2026-09-02T164714.png
security:
- kind: authentication
  name: Ubicquia Authentication
  slug: ubicquia-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ubicquia Domain Security
  slug: ubicquia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ubicquia Vulnerability Disclosure
  slug: ubicquia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ubicquia
tags:
- Company
- Smart Cities
- Internet of Things
- Energy
- Utilities
- Electric Grid
- Streetlights
- Public Safety
- Infrastructure
- Sensors
- Edge AI
- Transformer Monitoring
website: https://www.ubicquia.com/
---
