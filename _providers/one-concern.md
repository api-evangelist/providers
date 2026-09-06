---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.oneconcern.com
  baseurl_source: declared
  description: The Location API from One Concern — 5 operation(s) for location.
  name: One Concern Location API
  slug: one-concern-location-api
artifact_total: 5
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/one-concern-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/one-concern-domino-ai-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://oneconcern.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.oneconcern.com/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.oneconcern.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.oneconcern.com/api-spec
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.oneconcern.com/overview
- group: company
  title: ''
  type: Blog
  url: https://oneconcern.com/en/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://oneconcern.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://oneconcern.com/en/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oneconcern
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oneconcern.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oneconcern.com/en/privacy/
- group: company
  title: ''
  type: About
  url: https://oneconcern.com/en/about/
- group: other
  title: ''
  type: Products
  url: https://oneconcern.com/en/products/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oneconcern/
- group: build
  title: ''
  type: Packages
  url: packages/one-concern-packages.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/one-concern-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/one-concern-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/one-concern-domain-security.yml
created: '2026-08-26'
description: One Concern is a Palo Alto, California climate-resilience analytics company that builds a digital twin of the built environment to quantify physical climate and natural-catastrophe risk in units of time rather than broad-brush hazard bands. Its Domino AI platform models the recovery of an individual building together with the lifelines it depends on — power distribution, ports, airports, roads and bridges, the surrounding residential community — and returns business-interruption downtime statistics, property-damage ratios and a 1CRX resilience score for a given latitude and longitude, per peril (flood, tropical-cyclone wind, seismic ground shaking, or all perils integrated), per return period or planning horizon, and under baseline or 2050 climate-change scenarios. The company sells to insurers, reinsurers, financial services and real estate, and exposes the platform to customers through the Domino AI API, a five-operation REST contract documented at developer.oneconcern.com
  and served from api.oneconcern.com behind a Tyk gateway with a customer-issued x-1c-api-token header.
image: https://oneconcern.com/wp-content/uploads/2021/10/One-Concern-Logo.png
layout: provider
modified: '2026-08-26'
name: One Concern
nav: Providers
network: true
overview: 'One Concern publishes 1 API on the [APIs.io](https://apis.io/) network: Location API. Tagged areas include Climate Risk, Catastrophe Modeling, Resilience, Insurance, and Reinsurance.


  One Concern''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, and 16 more developer resources.'
plans:
- name: One Concern Plans Pricing
  plan_count: 0
  slug: one-concern-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: One Concern Rate Limits
  slug: one-concern-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 46.3
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 36.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/one-concern/refs/heads/main/screenshots/one-concern-2026-09-02T150842.png
security:
- kind: authentication
  name: One Concern Authentication
  slug: one-concern-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: One Concern Domain Security
  slug: one-concern-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: one-concern
tags:
- Climate Risk
- Catastrophe Modeling
- Resilience
- Insurance
- Reinsurance
- Risk Analytics
- Geospatial
- Business Interruption
- Real-Estate
- Financial-Services
- Artificial Intelligence
website: https://oneconcern.com/en/
---
