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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Aegis Marine Shipmanagement website at aegisships.com: the route index of the site''s content management system, catalogued as one site surface rather tha'
  name: Aegis Marine Shipmanagement Website (WordPress REST)
  slug: aegisships-com-website-wordpress-rest
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://aegisships.com/
- group: company
  title: ''
  type: About
  url: https://aegisships.com/about/
- group: other
  title: ''
  type: Services
  url: https://aegisships.com/services/
- group: company
  title: ''
  type: Newsroom
  url: https://aegisships.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://aegisships.com/contact/
- group: company
  title: ''
  type: Partners
  url: https://aegisships.com/affiliate/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aegisships.com/privacy-policy-2/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aegisships.com/disclaimer/
- group: auth
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/authentication/aegis-marine-shipmanagement-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aegis-marine-shipmanagement-authentication.yml
- group: design
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/errors/aegis-marine-shipmanagement-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aegis-marine-shipmanagement-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/conventions/aegis-marine-shipmanagement-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aegis-marine-shipmanagement-conventions.yml
- group: design
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/data-model/aegis-marine-shipmanagement-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aegis-marine-shipmanagement-data-model.yml
- group: design
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/conformance/aegis-marine-shipmanagement-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aegis-marine-shipmanagement-conformance.yml
- group: design
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/lifecycle/aegis-marine-shipmanagement-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aegis-marine-shipmanagement-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/rate-limits/aegis-marine-shipmanagement-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aegis-marine-shipmanagement-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/plans/aegis-marine-shipmanagement-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aegis-marine-shipmanagement-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/packages/aegis-marine-shipmanagement-packages.yml
  title: ''
  type: Packages
  url: packages/aegis-marine-shipmanagement-packages.yml
- group: build
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/examples/aegis-marine-shipmanagement-examples.yml
  title: ''
  type: Examples
  url: examples/aegis-marine-shipmanagement-examples.yml
- group: agent
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/llms/aegis-marine-shipmanagement-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aegis-marine-shipmanagement-llms.txt
- group: agent
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/mcp/aegis-marine-shipmanagement-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aegis-marine-shipmanagement-mcp.yml
- group: build
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/mcp/aegis-marine-shipmanagement-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aegis-marine-shipmanagement-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aegis-marine-shipmanagement/security/aegis-marine-shipmanagement-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aegis-marine-shipmanagement-domain-security.yml
coverage:
  checked: '2026-09-09'
  detail: Aegis Marine Shipmanagement is a Georgetown, Guyana ship manager whose product is crude oil and LNG vessel operation under commercial contract, not software; every artifact in this repo was derived by API Evangelist from the WordPress core REST API behind its 2019-era marketing site, because the company itself publishes no OpenAPI, developer portal, SDK, changelog, status page or /.well-known/ document on any host.
  evidence:
  - status: 200
    url: https://aegisships.com/wp-json/
  - status: 404
    url: https://aegisships.com/openapi.json
  - status: 404
    url: https://aegisships.com/llms.txt
  - status: 404
    url: https://aegisships.com/.well-known/agent-card.json
  - status: 404
    url: https://aegisships.com/.well-known/security.txt
  - status: 200
    url: https://aegisships.com/wp-json/wp/v2/posts?per_page=1
  reason: not-a-software-company
  state: none
created: '2026-09-09'
description: 'Aegis Marine Shipmanagement Inc. is a privately owned marine vessel transportation and ship management company headquartered at 215 South Road and King Street, Lacytown, Georgetown, Guyana, with a secondary office in Brooklyn, New York. Founded in 2018 by Guyanese-American businessman Sean Clarke, it serves the oil and gas sector, operating crude oil tankers, liquefied natural gas tankers and offshore support service vessels on behalf of third-party owners, partners and investors. Its services span commercial, technical, safety and quality, and logistics ship management, delivered through partnerships with established marine service providers, and include vessel registration under various flags, technical inspection and marine engine spares, marine vessel chartering, commodity trader engagement, and crew management covering recruitment, familiarization, training, retention and career promotion. Aegis Marine Shipmanagement is a shipping operator rather than a software vendor.
  It publishes no developer portal, no API documentation, no SDKs and no commercial or partner-facing product API. The only machine-readable interface it exposes is the WordPress core REST content API behind its corporate website at aegisships.com, which is captured here for discovery purposes: it is anonymously readable, effectively read-only, and serves the marketing site''s own pages, media and taxonomy rather than any fleet, chartering or vessel-operations data.'
image: https://aegisships.com/wp-content/uploads/2018/11/cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: MCP server; 10 tools listed. A candidate, not confirmed as published by the provider.
  name: Aegis Marine Shipmanagement MCP Server
  slug: aegis-marine-shipmanagement-mcp-yml
modified: '2026-09-09'
name: Aegis Marine Shipmanagement
nav: Providers
network: true
overview: 'Aegis Marine Shipmanagement publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Ship Management, Maritime, and Marine Transportation.


  Aegis Marine Shipmanagement''s developer surface includes authentication, code examples, and 21 more developer resources.'
plans:
- name: Aegis Marine Shipmanagement Plans Pricing
  plan_count: 0
  slug: aegis-marine-shipmanagement-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Aegis Marine Shipmanagement Rate Limits
  slug: aegis-marine-shipmanagement-rate-limits
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 18.5
    discoverability: 65.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - guyana
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 20.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/aegis-marine-shipmanagement/aegis-marine-shipmanagement-2026-10-11T092913.png
security:
- kind: authentication
  name: Aegis Marine Shipmanagement Authentication
  slug: aegis-marine-shipmanagement-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aegis Marine Shipmanagement Domain Security
  slug: aegis-marine-shipmanagement-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: browse-aegis-media-library
  slug: aegis-marine-shipmanagement-browse-media-library
- name: inspect-aegis-api-surface
  slug: aegis-marine-shipmanagement-inspect-surface
- name: read-aegis-company-profile
  slug: aegis-marine-shipmanagement-read-company-profile
slug: aegis-marine-shipmanagement
tags:
- Company
- Shipping
- Ship Management
- Maritime
- Marine Transportation
- Oil and Gas
- Crude Oil Tankers
- LNG
- Offshore
- Chartering
- Crew Management
- Logistics
- Guyana
website: https://aegisships.com/
---
