---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-09-25'
api_count: 2
apis:
- baseURL: https://api.unirateapi.com
  baseurl_source: declared
  description: Precious metals prices (Gold, Silver, Platinum, Palladium) - Pro subscription required
  name: UniRate API Commodity API
  slug: unirateapi-commodity-api
- baseURL: https://api.unirateapi.com
  baseurl_source: declared
  description: Current exchange rates and conversion operations
  name: UniRate API Currency API
  slug: unirateapi-currency-api
- baseURL: https://api.unirateapi.com
  baseurl_source: declared
  description: Historical exchange rates data (1999-2026)
  name: UniRate API Historical Currency API
  slug: unirateapi-historical-currency-api
- baseURL: https://api.unirateapi.com
  baseurl_source: declared
  description: The VAT Rates API from UniRate API — 1 operation(s) for vat rates.
  name: UniRate API VAT Rates API
  slug: unirateapi-vat-rates-api
artifact_total: 9
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/overlays/unirateapi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unirateapi-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/mcp/unirateapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unirateapi-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/security/unirateapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unirateapi-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/authentication/unirateapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unirateapi-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/packages/unirateapi-packages.yml
  title: ''
  type: Packages
  url: packages/unirateapi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/packages/unirateapi-packages.yml
  title: ''
  type: SDKs
  url: packages/unirateapi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/cli/unirateapi-cli.yml
  title: ''
  type: CLI
  url: cli/unirateapi-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/llms/unirateapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unirateapi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unirateapi/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://unirateapi.com
- group: start
  title: ''
  type: Portal
  url: https://unirateapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://unirateapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://unirateapi.com/register
- group: start
  title: ''
  type: Login
  url: https://unirateapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unirateapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unirateapi.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://unirateapi.com/articles/
- group: other
  title: ''
  type: APIsJSON
  url: https://raw.githubusercontent.com/UniRate-API/openapi/main/apis.json
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/UniRate-API
created: '2026-09-16'
description: The UniRate API provides current foreign-exchange rates, currency conversion, a list of supported currencies, and country VAT rates over a simple REST interface. Current-rate endpoints are available on a free, self-serve tier (get a key at https://unirateapi.com); historical, precious-metals and commodities endpoints require a Pro subscription. Open-source client libraries are published for Python, Node/TypeScript, Go, Rust, Ruby, PHP, Java, Swift, .NET and more, plus an official MCP server for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Official Model Context Protocol server for the UniRate API. Gives MCP-compatible AI assistants (Claude Desktop, Cursor, Continue, Cline) a typed, currency-aware tool surface over UniRate's currency co
  name: UniRate MCP Server
  slug: unirate-mcp-server
modified: '2026-09-16'
name: UniRate API
nav: Providers
network: true
overview: 'UniRate API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Commodity API, Currency API, Historical Currency API, and 1 more. Tagged areas include Currency, Exchange Rates, Foreign Exchange, Forex, and Currency Conversion.


  UniRate API''s developer surface includes authentication, CLI, developer portal, pricing, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Unirateapi Plans Pricing
  plan_count: 2
  slug: unirateapi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Unirateapi Rate Limits
  slug: unirateapi-rate-limits
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 41.0
    developer_ergonomics: 56.5
    discoverability: 65.0
    operational_transparency: 36.8
  previous_composite: 48.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Unirateapi Authentication
  slug: unirateapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unirateapi Domain Security
  slug: unirateapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unirateapi
tags:
- Currency
- Exchange Rates
- Foreign Exchange
- Forex
- Currency Conversion
- VAT
- Finance
- Financial Data
website: https://unirateapi.com
---
