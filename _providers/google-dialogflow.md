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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Google Dialogflow Agentic Access
  operation_count: 14
  slug: google-dialogflow-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- description: The Projects API from Google Dialogflow — 9 operation(s) for projects.
  name: Google Dialogflow Projects API
  slug: google-dialogflow-projects-api
artifact_total: 10
collections:
- collection_type: open
  name: Dialogflow ES API
  slug: open-google-dialogflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-dialogflow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-dialogflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-dialogflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-dialogflow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-dialogflow-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dialogflow
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/dialogflow
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/dialogflow/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/dialogflow/docs/authentication
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/ai-machine-learning
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/dialogflow/docs/support
created: '2024-01-01'
description: Google Dialogflow is a natural language understanding platform that makes it easy to design and integrate conversational user interfaces into mobile apps, web applications, devices, bots, and interactive voice response systems.
finops:
- name: Google Dialogflow Finops
  service_category: API
  slug: google-dialogflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-dialogflow.png
layout: provider
modified: '2026-04-28'
name: Google Dialogflow
nav: Providers
network: true
overview: 'Google Dialogflow publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Artificial Intelligence, Chatbots, Conversational AI, Machine Learning, and Natural Language Processing.


  Google Dialogflow''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 9 more developer resources.'
plans:
- name: Google Dialogflow Plans Pricing
  plan_count: 3
  slug: google-dialogflow-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Google Dialogflow Rate Limits
  slug: google-dialogflow-rate-limits
scopes:
- name: Google Dialogflow Scopes
  scope_count: 2
  slug: google-dialogflow-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 46.0
  delta: -1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.0
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-dialogflow/refs/heads/main/screenshots/google-dialogflow-2026-06-20T182157.png
security:
- kind: authentication
  name: Google Dialogflow Authentication
  slug: google-dialogflow-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Dialogflow Domain Security
  slug: google-dialogflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Dialogflow Vulnerability Disclosure
  slug: google-dialogflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-dialogflow
tags:
- Artificial Intelligence
- Chatbots
- Conversational AI
- Machine Learning
- Natural Language Processing
- Voice Assistants
website: https://cloud.google.com/dialogflow
---
