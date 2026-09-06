---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Ember API returns per-structure property risk scores, modeled expected annual loss, and retrofit-impact evaluation for individual homes, driven by physics-based hazard simulation and a learned sur
  name: Ember API
  slug: risklytics-ember-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/risklytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.risklytics.ai/
- group: start
  title: ''
  type: Portal
  url: https://platform.risklytics.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.risklytics.ai/docs
- group: start
  title: ''
  type: Login
  url: https://platform.risklytics.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.risklytics.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.risklytics.ai/terms
- group: other
  title: ''
  type: Methodology
  url: https://www.risklytics.ai/methodology
- group: auth
  title: ''
  type: Authentication
  url: authentication/risklytics-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/risklytics-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/risklytics-llms.txt
created: '2026-07-17'
description: Risklytics is an AI-native property and catastrophe risk company (Y Combinator Summer 2026, based in San Francisco, founded 2026 by Samuel Gold and Alexander Risio). It builds hyper-localized disaster risk models that simulate specific natural hazards - wildfire, flood, wind, earthquake, and debris runout - against individual home structures rather than ZIP-code averages, creating a per-structure digital twin from building footprints, lidar, and public records. Its Ember API returns property risk scores, modeled annual loss estimates, and retrofit-impact modeling used for insurance risk selection and portfolio triage (currently California-only, production model ember-1.3.0-firewall). The company also operates the FireCast platform and an AI-native brokerage for hard-to-place commercial insurance. API access is via a personal API key issued through the platform dashboard; there is no public OpenAPI, developer portal, or blog published to date, so this profile captures the company
  identity, the documented Ember API plans and authentication model, and the security posture of its web surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/risklytics.png
layout: provider
modified: '2026-07-21'
name: Risklytics
nav: Providers
network: true
overview: 'Risklytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Risk, and Wildfire.


  Risklytics'' developer surface includes developer portal, documentation, pricing, authentication, and 7 more developer resources.'
plans:
- name: Risklytics Plans Pricing
  plan_count: 2
  slug: risklytics-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/risklytics/refs/heads/main/screenshots/risklytics-2026-09-02T153903.png
security:
- kind: authentication
  name: Risklytics Authentication
  slug: risklytics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Risklytics Domain Security
  slug: risklytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: risklytics
tags:
- Company
- Insurance
- Insurtech
- Risk
- Wildfire
- Property
- Catastrophe
- Analytics
- Machine-Learning
- Underwriting
website: https://www.risklytics.ai/
---
