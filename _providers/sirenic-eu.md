---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 73.4
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sirenic Eu Agentic Access
  operation_count: 125
  slug: sirenic-eu-agentic-access
  summary_line: 125 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.sirenic.eu
  baseurl_source: declared
  description: 'Pay-per-call REST API for official French and European company data: company search and profiles by SIREN/SIRET (INSEE Sirene, INPI RNE), establishments, officers, annual accounts, BODACC legal alerts'
  name: Sirenic API
  slug: sirenic-api
- description: 'Remote Model Context Protocol server (streamable HTTP) over the same official French and European company-data routes: 77 tools such as search_french_companies, get_french_company_kyb_file, screen_san'
  name: Sirenic MCP Server
  slug: sirenic-mcp-server
- description: 'Agent2Agent JSON-RPC endpoint exposing the 116 paid routes as A2A skills (skill ids are the OpenAPI path templates) with the a2a-x402 v0.1 payment extension: a first SendMessage returns an input-requi'
  name: Sirenic A2A Agent
  slug: sirenic-a2a-agent
artifact_total: 10
asyncapis:
- description: ''
  name: Sirenic Eu Webhooks
  slug: sirenic-eu-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sirenic.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sirenic.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://api.sirenic.eu/api
- group: docs
  title: ''
  type: APIReference
  url: https://api.sirenic.eu/api
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/sirenic-eu/sirenic-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sirenic-eu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.sirenic.eu/confidentialite
- group: commercial
  title: ''
  type: LegalNotice
  url: https://api.sirenic.eu/mentions-legales
- group: operate
  title: ''
  type: Support
  url: mailto:contact@sirenic.eu
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/llms/sirenic-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sirenic-eu-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.sirenic.eu/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sirenic-eu-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/sirenic-eu-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sirenic-eu-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/sirenic-eu-robots.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-oauth-authorization-server.json
  title: ''
  type: OAuthAuthorizationServer
  url: well-known/sirenic-eu-oauth-authorization-server.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-oauth-protected-resource.json
  title: ''
  type: OAuthProtectedResource
  url: well-known/sirenic-eu-oauth-protected-resource.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/well-known/sirenic-eu-x402.json
  title: ''
  type: X402
  url: well-known/sirenic-eu-x402.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/packages/sirenic-eu-packages.yml
  title: ''
  type: Packages
  url: packages/sirenic-eu-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/packages/sirenic-eu-packages.yml
  title: ''
  type: SDKs
  url: packages/sirenic-eu-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/mcp/sirenic-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sirenic-eu-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/a2a/sirenic-eu-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sirenic-eu-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/authentication/sirenic-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sirenic-eu-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/scopes/sirenic-eu-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sirenic-eu-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/conformance/sirenic-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sirenic-eu-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/conformance/sirenic-eu-conformance.yml
  title: ''
  type: Compliance
  url: conformance/sirenic-eu-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/errors/sirenic-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sirenic-eu-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/lifecycle/sirenic-eu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sirenic-eu-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/conventions/sirenic-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sirenic-eu-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/rate-limits/sirenic-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sirenic-eu-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/plans/sirenic-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sirenic-eu-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/sandbox/sirenic-eu-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sirenic-eu-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/data-model/sirenic-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sirenic-eu-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/asyncapi/sirenic-eu-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sirenic-eu-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/agentic-access/sirenic-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sirenic-eu-agentic-access.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/mcp/sirenic-eu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sirenic-eu-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/regulatory/sirenic-eu-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/sirenic-eu-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://api.sirenic.eu/confidentialite
- group: operate
  title: ''
  type: IncidentNotification
  url: https://api.sirenic.eu/confidentialite
- group: other
  title: ''
  type: Subprocessors
  url: https://api.sirenic.eu/confidentialite
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sirenic-eu/refs/heads/main/overlays/sirenic-eu-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sirenic-eu-openapi-overlay.yaml
created: '2026-09-19'
description: Sirenic is a French pay-per-call API for official company data across France and Europe, built for AI agents. It serves company search and profiles by SIREN/SIRET from INSEE Sirene and INPI RNE, establishments, officers, filed accounts and ratios, BODACC legal alerts, a default-risk score, sanctions screening against six official lists, KYB dossiers, live VIES VAT and IBAN checks with a ready-to-invoice verdict for the 2026 French e-invoicing mandate, public-procurement records, watchlists with Ed25519-signed webhooks, and profiles, accounts and events from thirteen European registers plus LEI/GLEIF groups. Every /v1 route is a GET priced per call ($0.002 to $1.00) and paid either through the x402 protocol in USDC or EURC on Base with no account, or with an srn_live_ API key and prepaid euro credits. It publishes an OpenAPI 3.1, llms.txt, an RFC 9727 api-catalog, an MCP server, an A2A agent card, x402 discovery and OAuth metadata from api.sirenic.eu.
layout: provider
mcp_servers:
- description: Can you safely invoice or pay this company? Verify a supplier before payment in one call — legal identity, VAT checked live against VIES, IBAN form-checked with its bank identified from official regis
  name: Sirenic MCP Server
  slug: sirenic-mcp-server
modified: '2026-09-19'
name: Sirenic
nav: Providers
network: true
overview: 'Sirenic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company Data, Business Registry, KYB, Know Your Business, and Sanctions Screening.


  The Sirenic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sirenic''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 36 more developer resources.'
plans:
- name: Sirenic Eu Plans Pricing
  plan_count: 3
  slug: sirenic-eu-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Sirenic Eu Rate Limits
  slug: sirenic-eu-rate-limits
scopes:
- name: Sirenic Eu Scopes
  scope_count: 0
  slug: sirenic-eu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 20.4
    developer_ergonomics: 70.8
    discoverability: 72.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Sirenic Eu Authentication
  slug: sirenic-eu-authentication
  summary_line: x402 payment (no credential)/apiKey/http bearer/oauth2 (MCP connector only) · 4 schemes
slug: sirenic-eu
tags:
- Company Data
- Business Registry
- KYB
- Know Your Business
- Sanctions Screening
- Financial Data
- Credit Risk
- VAT Validation
- IBAN Validation
- E-Invoicing
- Public Procurement
- Open Data
- France
- Europe
- x402
- Agentic Commerce
- MCP
- A2A
- Company
website: https://sirenic.eu/
---
