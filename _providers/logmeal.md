---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Logmeal Agentic Access
  operation_count: 4
  slug: logmeal-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: Retrieve a user's logged food intakes over time.
  name: LogMeal History API
  slug: logmeal-history-api
- description: Detect food items in user-submitted images.
  name: LogMeal Image Recognition API
  slug: logmeal-image-recognition-api
- description: Retrieve ingredients and nutritional information for confirmed intakes.
  name: LogMeal Nutrition API
  slug: logmeal-nutrition-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LogMeal Food Recognition API
  slug: open-logmeal-food-recognition-api
- collection_type: open
  name: LogMeal Food Recognition History API
  slug: open-logmeal-history-api
- collection_type: open
  name: LogMeal Food Recognition History Image Recognition API
  slug: open-logmeal-image-recognition-api
- collection_type: open
  name: LogMeal Food Recognition History Nutrition API
  slug: open-logmeal-nutrition-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/logmeal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logmeal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/logmeal-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logmeal
- group: company
  title: ''
  type: Website
  url: https://logmeal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logmeal.com
- group: start
  title: ''
  type: Portal
  url: https://logmeal.com/api/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.logmeal.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.logmeal.com/feed/
created: '2025-03-01'
description: LogMeal provides a Food Recognition Image API that detects foods, drinks, vegetables, fruits and prepared dishes from images. The platform offers semantic tagging including food group, dish and ingredients recognition, as well as nutritional information analysis with 35+ nutritional indicators and user intake history tracking.
finops:
- name: Logmeal Finops
  service_category: API
  slug: logmeal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logmeal.png
layout: provider
modified: '2026-05-19'
name: LogMeal
nav: Providers
network: true
overview: 'LogMeal publishes 3 APIs on the [APIs.io](https://apis.io/) network: History API, Image Recognition API, and Nutrition API. Tagged areas include Computer-Vision, Food, Image Recognition, Nutrition, and Semantic Tagging.


  LogMeal''s developer surface includes authentication, documentation, developer portal, engineering blog, and 5 more developer resources.'
plans:
- name: Logmeal Plans Pricing
  plan_count: 3
  slug: logmeal-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Logmeal Rate Limits
  slug: logmeal-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logmeal/refs/heads/main/screenshots/logmeal-2026-06-20T184658.png
security:
- kind: authentication
  name: Logmeal Authentication
  slug: logmeal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Logmeal Domain Security
  slug: logmeal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: logmeal
tags:
- Computer-Vision
- Food
- Image Recognition
- Nutrition
- Semantic Tagging
website: https://logmeal.com
---
