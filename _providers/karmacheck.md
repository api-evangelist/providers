---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Authentication API from KarmaCheck — 1 operation(s) for authentication.
  name: KarmaCheck Authentication API
  slug: karmacheck-authentication-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Candidate onboarding API from KarmaCheck — 20 operation(s) for candidate onboarding.
  name: KarmaCheck Candidate onboarding API
  slug: karmacheck-candidate-onboarding-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Case API from KarmaCheck — 2 operation(s) for case.
  name: KarmaCheck Case API
  slug: karmacheck-case-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Cases API from KarmaCheck — 22 operation(s) for cases.
  name: KarmaCheck Cases API
  slug: karmacheck-cases-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Packages API from KarmaCheck — 4 operation(s) for packages.
  name: KarmaCheck Packages API
  slug: karmacheck-packages-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Secure documents API from KarmaCheck — 6 operation(s) for secure documents.
  name: KarmaCheck Secure documents API
  slug: karmacheck-secure-documents-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Services API from KarmaCheck — 5 operation(s) for services.
  name: KarmaCheck Services API
  slug: karmacheck-services-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Users API from KarmaCheck — 1 operation(s) for users.
  name: KarmaCheck Users API
  slug: karmacheck-users-api
- baseURL: https://api.karmacheck.io
  baseurl_source: declared
  description: The Verification Book API from KarmaCheck — 1 operation(s) for verification book.
  name: KarmaCheck Verification Book API
  slug: karmacheck-verification-book-api
artifact_total: 15
asyncapis:
- description: ''
  name: Karmacheck Webhooks
  slug: karmacheck-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/karmacheck-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/karmacheck-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.karmacheck.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.karmacheck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.karmacheck.com/background-check-api/overview/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.karmacheck.com/api-reference/authentication/authenticate-api-client
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.karmacheck.com/background-check-api/guides/candidate-provided-pii-flow
- group: operate
  title: ''
  type: Support
  url: https://www.karmacheck.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.karmacheck.com/blogs
- group: start
  title: ''
  type: Login
  url: https://app.karmacheck.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.karmacheck.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.karmacheck.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/karmacheck-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/karmacheck-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/karmacheck-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/karmacheck-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/karmacheck-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/karmacheck-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/karmacheck-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/karmacheck-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/karmacheck-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/karmacheck-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/karmacheck-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/karmacheck-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/karmacheck-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/karmacheck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/karmacheck-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karmacheck-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/karmacheck-well-known.yml
created: '2026-08-23'
description: 'KarmaCheck Inc. is a San Francisco based, API-first background check and credential verification company serving staffing, healthcare, gig-economy, call-center and IT/tech hiring workflows. The KarmaCheck API is a REST contract on api.karmacheck.io covering the full screening lifecycle: creating and placing cases, candidate onboarding with FCRA, e-signature, Canada, international and location-specific disclosure acknowledgement, criminal, identity, motor vehicle record, education, employment, professional-licence and occupational-health screenings, secure document upload and retrieval, package and service catalogs, jurisdiction lookup, verification-book search, adjudication and pre-adverse-action documents. Results are pushed asynchronously through Svix-delivered, HMAC-SHA256 signed webhooks (case.statuschange and casedata.statuschange). KarmaCheck also operates a remote MCP server so agents can order and track screenings from natural language, and integrates with Bullhorn,
  Workday and symplr CTM. The company holds a SOC 2 Type 2 report and operates as an FCRA consumer reporting agency.'
image: https://cdn.prod.website-files.com/673634b37e2e1340c1ee5f3d/6736aa68f0e954a84817b9c0_Favicon-Icon.png
layout: provider
mcp_servers:
- description: ''
  name: KarmaCheck MCP Server
  slug: karmacheck-mcp-server
modified: '2026-08-23'
name: KarmaCheck
nav: Providers
network: true
overview: 'KarmaCheck publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Candidate onboarding API, Case API, and 6 more. Tagged areas include Background Checks, Employment Screening, Identity Verification, Credential Verification, and Motor Vehicle Records.


  The KarmaCheck catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KarmaCheck''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 23 more developer resources.'
plans:
- name: Karmacheck Plans Pricing
  plan_count: 0
  slug: karmacheck-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Karmacheck Rate Limits
  slug: karmacheck-rate-limits
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 66.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 52.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karmacheck/refs/heads/main/screenshots/karmacheck-2026-09-02T150133.png
security:
- kind: authentication
  name: Karmacheck Authentication
  slug: karmacheck-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Karmacheck Domain Security
  slug: karmacheck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: karmacheck
tags:
- Background Checks
- Employment Screening
- Identity Verification
- Credential Verification
- Motor Vehicle Records
- Occupational Health Screening
- Drug Screening
- HR Tech
- Staffing
- Healthcare
- Compliance
- FCRA
- Adjudication
- Webhook
- MCP Server
- agent-native
website: https://www.karmacheck.com/
---
