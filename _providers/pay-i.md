---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Anthropic Requests
  name: Pay-i Anthropic Requests API
  slug: pay-i-anthropic-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: AWS Bedrock Requests
  name: Pay-i AWS Bedrock Requests API
  slug: pay-i-aws-bedrock-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Azure Anthropic Requests
  name: Pay-i Azure Anthropic Requests API
  slug: pay-i-azure-anthropic-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Azure OpenAI Requests
  name: Pay-i Azure OpenAI Requests API
  slug: pay-i-azure-openai-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: System and Custom Categories
  name: Pay-i Categories API
  slug: pay-i-categories-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Google Vertex Requests
  name: Pay-i Google Vertex Requests API
  slug: pay-i-google-vertex-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Ingest Requests
  name: Pay-i Ingest Events API
  slug: pay-i-ingest-events-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: KPIs
  name: Pay-i KP Is API
  slug: pay-i-kpis-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Limits
  name: Pay-i Limits API
  slug: pay-i-limits-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: OpenAI Requests
  name: Pay-i OpenAI Requests API
  slug: pay-i-openai-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Public API for retrieving reports.
  name: Pay-i Reports API
  slug: pay-i-reports-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Requests
  name: Pay-i Requests API
  slug: pay-i-requests-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Resources
  name: Pay-i Resources API
  slug: pay-i-resources-api
- baseURL: https://api.pay-i.com
  baseurl_source: declared
  description: Use Cases
  name: Pay-i Use Cases API
  slug: pay-i-use-cases-api
artifact_total: 19
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/pay-i-openapi-overlay.yaml
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
overview: 'Pay-i publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Anthropic Requests API, AWS Bedrock Requests API, Azure Anthropic Requests API, and 11 more. Tagged areas include Company, Artificial Intelligence, FinOps, Observability, and Cost Management.


  Pay-i''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, and 18 more developer resources.'
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
  composite: 38.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 53.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pay-i/refs/heads/main/screenshots/pay-i-2026-09-02T150923.png
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
