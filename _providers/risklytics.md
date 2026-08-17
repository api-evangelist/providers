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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
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
overview: 'Risklytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, InsurTech, Risk, and Wildfire.


  Risklytics'' developer surface includes developer portal, documentation, pricing, authentication, and 7 more developer resources.'
plans:
- name: Risklytics Plans Pricing
  plan_count: 2
  slug: risklytics-plans-pricing
random_paper: 62
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- InsurTech
- Risk
- Wildfire
- Property
- Catastrophe
- Analytics
- Machine Learning
- Underwriting
website: https://www.risklytics.ai/
---
