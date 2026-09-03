---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The WordPress REST API served by the Mobia Medical corporate site at https://www.mobia.com/wp-json/. It is the content-management API behind the marketing site — 320 routes across 22 namespaces includ
  name: Mobia Medical Site REST API (WordPress)
  slug: mobia-medical-site-rest-api-wordpress
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microtransponder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mobia.com/
- group: other
  title: ''
  type: ProductSite
  url: https://www.vivistim.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mobia.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://ir.mobia.com/news-events/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mobia.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mobia.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.mobia.com/compliance/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microtransponder
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microtransponder-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microtransponder-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microtransponder-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microtransponder-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microtransponder-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microtransponder-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microtransponder-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microtransponder-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/microtransponder-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/microtransponder-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/microtransponder-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/microtransponder-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microtransponder-llms.txt
created: '2026-08-25'
description: 'MicroTransponder, Inc. — renamed Mobia Medical, Inc. on 2026-02-24 — is a privately founded, Austin/Dallas Texas medical device company that develops the FDA-approved Vivistim Paired VNS System, an implantable vagus nerve stimulation device paired with rehabilitation therapy to reduce upper-extremity motor deficits in chronic ischemic stroke survivors. The company is a medical device manufacturer, not a software vendor: it publishes no developer portal, no product API, no SDKs and no public source repositories. The only machine-readable surface API Evangelist could reach on hosts the company controls is the WordPress REST API behind its corporate site (www.mobia.com) and its product site (www.vivistim.com), plus an OAuth-protected Model Context Protocol endpoint the corporate site serves via the WordPress MCP Adapter, with RFC 8414 and RFC 9728 discovery documents. This profile records that surface and nothing more.'
image: https://www.mobia.com/wp-content/uploads/2026/04/mobia-social-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: MicroTransponder MCP Server
  slug: microtransponder-mcp-server
modified: '2026-08-26'
name: MicroTransponder
nav: Providers
network: true
overview: 'MicroTransponder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Neurotechnology, and Neuromodulation.


  MicroTransponder''s developer surface includes support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Microtransponder Plans Pricing
  plan_count: 0
  slug: microtransponder-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Microtransponder Rate Limits
  slug: microtransponder-rate-limits
scopes:
- name: Microtransponder Scopes
  scope_count: 0
  slug: microtransponder-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microtransponder/refs/heads/main/screenshots/microtransponder-2026-09-02T150536.png
security:
- kind: authentication
  name: Microtransponder Authentication
  slug: microtransponder-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Microtransponder Domain Security
  slug: microtransponder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microtransponder
tags:
- Company
- Medical Devices
- Healthcare
- Neurotechnology
- Neuromodulation
- Stroke Rehabilitation
- Implantable Devices
- Life Sciences
- WordPress
- MCP
website: https://www.mobia.com/
---
