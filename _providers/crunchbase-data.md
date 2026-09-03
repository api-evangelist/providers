---
access_model:
  confidence: high
  label: Paid · Contact sales
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - https://data.crunchbase.com/docs/using-the-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 153
  human_in_the_loop: 0
  name: Crunchbase Data Agentic Access
  operation_count: 421
  slug: crunchbase-data-agentic-access
  summary_line: 421 operations · 153 acting
api_count: 6
apis:
- description: First-party remote Model Context Protocol server over Streamable HTTP, exposing fourteen tools - five natural-language expert tools, four structured schema/lookup/search tools, four Crunchbase list to
  name: Crunchbase MCP Server
  slug: crunchbase-data-mcp
- baseURL: https://api.crunchbase.com/v4/data
  baseurl_source: declared
  description: The Autocomplete API from Crunchbase — 1 operation(s) for autocomplete.
  name: Crunchbase Autocomplete API
  slug: crunchbase-data-autocomplete-api
- baseURL: https://api.crunchbase.com/v4/data
  baseurl_source: declared
  description: The Deleted Entities API from Crunchbase — 2 operation(s) for deleted entities.
  name: Crunchbase Deleted Entities API
  slug: crunchbase-data-deleted-entities-api
- baseURL: https://api.crunchbase.com/v4/data
  baseurl_source: declared
  description: The Entity API from Crunchbase — 60 operation(s) for entity.
  name: Crunchbase Entity API
  slug: crunchbase-data-entity-api
- baseURL: https://api.crunchbase.com/v4/data
  baseurl_source: declared
  description: The Metadata API from Crunchbase — 3 operation(s) for metadata.
  name: Crunchbase Metadata API
  slug: crunchbase-data-metadata-api
- baseURL: https://api.crunchbase.com/v4/data
  baseurl_source: declared
  description: The Search API from Crunchbase — 43 operation(s) for search.
  name: Crunchbase Search API
  slug: crunchbase-data-search-api
- description: Type-ahead suggestions for entities.
  name: Crunchbase Autocomplete API
  slug: crunchbase-autocomplete-api
- description: Feeds of deleted entities for downstream sync.
  name: Crunchbase Deletes API
  slug: crunchbase-deletes-api
- description: Entity lookup endpoints for organizations, people, funding rounds, acquisitions, and IPOs.
  name: Crunchbase Entities API
  slug: crunchbase-entities-api
- description: Full-text and faceted search across entity types.
  name: Crunchbase Search API
  slug: crunchbase-search-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crunchbase Data API v4 Autocomplete API
  slug: open-crunchbase-data-autocomplete-api
- collection_type: open
  name: Crunchbase Data API v4 Autocomplete Deleted Entities API
  slug: open-crunchbase-data-deleted-entities-api
- collection_type: open
  name: Crunchbase Data API v4 Autocomplete Entity Lookup API
  slug: open-crunchbase-data-entity-lookup-api
- collection_type: open
  name: Crunchbase Data API v4 Autocomplete Search API
  slug: open-crunchbase-data-search-api
- collection_type: open
  name: Crunchbase Data API v4
  slug: open-crunchbase-data
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/crunchbase-data-firmographic-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crunchbase-data-core-financials-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crunchbase-data-advanced-financials-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crunchbase-data-insights-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crunchbase-data-predictions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/crunchbase-data-predictions-insights-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.crunchbase.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.crunchbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://data.crunchbase.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://data.crunchbase.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://data.crunchbase.com/docs/welcome-to-crunchbase-data
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.crunchbase.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://about.crunchbase.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crunchbase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crunchbase
- group: commercial
  title: ''
  type: Pricing
  url: https://about.crunchbase.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://about.crunchbase.com/products/crunchbase-api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.crunchbase.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.crunchbase.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://about.crunchbase.com/product-updates/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crunchbase-data-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crunchbase-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crunchbase-data-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crunchbase-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crunchbase-data-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crunchbase-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crunchbase-data-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crunchbase-data-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/crunchbase-data-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crunchbase-data-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/crunchbase-data-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/crunchbase-data-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.crunchbase.com/.well-known/security-policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crunchbase-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crunchbase-data-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crunchbase-data-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crunchbase-data-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crunchbase-data-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crunchbase-data-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crunchbase-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crunchbase-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crunchbase-data-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.crunchbase.com/blog
created: '2026-07-11'
description: Crunchbase is a leading source of private and public company, funding, and investor data - firmographics, funding rounds, acquisitions, investors, people, events, and AI-generated predictions and insights across the global startup and business landscape. The Crunchbase Data API (REST v4, base https://api.crunchbase.com/v4/data) exposes this graph programmatically through Entity Lookup, Search, Autocomplete, and Deleted Entities across 43 entity collections, and is published as six package-scoped OpenAPI 3.0.1 documents - Firmographic, Core Financials, Advanced Financials, Insights, Predictions, and Predictions & Insights - discoverable through an RFC 9727 api-catalog at data.crunchbase.com. Crunchbase also ships a first-party remote MCP server at mcp.crunchbase.com over Streamable HTTP with fourteen documented tools, authenticated with OAuth 2.1 + PKCE and sold as per-user MCP seats. The REST API is read-only and authenticated with a single account-level API key (user_key query
  parameter or X-cb-user-key header); which of the six packages that key is provisioned against determines which operations it can call. Access is subscription-gated with no published pricing - the full API requires a Crunchbase Enterprise or Applications licence, with a reduced Basic API for Crunchbase Basic plan holders.
finops:
- name: Crunchbase Data Finops
  service_category: Data and Analytics
  slug: crunchbase-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crunchbase-data.png
layout: provider
mcp_servers:
- description: 'Crunchbase ships a first-party REMOTE MCP server at https://mcp.crunchbase.com over Streamable HTTP, authenticated with OAuth 2.1 + PKCE against the user''s own Crunchbase account. It is not a wrapper '
  name: Crunchbase
  slug: crunchbase
modified: '2026-08-14'
name: Crunchbase
nav: Providers
network: true
overview: 'Crunchbase publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Deleted Entities API, Entity API, and 6 more. Tagged areas include Company Data, Web Intelligence, Funding Data, Firmographics, and B2B Data.


  Crunchbase''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 37 more developer resources.'
plans:
- name: Crunchbase Data Plans Pricing
  plan_count: 8
  slug: crunchbase-data-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Crunchbase Data Rate Limits
  slug: crunchbase-data-rate-limits
scopes:
- name: Crunchbase Data Scopes
  scope_count: 2
  slug: crunchbase-data-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 42.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.1
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 37.9
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 50.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchbase-data/refs/heads/main/screenshots/crunchbase-data-2026-07-25T210816.png
security:
- kind: authentication
  name: Crunchbase Data Authentication
  slug: crunchbase-data-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Crunchbase Data Domain Security
  slug: crunchbase-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crunchbase Data Vulnerability Disclosure
  slug: crunchbase-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crunchbase-data
tags:
- Company Data
- Web Intelligence
- Funding Data
- Firmographics
- B2B Data
- investor-data
- Reference Data
- Private Markets
- Predictions
- Market Insights
- MCP
- Fortune 1000
website: https://www.crunchbase.com
---
