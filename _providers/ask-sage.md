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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 26.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 188
  human_in_the_loop: 6
  name: Ask Sage Agentic Access
  operation_count: 219
  slug: ask-sage-agentic-access
  summary_line: 219 operations · 188 acting · 6 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Admin operations for organization management
  name: Ask Sage Admin API
  slug: ask-sage-admin-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Agent builder workflow and agent management
  name: Ask Sage Agent Builder API
  slug: ask-sage-agent-builder-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Token allocation and distribution policies
  name: Ask Sage Allocation API
  slug: ask-sage-allocation-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: API key operations
  name: Ask Sage API Key Management API
  slug: ask-sage-api-key-management-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Audio processing (TTS/STT)
  name: Ask Sage Audio API
  slug: ask-sage-audio-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: User authentication and authorization
  name: Ask Sage Authentication API
  slug: ask-sage-authentication-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Chat session operations
  name: Ask Sage Chat Management API
  slug: ask-sage-chat-management-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Text generation and completions
  name: Ask Sage Completions API
  slug: ask-sage-completions-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: System configuration endpoints
  name: Ask Sage Configuration API
  slug: ask-sage-configuration-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Dataset operations and permissions
  name: Ask Sage Dataset Management API
  slug: ask-sage-dataset-management-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Knowledge dataset management
  name: Ask Sage Datasets API
  slug: ask-sage-datasets-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Deep agent operations
  name: Ask Sage Deep Agent API
  slug: ask-sage-deep-agent-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: The Execute Agent API from Ask Sage — 1 operation(s) for execute agent.
  name: Ask Sage Execute Agent API
  slug: ask-sage-execute-agent-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: User feedback operations
  name: Ask Sage Feedback API
  slug: ask-sage-feedback-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: File processing and analysis
  name: Ask Sage Files API
  slug: ask-sage-files-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: The List Agents API from Ask Sage — 1 operation(s) for list agents.
  name: Ask Sage List Agents API
  slug: ask-sage-list-agents-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Model Context Protocol server management
  name: Ask Sage MCP Servers API
  slug: ask-sage-mcp-servers-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Memo management within workbooks
  name: Ask Sage Memos API
  slug: ask-sage-memos-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: AI model management
  name: Ask Sage Models API
  slug: ask-sage-models-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Plugin execution and management
  name: Ask Sage Plugins API
  slug: ask-sage-plugins-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Source management within workbooks
  name: Ask Sage Sources API
  slug: ask-sage-sources-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Superadmin system operations
  name: Ask Sage Superadmin API
  slug: ask-sage-superadmin-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: System utilities and health checks
  name: Ask Sage System API
  slug: ask-sage-system-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Tabular data ingestion and querying
  name: Ask Sage Tabular Data API
  slug: ask-sage-tabular-data-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Token request and approval workflow
  name: Ask Sage Token Requests API
  slug: ask-sage-token-requests-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Model training and content ingestion
  name: Ask Sage Training API
  slug: ask-sage-training-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Token usage tracking
  name: Ask Sage Usage API
  slug: ask-sage-usage-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: User data and logs
  name: Ask Sage User Information API
  slug: ask-sage-user-information-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: User profile and settings management
  name: Ask Sage User Management API
  slug: ask-sage-user-management-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Utility endpoints
  name: Ask Sage Utilities API
  slug: ask-sage-utilities-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Widget/bot management
  name: Ask Sage Widgets API
  slug: ask-sage-widgets-api
- baseURL: https://api.asksage.ai/server
  baseurl_source: declared
  description: Workbook management
  name: Ask Sage Workbooks API
  slug: ask-sage-workbooks-api
artifact_total: 70
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ask Sage Server Admin API
  slug: open-ask-sage-admin-api
- collection_type: open
  name: Ask Sage Server Admin Agent Builder API
  slug: open-ask-sage-agent-builder-api
- collection_type: open
  name: Ask Sage Server Admin Allocation API
  slug: open-ask-sage-allocation-api
- collection_type: open
  name: Ask Sage Server Admin API Key Management API
  slug: open-ask-sage-api-key-management-api
- collection_type: open
  name: Ask Sage Server Admin Audio API
  slug: open-ask-sage-audio-api
- collection_type: open
  name: Ask Sage Server Admin Authentication API
  slug: open-ask-sage-authentication-api
- collection_type: open
  name: Ask Sage Server Admin Chat Management API
  slug: open-ask-sage-chat-management-api
- collection_type: open
  name: Ask Sage Server Admin Completions API
  slug: open-ask-sage-completions-api
- collection_type: open
  name: Ask Sage Server Admin Configuration API
  slug: open-ask-sage-configuration-api
- collection_type: open
  name: Ask Sage Server Admin Dataset Management API
  slug: open-ask-sage-dataset-management-api
- collection_type: open
  name: Ask Sage Server Admin Datasets API
  slug: open-ask-sage-datasets-api
- collection_type: open
  name: Ask Sage Server Admin Deep Agent API
  slug: open-ask-sage-deep-agent-api
