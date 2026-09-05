---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Dopesecurity Agentic Access
  operation_count: 26
  slug: dopesecurity-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.flightdeck.dope.security/v1
  baseurl_source: declared
  description: Everything about authorizing calls to Flightdeck
  name: dope.security Authorization API
  slug: dopesecurity-authorization-api
- baseURL: https://api.flightdeck.dope.security/v1
  baseurl_source: declared
  description: Everything about your Custom Categories
  name: dope.security Custom Categories API
  slug: dopesecurity-custom-categories-api
- baseURL: https://api.flightdeck.dope.security/v1
  baseurl_source: declared
  description: Everything about your endpoints
  name: dope.security Endpoints API
  slug: dopesecurity-endpoints-api
- baseURL: https://api.flightdeck.dope.security/v1
  baseurl_source: declared
  description: Everything about your Policies
  name: dope.security Policies API
  slug: dopesecurity-policies-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flightdeck - dope.security - Public API specification Authorization API
  slug: open-dopesecurity-authorization-api
- collection_type: open
  name: Flightdeck - dope.security - Public API specification Authorization Custom Categories API
  slug: open-dopesecurity-custom-categories-api
- collection_type: open
  name: Flightdeck - dope.security - Public API specification Authorization Endpoints API
  slug: open-dopesecurity-endpoints-api
- collection_type: open
  name: Flightdeck - dope.security - Public API specification Authorization Policies API
  slug: open-dopesecurity-policies-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/dopesecurity-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://dope.security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://inflight.dope.security
- group: docs
  title: ''
  type: Documentation
  url: https://inflight.dope.security
- group: docs
  title: ''
  type: APIReference
  url: https://inflight.dope.security/dope.apis/public-api-specification
- group: start
  title: ''
  type: GettingStarted
  url: https://inflight.dope.security/introducing-dope.swg/quick-start-guide
- group: company
  title: ''
  type: Blog
  url: https://dope.security/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dope.security/pricing
- group: start
  title: ''
  type: Login
  url: https://fly.dope.security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dope.security/legal/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dope.security/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@dope.security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dopesecurity
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dope.security
- group: auth
  title: ''
  type: Compliance
  url: https://dope.security/legal/soc-2
- group: auth
  title: ''
  type: Security
  url: https://dope.security/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dopesecurity-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dopesecurity-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/dopesecurity-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dopesecurity-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dopesecurity-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dopesecurity-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dopesecurity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dopesecurity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dopesecurity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dopesecurity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dopesecurity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dopesecurity-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dopesecurity-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dopesecurity-flightdeck-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dopesecurity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dopesecurity-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dopesecurity-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: dope.security is a cybersecurity company that builds the first fly-direct Secure Web Gateway (dope.swg) — a next-generation SWG that runs security directly on the endpoint (on-device proxy, local SSL inspection, URL and category filtering, cloud application control) instead of routing traffic through a data-center stopover, alongside AI-powered Data Loss Prevention and a neural CASB (casb.neural) for shadow IT/AI discovery and data posture. Its Flightdeck partner API lets administrators manage policies, custom URL categories, URL/application bypass lists, SSL inspection, and endpoint status programmatically, and it ships an official open-source MCP server. Founded in 2021, based in Mountain View and Cork, and backed by GV.
image: https://fly.dope.security/DS_192x192.png
layout: provider
mcp_servers:
- description: Official open-source local MCP server for dope.security. Lets an AI assistant talk to your dope.security tenant — inspect endpoints, read and modify web policies, and curate custom URL categories. Wra
  name: dope.security MCP Server
  slug: dopesecurity-mcp-server
modified: '2026-07-18'
name: dope.security
nav: Providers
network: true
overview: 'dope.security publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Custom Categories API, Endpoints API, and 1 more. Tagged areas include Company, Enterprise, Security, Cybersecurity, and Secure Web Gateway.


  dope.security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, CLI, and 27 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 56.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dopesecurity/refs/heads/main/screenshots/dopesecurity-2026-07-25T212307.png
security:
- kind: authentication
  name: Dopesecurity Authentication
  slug: dopesecurity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dopesecurity Domain Security
  slug: dopesecurity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dopesecurity Vulnerability Disclosure
  slug: dopesecurity-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dopesecurity Trust Center
  slug: dopesecurity-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: dopesecurity
tags:
- Company
- Enterprise
- Security
- Cybersecurity
- Secure Web Gateway
- SASE
- SSE
- Data Loss Prevention
- CASB
- Endpoint Security
website: https://dope.security
---
