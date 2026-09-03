---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gridspace Agentic Access
  operation_count: 8
  slug: gridspace-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.goguava.ai/v1
  baseurl_source: declared
  description: Retrieve, inspect, and delete conversation data for completed calls.
  name: Gridspace Conversations API
  slug: gridspace-conversations-api
- baseURL: https://api.goguava.ai/v1
  baseurl_source: declared
  description: Send SMS messages and read inbound messages received on your Guava numbers.
  name: Gridspace Messages API
  slug: gridspace-messages-api
- baseURL: https://api.goguava.ai/v1
  baseurl_source: declared
  description: SDK lifecycle utilities.
  name: Gridspace SDK API
  slug: gridspace-sdk-api
arazzos:
- description: List recent conversations, then fetch one call's details, transcript, and recording.
  name: Pull a call's full record
  slug: gridspace-pull-call-record
- description: Send an SMS from a Guava number, then poll the inbox for the recipient's reply.
  name: Send an SMS and poll for the reply
  slug: gridspace-send-and-poll-sms
artifact_total: 17
collections:
- collection_type: postman
  name: Guava Voice Agent REST Conversations API
  slug: postman-gridspace-conversations-api
- collection_type: postman
  name: Guava Voice Agent REST Conversations Messages API
  slug: postman-gridspace-messages-api
- collection_type: postman
  name: Guava Voice Agent REST Conversations SDK API
  slug: postman-gridspace-sdk-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Guava Voice Agent REST Conversations API
  slug: open-gridspace-conversations-api
- collection_type: open
  name: Guava Voice Agent REST Conversations Messages API
  slug: open-gridspace-messages-api
- collection_type: open
  name: Guava Voice Agent REST Conversations SDK API
  slug: open-gridspace-sdk-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gridspace/overview
- group: company
  title: ''
  type: Website
  url: https://goguava.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://goguava.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://goguava.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://goguava.ai/docs/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://goguava.ai/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.goguava.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://goguava.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goguava.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goguava.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://goguava.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:hi@goguava.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goguava-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goguava.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://goguava.ai/docs/release-notes
- group: auth
  title: ''
  type: Authentication
  url: authentication/gridspace-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/gridspace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gridspace-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/gridspace-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gridspace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gridspace-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gridspace-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gridspace-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gridspace-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gridspace-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gridspace-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/gridspace-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/gridspace-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gridspace-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gridspace-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gridspace-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gridspace-guava-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gridspace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridspace-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gridspace-pull-call-record.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gridspace-send-and-poll-sms.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gridspace-plans.yml
created: '2026-07-17'
description: Gridspace is a voice AI company (founded 2013) that now operates as Guava (goguava.ai) — a voice agent platform built for regulated industries such as healthcare, banking, insurance, BPOs, and government. Guava provides an end-to-end conversational voice stack (ASR, LLM, TTS, plus compliance guardrails) exposed through Python, TypeScript, and Elixir SDKs, a "guava" CLI, a managed cloud deployment platform, and a REST API for managing conversations, transcripts, recordings, and SMS. It supports inbound and outbound calling over WebRTC and SIP, with SOC 2 Type II, HITRUST i1, and PCI DSS posture and built-in TCPA / A2P 10DLC / SHAKEN-STIR telephony compliance workflows. The legacy gridspace.com domain now redirects to goguava.ai.
image: https://goguava.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Gridspace MCP Server
  slug: gridspace-mcp-server
modified: '2026-07-19'
name: Gridspace
nav: Providers
network: true
overview: 'Gridspace publishes 3 APIs on the [APIs.io](https://apis.io/) network: Conversations API, Messages API, and SDK API. Tagged areas include Company, Voice AI, Conversational AI, Voice Agents, and Speech Recognition.


  Gridspace''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 31 more developer resources.'
plans:
- name: Gridspace Plans
  plan_count: 4
  slug: gridspace-plans
random_paper: 1
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 25
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 54.2
    developer_ergonomics: 85.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gridspace/refs/heads/main/screenshots/gridspace-2026-07-25T220327.png
security:
- kind: authentication
  name: Gridspace Authentication
  slug: gridspace-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Gridspace Domain Security
  slug: gridspace-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gridspace
tags:
- Company
- Voice AI
- Conversational AI
- Voice Agents
- Speech Recognition
- Telephony
- SMS
- Contact Center
- Regulated Industries
- Healthcare
website: https://goguava.ai
---
