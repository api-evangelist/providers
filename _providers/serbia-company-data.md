---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Serbia Company Data Agentic Access
  operation_count: 3
  slug: serbia-company-data-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://serbia-company-x402.vercel.app
  baseurl_source: declared
  description: The Company API from Serbia Company Data — 2 operation(s) for company.
  name: Serbia Company Data Company API
  slug: serbia-company-data-company-api
- baseURL: https://serbia-company-x402.vercel.app
  baseurl_source: declared
  description: The Search API from Serbia Company Data — 1 operation(s) for search.
  name: Serbia Company Data Search API
  slug: serbia-company-data-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Serbia Data Company API
  slug: open-serbia-company-data-company-api
- collection_type: open
  name: Serbia Company Data Search API
  slug: open-serbia-company-data-search-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serbia-company-data-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serbia-company-data-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serbia-company-data-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/serbia-company-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/serbia-company-data-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/serbia-company-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/serbia-company-data-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/serbia-company-data-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/serbia-company-data-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/serbia-company-data-sample-response.json
- group: build
  title: ''
  type: Examples
  url: examples/serbia-company-data-402-payment-required.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/serbia-company-data-getSerbianCompany-bazaar-schema.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/serbia-company-data-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/serbia-company-data-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/serbia-company-data-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/serbia-company-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/serbia-company-data-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://serbia-company-x402.vercel.app/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/serbia-company-data-rate-limits.yml
- group: build
  title: ''
  type: Examples
  url: examples/serbia-company-data-health-response.json
created: '2026-07-28'
description: A single-purpose, pay-per-call REST API serving normalized Serbian company registry data and latest financial-statement summaries from official APR high-value open data. Access is gated by HTTP 402 micropayments via the x402 protocol settled in Base USDC, requiring no account or API key.
examples:
- key_count: 2
  name: Serbia Company Data 402 Payment Required
  slug: serbia-company-data-402-payment-required
- key_count: 5
  name: Serbia Company Data Health Response
  slug: serbia-company-data-health-response
- key_count: 3
  name: Serbia Company Data Sample Response
  slug: serbia-company-data-sample-response
image: https://serbia-company-x402.vercel.app/favicon.svg
json_schemas:
- name: Serbia Company Data Batchgetserbiancompanies Bazaar
  property_count: 2
  slug: serbia-company-data-batchGetSerbianCompanies-bazaar
- name: Serbia Company Data Getserbiancompany Bazaar
  property_count: 2
  slug: serbia-company-data-getSerbianCompany-bazaar
- name: Serbia Company Data Searchserbiancompanies Bazaar
  property_count: 2
  slug: serbia-company-data-searchSerbianCompanies-bazaar
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool list derived from the OpenAPI — no server is published
  slug: candidate-mcp-tool-list-derived-from-the-openapi-no-server-is-published
modified: '2026-08-14'
name: Serbia Company Data
nav: Providers
network: true
overview: 'Serbia Company Data publishes 2 APIs on the [APIs.io](https://apis.io/) network: Company API and Search API. Tagged areas include Serbia, Company Data, Business Registry, Open Data, and x402.


  Serbia Company Data''s developer surface includes authentication, sandbox, code examples, pricing, and 17 more developer resources.'
plans:
- name: Serbia Company Data Plans Pricing
  plan_count: 0
  slug: serbia-company-data-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Serbia Company Data Rate Limits
  slug: serbia-company-data-rate-limits
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 53.7
    developer_ergonomics: 44.6
    discoverability: 63.0
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serbia-company-data/refs/heads/main/screenshots/serbia-company-data-2026-09-02T154940.png
security:
- kind: authentication
  name: Serbia Company Data Authentication
  slug: serbia-company-data-authentication
  summary_line: none/x402-payment · 1 scheme
- kind: domain-security
  name: Serbia Company Data Domain Security
  slug: serbia-company-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: serbia-company-data
tags:
- Serbia
- Company Data
- Business Registry
- Open Data
- x402
- base-usdc
- OpenAPI
- Financial Statements
- pay-per-call
- agent-native
---
