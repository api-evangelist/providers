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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Read-only shopping tools for finding grouped products, comparing current merchant offers and delivered totals, and checking price history.
  name: BestPrice Shopping MCP
  slug: shopping-mcp
artifact_total: 14
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/TheBestCo/bestprice-mcp/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bestprice-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bestprice-mcp.yml
- group: agent
  title: ''
  type: WebMCP
  url: mcp/bestprice-webmcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bestprice-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bestprice-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/bestprice-ard.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bestprice-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bestprice-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bestprice-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bestprice-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bestprice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bestprice-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bestprice-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bestprice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bestprice-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/bestprice-packages.yml
- group: design
  title: ''
  type: Components
  url: components/bestprice-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bestprice-data-model.yml
- group: auth
  title: ''
  type: Security
  url: security/bestprice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bestprice-vulnerability-disclosure.yml
- group: agent
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
description: BestPrice.gr is Greece's largest price-comparison marketplace, run by The Best Company S.A., covering roughly 25.7 million products from about 3,650 merchants and 42,000 manufacturers with hourly merchant-feed refreshes. Its developer surface is not a REST API but a public, keyless, read-only MCP server at https://mcp.bestprice.gr/mcp, exposing three tools - search_products, compare_offers and get_price_history - whose JSON Schema 2020-12 input and output contracts are served live and anonymously. Alongside it BestPrice publishes an APIs.json 0.23 index, an llms.txt, an RFC 9116 security.txt, an Agentic Resource Discovery manifest and an experimental WebMCP manifest of 13 browser-tab tools.
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
- name: Bestprice Search Products Input
  property_count: 8
  slug: bestprice-search-products-input
- name: Bestprice Search Products Output
  property_count: 0
  slug: bestprice-search-products-output
layout: provider
mcp_servers:
- description: ''
  name: Production Streamable HTTP endpoint
  slug: production-streamable-http-endpoint
- description: ''
  name: Probed MCP server profile (tools, schemas, deployment)
  slug: probed-mcp-server-profile-tools-schemas-deployment
modified: '2026-08-27'
name: BestPrice Agent Commerce
nav: Providers
network: true
overview: 'BestPrice Agent Commerce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shopping, Price Comparison, E-Commerce, Retail, and MCP.


  BestPrice Agent Commerce''s developer surface includes authentication, changelog, documentation, engineering blog, support, and 25 more developer resources.'
plans:
- name: Bestprice Plans Pricing
  plan_count: 0
  slug: bestprice-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Bestprice Rate Limits
  slug: bestprice-rate-limits
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 13.3
    developer_ergonomics: 58.9
    discoverability: 94.4
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bestprice/refs/heads/main/screenshots/bestprice-2026-09-02T144927.png
security:
- kind: authentication
  name: Bestprice Authentication
  slug: bestprice-authentication
  summary_line: 0 schemes
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
- Agent Commerce
- Greece
website: https://www.bestprice.gr/mcp
---
