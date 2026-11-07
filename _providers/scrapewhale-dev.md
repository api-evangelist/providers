---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://scrapewhale.dev
  baseurl_source: declared
  description: 'Web data for marketing agents: traffic, ads, social profiles, and clean markdown from any URL or file.'
  name: ScrapeWhale API
  slug: scrapewhale-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/scrapewhale-dev/rate-limits/scrapewhale-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scrapewhale-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/scrapewhale-dev/plans/scrapewhale-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scrapewhale-dev-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/scrapewhale-dev/authentication/scrapewhale-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scrapewhale-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/scrapewhale-dev/errors/scrapewhale-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scrapewhale-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scrapewhale-dev/conformance/scrapewhale-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrapewhale-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scrapewhale-dev/llms/scrapewhale-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrapewhale-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/scrapewhale-dev/mcp/scrapewhale-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scrapewhale-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/scrapewhale-dev/well-known/scrapewhale-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scrapewhale-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/scrapewhale-dev/hosts/scrapewhale-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrapewhale-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/scrapewhale-dev/vendors/scrapewhale-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scrapewhale-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scrapewhale-dev/security/scrapewhale-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrapewhale-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrapewhale.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://scrapewhale.dev/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://scrapewhale.dev/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://scrapewhale.dev/docs/api
- group: operate
  title: ''
  type: Support
  url: https://scrapewhale.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://scrapewhale.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://scrapewhale.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://scrapewhale.dev/auth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrapewhale.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrapewhale.dev/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://scrapewhale.dev/openapi.json
  - status: 401
    url: https://scrapewhale.dev/mcp
  - status: 200
    url: https://scrapewhale.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: ScrapeWhale provides a web data API that enables marketing agents and developers to retrieve deep-dive information about any brand, including estimated traffic, advertising activity, social profiles, logos, and clean markdown representations of webpages. The service offers structured JSON responses optimized for AI agents, with free credits for new users and a transparent pricing model. It emphasizes public data only, no subscription lock‑ins, and refunds for failed calls.
image: https://scrapewhale.dev/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at scrapewhale.dev requiring an API key.
  name: scrapewhale-dev MCP Server
  slug: scrapewhale-dev-mcp-yml
modified: '2026-10-31'
name: scrapewhale-dev
nav: Providers
network: true
overview: 'scrapewhale-dev is listed with 1 API on the [APIs.io](https://apis.io/) network: ScrapeWhale API. Tagged areas include Data, Marketing, Web Scraping, and Artificial Intelligence.


  scrapewhale-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Scrapewhale Dev Plans Pricing
  plan_count: 4
  slug: scrapewhale-dev-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Scrapewhale Dev Rate Limits
  slug: scrapewhale-dev-rate-limits
scopes:
- name: Scrapewhale Dev Scopes
  scope_count: 0
  slug: scrapewhale-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 46.0
    catalog_earned_first_party: 12.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 30.5
    developer_ergonomics: 29.8
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 42.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scrapewhale-dev/scrapewhale-dev-2026-11-03T142832.png
security:
- kind: authentication
  name: Scrapewhale Dev Authentication
  slug: scrapewhale-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Scrapewhale Dev Domain Security
  slug: scrapewhale-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scrapewhale-dev
tags:
- Data
- Marketing
- Web Scraping
- Artificial Intelligence
website: https://scrapewhale.dev/
---
