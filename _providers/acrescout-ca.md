---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/acrescout-ca/plans/acrescout-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acrescout-ca-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/acrescout-ca/llms/acrescout-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acrescout-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/acrescout-ca/mcp/acrescout-ca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acrescout-ca-mcp.yml
- group: other
  href: https://artifacts.apis.io/acrescout-ca/hosts/acrescout-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acrescout-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/acrescout-ca/vendors/acrescout-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acrescout-ca-vendors.yml
- group: auth
  href: https://artifacts.apis.io/acrescout-ca/security/acrescout-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acrescout-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acrescout.ca/
- group: company
  title: ''
  type: About
  url: https://acrescout.ca/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acrescout.ca/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acrescout.ca/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://acrescout.ca/plans
coverage:
  checked: '2026-10-31'
  detail: No public API documentation or machine‑readable contract was found on the provider's site.
  evidence:
  - status: 404
    url: https://acrescout.ca/api
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: AcreScout is a Canadian land‑for‑sale platform that aggregates rural property listings across Canada, ranking them by price per acre, water frontage and value. Operated by Buretto Technologies Inc., the service provides data from public sources such as Kijiji, CREA, Centris and Zillow, and offers tools for filtering by region, size, price and amenities. It includes detailed information on taxes, approvals and ownership limits for Canadian citizens and residents, and supplies open‑data credits and licensing information.
image: https://acrescout.ca/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at acrescout.ca.
  name: AcreScout MCP Server
  slug: acrescout-ca-mcp-yml
modified: '2026-10-31'
name: AcreScout
nav: Providers
network: true
overview: 'AcreScout is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Canada, Land Listings, Data Aggregation, and Open Data.


  AcreScout''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Acrescout Ca Plans Pricing
  plan_count: 3
  slug: acrescout-ca-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 17.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acrescout Ca Domain Security
  slug: acrescout-ca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acrescout-ca
tags:
- Real Estate
- Canada
- Land Listings
- Data Aggregation
- Open Data
website: https://acrescout.ca/
---
