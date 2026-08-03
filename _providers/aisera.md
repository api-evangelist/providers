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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: Push data directly into the Aisera platform from any external system that supports webhooks — Knowledge Articles and Requests. Authenticates with an x-app-token header plus an OAuth 2.0 password-grant
  name: Aisera Ingestion APIs
  slug: aisera-ingestion-apis
- description: GET /dsexecution returns ingestion-pipeline job status (SUCCEEDED / PENDING / RUNNING / FAILED / KILLED) and run metrics for a tenant's data source. Uses HTTP Basic auth.
  name: Aisera Data Source Ingestion Monitoring API
  slug: aisera-data-source-ingestion-monitoring-api
- description: SCIM-style user lifecycle endpoints — /scim/provision-user, /scim/update-user and /scim/de-provision-user — for managing Aisera platform users. Basic or Bearer auth plus x-app-token.
  name: Aisera User Provisioning APIs
  slug: aisera-user-provisioning-apis
- description: Build custom conversational interfaces for AiseraGPT applications — decoration, NLP/NLU processing, slot filling, context management, and notifications — over REST and WebSocket.
  name: Aisera Conversation & Workflows API and WebSocket
  slug: aisera-conversation-workflows-api-and-websocket
artifact_total: 9
asyncapis:
- description: ''
  name: Aisera Events Webhooks
  slug: aisera-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://aisera.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aisera.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aisera.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aisera.com/apis/apis.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aisera.com/overview-of-aisera/getting-started-guide.md
- group: company
  title: ''
  type: Blog
  url: https://aisera.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aisera.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aisera.com/product-release-notes
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aisera.com/aisera-platform/llm-operations/understanding-llm-capabilities/llm-lifecycle/bot-deprecation/bot-deprecation-guidelines.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aisera.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aisera.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.automationanywhere.com/products/security
- group: auth
  title: ''
  type: Security
  url: https://www.automationanywhere.com/legal/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aisera-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/aisera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aisera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aisera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aisera-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aisera-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aisera-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aisera-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aisera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aisera-trust-center.yml
- group: design
  title: ''
  type: Components
  url: components/aisera-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aisera-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aisera-events-webhooks.yml
created: '2026-07-17'
description: Aisera is an enterprise agentic AI platform that builds, deploys, and orchestrates AI agents and assistants for IT service management, HR, finance, procurement, and customer service. The AiseraGPT platform combines domain-specific LLMs, conversational AI, enterprise/neural search, knowledge generation, and AI workflow automation to autonomously resolve requests, deflect tickets, and serve knowledge across channels (Webchat, Slack, MS Teams, email, IVR, and more). For developers, Aisera exposes tenant-scoped REST APIs — Ingestion APIs for pushing knowledge and requests into the platform, a Data Source Ingestion Monitoring API, SCIM-style User Provisioning APIs, and a Conversation & Workflows API with WebSocket — plus Event Studio for event-driven workflows and a large library of data-source connectors. Aisera was acquired by Automation Anywhere.
image: https://aisera.com/wp-content/uploads/2025/06/homepage-social-card.png
layout: provider
modified: '2026-07-17'
name: Aisera
nav: Providers
network: true
overview: 'Aisera publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agentic AI, Conversational AI, IT Service Management, and Customer Service.


  The Aisera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aisera''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 20 more developer resources.'
random_paper: 59
score:
  band: developing
  composite: 44.9
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 51.6
    developer_ergonomics: 47.8
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 57.9
  previous_composite: 44.9
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aisera/refs/heads/main/screenshots/aisera-2026-07-25T195449.png
security:
- kind: authentication
  name: Aisera Authentication
  slug: aisera-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Aisera Domain Security
  slug: aisera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aisera Vulnerability Disclosure
  slug: aisera-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Aisera Trust Center
  slug: aisera-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO 27001, ISO 22301, HITRUST, GDPR, FIPS-140
slug: aisera
tags:
- Company
- Agentic AI
- Conversational AI
- IT Service Management
- Customer Service
- Enterprise Search
- AI Copilot
- Knowledge Management
- Workflow Automation
- Large Language Models
website: https://aisera.com
---
