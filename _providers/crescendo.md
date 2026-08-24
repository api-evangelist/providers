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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Crescendo Agentic Access
  operation_count: 17
  slug: crescendo-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 5
apis:
- description: Model Context Protocol (MCP) endpoints.
  name: Crescendo MCP API
  slug: crescendo-mcp-api
- description: Tenant-scoped provisioning resources.
  name: Crescendo Provisioning API
  slug: crescendo-provisioning-api
- description: Reporting-friendly exports (cursor pagination).
  name: Crescendo Reporting API
  slug: crescendo-reporting-api
- description: Service metadata and health.
  name: Crescendo Service API
  slug: crescendo-service-api
- description: Upload recordings for VOC processing.
  name: Crescendo VOC API
  slug: crescendo-voc-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crescendo Platform MCP API
  slug: open-crescendo-mcp-api
- collection_type: open
  name: Crescendo Platform MCP Provisioning API
  slug: open-crescendo-provisioning-api
- collection_type: open
  name: Crescendo Platform MCP Reporting API
  slug: open-crescendo-reporting-api
- collection_type: open
  name: Crescendo Platform MCP Service API
  slug: open-crescendo-service-api
- collection_type: open
  name: Crescendo Platform MCP VOC API
  slug: open-crescendo-voc-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/crescendo-platform-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crescendo.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.crescendo.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crescendo.ai/api-reference/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://docs.crescendo.ai/quickstart
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crescendo-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.crescendo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.crescendo.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crescendo.ai/policies/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crescendo.ai/policies/privacy
- group: company
  title: ''
  type: Website
  url: https://www.crescendo.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crescendo-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crescendo-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crescendo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crescendo-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crescendo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crescendo-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crescendo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crescendo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crescendo-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/crescendo-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Crescendo is an AI-native customer experience (CX) platform that unifies AI agents for chat, voice, email, and messaging with quality assurance, workforce management, and business insights. The Crescendo Platform API (OpenAPI 3.1) is a tenant-scoped HTTP API for provisioning tenant configuration and documents, exporting assistant and voice-of-customer (VOC) conversations for reporting with cursor pagination, uploading audio recordings for asynchronous VOC processing, and driving assistants through a hosted Model Context Protocol (MCP) bots server over Streamable HTTP. Authentication is a tenant-scoped bearer API key. Crescendo is backed by General Catalyst and Trinity Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crescendo.png
layout: provider
mcp_servers:
- description: ''
  name: Crescendo MCP Server
  slug: crescendo-mcp-server
modified: '2026-07-18'
name: Crescendo
nav: Providers
network: true
overview: 'Crescendo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including MCP API, Provisioning API, Reporting API, and 2 more. Tagged areas include Company, Customer Experience, Customer-Support, Artificial Intelligence, and AI Agents.


  Crescendo''s developer surface includes documentation, API reference, quickstart, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 39.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 54.9
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crescendo/refs/heads/main/screenshots/crescendo-2026-07-25T210727.png
security:
- kind: authentication
  name: Crescendo Authentication
  slug: crescendo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Crescendo Domain Security
  slug: crescendo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crescendo
tags:
- Company
- Customer Experience
- Customer-Support
- Artificial Intelligence
- AI Agents
- Contact Center
- Conversational AI
- Voice of Customer
- MCP
website: https://www.crescendo.ai
---
