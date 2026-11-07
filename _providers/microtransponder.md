---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the MicroTransponder website at www.mobia.com: the route index of the site''s content management system, catalogued as one site surface rather than as separat'
  name: MicroTransponder Website (WordPress REST)
  slug: mobia-com-website-wordpress-rest
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/microtransponder/security/microtransponder-domain-security.yml
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
  href: https://artifacts.apis.io/microtransponder/well-known/microtransponder-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microtransponder-well-known.yml
- group: agent
  href: https://artifacts.apis.io/microtransponder/mcp/microtransponder-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microtransponder-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microtransponder/authentication/microtransponder-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microtransponder-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microtransponder/scopes/microtransponder-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microtransponder-scopes.yml
- group: design
  href: https://artifacts.apis.io/microtransponder/errors/microtransponder-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microtransponder-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microtransponder/conventions/microtransponder-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microtransponder-conventions.yml
- group: design
  href: https://artifacts.apis.io/microtransponder/data-model/microtransponder-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microtransponder-data-model.yml
- group: design
  href: https://artifacts.apis.io/microtransponder/lifecycle/microtransponder-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microtransponder-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microtransponder/conformance/microtransponder-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microtransponder-conformance.yml
- group: operate
  href: https://artifacts.apis.io/microtransponder/rate-limits/microtransponder-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microtransponder-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microtransponder/plans/microtransponder-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microtransponder-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/microtransponder/packages/microtransponder-packages.yml
  title: ''
  type: Packages
  url: packages/microtransponder-packages.yml
- group: agent
  href: https://artifacts.apis.io/microtransponder/llms/microtransponder-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microtransponder-llms.txt
created: '2026-08-25'
description: 'MicroTransponder, Inc. — renamed Mobia Medical, Inc. on 2026-02-24 — is a privately founded, Austin/Dallas Texas medical device company that develops the FDA-approved Vivistim Paired VNS System, an implantable vagus nerve stimulation device paired with rehabilitation therapy to reduce upper-extremity motor deficits in chronic ischemic stroke survivors. The company is a medical device manufacturer, not a software vendor: it publishes no developer portal, no product API, no SDKs and no public source repositories. The only machine-readable surface API Evangelist could reach on hosts the company controls is the WordPress REST API behind its corporate site (www.mobia.com) and its product site (www.vivistim.com), plus an OAuth-protected Model Context Protocol endpoint the corporate site serves via the WordPress MCP Adapter, with RFC 8414 and RFC 9728 discovery documents. This profile records that surface and nothing more.'
image: https://www.mobia.com/wp-content/uploads/2026/04/mobia-social-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.mobia.com over HTTP requiring OAuth.
  name: MicroTransponder MCP Server
  slug: mcp-oauth-server
modified: '2026-08-26'
name: MicroTransponder
nav: Providers
network: true
overview: 'MicroTransponder is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Neurotechnology, and Neuromodulation.


  MicroTransponder''s developer surface includes support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Microtransponder Plans Pricing
  plan_count: 0
  slug: microtransponder-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Microtransponder Rate Limits
  slug: microtransponder-rate-limits
scopes:
- name: Microtransponder Scopes
  scope_count: 1
  slug: microtransponder-scopes
  summary_line: 1 scope · authorization_code
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 60.0
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    conformance: first-party
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microtransponder/microtransponder-2026-09-02T150536.png
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
