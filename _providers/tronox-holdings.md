---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: An authenticated Model Context Protocol (MCP) endpoint served from Tronox's own corporate WordPress host, found by probe on 2026-09-17 rather than by documentation. Anonymous discovery works end to en
  name: Tronox MCP Server (WordPress MCP Adapter)
  slug: tronox-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.tronox.com
- group: company
  title: ''
  type: Blog
  url: https://www.tronox.com/news-media/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tronox.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tronox
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCiMqXZqm5vTUCmqDmP4Hqog
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.tronox.com/
- group: company
  title: ''
  type: Careers
  url: https://www.tronox.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.tronox.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tronox.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tronox.com/terms-of-use/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/security/tronox-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tronox-holdings-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/well-known/tronox-holdings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tronox-holdings-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/mcp/tronox-holdings-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tronox-holdings-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/authentication/tronox-holdings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tronox-holdings-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/scopes/tronox-holdings-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tronox-holdings-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/conformance/tronox-holdings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tronox-holdings-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/errors/tronox-holdings-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tronox-holdings-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/llms/tronox-holdings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tronox-holdings-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/plans/tronox-holdings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tronox-holdings-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/rate-limits/tronox-holdings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tronox-holdings-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/finops/tronox-holdings-finops.yml
  title: ''
  type: FinOps
  url: finops/tronox-holdings-finops.yml
created: '2026-04-19'
description: Tronox Holdings plc is a vertically integrated producer of titanium dioxide (TiO2) pigment, mineral sands (titanium feedstock and zircon) and titanium chemicals, a Fortune 1000 chemicals and mining company operating mines and plants on three continents. It runs no developer program and publishes no product API, SDK or machine-readable contract; supplier transactions run on the third-party Coupa Supplier Portal and customer supply is contracted directly. The one protocol surface on a Tronox host is an OAuth-gated MCP endpoint served by the WordPress MCP Adapter on the corporate site, recorded here as a probed platform surface rather than a Tronox business API.
finops:
- name: Tronox Holdings Finops
  service_category: Chemicals & Materials
  slug: tronox-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tronox-holdings.png
layout: provider
mcp_servers:
- description: ''
  name: Tronox MCP Server (WordPress MCP Adapter)
  slug: tronox-mcp-server-wordpress-mcp-adapter
modified: '2026-09-17'
name: Tronox Holdings
nav: Providers
network: true
overview: 'Tronox Holdings publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Titanium Dioxide, Chemicals, Mining, Mineral Sands, and Zircon.


  Tronox Holdings'' developer surface includes engineering blog, YouTube channel, authentication, and 18 more developer resources.'
plans:
- name: Tronox Holdings Plans Pricing
  plan_count: 1
  slug: tronox-holdings-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Tronox Holdings Rate Limits
  slug: tronox-holdings-rate-limits
scopes:
- name: Tronox Holdings Scopes
  scope_count: 0
  slug: tronox-holdings-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    operational_transparency: 21.1
  previous_composite: 11.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/tronox-holdings/refs/heads/main/screenshots/tronox-holdings-2026-06-20T195742.png
security:
- kind: authentication
  name: Tronox Holdings Authentication
  slug: tronox-holdings-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tronox Holdings Domain Security
  slug: tronox-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tronox-holdings
tags:
- Titanium Dioxide
- Chemicals
- Mining
- Mineral Sands
- Zircon
- Pigments
- Manufacturing
website: https://www.tronox.com
---
