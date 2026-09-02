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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.9
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Single-endpoint healthcare interoperability API exposing proprietary LK* operations (appointments, patient bridge/search, documents, charges, patient balance, master lists) that bi-directionally conne
  name: LKCloud Interop API
  slug: lkcloud-interop-api
- description: HL7 FHIR R4 RESTful API (read/search/create/update/delete across R4 resources) over the ELLKAY interoperability platform, with a published CapabilityStatement. OAuth 2.0 Bearer + SiteServiceKey; error
  name: LKCloud FHIR R4 API
  slug: lkcloud-fhir-r4-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.ellkay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lkcloud-api.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://lkcloud-api.readme.io/docs/lk-cloud-overview
- group: docs
  title: ''
  type: APIReference
  url: https://lkcloud-api.readme.io/reference
- group: auth
  title: ''
  type: Authentication
  url: authentication/ellkay-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ellkay-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ellkay.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.ellkay.com/support
- group: start
  title: ''
  type: Login
  url: https://dashboard.ellkay.com/Login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ellkay.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ellkay-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ellkay-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ellkay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ellkay-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ellkay-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ellkay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ellkay-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ellkay-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ellkay-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ellkay-domain-security.yml
created: '2026-07-17'
description: 'ELLKAY is a healthcare data interoperability and data-management company that connects disparate health IT systems so clinical and financial data can move where it is needed. Its LKOpera, LKOrbit, and LKOasis product lines provide interface-engine integration, orders and results, payer data retrieval, network/lab connectivity, and data archiving/migration across 750+ EMR/PM systems, 400+ hospitals, 58k+ practices, and 725+ laboratories. For developers, ELLKAY exposes the LKCloud platform: a single-endpoint Interop API (proprietary LK* operations) and a full HL7 FHIR R4 RESTful API, both authenticated with OAuth 2.0 against the LKIdentity authorization server and routed with a SiteServiceKey.'
image: https://cdn.prod.website-files.com/68470d9028f4a074323fde70/689b3ac60177b4bae93d407b_Asset%2028.png
layout: provider
mcp_servers:
- description: ''
  name: ELLKAY MCP Server
  slug: ellkay-mcp-server
modified: '2026-07-19'
name: ELLKAY
nav: Providers
network: true
overview: 'ELLKAY publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Interoperability, FHIR, and HL7.


  ELLKAY''s developer surface includes documentation, API reference, authentication, changelog, engineering blog, support, sandbox, and 13 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Ellkay Rate Limits
  slug: ellkay-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 39.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 28.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/screenshots/ellkay-2026-07-25T213153.png
security:
- kind: authentication
  name: Ellkay Authentication
  slug: ellkay-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Ellkay Domain Security
  slug: ellkay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ellkay
tags:
- Company
- Healthcare
- Interoperability
- FHIR
- HL7
- EHR Integration
- Health Data
website: https://www.ellkay.com/
---
