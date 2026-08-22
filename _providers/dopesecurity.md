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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Dopesecurity Agentic Access
  operation_count: 26
  slug: dopesecurity-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 4
apis:
- description: Everything about authorizing calls to Flightdeck
  name: dope.security Authorization API
  slug: dopesecurity-authorization-api
- description: Everything about your Custom Categories
  name: dope.security Custom Categories API
  slug: dopesecurity-custom-categories-api
- description: Everything about your endpoints
  name: dope.security Endpoints API
  slug: dopesecurity-endpoints-api
- description: Everything about your Policies
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
- description: ''
  name: dopesecurity-mcp.yml
  slug: dopesecurity-mcpyml
modified: '2026-07-18'
name: dope.security
nav: Providers
network: true
overview: 'dope.security publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Custom Categories API, Endpoints API, and 1 more. Tagged areas include Company, Enterprise, Security, Cybersecurity, and Secure Web Gateway.


  dope.security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, CLI, and 27 more developer resources.'
random_paper: 10
score:
  band: strong
  composite: 55.1
  delta: -4.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 57.9
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 28.9
  previous_composite: 59.1
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- API
website: https://dope.security
---
