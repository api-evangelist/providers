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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api-2445582032290.production.gw.apicast.io
  baseurl_source: declared
  description: The Food Recognition API from Azumio — 2 operation(s) for food recognition.
  name: Azumio Food Recognition API
  slug: azumio-food-recognition-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Calorie Mama Food Recognition API
  slug: open-azumio-food-recognition-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/azumio-food-recognition-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://azumio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.caloriemama.ai
- group: docs
  title: ''
  type: Documentation
  url: https://dev.caloriemama.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.caloriemama.ai/docs
- group: start
  title: ''
  type: SignUp
  url: https://dev.caloriemama.ai/signup
- group: start
  title: ''
  type: Login
  url: https://dev.caloriemama.ai/login
- group: company
  title: ''
  type: Blog
  url: https://azumio.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@azumio.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azumio.com/privacy-policy-and-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azumio.com/privacy-policy-and-terms-of-use
- group: auth
  title: ''
  type: Authentication
  url: authentication/azumio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/azumio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/azumio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/azumio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/azumio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/azumio-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/azumio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/azumio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/azumio-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azumio-domain-security.yml
created: '2026-07-17'
description: 'Azumio is an AI-driven digital health company whose consumer apps (Argus, Instant Heart Rate, Fitness Buddy, Glucose Buddy, Sleep Time, Calorie Mama) have been downloaded more than 100 million times. Beyond its apps, Azumio offers developer APIs and SDKs built on its deep-learning and digital-biomarker technology: the Calorie Mama Food Recognition API (identify food from a photo and return calories, macronutrients, and full nutrition), the Azumio 360 tracking API/SDK for diet, fitness and sleep, and diabetes-focused APIs including an AI Instant Diabetes Test biomarker and blood-glucose management. The flagship, publicly documented developer product is the Calorie Mama Food Recognition API, a 3scale-gateway REST API using API-key authentication.'
image: https://azumio.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Azumio
nav: Providers
network: true
overview: 'Azumio publishes 1 API on the [APIs.io](https://apis.io/) network: Food Recognition API. Tagged areas include Company, Health, Digital Health, Nutrition, and Food Recognition.


  Azumio''s developer surface includes documentation, API reference, signup flow, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 40.2
  provenance:
    conformance: derived
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
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azumio/refs/heads/main/screenshots/azumio-2026-07-25T202122.png
security:
- kind: authentication
  name: Azumio Authentication
  slug: azumio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Azumio Domain Security
  slug: azumio-domain-security
  summary_line: TLSv1.3
slug: azumio
tags:
- Company
- Health
- Digital Health
- Nutrition
- Food Recognition
- Machine-Learning
- Artificial Intelligence
- Fitness
- Diabetes
website: https://azumio.com
---
