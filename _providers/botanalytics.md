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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Messages API from Botanalytics — 1 operation(s) for messages.
  name: Botanalytics Messages API
  slug: botanalytics-messages-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Botanalytics Message Ingestion Messages API
  slug: open-botanalytics-messages-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/botanalytics-messages-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://botanalytics.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.beta.botanalytics.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beta.botanalytics.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beta.botanalytics.co/docs/integration/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beta.botanalytics.co/docs/integration/sdks/node/getting-started
- group: build
  title: ''
  type: Postman
  url: https://docs.beta.botanalytics.co/docs/postman/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/botanalytics
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/botanalytics-family/shared_invite/zt-1zfrciqxj-XT5pL0Pl3fDdUPxvQ~APyw
- group: start
  title: ''
  type: SignUp
  url: https://tally.so/r/wgq9vM
- group: start
  title: ''
  type: Login
  url: https://login.beta.botanalytics.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.botanalytics.co/docs/terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.botanalytics.co/docs/privacy.pdf
- group: build
  title: ''
  type: Packages
  url: packages/botanalytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/botanalytics-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/botanalytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/botanalytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/botanalytics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/botanalytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/botanalytics-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/botanalytics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/botanalytics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/botanalytics-domain-security.yml
created: '2026-07-17'
description: Botanalytics is a conversational analytics platform for AI chatbots and voice assistants. It helps bot builders and product teams measure engagement, understand user intents and natural-language understanding (NLU) quality, segment conversations, identify bottlenecks and drop-off points, and surface audience insights across 20+ languages and multiple messaging and voice channels (Facebook Messenger, Amazon Alexa, Microsoft Bot Framework, Samsung Bixby, and a universal channel). Conversation data is sent either through native no-code integrations, first-party SDKs (Node, Python, Java, Ruby), or a v2 REST ingestion API secured with Bearer JWT API keys. Botanalytics is backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/botanalytics.png
layout: provider
mcp_servers:
- description: ''
  name: botanalytics-mcp.yml
  slug: botanalytics-mcpyml
modified: '2026-07-18'
name: Botanalytics
nav: Providers
network: true
overview: 'Botanalytics publishes 1 API on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include Company, Conversational Analytics, Chatbots, Voice Assistants, and Bot Analytics.


  Botanalytics'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 101
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.2
    developer_ergonomics: 64.7
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/botanalytics/refs/heads/main/screenshots/botanalytics-2026-07-25T203639.png
security:
- kind: authentication
  name: Botanalytics Authentication
  slug: botanalytics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Botanalytics Domain Security
  slug: botanalytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: botanalytics
tags:
- Company
- Conversational Analytics
- Chatbots
- Voice Assistants
- Bot Analytics
- Analytics
- Natural Language Understanding
- Developer Tools
website: https://botanalytics.co
---
