---
access_model:
  confidence: medium
  label: Open discovery, gated execution — tools/list is anonymous, tools/call needs an agent profile and a JWT
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://hearthnhome.com/api/ucp/mcp'', ''status'': 200, ''note'': ''JSON-RPC tools/list returned all 13 tools with full inputSchemas and no Authorization header; tools/call on the same endpoint returned -32000 AuthenticationRequired (a Shopify agent JWT) and -32001 invalid_profile_url (a fetchable meta.ucp-agent.profile URI) — discovery is open, execution is gated (probed 2026-09-13)''}'
  - '{''url'': ''https://www.hni.com'', ''status'': 301, ''note'': ''the previously recorded website hni.com 301s to acrisure.com/midwest — that is HNI Risk Services / Acrisure Midwest, a DIFFERENT company; HNI Corporation is www.hnicorp.com (probed 2026-09-13, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: The Hearth & Home Technologies storefront implements the Universal Commerce Protocol (UCP) over an anonymous Model Context Protocol endpoint. A tools/list probe on 2026-09-13 returned 13 tools — searc
  name: Hearth & Home Technologies Agent Commerce (UCP/MCP)
  slug: hearth-home-agent-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.hnicorp.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hni-corporation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hnicorp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hnicorp.com/terms-of-use
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/security/hni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hni-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/well-known/hni-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hni-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/llms/hni-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hni-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/conformance/hni-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hni-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/authentication/hni-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hni-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/scopes/hni-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hni-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/conventions/hni-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hni-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/conventions/hni-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hni-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/lifecycle/hni-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hni-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/rate-limits/hni-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hni-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/plans/hni-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hni-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/packages/hni-packages.yml
  title: ''
  type: Packages
  url: packages/hni-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/errors/hni-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hni-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/data-model/hni-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hni-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/mcp/hni-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hni-mcp.yml
created: '2026-04-28'
description: 'HNI Corporation (NYSE: HNI) is a manufacturer founded in 1944 and headquartered in Muscatine, Iowa, built around two operating segments. Workplace Furnishings makes office seating, desks, storage, tables, panel systems and ancillary furnishings sold through independent dealers under the HON, Allsteel, Gunlocke, HBF and Kimball International brands. Residential Building Products is the hearth business, operated by Hearth & Home Technologies under the Heatilator, Heat & Glo, Majestic, Monessen, Quadra-Fire, Harman, SimpliFire and PelPro brands. HNI publishes no developer portal, REST API or OpenAPI for either segment. Its one public machine-readable surface is the agent-commerce stack on the Hearth & Home Technologies storefront at hearthnhome.com, which serves an llms.txt, a Universal Commerce Protocol merchant profile and an anonymous MCP endpoint exposing 13 catalog, cart and checkout tools.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hni.png
layout: provider
mcp_servers:
- description: ''
  name: Hearth & Home Technologies Agent Commerce MCP Server
  slug: hearth-home-technologies-agent-commerce-mcp-server
modified: '2026-09-13'
name: HNI Corporation
nav: Providers
network: true
overview: 'HNI Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Manufacturing, Office Furniture, Workplace, and Building Products.


  HNI Corporation''s developer surface includes authentication and 19 more developer resources.'
plans:
- name: Hni Plans Pricing
  plan_count: 0
  slug: hni-plans-pricing
press:
- date: ''
  title: The companies have closed on the acquisition deal, HNI ...
  url: https://www.facebook.com/woodtv/posts/the-companies-have-closed-on-the-acquisition-deal-hni-announced-today/1362395972586911/
- date: ''
  title: HNI signals fifth year of double-digit EPS growth with $120 ...
  url: https://seekingalpha.com/news/4557045-hni-signals-fifth-year-of-double-digit-eps-growth-with-120m-synergy-target-following
- date: ''
  title: HNI Corporation
  url: https://www.hnicorp.com/
- date: ''
  title: HNI to purchase Steelcase Inc., HNI's headquarters ...
  url: https://www.kwqc.com/2025/08/04/hni-purchase-steelcase-inc-hnis-headquarters-remain-muscatine/
- date: ''
  title: HNI) 2026 proxy details Steelcase deal, pay and ESG
  url: https://www.stocktitan.net/sec-filings/HNI/def-14a-hni-corp-definitive-proxy-statement-3603a98d9fc3.html
random_paper: 11
rate_limits:
- limit_count: 0
  name: Hni Rate Limits
  slug: hni-rate-limits
scopes:
- name: Hni Scopes
  scope_count: 0
  slug: hni-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hni/refs/heads/main/screenshots/hni-2026-06-20T182807.png
security:
- kind: authentication
  name: Hni Authentication
  slug: hni-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Hni Domain Security
  slug: hni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hni
tags:
- Fortune 1000
- Manufacturing
- Office Furniture
- Workplace
- Building Products
- Hearth
- Retail
- E-Commerce
- Agentic Commerce
- MCP
website: https://www.hnicorp.com
---
