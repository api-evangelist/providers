---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 41
  human_in_the_loop: 41
  name: Netomi Agentic Access
  operation_count: 67
  slug: netomi-agentic-access
  summary_line: 67 operations · 41 acting · 41 human-in-the-loop
api_count: 2
apis:
- description: The Netomi backend service that fronts the Agentic OS for CX. It backs the first-party mobile Chat SDKs (session establishment, message exchange, rich media, file attachments, forms, live agent handof
  name: Netomi Platform API
  slug: netomi-platform-api
- description: Public machine-readable status feed for the Netomi platform, served by Atlassian Statuspage at status.netomi.com. Exposes the standard Statuspage v2 JSON surface (summary, status, components, incident
  name: Netomi Status API
  slug: netomi-status-api
artifact_total: 7
asyncapis:
- description: ''
  name: Netomi Events
  slug: netomi-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netomi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/netomi-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.netomi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/msgai/netomi-chat-ios
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/msgai/netomi-chat-ios#-quick-start
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.netomi.com/
- group: operate
  title: ''
  type: Support
  url: https://support.netomi.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/msgai
- group: start
  title: ''
  type: Login
  url: https://studio.netomi.com
- group: start
  title: ''
  type: SignUp
  url: https://www.netomi.com/request-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netomi.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netomi.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.netomi.com/governance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.netomi.com
- group: build
  title: ''
  type: SDKs
  url: packages/netomi-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/netomi-packages.yml
- group: design
  title: ''
  type: Components
  url: components/netomi-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netomi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/netomi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/netomi-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/netomi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/msgai/netomi-chat-ios/blob/main/docs/installation.md#cocoapods-sunset-timeline
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/netomi-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/netomi-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/netomi-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/netomi-events.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netomi-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/netomi-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/netomi-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/netomi-agentdesk-openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://api.netomi.com/swagger-ui.html
- group: other
  title: ''
  type: Overlay
  url: overlays/netomi-agentdesk-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/netomi-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Netomi (founded 2016 as msg.ai) is an enterprise agentic AI platform for customer experience. Its "Agentic OS for CX" orchestrates a network of AI agents across chat, email, telephony, social, search, MCP and API channels, layering a governance tier (topic and policy guardrails, prompt security, response validation) over a task-planning orchestration agent and specialised knowledge-retrieval, action, personalisation and sentiment agents, with RAG/Graph-RAG retrieval, reinforcement-learning feedback and AI observability. Netomi ships first-party mobile Chat SDKs for iOS (Swift Package Manager, plus the deprecated NetomiChatSDK CocoaPod), Android (com.netomi.chat:chat-widget-android on Maven Central) and React Native (@netomi.com/netomi-chat-react-native on npm), all backed by the api.netomi.com service with optional JWT-authenticated sessions, guest sessions, custom API headers and a bidirectional SDK event bus. The platform runs in US, EU and Singapore production regions and
  publishes SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, GDPR, CCPA and PDPA compliance posture. The Agentic Studio console and the developer documentation portal are gated behind an enterprise account, but a live, unlinked OpenAPI 3.1.0 contract for the AgentDesk REST API — 56 paths, 67 operations, 103 schemas, covering the conversation engine, NLU prediction, query analysis, conversation history, per-bot rate-limit configuration, visitor authorization and sixteen inbound channel webhooks (Zendesk, Zoho, Salesforce, Freshdesk, Gladly, Helpshift, Sprinklr, Sunshine Conversations, Facebook, Twitter, Google Assistant, Firebase) — is served publicly at https://api.netomi.com/v3/api-docs with Swagger UI at https://api.netomi.com/swagger-ui.html.
image: https://www.netomi.com/apple-touch-icon.png
layout: provider
modified: '2026-08-01'
name: Netomi
nav: Providers
network: true
overview: 'Netomi publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Company, Artificial Intelligence, Agentic AI, Customer Experience, and Customer Service.


  The Netomi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Netomi''s developer surface includes documentation, getting-started guide, support, signup flow, authentication, changelog, sandbox, and 27 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 51.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.6
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netomi/refs/heads/main/screenshots/netomi-2026-08-07T185015.png
security:
- kind: authentication
  name: Netomi Authentication
  slug: netomi-authentication
  summary_line: bearer-jwt/tenant-identifier · 4 schemes
- kind: domain-security
  name: Netomi Domain Security
  slug: netomi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Netomi Trust Center
  slug: netomi-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, GDPR, CCPA, PDPA
slug: netomi
tags:
- Company
- Artificial Intelligence
- Agentic AI
- Customer Experience
- Customer Service
- Customer Support
- Conversational AI
- Chatbots
- Chat
- Voice
- Telephony
- SDKs
- Mobile
website: https://www.netomi.com/
---
