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
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: RESTful backend API for the Sigfox 0G network — manage devices, device types, contracts, groups, users and base stations; retrieve device messages; predict coverage; and configure callbacks that deliv
  name: Sigfox Cloud API
  slug: sigfox-cloud-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigfox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sigfox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://build.sigfox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.sigfox.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://support.sigfox.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sigfox.com/docs/api-first-connection
- group: operate
  title: ''
  type: Support
  url: https://support.sigfox.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sigfox
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sigfox.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://support.sigfox.com/docs/api-versioning
- group: start
  title: ''
  type: SignUp
  url: https://buy.sigfox.com/buy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sigfox.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sigfox.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sigfox-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sigfox-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sigfox-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sigfox-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sigfox-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sigfox-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sigfox-llms.txt
created: '2026-07-17'
description: Sigfox is the 0G low-power wide-area network (LPWAN) for massive IoT, now operated as a technology by UnaBiz. The Sigfox Cloud exposes a RESTful backend API (base https://api.sigfox.com/v2) for managing devices, device types, contracts, groups, users, base stations, coverage predictions, and for retrieving device messages and configuring callbacks that push uplink data to customer systems. The network reaches 70+ countries and millions of connected devices. The API uses HTTP Basic authentication with API-access credentials scoped by role-based profiles, URI-path versioning (/v2), documented rate limits, and a published OpenAPI specification.
image: https://github.com/sigfox.png
layout: provider
modified: '2026-07-21'
name: Sigfox
nav: Providers
network: true
overview: 'Sigfox publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud API. Tagged areas include Company, Industrial, Energy & Iot, IoT, LPWAN, and Connectivity.


  Sigfox''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 12
  name: Sigfox Rate Limits
  slug: sigfox-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 38.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sigfox/refs/heads/main/screenshots/sigfox-2026-09-02T155418.png
security:
- kind: authentication
  name: Sigfox Authentication
  slug: sigfox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sigfox Domain Security
  slug: sigfox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sigfox
tags:
- Company
- Industrial, Energy & Iot
- IoT
- LPWAN
- Connectivity
- Device Management
- Networking
- Telecommunications
website: https://sigfox.com/
---
