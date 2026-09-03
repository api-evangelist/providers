---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: TimeEngine (package name `mdtsdb`) is QOMPLX's multi-dimensional time-series database and analytics engine. It exposes an HTTP interface for event ingestion (`/api/v1/ingest`), query-language executio
  name: QOMPLX TimeEngine HTTP API
  slug: qomplx-timeengine
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qomplx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qomplx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QOMPLX-INC
- group: build
  title: ''
  type: Packages
  url: packages/qomplx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qomplx-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qomplx-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qomplx-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qomplx-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qomplx-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qomplx-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qomplx-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qomplx-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qomplx-llms.txt
coverage:
  checked: '2026-08-26'
  detail: QOMPLX's only published API contract is the source of three first-party TimeEngine client libraries on GitHub — there is no OpenAPI, AsyncAPI, GraphQL SDL or Postman collection anywhere, and www.qomplx.com is now a single-page Ghost install where every content page in its own sitemap, including the terms of service, SLA and vulnerability-disclosure policy, returns a 301 self-redirect loop.
  evidence:
  - status: 404
    url: https://www.qomplx.com/openapi.json
  - status: 200
    url: https://www.qomplx.com/llms.txt
  - status: 301
    url: https://www.qomplx.com/vulnerability-disclosure-policy/
  - status: 301
    url: https://www.qomplx.com/service-level-agreement/
  - status: 404
    url: https://www.qomplx.com/pricing/
  - status: 200
    url: https://github.com/QOMPLX-INC/te-python-client
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-26'
description: QOMPLX, Inc. is a Reston, Virginia research and technology company building risk-analytics and cybersecurity products — Identity Threat Detection and Response (ITDR) for Active Directory and cloud credentials, Managed Detection and Response (MDR), attack-surface monitoring, Active Directory security assessment, offensive security services and vCISO engagements — sold into finance, legal and insurance. Its underlying data platform, QOMPLX:OS (Q:OS), includes TimeEngine, a multi-dimensional time-series database and analytics engine that QOMPLX exposes over an HTTP and WebSocket interface. QOMPLX publishes first-party TimeEngine client libraries for Python, Java and Erlang on GitHub, but ships no OpenAPI, AsyncAPI, GraphQL SDL or Postman collection, and operates no public developer portal, API reference or pricing page. As of this pass its own website has been reduced to a single-page Ghost install and every content page listed in its sitemap returns a 301 self-redirect loop.
image: https://www.qomplx.com/favicon.png
layout: provider
modified: '2026-08-26'
name: Qomplx
nav: Providers
network: true
overview: 'Qomplx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Identity Threat Detection, Managed Detection and Response, and Attack Surface Management.


  Qomplx''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Qomplx Plans Pricing
  plan_count: 0
  slug: qomplx-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Qomplx Rate Limits
  slug: qomplx-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 11.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qomplx/refs/heads/main/screenshots/qomplx-2026-09-02T152534.png
security:
- kind: authentication
  name: Qomplx Authentication
  slug: qomplx-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qomplx Domain Security
  slug: qomplx-domain-security
  summary_line: TLSv1.3
slug: qomplx
tags:
- Company
- Cybersecurity
- Identity Threat Detection
- Managed Detection and Response
- Attack Surface Management
- Time Series
- Analytics
- Risk Management
- Insurance
- Data Platform
website: https://www.qomplx.com/
---
