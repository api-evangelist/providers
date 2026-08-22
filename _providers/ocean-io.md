---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Ocean Io Agentic Access
  operation_count: 26
  slug: ocean-io-agentic-access
  summary_line: 26 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST API for B2B company and people intelligence — 26 operations across search (v2 and v3 filter and lookalike search for companies and people), enrichment (single and batch, by domain or LinkedIn han
  name: Ocean.io API
  slug: oceanio-api
artifact_total: 12
asyncapis:
- description: ''
  name: Ocean Io Webhooks
  slug: ocean-io-webhooks
collections:
- collection_type: open
  name: Ocean.io API Documentation
  slug: open-ocean-io-api
common:
- group: company
  title: ''
  type: Website
  url: https://ocean.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ocean.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.ocean.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.ocean.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://app.ocean.io/docs/getting-started/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://ocean.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ocean.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ocean-io-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocean-io-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ocean-io-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ocean-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ocean-io-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ocean-io-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ocean-io-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ocean-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ocean-io-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocean-io-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ocean-io-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ocean-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ocean.io/
- group: build
  title: ''
  type: Packages
  url: packages/ocean-io-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ocean-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ocean-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocean-io-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ocean-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ocean-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ocean-io-finops.yml
created: '2026-05-08'
description: 'Ocean.io is a B2B go-to-market data platform built around lookalike intelligence: give it a domain or a set of closed-won customers and it returns the most similar companies from a database of 67M company profiles and 250M+ employee records, each carrying 100+ signals assembled from the open web. Alongside the web app it ships a public REST API at api.ocean.io covering company and people search (filter, Boolean and lookalike), company and person enrichment, domain and LinkedIn-handle lookup, verified email and phone reveal, autocomplete for filter values, and a stateful segmentation service that clusters a customer list into scored segments and attributes new domains to the closest one. The API is documented with a public OpenAPI 3.1 document, meters every call from a single credit pool, delivers batch and reveal results by webhook callback, and is also exposed to agents through a first-party hosted MCP server at api.ocean.io/mcp.'
finops:
- name: Ocean Io Finops
  service_category: Sales Intelligence
  slug: ocean-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ocean-io.png
layout: provider
mcp_servers:
- description: ''
  name: ocean-io-mcp.yml
  slug: ocean-io-mcpyml
modified: '2026-08-13'
name: Ocean.io
nav: Providers
network: true
overview: 'Ocean.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Intelligence, B2B, Enrichment, Lookalike, and ABM.


  The Ocean.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ocean.io''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, and 23 more developer resources.'
plans:
- name: Ocean Io Plans Pricing
  plan_count: 0
  slug: ocean-io-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Ocean Io Rate Limits
  slug: ocean-io-rate-limits
scopes:
- name: Ocean Io Scopes
  scope_count: 0
  slug: ocean-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.1
  delta: -4.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 62.9
    developer_ergonomics: 23.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 55.3
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocean-io/refs/heads/main/screenshots/ocean-io-2026-06-20T190601.png
security:
- kind: authentication
  name: Ocean Io Authentication
  slug: ocean-io-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Ocean Io Domain Security
  slug: ocean-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ocean Io Trust Center
  slug: ocean-io-trust-center
  summary_line: SOC 2
slug: ocean-io
tags:
- Sales Intelligence
- B2B
- Enrichment
- Lookalike
- ABM
- Prospecting
- Company Data
- People Data
- Contact Data
- Segmentation
- Go-To-Market
- MCP
website: https://ocean.io/
---
