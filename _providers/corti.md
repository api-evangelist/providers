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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-03'
api_count: 8
apis:
- description: Real-time, bidirectional stateless dictation over WebSocket, returning live transcripts and detected commands.
  name: Corti Speech to Text API
  slug: corti-speech-to-text-api
- description: Real-time ambient documentation over WebSocket, returning live transcripts and extracted clinical facts.
  name: Corti Ambient Documentation API
  slug: corti-ambient-documentation-api
- description: Generate clinical documents and structured/guided documents from interactions and templates.
  name: Corti Text Generation API
  slug: corti-text-generation-api
- description: Stateless prediction of ICD-10-CM/PCS, ICD-10 (international/UK/FR/GM), OPCS-4, OPS, CCAM and CPT codes from clinical text.
  name: Corti Medical Coding API
  slug: corti-medical-coding-api
- description: Build and orchestrate healthcare agents over the A2A protocol with prebuilt medical experts and MCP tool integration.
  name: Corti Agentic Framework API
  slug: corti-agentic-framework-api
- description: OpenAI-compatible (Chat Completions, Responses, Completions, Embeddings) and Anthropic-compatible (Messages) frontier models hosted on EU infrastructure.
  name: Corti Models API
  slug: corti-models-api
- description: Programmatically manage customers, users, quotas and usage for a Corti Console project.
  name: Corti Administration API
  slug: corti-administration-api
- description: Embeddable ambient clinical scribe via Web Component, PostMessage (iframe/WebView) and Window APIs.
  name: Corti Assistant Embedded
  slug: corti-assistant-embedded
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corti-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corti.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.corti.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corti.ai/get_started/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.corti.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.corti.ai/get_started/welcome
- group: operate
  title: ''
  type: Support
  url: https://help.corti.ai/en/
- group: company
  title: ''
  type: Blog
  url: https://corti.ai/stories
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corticph
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.corti.ai/about/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://corti.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.corti.app/signup
- group: start
  title: ''
  type: Login
  url: https://console.corti.app/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corti.ai/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corti.ai/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.corti.ai
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.corti.ai/release-notes/change-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://corti.ai/safety
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corti-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corti-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corti-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/corti-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/corti-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/corti-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corti-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/corti-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corti-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/corti-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corti-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/corti-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/corti-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/corti-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/corti-error-codes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/corti-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/corti-transcribe-asyncapi.json
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/corti-stream-asyncapi.json
- group: design
  title: ''
  type: Webhooks
  url: https://docs.corti.ai/assistant/events
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corti-realtime-transcription.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corti-ambient-documentation.md
created: '2026-07-17'
description: 'Corti is a healthcare AI platform for developers, offering a full stack of clinical AI building blocks over a single OAuth 2.0-secured API: real-time speech-to-text (dictation and ambient documentation over WebSocket), clinical text generation and structured/guided documents, AI-assisted medical coding (ICD-10, CPT, OPCS-4, CCAM, OPS and more), fact extraction, an Agentic Framework (A2A protocol with prebuilt medical experts and MCP integration), OpenAI/Anthropic-compatible EU-hosted Corti Models, and an embeddable Corti Assistant clinical scribe. The platform is EU/US data-resident and carries extensive healthcare compliance (SOC 2, ISO 27001/13485/42001, HIPAA, GDPR, EU AI Act, FedRAMP, NHS DTAC/DCB0129). Backed by Atomico and Prosus Ventures.'
image: https://mintlify.s3.us-west-1.amazonaws.com/corti/logo/embedded-assistant.svg
layout: provider
mcp_servers:
- description: ''
  name: corti-mcp.yml
  slug: corti-mcpyml
modified: '2026-07-18'
name: Corti
nav: Providers
network: true
overview: 'Corti publishes 2 APIs on the [APIs.io](https://apis.io/) network: Speech to Text API and Ambient Documentation API. Tagged areas include Company, Health, Healthcare, Artificial Intelligence, and Speech to Text.


  Corti''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 70
scopes:
- name: Corti Scopes
  scope_count: 44
  slug: corti-scopes
  summary_line: 44 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 56.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.4
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 57.9
  previous_composite: 56.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corti/refs/heads/main/screenshots/corti-2026-07-25T210446.png
security:
- kind: authentication
  name: Corti Authentication
  slug: corti-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Corti Domain Security
  slug: corti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Corti Trust Center
  slug: corti-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, ISO 13485, ISO 42001, ISO 14971, ISO 62366, HIPAA, GDPR, EU AI Act, DORA, NIS2, NHS DSPT, NHS DTAC, NHS DCB0129, FedRAMP, Cyber Essentials Plus, ISAE 3000, BSI C5, CE Mark
slug: corti
tags:
- Company
- Health
- Healthcare
- Artificial Intelligence
- Speech to Text
- Medical Coding
- Clinical Documentation
- Agents
- Machine Learning
website: https://www.corti.ai
---
