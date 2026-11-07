---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    agent_skills: derived
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
  score: 22.8
  scored_at: '2026-11-06'
api_count: 9
apis:
- description: 'A live Model Context Protocol server served from www.aerofarms.com at /wp-json/mcp/mcp-oauth-server. It answers JSON-RPC over HTTP and is protected by OAuth 2.1: an anonymous tools/list returns HTTP 4'
  name: AeroFarms MCP Server
  slug: aerofarms-mcp-server
- description: 'The public WordPress REST API (wp-json) of the AeroFarms website at www.aerofarms.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate A'
  name: AeroFarms Website (WordPress REST)
  slug: aerofarms-com-website-wordpress-rest
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.aerofarms.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aerofarms.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.aerofarms.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerofarms.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerofarms.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AeroFarms
- group: agent
  href: https://artifacts.apis.io/aerofarms/llms/aerofarms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerofarms-llms.txt
- group: agent
  href: https://artifacts.apis.io/aerofarms/well-known/aerofarms-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aerofarms-well-known.yml
- group: agent
  href: https://artifacts.apis.io/aerofarms/mcp/aerofarms-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aerofarms-mcp.yml
- group: build
  href: https://artifacts.apis.io/aerofarms/mcp/aerofarms-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aerofarms-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/aerofarms/authentication/aerofarms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aerofarms-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aerofarms/scopes/aerofarms-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aerofarms-scopes.yml
- group: design
  href: https://artifacts.apis.io/aerofarms/conformance/aerofarms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aerofarms-conformance.yml
- group: design
  href: https://artifacts.apis.io/aerofarms/conventions/aerofarms-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aerofarms-conventions.yml
- group: design
  href: https://artifacts.apis.io/aerofarms/errors/aerofarms-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aerofarms-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aerofarms/lifecycle/aerofarms-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aerofarms-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aerofarms/data-model/aerofarms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aerofarms-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/aerofarms/plans/aerofarms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aerofarms-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aerofarms/rate-limits/aerofarms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aerofarms-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/aerofarms/security/aerofarms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerofarms-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/aerofarms/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-10'
description: 'AeroFarms is an indoor vertical farming company founded in 2004 and headquartered in Newark, New Jersey, where it grows leafy greens and nutrient-dense microgreens — micro broccoli, micro arugula, micro wasabi mustard and the FlavorSpectrum blends — aeroponically, without sun or soil, under LED light recipes driven by its proprietary agSTACK PLC/SCADA control stack. It sells through US grocery retail rather than through software, is a Certified B Corporation, and was acquired by an affiliate of Palm Ventures in June 2026. AeroFarms is a produce grower, not a software vendor: no developer portal, no API documentation, no SDKs, no API product. The machine-readable surface profiled here is the anonymous, read-only WordPress and WooCommerce REST API behind www.aerofarms.com, a live OAuth-protected MCP server at /wp-json/mcp/mcp-oauth-server, and a published llms.txt.'
image: https://www.aerofarms.com/wp-content/uploads/2021/04/cropped-AF-Favicon-copy.png
layout: provider
mcp_servers:
- description: 'AeroFarms serves a live, reachable Model Context Protocol server from its own website host. This is not a candidate derived from OpenAPI operations: the endpoint exists, answers JSON-RPC, and defends '
  name: AeroFarms MCP Server
  slug: mcp-oauth-server
modified: '2026-09-10'
name: AeroFarms
nav: Providers
network: true
overview: 'AeroFarms publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Vertical Farming, Indoor Farming, and AgTech.


  AeroFarms'' developer surface includes engineering blog, support, authentication, and 18 more developer resources.'
plans:
- name: Aerofarms Plans Pricing
  plan_count: 0
  slug: aerofarms-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Aerofarms Rate Limits
  slug: aerofarms-rate-limits
scopes:
- name: Aerofarms Scopes
  scope_count: 1
  slug: aerofarms-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 71.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.9
  provenance:
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/aerofarms/aerofarms-2026-10-11T092929.png
security:
- kind: authentication
  name: Aerofarms Authentication
  slug: aerofarms-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aerofarms Domain Security
  slug: aerofarms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: aerofarms-answer-from-published-content
  slug: aerofarms-answer-from-published-content
- name: aerofarms-read-product-catalog
  slug: aerofarms-read-product-catalog
- name: aerofarms-track-news
  slug: aerofarms-track-news
slug: aerofarms
tags:
- Company
- Agriculture
- Vertical Farming
- Indoor Farming
- AgTech
- Food and Beverage
- Consumer Packaged Goods
- Microgreens
- Sustainability
- Content
- Commerce
- MCP
website: https://www.aerofarms.com/
---
