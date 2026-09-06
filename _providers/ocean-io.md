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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Ocean Io Agentic Access
  operation_count: 26
  slug: ocean-io-agentic-access
  summary_line: 26 operations · 23 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Autocomplete API from Ocean.io — 5 operation(s) for autocomplete.
  name: Ocean.io Autocomplete API
  slug: ocean-io-autocomplete-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Enrich API from Ocean.io — 4 operation(s) for enrich.
  name: Ocean.io Enrich API
  slug: ocean-io-enrich-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Lookup API from Ocean.io — 2 operation(s) for lookup.
  name: Ocean.io Lookup API
  slug: ocean-io-lookup-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Ocean.io API Documentation API from Ocean.io — 0 operation(s) for ocean.io api documentation.
  name: Ocean.io Ocean.io API Documentation API
  slug: ocean-io-ocean-io-api-documentation-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Other API from Ocean.io — 3 operation(s) for other.
  name: Ocean.io Other API
  slug: ocean-io-other-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Reveal API from Ocean.io — 2 operation(s) for reveal.
  name: Ocean.io Reveal API
  slug: ocean-io-reveal-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Search API from Ocean.io — 6 operation(s) for search.
  name: Ocean.io Search API
  slug: ocean-io-search-api
- baseURL: https://api.ocean.io
  baseurl_source: declared
  description: The Segmentation API from Ocean.io — 4 operation(s) for segmentation.
  name: Ocean.io Segmentation API
  slug: ocean-io-segmentation-api
artifact_total: 19
asyncapis:
- description: ''
  name: Ocean Io Webhooks
  slug: ocean-io-webhooks
collections:
- collection_type: open
  name: Ocean.io API Documentation
  slug: open-ocean-io-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ocean-io-api-overlay.yaml
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
- description: Ocean.io publishes a first-party hosted (remote) MCP server that exposes the company/people data API to any MCP-aware client. It is a single HTTPS endpoint the client POSTs to; authentication is the s
  name: Ocean.io MCP Server
  slug: oceanio-mcp-server
modified: '2026-08-13'
name: Ocean.io
nav: Providers
network: true
overview: 'Ocean.io publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Enrich API, Lookup API, and 5 more. Tagged areas include Sales Intelligence, B2B, Enrichment, Lookalike, and Account Based Marketing.


  The Ocean.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ocean.io''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, and 24 more developer resources.'
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
  composite: 41.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 56.8
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Account Based Marketing
- Prospecting
- Company Data
- People Data
- Contact Data
- Segmentation
- Go-To-Market
- MCP
website: https://ocean.io/
---
