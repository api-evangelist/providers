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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: Asynchronous speech-to-text transcription API that turns audio and video into text with high accuracy. Supports batch, real-time, and human-in-the-loop transcription, multipart and remote-URL submissi
  name: Kensho Scribe
  slug: kensho-scribe
- description: 'Document intelligence API that transforms PDF documents into structured JSON, with hierarchical extraction, optical character recognition (OCR), enhanced table extraction, and bounding-box locations. '
  name: Kensho Extract
  slug: kensho-extract
- description: Named Entity Recognition and Disambiguation API that identifies and links concepts in text to knowledge bases (Wikimedia for general entities, S&P Capital IQ for financial organizations and people), r
  name: Kensho NERD
  slug: kensho-nerd
- description: LLM-ready API that connects LLMs, agents, and AI applications to S&P Global's trusted data through flexible retrieval, Adaptive Retrieval data agents, a Python library (kensho-kfinance), and a hosted,
  name: Kensho LLM-ready API (kfinance)
  slug: kensho-llm-ready-api-kfinance
artifact_total: 11
asyncapis:
- description: ''
  name: Kensho Scribe Webhooks
  slug: kensho-scribe-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://kensho.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kensho.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kensho.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kensho.com/llmreadyapi/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kensho.com/authentication/personal-token
- group: auth
  title: ''
  type: Authentication
  url: authentication/kensho-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kensho-scopes.yml
- group: start
  title: ''
  type: SignUp
  url: https://services.kensho.com/free-trial
- group: operate
  title: ''
  type: Support
  url: https://docs.kensho.com/llmreadyapi/support
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kensho.com/llmreadyapi/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kensho-technologies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kensho.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kensho.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kensho.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kensho-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kensho-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kensho-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/kensho-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kensho-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kensho-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kensho-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kensho-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kensho-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kensho-scribe-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kensho-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kensho-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kensho-domain-security.yml
created: '2026-07-17'
description: 'Kensho Technologies is the AI innovation hub of S&P Global, building machine learning and AI systems that structure, connect, and extract meaning from the world''s financial and business data. Kensho''s developer platform exposes a suite of production APIs: Scribe for speech-to-text transcription of audio and video, Extract for turning PDF documents into structured JSON, NERD for named-entity recognition and disambiguation against Wikimedia and S&P Capital IQ knowledge bases, and the LLM-ready API (kfinance) that connects LLMs, agents, and AI applications to S&P Global''s trusted data through Adaptive Retrieval and a hosted, OAuth-secured Model Context Protocol (MCP) server. Authentication is bearer-token based, issued from Kensho''s services platform via personal tokens or production key pairs, with OAuth 2.0 (authorization code, client credentials, and refresh token flows, PKCE, and dynamic client registration) for the MCP surface.'
image: https://services.kensho.com/icons/favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: Kensho MCP Server
  slug: kensho-mcp-server
- description: Official hosted Model Context Protocol (MCP) server for the Kensho / S&P Global LLM-ready API (kfinance). Exposes S&P Global's trusted financial data to LLMs and agents. Verified via RFC 9728 protecte
  name: Kensho MCP Server
  slug: kensho-mcp-server-2
modified: '2026-07-19'
name: Kensho
nav: Providers
network: true
overview: 'Kensho publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Financial Data, and Speech-to-Text.


  The Kensho catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kensho''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, changelog, and 21 more developer resources.'
random_paper: 18
scopes:
- name: Kensho Scopes
  scope_count: 2
  slug: kensho-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 43.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kensho/refs/heads/main/screenshots/kensho-2026-07-25T223619.png
security:
- kind: authentication
  name: Kensho Authentication
  slug: kensho-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Kensho Domain Security
  slug: kensho-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Kensho Trust Center
  slug: kensho-trust-center
  summary_line: SOC 2
slug: kensho
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Financial Data
- Speech-to-Text
- Transcription
- Document Extraction
- Named Entity Recognition
- Natural Language Processing
- LLM
- MCP
- Retrieval
- S&P Global
website: https://kensho.com/
---
