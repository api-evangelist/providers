---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
  - '{''url'': ''https://www.potlatchdeltic.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.rayonier.com/ — a different registrable domain (potlatchdeltic.com -> rayonier.com), possible rename or acquisition (probed 2026-09-03, roadmap#169); CONFIRMED 2026-09-14 as the Rayonier merger of equals that closed 2026-01-30''}'
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/potlatch/plans/potlatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/potlatch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/potlatch/rate-limits/potlatch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/potlatch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/potlatch/finops/potlatch-finops.yml
  title: ''
  type: FinOps
  url: finops/potlatch-finops.yml
- group: auth
  href: https://artifacts.apis.io/potlatch/security/potlatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/potlatch-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/potlatchdeltic
- group: company
  title: ''
  type: Website
  url: https://www.potlatchdeltic.com
coverage:
  checked: '2026-09-14'
  detail: PotlatchDeltic was absorbed into Rayonier Inc. on 2026-01-30 in an $8.2B merger of equals and www.potlatchdeltic.com now answers a blanket HTTP 301 to www.rayonier.com on every path including /openapi.json, /apis.json, /llms.txt and every /.well-known/ path, while the two developer hosts an earlier pass recorded — api.potlatchdeltic.com and developer.potlatchdeltic.com — are NXDOMAIN and the four surviving legacy subdomains are human login portals that 404 every discovery path.
  evidence:
  - status: 301
    url: https://www.potlatchdeltic.com/
  - status: 301
    url: https://www.potlatchdeltic.com/openapi.json
  - status: 301
    url: https://www.potlatchdeltic.com/.well-known/agent-card.json
  - status: 0
    url: https://api.potlatchdeltic.com
  - status: 0
    url: https://developer.potlatchdeltic.com/docs
  - status: 404
    url: https://supplier.potlatchdeltic.com/openapi.json
  - status: 404
    url: https://customer.potlatchdeltic.com/.well-known/security.txt
  - status: 404
    url: https://rlms.potlatchdeltic.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/potlatchdeltic
  reason: defunct
  state: none
created: '2026-04-19'
description: 'PotlatchDeltic Corporation was a Spokane, Washington timberland real estate investment trust and diversified wood products manufacturer, formed in 2018 when Potlatch Corporation — a company whose roots reach back to the 1903 Potlatch Lumber Company in Idaho — merged with Deltic Timber Corporation of Arkansas. At the time of its own merger it owned roughly 2.2 million acres of timberland across Alabama, Arkansas, Georgia, Idaho, Louisiana, Minnesota, Mississippi and South Carolina, ran six sawmills and an industrial-grade plywood mill, and operated a rural land sales program and residential and commercial real estate development business in central Arkansas. It traded on Nasdaq as PCH. PotlatchDeltic ceased to exist as an independent company on 30 January 2026, when its $8.2 billion all-stock merger of equals with Rayonier Inc. closed; the combined company retained the Rayonier name and the NYSE ticker RYN and holds over four million acres of US timberland. PotlatchDeltic never
  operated a public developer program: no developer portal, API reference, SDK, package, GitHub organization or machine-readable specification of any kind was ever published. Its integration surface was, and for the surviving legacy portals still is, a set of human login pages for log-and-fiber suppliers, customers and recreational lease holders. The corporate site now redirects wholesale to rayonier.com, so there is no live API surface to catalog. This profile is retained as a historical record; the live entity is catalogued at all/rayonier.'
finops:
- has_sources: true
  method: generated
  name: Potlatch Finops
  primary_unit: ''
  service_category: Materials
  slug: potlatch-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/potlatch.png
layout: provider
modified: '2026-09-14'
name: PotlatchDeltic
nav: Providers
network: true
overview: PotlatchDeltic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Timber, Real Estate, Wood Products, Forest Products, and REIT.
plans:
- name: Potlatch Plans Pricing
  plan_count: 1
  slug: potlatch-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Potlatch Rate Limits
  slug: potlatch-rate-limits
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 5.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/potlatch/potlatch-2026-06-20T192021.png
security:
- kind: domain-security
  name: Potlatch Domain Security
  slug: potlatch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: potlatch
tags:
- Timber
- Real Estate
- Wood Products
- Forest Products
- REIT
- Lumber
- Land Management
- Manufacturing
- Company
- Absorbed
website: https://www.potlatchdeltic.com
---
