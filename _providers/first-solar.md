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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.firstsolar.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-solar
- group: operate
  title: ''
  type: Support
  url: https://www.firstsolar.com/Products/Post-Sales-Support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstsolar.com/Policies/Terms-of-Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstsolar.com/Policies/Privacy-Policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-solar-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-solar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/first-solar-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-solar-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/first-solar-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/first-solar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/first-solar-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-solar-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-solar-domain-security.yml
created: '2025-03-01'
description: 'First Solar, Inc. (NASDAQ: FSLR) is the largest American manufacturer of solar modules and the leading producer of thin-film cadmium telluride (CdTe) photovoltaic technology, an alternative to conventional crystalline silicon. It designs and manufactures Series 6 and Series 7 modules at vertically integrated factories in Ohio, Alabama, Louisiana, India, Malaysia and Vietnam, and supports utility-scale PV projects with energy prediction, plant design and post-sales technical services. First Solar publishes no public API, developer program or machine-readable contract. Its "Developer Portal" is a Salesforce Experience Cloud site for solar project developers and EPC partners, not software developers, and requires a login. PlantPredict, the energy-modelling API and Python SDK First Solar built, was acquired by Terabase Energy in October 2021 and is catalogued against Terabase.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-solar.png
layout: provider
modified: '2026-09-10'
name: First Solar
nav: Providers
network: true
overview: 'First Solar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Solar, Energy, Renewable Energy, Manufacturing, and Fortune 1000.


  First Solar''s developer surface includes support, authentication, and 12 more developer resources.'
plans:
- name: First Solar Plans Pricing
  plan_count: 0
  slug: first-solar-plans-pricing
press:
- date: '2026-05-25'
  title: Overview
  url: https://www.firstsolar.com/About-Us/Overview
- date: '2026-05-25'
  title: First Solar Inaugurates New $1.1 Billion AI-Enabled ...
  url: https://www.businesswire.com/news/home/20251121295144/en/First-Solar-Inaugurates-New-%241.1-Billion-AI-Enabled-Louisiana-Manufacturing-Facility
- date: '2026-05-25'
  title: First Solar Selects Everstream Analytics to Enhance Risk ...
  url: https://www.everstream.ai/media/first-solar-selects-everstream-analytics-to-enhance-risk-mitigation-and-multi-tier-supply-chain-visibility/
- date: '2026-05-25'
  title: Buy First Solar Stock Now for AI Energy Growth and Value
  url: https://www.zacks.com/commentary/2764875/buy-first-solar-stock-now-for-ai-energy-growth-and-value
- date: '2026-05-25'
  title: First Solar Inaugurates New $1.1 Billion AI-Enabled ...
  url: https://www.opportunitylouisiana.gov/news/first-solar-inaugurates-new-1-1-billion-ai-enabled-louisiana-manufacturing-facility
random_paper: 8
rate_limits:
- limit_count: 0
  name: First Solar Rate Limits
  slug: first-solar-rate-limits
scopes:
- name: First Solar Scopes
  scope_count: 36
  slug: first-solar-scopes
  summary_line: 36 scopes · authorizationCode
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 20.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/first-solar/refs/heads/main/screenshots/first-solar-2026-06-20T181242.png
security:
- kind: authentication
  name: First Solar Authentication
  slug: first-solar-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: First Solar Domain Security
  slug: first-solar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: first-solar
tags:
- Solar
- Energy
- Renewable Energy
- Manufacturing
- Fortune 1000
- Photovoltaic
- Thin Film
- Utility-Scale Solar
- Clean Energy
website: https://www.firstsolar.com
---
