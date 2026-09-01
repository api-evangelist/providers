---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Legal Ge Public Apis Agentic Access
  operation_count: 6
  slug: legal-ge-public-apis-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 2
apis:
- description: Look up services, practice areas and verified specialists on legal.ge.
  name: legal.ge Public APIs Directory API
  slug: legal-ge-public-apis-directory-api
- description: Map a free-text legal question to practice areas, and optionally to ranked verified specialists.
  name: legal.ge Public APIs Matching API
  slug: legal-ge-public-apis-matching-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: legal.ge Public Directory API
  slug: open-legal-ge-public-apis-directory-api
- collection_type: open
  name: legal.ge Public Matching API
  slug: open-legal-ge-public-apis-matching-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legal-ge-public-apis-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/legal-ge-public-apis-agentic-access.yml
- group: docs
  title: ''
  type: Documentation
  url: https://legal.ge/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://legal.ge/api/openapi.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infolegalge
- group: operate
  title: ''
  type: Support
  url: https://legal.ge/en/contact
- group: company
  title: ''
  type: Blog
  url: https://legal.ge/en/news
- group: commercial
  title: ''
  type: Pricing
  url: https://legal.ge/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://legal.ge/en/register
- group: start
  title: ''
  type: Login
  url: https://legal.ge/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.ge/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.ge/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/legal-ge-public-apis-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/legal-ge-public-apis-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/legal-ge-public-apis-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/legal-ge-public-apis-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/legal-ge-public-apis-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/legal-ge-public-apis-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/legal-ge-public-apis-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/legal-ge-public-apis-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/legal-ge-public-apis-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/legal-ge-public-apis-examples.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/legal-ge-public-apis-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/legal-ge-public-apis-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/legal-ge-public-apis-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/legal-ge-public-apis-openapi-overlay.yaml
- group: other
  title: ''
  type: APIsJSON
  url: https://legal.ge/apis.json
created: '2026-08-09'
description: 'Georgia''s (the country''s) legal marketplace, exposing a public, keyless, read-only REST API that turns a natural-language description of a legal problem into matched practice areas and a ranked list of verified specialists — lawyers, law firms, accountants, tax consultants, mediators and enforcement agents — each with a canonical, locale-prefixed profile URL. The surface is deliberately agent-first: an OpenAPI 3.1 contract at /api/openapi.json, an APIs.json 0.19 index at /apis.json, an llms.txt trust contract at /llms.txt, a robots.txt that names and allows eleven AI crawlers on the public API paths, and an installable MCP server (@legalge/mcp, MIT) exposing find_legal_specialists and classify_legal_intent to Claude Desktop, Cursor and any MCP-aware client. Trilingual across Georgian, English and Russian; every specialist returned is verification-checked, and contact details are opt-in only.'
examples:
- key_count: 4
  name: Legal Ge Public Apis Classify Response
  slug: legal-ge-public-apis-classify-response
image: https://legal.ge/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: legal.ge Public APIs MCP Server
  slug: legalge-public-apis-mcp-server
modified: '2026-08-09'
name: legal.ge Public APIs
nav: Providers
network: true
overview: 'legal.ge Public APIs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Directory API and Matching API. Tagged areas include Legal, Law, Legal Services, Directory, and Georgia.


  legal.ge Public APIs'' developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 4
  name: Legal Ge Public Apis Rate Limits
  slug: legal-ge-public-apis-rate-limits
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legal-ge-public-apis/refs/heads/main/screenshots/legal-ge-public-apis-2026-08-17T081028.png
security:
- kind: authentication
  name: Legal Ge Public Apis Authentication
  slug: legal-ge-public-apis-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Legal Ge Public Apis Domain Security
  slug: legal-ge-public-apis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: legal-ge-public-apis
tags:
- Legal
- Law
- Legal Services
- Directory
- Georgia
- AI Agents
- MCP
- specialists
- Professional Services
- Marketplace
- Multilingual
- Legal Tech
---
