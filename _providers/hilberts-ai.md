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
  band: agent-ready
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
    error_semantics: documented
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
  score: 33.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://app-api.hilberts.ai/api/v1
  baseurl_source: declared
  description: The backend API of the Hilbert growth-infrastructure application. Its OpenAPI 3.0.0 document is published unauthenticated through a Swagger UI at https://app-api.hilberts.ai/api-docs. The document dec
  name: Hilbert's Program API
  slug: hilberts-program-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hilberts-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hilberts.ai
- group: start
  title: ''
  type: Login
  url: https://app.hilberts.ai/
- group: start
  title: ''
  type: SignUp
  url: https://hilberts.ai/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hilberts.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hilberts.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://hilberts.ai
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hilberts-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hilberts-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hilberts-ai-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://hilberts.ai/growth-hub
created: '2026-07-17'
description: 'Hilbert''s AI is an AI-native growth infrastructure platform for B2C companies, backed by a16z. It unifies fragmented product, marketing, and finance data into a single source of truth and layers agentic automation on top through four intelligence stages: Detect (anomalies, churn signals, and behavioral shifts), Reason (ML/deep-learning root-cause analysis and forecasting), Act (autonomous growth interventions such as churn plays and channel adjustments), and Optimize (continuous budget and strategy tuning). A natural-language interface lets growth, product, and finance teams collapse months-long decision cycles into minutes without writing code or navigating dashboards. Hilbert connects to existing data and paid-media stacks via prebuilt integrations (Meta, Google, Pinterest, Snapchat, Reddit, Google Analytics 4, Triple Whale, Klaviyo, Braze) and states SOC 2 on its own site. The product is delivered as a hosted application. There is no public developer program, but the application
  backend does publish a reachable Swagger UI and an OpenAPI 3.0.0 document at https://app-api.hilberts.ai/api-docs, which declares the platform''s security schemes and core data models while shipping an empty paths object, so no operations are documented.'
image: https://cdn.prod.website-files.com/69241c9125ae02b952e6e87e/69d687860ff71b79e5d2cf94_OG.png
layout: provider
modified: '2026-08-13'
name: Hilbert's AI
nav: Providers
network: true
overview: 'Hilbert''s AI publishes 1 API on the [APIs.io](https://apis.io/) network: Hilbert''s Program API. Tagged areas include Company, Artificial Intelligence, Growth, Analytics, and Marketing.


  Hilbert''s AI''s developer surface includes signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Hilberts Ai Plans Pricing
  plan_count: 0
  slug: hilberts-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Hilberts Ai Rate Limits
  slug: hilberts-ai-rate-limits
scopes:
- name: Hilberts Ai Scopes
  scope_count: 14
  slug: hilberts-ai-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 32.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 32.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hilberts-ai/refs/heads/main/screenshots/hilberts-ai-2026-07-25T221242.png
security:
- kind: authentication
  name: Hilberts Ai Authentication
  slug: hilberts-ai-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Hilberts Ai Domain Security
  slug: hilberts-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hilberts-ai
tags:
- Company
- Artificial Intelligence
- Growth
- Analytics
- Marketing
- Data Science
- Automation
- Agentic AI
- B2C
website: https://hilberts.ai
---
