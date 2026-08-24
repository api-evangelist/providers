---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/infutor-plans-pricing.yml
  - authentication/infutor-authentication.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: Real-time GET query to authenticate a LeadiD token against an account code, confirming lead capture provenance. Credentials are passed as query parameters (lac account code, id LeadiD token).
  name: InfutorData Authentication API
  slug: infutordata-authentication-api
- description: 'Real-time GET query (SingleQuery) returning a lead audit object with authentication status, data-integrity checks, device/IP/frequency metrics, TCPA compliance data, consumer scoring, and demographic '
  name: InfutorData Intelligence / Lead Audit API
  slug: infutordata-intelligence-lead-audit-api
- description: 'The TCPA Guardian projection of the SingleQuery lead audit: given a LeadiD token minted by the Create campaign script, it returns whether a matching TCPA consent disclosure was present on the original'
  name: InfutorData TCPA Guardian (3rd Party) API
  slug: infutordata-tcpa-guardian-3rd-party-api
- description: Real-time GET query (SinglePreAudit) that lets a publisher or lead seller test a lead against a named advertiser's default audit profile BEFORE selling it, returning the yellow and red flags that adve
  name: InfutorData Pre-Audit API
  slug: infutordata-pre-audit-api
- description: 'The batch counterpart to the real-time LeadiD queries — a versioned REST surface on myJornaya for driving Activate audience instances: list the Activate instances on an account, retrieve a presigned u'
  name: InfutorData Activate API
  slug: infutordata-activate-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infutor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infutor.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.infutor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.infutor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.infutor.com/docs/infutor-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.infutor.com/docs/intelligence-getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.infutor.com/
- group: company
  title: ''
  type: Blog
  url: https://infutor.com/category/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infutor.com/privacy-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infutor.com/terms-and-conditions/
- group: auth
  title: ''
  type: Authentication
  url: authentication/infutor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infutor-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/infutor-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infutor-llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.jornaya.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infutor.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infutor-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infutor-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infutor-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/infutor-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/infutor-packages.yml
- group: design
  title: ''
  type: Components
  url: components/infutor-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infutor-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infutor-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infutor-mcp.yml
created: '2026-07-17'
description: InfutorData (part of ActiveProspect, formerly Infutor / Jornaya / LeadiD) is a consumer identity and data-solutions provider that helps marketers identify, understand, and reach consumers while maintaining privacy and compliance. Its platform delivers identity resolution and completion, identity scoring, consumer data enrichment and attributes, audience activation, and lead-quality and TCPA compliance tooling (TCPA Guardian, LeadiD tokens). Real-time query APIs on api.leadid.com support authentication, lead audit, intelligence, and privacy-guardian lookups, documented in the InfutorData help center. Backed by Norwest Venture Partners.
image: https://infutor.com/wp-content/uploads/2026/04/ID_primary_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Infutor MCP Server
  slug: infutor-mcp-server
modified: '2026-08-13'
name: Infutor
nav: Providers
network: true
overview: 'Infutor publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity Resolution, Consumer Data, Data Enrichment, and Lead Verification.


  Infutor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Infutor Plans Pricing
  plan_count: 0
  slug: infutor-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Infutor Rate Limits
  slug: infutor-rate-limits
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 33.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infutor/refs/heads/main/screenshots/infutor-2026-07-25T222430.png
security:
- kind: authentication
  name: Infutor Authentication
  slug: infutor-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Infutor Domain Security
  slug: infutor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infutor
tags:
- Company
- Identity Resolution
- Consumer Data
- Data Enrichment
- Lead Verification
- TCPA Compliance
- Marketing
- Identity
website: https://infutor.com
---
