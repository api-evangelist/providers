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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Predicthq Agentic Access
  operation_count: 5
  slug: predicthq-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 4
apis:
- description: The Events API from PredictHQ — 2 operation(s) for events.
  name: PredictHQ Events API
  slug: predicthq-events-api
- description: The Features API from PredictHQ — 1 operation(s) for features.
  name: PredictHQ Features API
  slug: predicthq-features-api
- description: The Places API from PredictHQ — 1 operation(s) for places.
  name: PredictHQ Places API
  slug: predicthq-places-api
- description: The Suggested Radius API from PredictHQ — 1 operation(s) for suggested radius.
  name: PredictHQ Suggested Radius API
  slug: predicthq-suggested-radius-api
artifact_total: 11
collections:
- collection_type: open
  name: PredictHQ API
  slug: open-predicthq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/predicthq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/predicthq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/predicthq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/predicthq
- group: start
  title: ''
  type: Portal
  url: https://www.predicthq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.predicthq.com/
- group: start
  title: ''
  type: Signup
  url: https://control.predicthq.com/signup
- group: start
  title: ''
  type: Login
  url: https://control.predicthq.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.predicthq.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.predicthq.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.predicthq.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.predicthq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.predicthq.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.predicthq.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.predicthq.com/legal/data-security-and-availability
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/predicthq
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.predicthq.com/llms.txt
created: '2025-02-24'
description: PredictHQ is an AI-powered demand intelligence platform that predicts the impact of real-world events on business demand. The PredictHQ API delivers structured, deduplicated event data, machine learning features, demand forecasts, and impact analytics across categories such as concerts, sports, conferences, public holidays, school terms, severe weather, and more, helping enterprises make smarter decisions about staffing, inventory, pricing, and marketing.
finops:
- name: Predicthq Finops
  service_category: API
  slug: predicthq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/predicthq.png
layout: provider
modified: '2026-05-19'
name: PredictHQ
nav: Providers
network: true
overview: 'PredictHQ publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Features API, Places API, and 1 more. Tagged areas include Demand Intelligence, Events, Forecasting, Machine Learning, and Real-World Events.


  PredictHQ''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Predicthq Plans Pricing
  plan_count: 3
  slug: predicthq-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Predicthq Rate Limits
  slug: predicthq-rate-limits
score:
  band: developing
  composite: 45.6
  delta: -7.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 56.7
    developer_ergonomics: 34.8
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/predicthq/refs/heads/main/screenshots/predicthq-2026-06-20T192049.png
security:
- kind: authentication
  name: Predicthq Authentication
  slug: predicthq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Predicthq Domain Security
  slug: predicthq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: predicthq
tags:
- Demand Intelligence
- Events
- Forecasting
- Machine Learning
- Real-World Events
website: https://www.predicthq.com/
---
