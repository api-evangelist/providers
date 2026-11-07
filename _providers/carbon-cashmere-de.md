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
api_count: 1
apis:
- description: Provides market regime analysis, funding classification and real‑time market data via a private MCP endpoint.
  name: Carbon & Cashmere API
  slug: carbon-cashmere-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/carbon-cashmere-de/plans/carbon-cashmere-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carbon-cashmere-de-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/carbon-cashmere-de/mcp/carbon-cashmere-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carbon-cashmere-de-mcp.yml
- group: agent
  href: https://artifacts.apis.io/carbon-cashmere-de/well-known/carbon-cashmere-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carbon-cashmere-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/carbon-cashmere-de/hosts/carbon-cashmere-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbon-cashmere-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/carbon-cashmere-de/vendors/carbon-cashmere-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbon-cashmere-de-vendors.yml
- group: build
  href: https://artifacts.apis.io/carbon-cashmere-de/packages/carbon-cashmere-de-packages.yml
  title: ''
  type: SDKs
  url: packages/carbon-cashmere-de-packages.yml
- group: build
  href: https://artifacts.apis.io/carbon-cashmere-de/packages/carbon-cashmere-de-packages.yml
  title: ''
  type: Packages
  url: packages/carbon-cashmere-de-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.carbon-cashmere.de/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.carbon-cashmere.de/blog
- group: auth
  href: https://artifacts.apis.io/carbon-cashmere-de/security/carbon-cashmere-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbon-cashmere-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbon-cashmere.de/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.carbon-cashmere.de/openopenapi.json
  - status: 404
    url: https://api.carbon-cashmere.de/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Carbon & Cashmere is a German-language crypto community and data service offering on‑chain market regime analysis, funding classification and real‑time market data without hype or investment advice. The platform provides transparent, subscription‑based access to market metrics, charts and community insights, emphasizing substance over speculation.
image: https://www.carbon-cashmere.de/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.carbon-cashmere.de.
  name: Carbon & Cashmere MCP Server
  slug: carbon-cashmere-de-mcp-yml
modified: '2026-11-03'
name: Carbon & Cashmere
nav: Providers
network: true
overview: 'Carbon & Cashmere is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Community, Data, and German.


  Carbon & Cashmere''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Carbon Cashmere De Plans Pricing
  plan_count: 5
  slug: carbon-cashmere-de-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbon Cashmere De Domain Security
  slug: carbon-cashmere-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-cashmere-de
tags:
- Company
- Cryptocurrency
- Community
- Data
- German
website: https://carbon-cashmere.de/
---
