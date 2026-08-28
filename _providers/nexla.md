---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: RESTful control-plane API for the Nexla platform. 155 paths / 274 operations across 31 tags covering data flows, sources, Nexsets (data sets), sinks, credentials, data maps, transforms, code container
  name: Nexla REST API
  slug: nexla-rest-api
- description: OpenAPI 3.1 contract for Nexla's GenAI service, combining the Agentic RAG query API with MCPaaS — the MCP Tools control plane. 110 paths / 131 operations covering agentic RAG query and cache, per-nexs
  name: Nexla GenAI API (RAG + MCPaaS)
  slug: nexla-genai-api-rag-mcpaas
artifact_total: 10
asyncapis:
- description: ''
  name: Nexla Webhooks
  slug: nexla-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/nexla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nexla.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nexla.com/dev-guides/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexla.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nexla.com/reference/nexla-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nexla.com/user-guides/get-started/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://nexla.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://nexla.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nexla-opensource
- group: commercial
  title: ''
  type: Pricing
  url: https://nexla.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dataops.nexla.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nexla.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nexla.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://nexla.com/data-security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexla-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexla-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/nexla-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nexla-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nexla-cli.yml
- group: design
  title: ''
  type: Components
  url: components/nexla-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexla-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexla-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexla-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nexla-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexla-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexla-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nexla-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nexla-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nexla-plans-pricing.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexla-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nexla-webhooks.yml
created: '2026-08-26'
description: 'Nexla is an enterprise data integration and AI-data platform, founded in 2016 and headquartered in San Mateo, California. Its core abstraction is the Nexset — a logical, schema-aware, bi-directionally usable data product that Nexla generates automatically from any connected system. The platform spans ETL/ELT, streaming and CDC, API ingestion and delivery, RAG pipelines and, since 2026, an MCP Tools layer (MCP Studio, MCP Gateway, Agentic Probe) that turns governed Nexsets into task-scoped MCP servers for AI agents. Nexla exposes two public machine-readable contracts: a 274-operation OpenAPI 3.1 REST API covering flows, sources, Nexsets, sinks, credentials, transforms, projects, teams, organizations, access control, notifications, audit logs and metrics; and a 131-operation OpenAPI 3.1 GenAI (RAG + MCPaaS) API covering agentic RAG, nexset filters, skills, tools, toolsets, MCP gateway and audit receipts. First-party clients ship as a Python SDK, a TypeScript/JS SDK, a React embedding
  SDK and a Python CLI. Nexla is SOC 2 Type II, HIPAA, GDPR and CCPA compliant.'
image: https://cdn.nexla.io/ui/assets/brand/v2/nexla-logo-color-portrait.svg
layout: provider
mcp_servers:
- description: ''
  name: Nexla MCP Server (MCP Tools / MCPaaS)
  slug: nexla-mcp-server-mcp-tools-mcpaas
modified: '2026-08-26'
name: Nexla
nav: Providers
network: true
overview: 'Nexla publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API and GenAI API (RAG + MCPaaS). Tagged areas include Company, Data Integration, Data Engineering, ETL, and ELT.


  The Nexla catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nexla''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Nexla Plans Pricing
  plan_count: 3
  slug: nexla-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Nexla Rate Limits
  slug: nexla-rate-limits
score:
  band: strong
  composite: 61.9
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 30.3
    contract_quality: 52.8
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Nexla Authentication
  slug: nexla-authentication
  summary_line: http/apiKey · 6 schemes
- kind: domain-security
  name: Nexla Domain Security
  slug: nexla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nexla Vulnerability Disclosure
  slug: nexla-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Nexla Trust Center
  slug: nexla-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, GDPR, CCPA
slug: nexla
tags:
- Company
- Data Integration
- Data Engineering
- ETL
- ELT
- Data Products
- Streaming
- Change Data Capture
- Data Governance
- Artificial Intelligence
- Retrieval Augmented Generation
- MCP
- Agent Tools
- Data Pipelines
- Connectors
website: https://nexla.com/
---
