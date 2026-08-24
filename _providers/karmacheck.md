---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for ordering and tracking background checks, credential verifications and occupational health screenings. 69 operations across 62 paths covering authentication, cases, candidate onboarding an
  name: KarmaCheck API
  slug: karmacheck-api
artifact_total: 7
asyncapis:
- description: ''
  name: Karmacheck Webhooks
  slug: karmacheck-webhooks
common:
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
overview: 'KarmaCheck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Background Checks, Employment Screening, Identity Verification, Credential Verification, and Motor Vehicle Records.


  The KarmaCheck catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KarmaCheck''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 21 more developer resources.'
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
  band: strong
  composite: 57.9
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 67.7
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 23.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
