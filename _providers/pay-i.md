---
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Pay-i REST API. A metering proxy in front of the major GenAI providers plus management endpoints for spend limits, use cases, KPIs, categories/resources, requests and reports. 63 operations across
  name: Pay-i API
  slug: pay-i-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.pay-i.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pay-i.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pay-i.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pay-i.com/reference/getlimits
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pay-i.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.pay-i.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pay-i.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pay-i.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pay-i
- group: company
  title: ''
  type: Blog
  url: https://www.pay-i.com/resources
- group: build
  title: ''
  type: Packages
  url: packages/pay-i-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pay-i-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pay-i-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pay-i-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pay-i-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pay-i-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pay-i-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pay-i-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pay-i-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pay-i-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pay-i-rate-limits.yml
created: '2026-08-26'
description: 'Pay-i is a GenAI cost, capacity and ROI optimization platform founded by Microsoft veterans. It instruments generative-AI applications so enterprises can prove the business value of their AI spend. Pay-i exposes a REST API at api.pay-i.com built around three surfaces: a metering proxy that fronts OpenAI, Azure OpenAI, Anthropic, Azure Anthropic, AWS Bedrock and Google Vertex and records cost, latency and failure metadata for every inference request; an ingest API for submitting events from providers Pay-i does not proxy; and a management API covering Limits (spend budgets with risk thresholds and blocking states), Use Cases and their versions and instances, KPIs and value policies, Categories and Resources for model and price catalogs, and Reports. Instrumentation is driven by a family of xProxy-* request headers and first-party Python and TypeScript SDKs, plus an n8n community node and a Databricks integration.'
image: https://cdn.prod.website-files.com/698b13d019d0be64f91a6ae7/69a72aad61995c2a45243b2e_open-graph.png
layout: provider
mcp_servers:
- description: ''
  name: Pay-i MCP Server
  slug: pay-i-mcp-server
modified: '2026-08-26'
name: Pay-i
nav: Providers
network: true
overview: 'Pay-i publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, FinOps, Observability, and Cost Management.


  Pay-i''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Pay I Plans Pricing
  plan_count: 0
  slug: pay-i-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Pay I Rate Limits
  slug: pay-i-rate-limits
score:
  band: thin
  composite: 39.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 51.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Pay I Authentication
  slug: pay-i-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pay I Domain Security
  slug: pay-i-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pay-i
tags:
- Company
- Artificial Intelligence
- FinOps
- Observability
- Cost Management
- Generative AI
- LLM
- Analytics
- Governance
- Metering
website: https://www.pay-i.com/
---
