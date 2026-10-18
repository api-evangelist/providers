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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Hover Agentic Access
  operation_count: 76
  slug: hover-agentic-access
  summary_line: 76 operations · 31 acting
api_count: 5
apis:
- description: REST API for creating and managing property capture jobs, retrieving 3D models and measurement deliverables, inspections, estimates, instant-design leads, and webhooks. OAuth 2.0 authenticated. Versio
  name: HOVER API
  slug: hover-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Agreements API from HOVER — 1 operation(s) for agreements.
  name: HOVER Agreements API
  slug: hover-agreements-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Blueprints API from HOVER — 1 operation(s) for blueprints.
  name: HOVER Blueprints API
  slug: hover-blueprints-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Blueprints (COPY) API from HOVER — 1 operation(s) for blueprints (copy).
  name: HOVER Blueprints (COPY) API
  slug: hover-blueprints-copy-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Capture Requests API from HOVER — 6 operation(s) for capture requests.
  name: HOVER Capture Requests API
  slug: hover-capture-requests-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Deliverables API from HOVER — 1 operation(s) for deliverables.
  name: HOVER Deliverables API
  slug: hover-deliverables-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Estimates API from HOVER — 3 operation(s) for estimates.
  name: HOVER Estimates API
  slug: hover-estimates-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: 'The Https: API from HOVER — 2 operation(s) for https:.'
  name: 'HOVER Https: API'
  slug: hover-https-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Inspection Workflows API from HOVER — 2 operation(s) for inspection workflows.
  name: HOVER Inspection Workflows API
  slug: hover-inspection-workflows-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Inspections API from HOVER — 4 operation(s) for inspections.
  name: HOVER Inspections API
  slug: hover-inspections-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Instant Design API from HOVER — 4 operation(s) for instant design.
  name: HOVER Instant Design API
  slug: hover-instant-design-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Job Shares API from HOVER — 2 operation(s) for job shares.
  name: HOVER Job Shares API
  slug: hover-job-shares-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Jobs API from HOVER — 10 operation(s) for jobs.
  name: HOVER Jobs API
  slug: hover-jobs-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Models API from HOVER — 10 operation(s) for models.
  name: HOVER Models API
  slug: hover-models-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Notes API from HOVER — 1 operation(s) for notes.
  name: HOVER Notes API
  slug: hover-notes-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Notes.json API from HOVER — 1 operation(s) for notes.json.
  name: HOVER Notes.json API
  slug: hover-notes-json-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Oauth API from HOVER — 3 operation(s) for oauth.
  name: HOVER OAuth API
  slug: hover-oauth-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Orgs API from HOVER — 6 operation(s) for orgs.
  name: HOVER Orgs API
  slug: hover-orgs-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Payments API from HOVER — 4 operation(s) for payments.
  name: HOVER Payments API
  slug: hover-payments-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Users API from HOVER — 2 operation(s) for users.
  name: HOVER Users API
  slug: hover-users-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Wallets API from HOVER — 1 operation(s) for wallets.
  name: HOVER Wallets API
  slug: hover-wallets-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Waste Factor API from HOVER — 1 operation(s) for waste factor.
  name: HOVER Waste Factor API
  slug: hover-waste-factor-api
- baseURL: https://hover.to/api
  baseurl_source: declared
  description: The Webhooks API from HOVER — 4 operation(s) for webhooks.
  name: HOVER Webhooks API
  slug: hover-webhooks-api
artifact_total: 31
asyncapis:
- description: ''
  name: Hover Webhooks
  slug: hover-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/agentic-access/hover-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hover-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/rules/hover-rules.yml
  title: ''
  type: Spectral
  url: rules/hover-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/vocabulary/hover-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hover-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/hosts/hover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hover-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/integrations/hover-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hover-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/vendors/hover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hover-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://hover.to/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/scopes/hover-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hover-scopes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/rate-limits/hover-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hover-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/security/hover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hover.to
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hover.to
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hover.to/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hover.to/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hover.to/docs/creating-and-managing-integrations
- group: operate
  title: ''
  type: Support
  url: https://help.hover.to
- group: company
  title: ''
  type: Blog
  url: https://hover.to/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hoverinc
- group: commercial
  title: ''
  type: Pricing
  url: https://hover.to/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hover.to/onboarding/start
- group: start
  title: ''
  type: Login
  url: https://hover.to/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hover.to/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hover.to/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hover.to
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.hover.to/docs/release-notes
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/mcp/hover-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hover-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/llms/hover-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hover-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/changelog/hover-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hover-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/well-known/hover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hover-well-known.yml
created: '2026-07-17'
description: HOVER turns smartphone photos of a property into an accurate, interactive 3D model with complete exterior and interior measurements for the construction, roofing, insurance, and home-services industries. The HOVER API lets partners programmatically create and manage jobs, send capture requests that invite a homeowner or field technician to photograph a structure, receive real-time status updates via webhooks, and retrieve 3D models and measurement deliverables in JSON, PDF, XLSX, SKP, ESX, FML, and XML formats. Additional endpoints cover inspections, estimates and material lists, instant-design images and leads, blueprint reconstruction, job sharing, notes, users, wallets and payments. Authentication is OAuth 2.0 (authorization code + refresh), and a hosted MCP server exposes the same surface to AI agents. HOVER is backed by GV and Menlo Ventures.
image: https://hover.to/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at developers.hover.to over HTTP.
  name: HOVER MCP Server
  slug: hoverapi
modified: '2026-07-19'
name: HOVER
nav: Providers
network: true
overview: 'HOVER publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agreements API, Blueprints API, Blueprints (COPY) API, and 20 more. Tagged areas include Company, Enterprise, Construction, Roofing, and Insurance.


  The HOVER catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  HOVER''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 2
  name: Hover Rate Limits
  slug: hover-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: HOVER API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 3
  slug: hover-rules
scopes:
- name: Hover Scopes
  scope_count: 0
  slug: hover-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 53.8
    catalog_earned_first_party: 8.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.5
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 52.0
    developer_ergonomics: 45.2
    discoverability: 81.7
    operational_transparency: 39.5
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 22
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 41.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/screenshots/hover-2026-07-25T221536.png
security:
- kind: authentication
  name: Hover Authentication
  slug: hover-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hover Domain Security
  slug: hover-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hover
tags:
- Company
- Enterprise
- Construction
- Roofing
- Insurance
- 3D Modeling
- Property Data
- Measurements
- Home Services
- Geospatial
website: https://hover.to
---
