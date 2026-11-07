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
    dynamic_client_registration: true
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
  score: 26.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Reed Semiconductor website at www.reedsemi.com: the route index of the site''s content management system, catalogued as one site surface rather than as se'
  name: Reed Semiconductor Website (WordPress REST)
  slug: reedsemi-com-website-wordpress-rest
- description: A Model Context Protocol server mounted at the Reed Semiconductor apex domain by the Novamira WordPress plugin (v1.11.4). It advertises itself through RFC 9728 protected-resource metadata and RFC 8414
  name: Reed Semiconductor MCP Server
  slug: reed-semiconductor-mcp
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/reed-semiconductor/security/reed-semiconductor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reed-semiconductor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reedsemi.com/
- group: company
  title: ''
  type: Blog
  url: https://www.reedsemi.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.reedsemi.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.reedsemi.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.reedsemi.com/my-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reedsemi.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reedsemi.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reed-semiconductor-corp
- group: agent
  href: https://artifacts.apis.io/reed-semiconductor/well-known/reed-semiconductor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reed-semiconductor-well-known.yml
- group: agent
  href: https://artifacts.apis.io/reed-semiconductor/mcp/reed-semiconductor-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reed-semiconductor-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reed-semiconductor/llms/reed-semiconductor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reed-semiconductor-llms.txt
- group: auth
  href: https://artifacts.apis.io/reed-semiconductor/authentication/reed-semiconductor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reed-semiconductor-authentication.yml
- group: auth
  href: https://artifacts.apis.io/reed-semiconductor/scopes/reed-semiconductor-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/reed-semiconductor-scopes.yml
- group: design
  href: https://artifacts.apis.io/reed-semiconductor/conventions/reed-semiconductor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reed-semiconductor-conventions.yml
- group: design
  href: https://artifacts.apis.io/reed-semiconductor/errors/reed-semiconductor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reed-semiconductor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reed-semiconductor/data-model/reed-semiconductor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reed-semiconductor-data-model.yml
- group: design
  href: https://artifacts.apis.io/reed-semiconductor/lifecycle/reed-semiconductor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reed-semiconductor-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reed-semiconductor/conformance/reed-semiconductor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reed-semiconductor-conformance.yml
- group: auth
  href: https://artifacts.apis.io/reed-semiconductor/conformance/reed-semiconductor-conformance.yml
  title: ''
  type: Compliance
  url: conformance/reed-semiconductor-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/reed-semiconductor/plans/reed-semiconductor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reed-semiconductor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/reed-semiconductor/rate-limits/reed-semiconductor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reed-semiconductor-rate-limits.yml
created: '2026-08-26'
description: 'Reed Semiconductor Corp. is a fabless power-management semiconductor company founded in 2019 and headquartered in Rhode Island, USA, with offices in Taipei, Shenzhen and Bengaluru. The name stands for Robust, Efficient, Eco-friendly and Dense power solutions. It designs multiphase DC-DC controllers, smart power stages, half-bridge power stages, point-of-load converters, power modules, intermediate bus converters, eFuses and power multiplexers for data center and AI/HPC accelerators, 48V and 12V distribution, communication and datacom equipment, automotive ADAS and infotainment, industrial systems and personal electronics. Reed does not operate a developer program, but its WordPress/WooCommerce corporate site exposes real machine-readable surfaces: an anonymous WooCommerce Store API serving the 99-part parametric product catalog across 81 application and technology categories, the WordPress content API, and an OAuth 2.1 protected Model Context Protocol server published through
  RFC 8414 and RFC 9728 metadata at the apex domain.'
image: https://cdn.reedsemi.com/2024/09/reedsemi-og-logo.png
layout: provider
mcp_servers:
- description: 'Reed Semiconductor''s corporate WordPress site mounts a Model Context Protocol server at the apex domain. It is real, reachable and OAuth-gated: an anonymous JSON-RPC tools/list returns HTTP 401 with a'
  name: Reed Semiconductor MCP Server
  slug: reed-semiconductor-mcp-server
modified: '2026-08-26'
name: Reed Semiconductor
nav: Providers
network: true
overview: 'Reed Semiconductor is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Power Management, Electronic Components, and Data Center.


  Reed Semiconductor''s developer surface includes engineering blog, support, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Reed Semiconductor Plans Pricing
  plan_count: 0
  slug: reed-semiconductor-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Reed Semiconductor Rate Limits
  slug: reed-semiconductor-rate-limits
scopes:
- name: Reed Semiconductor Scopes
  scope_count: 1
  slug: reed-semiconductor-scopes
  summary_line: 1 scope · authorization_code/refresh_token/device_code
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.7
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 60.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.6
  provenance:
    conformance: first-party
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 36.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reed-semiconductor/reed-semiconductor-2026-09-02T153214.png
security:
- kind: authentication
  name: Reed Semiconductor Authentication
  slug: reed-semiconductor-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Reed Semiconductor Domain Security
  slug: reed-semiconductor-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: reed-semiconductor
tags:
- Company
- Semiconductors
- Power Management
- Electronic Components
- Data Center
- Artificial Intelligence
- Automotive
- Hardware
- Manufacturing
- Product Catalog
website: https://www.reedsemi.com/
---
