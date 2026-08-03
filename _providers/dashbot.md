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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Export API from Dashbot — 1 operation(s) for export.
  name: Dashbot Export API
  slug: dashbot-export-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.dimensionlabs.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dimensionlabs.io/docs/dimension-product-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dimensionlabs.io/docs/dimension-product-guide
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dimensionlabs.io/reference/using-the-integration-guides
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dimensionlabs.io/reference/generating-dashbot-api-key
- group: auth
  title: ''
  type: Authentication
  url: authentication/dashbot-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dashbot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/dashbot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dashbot-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dashbot-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dashbot-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actionably
- group: company
  title: ''
  type: Blog
  url: https://www.dimensionlabs.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dimensionlabs.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dimensionlabs.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://next.dimensionlabs.io/
created: '2026-07-17'
description: Dashbot is a conversational-data analytics platform (now operating as Dimension Labs) that ingests chatbot, voice-assistant, live-chat, call, survey and other unstructured customer conversations and enriches them into structured "dimensions" for causal intelligence and reporting. Data is sent in through a Universal REST tracker and dozens of one-click integrations (Twilio, Slack, Intercom, Zendesk, Salesforce, Amazon Lex/Connect, Google Dialogflow, Genesys, Cognigy, Kore.ai, Rasa, and more), then explored through dashboards, data explorer, flows and an analytics Agent. A REST Export API (api.dimensionlabs.io) and first-party JavaScript, Python and Ruby SDKs let teams pull enriched data back out programmatically. Dashbot was surfaced as a portfolio company of bessemer-venture-partners; the company rebranded to Dimension Labs while the API and SDKs retain the Dashbot name (api.dashbot.io still responds).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dashbot.png
layout: provider
modified: '2026-07-18'
name: Dashbot
nav: Providers
network: true
overview: 'Dashbot publishes 1 API on the [APIs.io](https://apis.io/) network: Export API. Tagged areas include Company, Ai Ml, Conversational Analytics, Chatbots, and Voice Assistants.


  Dashbot''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, and 11 more developer resources.'
random_paper: 76
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 45.7
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 37.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dashbot/refs/heads/main/screenshots/dashbot-2026-07-25T211226.png
security:
- kind: authentication
  name: Dashbot Authentication
  slug: dashbot-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dashbot Domain Security
  slug: dashbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dashbot
tags:
- Company
- Ai Ml
- Conversational Analytics
- Chatbots
- Voice Assistants
- Customer Experience
- Data Enrichment
- Analytics
- Contact Center
website: https://www.dimensionlabs.io/
---
