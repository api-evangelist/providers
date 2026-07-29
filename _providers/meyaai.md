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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Meya Grid HTTP gateway that receives inbound integration and API/webhook events for a Meya app. Webhook URLs follow the format https://grid.meya.ai/gateway/v2/{integration}/{app_id}/{dot_path}.
  name: Meya Grid Gateway
  slug: meya-grid-gateway
artifact_total: 3
asyncapis:
- description: ''
  name: Meyaai Webhooks
  slug: meyaai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://meya.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meya.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meya.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meya.ai/reference
- group: company
  title: ''
  type: Blog
  url: https://www.meya.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meya-customers
- group: start
  title: ''
  type: SignUp
  url: https://www.meya.ai/article/sign-up
- group: operate
  title: ''
  type: StatusPage
  url: https://meya-v2.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.meya.ai/docs/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meyaai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/meyaai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/meyaai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/meyaai-cli.yml
- group: design
  title: ''
  type: Components
  url: components/meyaai-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/meyaai-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meyaai-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meyaai-domain-security.yml
created: '2026-07-17'
description: Meya is a chatbot and CX-automation platform for building, coding, and launching customer-support conversational apps, digital assistants, and workflow automation. Developers use the Grid platform and Console to script flows in BFML (a YAML syntax with Jinja2 templating) and Python 3 with async I/O, embed the Meya Orb chat UI on web and mobile, and connect messaging, support, NLU, and analytics integrations (WhatsApp, Facebook Messenger, Twilio, Zendesk, Front, Salesforce, Dialogflow, Wit.ai, Segment). The platform exposes an HTTP gateway for inbound integration/API webhooks, a first-party Meya CLI for local development with live push, and the Orb SDKs for web, Flutter, and iOS.
image: https://files.readme.io/0187488-small-meya-wordmark.png
layout: provider
modified: '2026-07-20'
name: Meya.ai
nav: Providers
network: true
overview: 'Meya.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chatbots, Conversational AI, Customer Support, and CX Automation.


  The Meya.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Meya.ai''s developer surface includes documentation, API reference, engineering blog, signup flow, changelog, CLI, and 11 more developer resources.'
random_paper: 70
score:
  band: thin
  composite: 32.5
  delta: 1.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 51.6
    developer_ergonomics: 39.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 31.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Meyaai Domain Security
  slug: meyaai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meyaai
tags:
- Company
- Chatbots
- Conversational AI
- Customer Support
- CX Automation
- Messaging
- Webhooks
- Developer Platform
website: https://meya.ai
---
