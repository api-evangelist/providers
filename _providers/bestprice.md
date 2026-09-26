---
access_model:
  confidence: medium
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Read-only shopping tools for product recommendations and shopping decisions, grouped-product search, current Greek merchant offers and delivered totals, and price history.
  name: BestPrice Shopping MCP
  slug: shopping-mcp
artifact_total: 16
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/hosts/bestprice-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestprice-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/packages/bestprice-packages.yml
  title: ''
  type: SDKs
  url: packages/bestprice-packages.yml
- group: company
  title: ''
  type: Website
  url: https://bestprice.gr
- group: commercial
  title: ''
  type: License
  url: https://github.com/TheBestCo/bestprice-mcp/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/security/bestprice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestprice-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/mcp/bestprice-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bestprice-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/mcp/bestprice-webmcp.yml
  title: ''
  type: WebMCP
  url: mcp/bestprice-webmcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/well-known/bestprice-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bestprice-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/well-known/bestprice-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bestprice-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/well-known/bestprice-ard.json
  title: ''
  type: APICatalog
  url: well-known/bestprice-ard.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/llms/bestprice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestprice-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/authentication/bestprice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bestprice-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/conformance/bestprice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bestprice-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/conventions/bestprice-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bestprice-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/errors/bestprice-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bestprice-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/lifecycle/bestprice-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bestprice-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/changelog/bestprice-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bestprice-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/plans/bestprice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bestprice-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/rate-limits/bestprice-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bestprice-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/packages/bestprice-packages.yml
  title: ''
  type: Packages
  url: packages/bestprice-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/components/bestprice-components.yml
  title: ''
  type: Components
  url: components/bestprice-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/data-model/bestprice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bestprice-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/security/bestprice-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bestprice-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/security/bestprice-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bestprice-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheBestCo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/TheBestCo/bestprice-mcp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bestprice.gr/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://www.bestprice.gr/mcp
- group: company
  title: ''
  type: Blog
  url: https://www.bestprice.gr/stories
- group: operate
  title: ''
  type: Support
  url: https://www.bestprice.gr/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bestprice.gr/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bestprice.gr/policies/privacy
created: '2026-08-27'
description: 'BestPrice.gr is Greece''s largest price-comparison marketplace, run by The Best Company S.A., covering roughly 25.7 million products from about 3,650 merchants and 42,000 manufacturers with hourly merchant-feed refreshes. Its developer surface is not a REST API but a public, keyless, read-only MCP server at https://mcp.bestprice.gr/mcp (server 1.8.1, MCP Registry id gr.bestprice/mcp), exposing four tools - get_shopping_decision (the BestPrice Shopping Brain: recommendations, need-based comparisons and read-only basket plans), search_products, compare_offers and get_price_history - whose JSON Schema 2020-12 input and output contracts are served live and anonymously. Alongside it BestPrice publishes a provider-authored Agent Skill, an APIs.json 0.23 index, an llms.txt, an RFC 9116 security.txt, an Agentic Resource Discovery manifest, an AI catalog, an MCP server card, a stdio bridge for hosts that cannot speak HTTP, and an experimental WebMCP manifest of 16 browser-tab tools.'
image: https://www.bestprice.gr/images/logo.svg
json_schemas:
- name: Bestprice Compare Offers Input
  property_count: 6
  slug: bestprice-compare-offers-input
- name: Bestprice Compare Offers Output
  property_count: 0
  slug: bestprice-compare-offers-output
- name: Bestprice Get Price History Input
  property_count: 2
  slug: bestprice-get-price-history-input
- name: Bestprice Get Price History Output
  property_count: 0
  slug: bestprice-get-price-history-output
- name: Bestprice Get Shopping Decision Input
  property_count: 4
  slug: bestprice-get-shopping-decision-input
- name: Bestprice Get Shopping Decision Output
  property_count: 0
  slug: bestprice-get-shopping-decision-output
- name: Bestprice Search Products Input
  property_count: 8
  slug: bestprice-search-products-input
- name: Bestprice Search Products Output
  property_count: 0
  slug: bestprice-search-products-output
layout: provider
mcp_servers:
- description: Read-only shopping decisions, product search, offers, and price history for Greece.
  name: BestPrice Shopping MCP (probed profile)
  slug: bestprice-shopping-mcp-probed-profile
- description: ''
  name: Production Streamable HTTP endpoint
  slug: production-streamable-http-endpoint
modified: '2026-09-25'
name: BestPrice Agent Commerce
nav: Providers
network: true
overview: 'BestPrice Agent Commerce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shopping, Price Comparison, E-Commerce, Retail, and MCP.


  BestPrice Agent Commerce''s developer surface includes authentication, changelog, documentation, engineering blog, support, and 28 more developer resources.'
plans:
- name: Bestprice Plans Pricing
  plan_count: 1
  slug: bestprice-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Bestprice Rate Limits
  slug: bestprice-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.0
    catalog_earned_first_party: 16.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.2
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 12.0
    developer_ergonomics: 66.1
    discoverability: 91.7
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/screenshots/bestprice-2026-09-02T144927.png
security:
- kind: authentication
  name: Bestprice Authentication
  slug: bestprice-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bestprice Domain Security
  slug: bestprice-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bestprice Vulnerability Disclosure
  slug: bestprice-vulnerability-disclosure
  summary_line: Hackerone
slug: bestprice
tags:
- Shopping
- Price Comparison
- E-Commerce
- Retail
- MCP
- WebMCP
- Agentic Commerce
- Greece
- Product Recommendations
- Shopping Decisions
- Delivered Price
website: https://bestprice.gr
---
