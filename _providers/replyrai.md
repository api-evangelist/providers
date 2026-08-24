---
access_model:
  confidence: medium
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://replyr.ai/
  - https://app.replyr.ai/en/login
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'REST API for the Replyr operator console at app.replyr.ai. Covers business account details, admins and teams, tags, custom fields and bot fields, contacts (create, look up, tag, set fields), outbound '
  name: Replyr Platform API
  slug: replyr-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://replyr.ai
- group: docs
  title: ''
  type: APIReference
  url: https://app.replyr.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.replyr.ai/api
- group: start
  title: ''
  type: Login
  url: https://app.replyr.ai/en/login
- group: operate
  title: ''
  type: Support
  url: https://wa.me/60109696912
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replyrai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replyrai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replyrai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/replyrai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/replyrai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replyrai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replyrai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/replyrai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replyrai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/replyrai-platform-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/replyrai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/replyrai-rate-limits.yml
created: '2026-07-17'
description: Replyr.ai (Replyr Sdn Bhd, Kuala Lumpur, Malaysia) is an AI-powered customer engagement and patient-acquisition platform aimed at Malaysian clinics. It builds GPT-style chat assistants that reply instantly in multiple languages across WhatsApp, Instagram, Facebook Messenger and other chat channels to qualify leads, answer FAQs, recommend products and book appointments 24/7, and packages that with Meta and Google advertising campaigns and a BookAClinic discovery marketplace. The operator console at app.replyr.ai runs a white-labeled deployment of the ChatRace conversational-commerce platform and exposes a REST API of its own at https://app.replyr.ai/api, documented with a live Swagger UI and a Swagger 2.0 specification covering accounts, contacts, tags and custom fields, message sending across channels, sales pipelines and opportunities, AI agents, appointment calendars, templates and an ecommerce cart/order surface. Authentication is a single X-ACCESS-TOKEN API key header. Surfaced
  as a 500 Global portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replyrai.png
layout: provider
modified: '2026-08-13'
name: Replyr.ai
nav: Providers
network: true
overview: 'Replyr.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Replyr Platform API. Tagged areas include Company, Artificial Intelligence, Chatbots, Conversational AI, and Customer Engagement.


  Replyr.ai''s developer surface includes API reference, documentation, support, authentication, and 14 more developer resources.'
plans:
- name: Replyrai Plans Pricing
  plan_count: 0
  slug: replyrai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Replyrai Rate Limits
  slug: replyrai-rate-limits
score:
  band: thin
  composite: 28.0
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 38.9
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 21.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Replyrai Authentication
  slug: replyrai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Replyrai Domain Security
  slug: replyrai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: replyrai
tags:
- Company
- Artificial Intelligence
- Chatbots
- Conversational AI
- Customer Engagement
- Lead Generation
- WhatsApp
- Marketing
- Messaging
- CRM
- Appointment Scheduling
- Healthcare
- Malaysia
website: https://replyr.ai
---
