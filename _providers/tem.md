---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Private platform API powering the Tem RED utility application. Served from an AWS API Gateway at api.tem.energy and gated behind OIDC authentication; no public OpenAPI, SDK, or developer documentation
  name: Tem RED Platform API
  slug: tem-red-platform-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tem.energy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tem.energy
- group: operate
  title: ''
  type: Support
  url: https://tem.energy/get-in-touch
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tem.energy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tem.energy/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tem-energy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tem-energy/
created: '2026-07-17'
description: Tem (Tem-Energy Limited) is a UK-based energy technology company building AI-native transaction infrastructure for a modern energy market. Its RED platform is a modern utility that removes wholesale market markups to cut business electricity costs by up to 30%, provides transparent line-by-line billing from half-hourly meter data, and gives generators fairer earnings with renewable-energy traceability across 6,000+ sites. Backed by a February 2026 GBP 55M Series B led by Lightspeed Venture Partners. The customer-facing platform runs at app.tem.energy behind an OIDC login; the platform API at api.tem.energy is a private AWS API Gateway with no publicly documented developer surface at the time of profiling.
image: https://app.tem.energy/assets/images/tem-symbol-orange.png
layout: provider
modified: '2026-07-21'
name: Tem
nav: Providers
network: true
overview: 'Tem publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Utilities, and Sustainability.


  Tem''s developer surface includes support and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Tem Domain Security
  slug: tem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tem
tags:
- Company
- Energy
- Electricity
- Utilities
- Sustainability
- Renewable Energy
- Fintech
- Infrastructure
- United Kingdom
website: https://tem.energy
---
