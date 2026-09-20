---
access_model:
  confidence: high
  label: Free and anonymous — the UCP/MCP commerce endpoint at ridefox.com needs no account or key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://ridefox.com/api/ucp/mcp'', ''status'': 200, ''note'': ''anonymous JSON-RPC tools/list returned 13 tools (probed 2026-09-14)''}'
  - '{''url'': ''https://www.foxfactory.com'', ''status'': 301, ''note'': ''declared website redirects to https://ridefox.com/ — the FOX brand storefront, which is where the API surface lives (probed 2026-09-14)''}'
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
- description: The FOX storefront's Universal Commerce Protocol service, transported over the Model Context Protocol at https://ridefox.com/api/ucp/mcp. Anonymous JSON-RPC; every tool call carries a UCP agent profil
  name: FOX Commerce API (UCP over MCP)
  slug: fox-factory-holding-api
artifact_total: 8
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/mcp/fox-factory-holding-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fox-factory-holding-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/well-known/fox-factory-holding-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fox-factory-holding-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/llms/fox-factory-holding-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fox-factory-holding-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/authentication/fox-factory-holding-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fox-factory-holding-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/scopes/fox-factory-holding-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fox-factory-holding-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/conventions/fox-factory-holding-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fox-factory-holding-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/conventions/fox-factory-holding-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fox-factory-holding-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/errors/fox-factory-holding-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fox-factory-holding-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/lifecycle/fox-factory-holding-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fox-factory-holding-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/conformance/fox-factory-holding-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fox-factory-holding-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/data-model/fox-factory-holding-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fox-factory-holding-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/packages/fox-factory-holding-packages.yml
  title: ''
  type: Packages
  url: packages/fox-factory-holding-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/rate-limits/fox-factory-holding-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fox-factory-holding-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/plans/fox-factory-holding-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fox-factory-holding-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/security/fox-factory-holding-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fox-factory-holding-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ridefox.com/agents.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ridefox
- group: company
  title: ''
  type: Blog
  url: https://ridefox.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://ridefox.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridefox.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridefox.com/policies/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foxfactory
- group: company
  title: ''
  type: Website
  url: https://ridefox.com
created: '2026-04-19'
description: 'Fox Factory Holding Corp. (NASDAQ: FOXF) designs and manufactures performance ride dynamics products — FOX suspension for mountain bikes, trucks and powersports vehicles, plus Race Face and Easton Cycling components, Method Race Wheels, Tensor Tire and Marucci Sports. It runs no developer program and publishes no OpenAPI, but its direct-to-consumer storefronts do expose a real, callable agent surface: ridefox.com serves a live Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP 2026-08-25) at https://ridefox.com/api/ucp/mcp, answering an anonymous tools/list with 13 tools for catalog search, product lookup, cart lifecycle, checkout lifecycle and order retrieval. The store also publishes llms.txt and agents.md agent instructions, a UCP merchant profile, and OpenID Connect / OAuth 2.0 discovery documents for customer accounts. The same surface is served by the Race Face, Easton Cycling and Method Race Wheels storefronts.'
finops:
- name: Fox Factory Holding Finops
  service_category: Manufacturing & Components
  slug: fox-factory-holding-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fox-factory-holding.png
layout: provider
mcp_servers:
- description: Fox Factory Holding's FOX storefront at ridefox.com serves a live, anonymous Model Context Protocol endpoint at https://ridefox.com/api/ucp/mcp implementing the Universal Commerce Protocol (UCP) shopp
  name: FOX Commerce MCP (UCP)
  slug: fox-commerce-mcp-ucp
modified: '2026-09-14'
name: Fox Factory Holding
nav: Providers
network: true
overview: 'Fox Factory Holding publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Suspension, Cycling, Power-Sports, Manufacturing, and E-Commerce.


  Fox Factory Holding''s developer surface includes authentication, documentation, engineering blog, support, and 20 more developer resources.'
plans:
- name: Fox Factory Holding Plans Pricing
  plan_count: 0
  slug: fox-factory-holding-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Fox Factory Holding Rate Limits
  slug: fox-factory-holding-rate-limits
scopes:
- name: Fox Factory Holding Scopes
  scope_count: 0
  slug: fox-factory-holding-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 23.7
  previous_composite: 30.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/screenshots/fox-factory-holding-2026-06-20T181504.png
security:
- kind: authentication
  name: Fox Factory Holding Authentication
  slug: fox-factory-holding-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Fox Factory Holding Domain Security
  slug: fox-factory-holding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fox-factory-holding
tags:
- Suspension
- Cycling
- Power-Sports
- Manufacturing
- E-Commerce
- MCP
- Agentic Commerce
website: https://ridefox.com
---
