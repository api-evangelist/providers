---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: AdmitHub/Mainstay REST API v1.0 for syncing student and employee records and engagement data between Mainstay and external systems, with Bearer API-token authentication.
  name: Mainstay API
  slug: mainstay-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.mainstay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.mainstay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.mainstay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.mainstay.com/
- group: operate
  title: ''
  type: Support
  url: https://support.mainstay.com/
- group: company
  title: ''
  type: Blog
  url: https://mainstay.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdmitHub
- group: start
  title: ''
  type: Login
  url: https://app.mainstay.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mainstay.com/termsofuse/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mainstay.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://mainstay.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mainstay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mainstay-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mainstay-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mainstay-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mainstay-llms.txt
created: '2026-07-17'
description: Mainstay (formerly AdmitHub) is a student engagement platform for higher education that delivers human-centered, AI-enhanced conversational coaching to students via SMS text messaging, live chat, web chat, and social messaging. Grounded in behavioral science research, its two-way messaging assistant nudges students through enrollment, registration, financial aid, and academic milestones while giving institutional staff insights and tools to improve engagement, persistence, and outcomes. Mainstay is a Techstars portfolio company. It publishes an API-token authenticated REST API (v1.0, base URL https://api.admithub.com) documented at docs.api.mainstay.com, used to sync student and employee records and engagement data between Mainstay and external systems; tokens are generated from the Mainstay dashboard and presented as Bearer credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mainstay.png
layout: provider
modified: '2026-07-20'
name: Mainstay
nav: Providers
network: true
overview: 'Mainstay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Higher Education, and Conversational AI.


  Mainstay''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 28.7
  delta: 0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mainstay/refs/heads/main/screenshots/mainstay-2026-07-25T225921.png
security:
- kind: authentication
  name: Mainstay Authentication
  slug: mainstay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mainstay Domain Security
  slug: mainstay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mainstay Trust Center
  slug: mainstay-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: mainstay
tags:
- Company
- Education
- EdTech
- Higher Education
- Conversational AI
- Student Engagement
- Chatbot
- Messaging
website: https://www.mainstay.com/
---