- collection_type: open
  name: Ask Sage Server Admin Execute Agent API
  slug: open-ask-sage-execute-agent-api
- collection_type: open
  name: Ask Sage Server Admin Feedback API
  slug: open-ask-sage-feedback-api
- collection_type: open
  name: Ask Sage Server Admin Files API
  slug: open-ask-sage-files-api
- collection_type: open
  name: Ask Sage Server Admin List Agents API
  slug: open-ask-sage-list-agents-api
- collection_type: open
  name: Ask Sage Server Admin MCP Servers API
  slug: open-ask-sage-mcp-servers-api
- collection_type: open
  name: Ask Sage Server Admin Memos API
  slug: open-ask-sage-memos-api
- collection_type: open
  name: Ask Sage Server Admin Models API
  slug: open-ask-sage-models-api
- collection_type: open
  name: Ask Sage Server Admin Plugins API
  slug: open-ask-sage-plugins-api
- collection_type: open
  name: Ask Sage Server Admin Sources API
  slug: open-ask-sage-sources-api
- collection_type: open
  name: Ask Sage Server Admin Superadmin API
  slug: open-ask-sage-superadmin-api
- collection_type: open
  name: Ask Sage Server Admin System API
  slug: open-ask-sage-system-api
- collection_type: open
  name: Ask Sage Server Admin Tabular Data API
  slug: open-ask-sage-tabular-data-api
- collection_type: open
  name: Ask Sage Server Admin Token Requests API
  slug: open-ask-sage-token-requests-api
- collection_type: open
  name: Ask Sage Server Admin Training API
  slug: open-ask-sage-training-api
- collection_type: open
  name: Ask Sage Server Admin Usage API
  slug: open-ask-sage-usage-api
- collection_type: open
  name: Ask Sage Server Admin User Information API
  slug: open-ask-sage-user-information-api
- collection_type: open
  name: Ask Sage Server Admin User Management API
  slug: open-ask-sage-user-management-api
- collection_type: open
  name: Ask Sage Server Admin Utilities API
  slug: open-ask-sage-utilities-api
- collection_type: open
  name: Ask Sage Server Admin Widgets API
  slug: open-ask-sage-widgets-api
- collection_type: open
  name: Ask Sage Server Admin Workbooks API
  slug: open-ask-sage-workbooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ask-sage-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ask-sage-server-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.asksage.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.asksage.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.asksage.ai/docs/v1/api-documentation/api-documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.asksage.ai/docs/v1/api-documentation/api-endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asksage.ai/docs/v1/asksage-platform/getting-started/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://docs.asksage.ai/docs/v1/support.html
- group: company
  title: ''
  type: Blog
  url: https://www.asksage.ai/company/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ask-Sage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asksage.ai/how-to-buy/
- group: start
  title: ''
  type: SignUp
  url: https://chat.asksage.ai/
- group: start
  title: ''
  type: Login
  url: https://chat.asksage.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asksage.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asksage.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.asksage.ai/use-cases/compliance/
- group: build
  title: ''
  type: Packages
  url: packages/ask-sage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ask-sage-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ask-sage-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ask-sage-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ask-sage-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ask-sage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ask-sage-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ask-sage-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/ask-sage-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ask-sage-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ask-sage-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ask-sage-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ask-sage-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ask-sage-authentication.yml
created: '2026-07-17'
description: Ask Sage is a secure, government- and defense-grade generative AI platform that gives regulated organizations access to a broad catalog of commercial and open large language models behind a strict compliance boundary (FedRAMP High, DoD Impact Level 5/6, CMMC, NIST 800-53, GDPR). Beyond chat, it offers retrieval over private datasets, agents and an Agent Builder, plugins, a Deep Agent, and Model Context Protocol (MCP) integrations for Microsoft 365, GitHub, and Box. The platform is exposed through two REST APIs — a Server API for core AI operations (models, completions, agents, datasets, training) and a User API for authentication, API keys, and dataset management — plus OpenAI-, Anthropic-, and Gemini-style compatibility endpoints and an official Python client.
image: https://www.asksage.ai/wp-content/uploads/2021/06/3_WHT.png
layout: provider
mcp_servers:
- description: ''
  name: Ask Sage MCP Server
  slug: ask-sage-mcp-server
modified: '2026-07-18'
name: Ask Sage
nav: Providers
network: true
overview: 'Ask Sage publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agent Builder API, Allocation API, and 29 more. Tagged areas include Company, Artificial Intelligence, Generative AI, Large Language Models, and Government.


  Ask Sage''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 45.7
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ask-sage/refs/heads/main/screenshots/ask-sage-2026-07-25T201421.png
security:
- kind: authentication
  name: Ask Sage Authentication
  slug: ask-sage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ask Sage Domain Security
  slug: ask-sage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ask Sage Trust Center
  slug: ask-sage-trust-center
  summary_line: FedRAMP, GDPR
slug: ask-sage
tags:
- Company
- Artificial Intelligence
- Generative AI
- Large Language Models
- Government
- Defense
- Compliance
- FedRAMP
website: https://www.asksage.ai/
---
