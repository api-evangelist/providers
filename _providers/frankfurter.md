---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Frankfurter Agentic Access
  operation_count: 10
  slug: frankfurter-agentic-access
  summary_line: 10 operations
api_count: 6
apis:
- description: Supported currency reference data
  name: Frankfurter Currencies API
  slug: frankfurter-currencies-api
- description: Latest foreign exchange rates
  name: Frankfurter current-rates API
  slug: frankfurter-current-rates-api
- description: Historical exchange rates for specific dates and periods
  name: Frankfurter historical-rates API
  slug: frankfurter-historical-rates-api
- description: API reference data like available currencies
  name: Frankfurter metadata API
  slug: frankfurter-metadata-api
- description: Central-bank and institutional data providers
  name: Frankfurter Providers API
  slug: frankfurter-providers-api
- description: Blended currency exchange rates
  name: Frankfurter Rates API
  slug: frankfurter-rates-api
artifact_total: 87
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Frankfurter Currencies API
  slug: open-frankfurter-currencies-api
- collection_type: open
  name: Frankfurter Currencies current-rates API
  slug: open-frankfurter-current-rates-api
- collection_type: open
  name: Frankfurter Currencies historical-rates API
  slug: open-frankfurter-historical-rates-api
- collection_type: open
  name: Frankfurter Currencies metadata API
  slug: open-frankfurter-metadata-api
- collection_type: open
  name: Frankfurter Currencies Providers API
  slug: open-frankfurter-providers-api
- collection_type: open
  name: Frankfurter Currencies Rates API
  slug: open-frankfurter-rates-api
- collection_type: open
  name: Frankfurter API
  slug: open-frankfurter-v1
- collection_type: open
  name: Frankfurter API
  slug: open-frankfurter-v2
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/lineofflight/frankfurter/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frankfurter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frankfurter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frankfurter.dev
- group: docs
  title: ''
  type: Documentation
  url: https://frankfurter.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lineofflight
- group: build
  title: Frankfurter (canonical)
  type: GitHubRepository
  url: https://github.com/lineofflight/frankfurter
- group: build
  title: Frankfurter MCP Server
  type: GitHubRepository
  url: https://github.com/lineofflight/frankfurter-mcp
- group: commercial
  title: MIT License
  type: License
  url: https://github.com/lineofflight/frankfurter/blob/main/LICENSE
- group: other
  title: Docker (Frankfurter)
  type: ContainerImage
  url: https://hub.docker.com/r/lineofflight/frankfurter
- group: other
  title: Docker (Frankfurter MCP)
  type: ContainerImage
  url: https://ghcr.io/lineofflight/frankfurter-mcp
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/lineofflight/frankfurter-mcp
- group: build
  title: Hosted MCP Endpoint
  type: Tools
  url: https://mcp.frankfurter.dev/
- group: build
  title: MCP Registry Listing
  type: Tools
  url: https://github.com/modelcontextprotocol/registry
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: Issues
  url: https://github.com/lineofflight/frankfurter/issues
- group: operate
  title: ''
  type: Forums
  url: https://github.com/lineofflight/frankfurter/discussions
- group: design
  title: ''
  type: SpectralRules
  url: rules/frankfurter-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/frankfurter-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/frankfurter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/frankfurter-rate-limits.yml
created: '2026-05-28'
description: Frankfurter is an open-source (MIT) currency exchange rates API that blends foreign-exchange reference rates published by 50+ central banks and monetary authorities. It hosts a free, no-key public endpoint at api.frankfurter.dev (current v2 and frozen v1) and ships as a Docker image for unlimited self-hosting. Historical data extends back to 1948 and covers 201 currencies; the API serves JSON, NDJSON, and CSV.
examples:
- key_count: 4
  name: V1 Currencies Example
  slug: v1-currencies-example
- key_count: 3
  name: V1 Rates By Date Example
  slug: v1-rates-by-date-example
- key_count: 4
  name: V1 Rates Example
  slug: v1-rates-example
- key_count: 4
  name: V1 Rates On Date Example
  slug: v1-rates-on-date-example
- key_count: 6
  name: V2 Currency Detail Example
  slug: v2-currency-detail-example
- key_count: 6
  name: V2 Currency Example
  slug: v2-currency-example
- key_count: 11
  name: V2 Provider Example
  slug: v2-provider-example
- key_count: 5
  name: V2 Rate Example
  slug: v2-rate-example
features:
- description: Combines daily FX rates from 50+ central banks and monetary authorities into a consensus-filtered, outlier-rejecting blend.
  name: Blended Reference Rates
- description: JSON, NDJSON (streamed), and CSV from the same endpoint.
  name: Multi-Format Output
- description: Daily rates back to 1948 with optional week/month downsampling.
  name: Historical Time Series
- description: Active and legacy currency coverage with ISO 4217 metadata.
  name: 201 Currencies
- description: '`expand=providers` exposes each provider''s individual quote so callers can audit the blend, with `excluded: true` flags on outliers and peg overrides.'
  name: Per-Provider Expansion
- description: No keys, no accounts, no monthly or daily caps.
  name: No Authentication
- description: Single Docker image with optional SQLite volume mount.
  name: Self-Hostable
- description: Optional, no-cost provider keys for Bank Al-Maghrib, Banco de México, Banco Central de Chile, Bank of Thailand, US Federal Reserve, and the Turkish Central Bank widen self-hosted coverage.
  name: Free Upstream Provider Keys
- description: GET and OPTIONS allowed from any origin — direct browser use.
  name: Open CORS
- description: Full source on GitHub; community contributions and fork-friendly.
  name: Open Source (MIT)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frankfurter.png
integrations:
- description: Primary upstream provider (ECB reference rates).
  name: European Central Bank
- description: Optional upstream provider via free FED API key.
  name: US Federal Reserve
- description: Upstream provider (BOC) included in the blend.
  name: Bank of Canada
- description: Upstream provider (BCB).
  name: Banco Central do Brasil
- description: Optional upstream provider via free TCMB key.
  name: Turkish Central Bank
- description: Optional upstream provider via free BOT key.
  name: Bank of Thailand
- description: Optional upstream provider via free BCCh key.
  name: Banco Central de Chile
- description: Optional upstream provider via free Banxico key.
  name: Banco de México
- description: Optional upstream provider via free BAM key.
  name: Bank Al-Maghrib (Morocco)
- description: Official MCP server (lineofflight/frankfurter-mcp) registered at the MCP registry.
  name: Model Context Protocol
- description: Container distribution for self-hosting.
  name: Docker Hub / GHCR
- description: Community 'Show and Tell' for libraries and tools built on Frankfurter.
  name: GitHub Discussions
json_schemas:
- name: amount
  property_count: 0
  slug: v1-amount
- name: baseIn
  property_count: 0
  slug: v1-base-in
- name: base
  property_count: 0
  slug: v1-base
- name: currencies
  property_count: 0
  slug: v1-currencies
- name: date
  property_count: 0
  slug: v1-date
- name: ratesByDate
  property_count: 0
  slug: v1-rates-by-date
- name: ratesOnDate
  property_count: 4
  slug: v1-rates-on-date
- name: rates
  property_count: 0
  slug: v1-rates
- name: CurrencyDetail
  property_count: 6
  slug: v2-currency-detail
- name: Currency
  property_count: 6
  slug: v2-currency
- name: Provider
  property_count: 11
  slug: v2-provider
- name: Rate
  property_count: 5
  slug: v2-rate
json_structures:
- name: V1 Amount Structure
  property_count: 0
  slug: v1-amount-structure
- name: V1 Base In Structure
  property_count: 0
  slug: v1-base-in-structure
- name: V1 Base Structure
  property_count: 0
  slug: v1-base-structure
- name: V1 Currencies Structure
  property_count: 0
  slug: v1-currencies-structure
- name: V1 Date Structure
  property_count: 0
  slug: v1-date-structure
- name: V1 Rates By Date Structure
  property_count: 0
  slug: v1-rates-by-date-structure
- name: V1 Rates On Date Structure
  property_count: 4
  slug: v1-rates-on-date-structure
- name: V1 Rates Structure
  property_count: 0
  slug: v1-rates-structure
- name: V2 Currency Detail Structure
  property_count: 6
  slug: v2-currency-detail-structure
- name: V2 Currency Structure
  property_count: 6
  slug: v2-currency-structure
- name: V2 Provider Structure
  property_count: 11
  slug: v2-provider-structure
- name: V2 Rate Structure
  property_count: 5
  slug: v2-rate-structure
jsonld:
- class_count: 3
  name: Frankfurter V1 Context
  property_count: 4
  slug: frankfurter-v1-context
- class_count: 4
  name: Frankfurter V2 Context
  property_count: 22
  slug: frankfurter-v2-context
layout: provider
modified: '2026-05-29'
name: Frankfurter
nav: Providers
network: true
overview: 'Frankfurter publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Currencies API, current-rates API, historical-rates API, and 3 more. Tagged areas include Currency Exchange, Foreign Exchange, FX, Open Source, and MIT.


  The Frankfurter catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Frankfurter''s developer surface includes documentation, tooling, and 19 more developer resources.'
plans:
- name: Frankfurter Plans Pricing
  plan_count: 2
  slug: frankfurter-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Frankfurter Rate Limits
  slug: frankfurter-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Frankfurter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: frankfurter-jsonschema-spectral-rules
- effective_rule_count: 81
  extends:
  - spectral:oas
  name: Frankfurter API Rules
  rule_count: 40
  severity_counts:
    error: 14
    hint: 0
    info: 6
    warn: 20
  slug: frankfurter-spectral-rules
score:
  band: developing
  composite: 39.9
  delta: -6.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 25.0
    contract_quality: 66.2
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/frankfurter/refs/heads/main/screenshots/frankfurter-2026-06-20T181506.png
security:
- kind: domain-security
  name: Frankfurter Domain Security
  slug: frankfurter-domain-security
  summary_line: TLSv1.3
slug: frankfurter
solutions:
- description: api.frankfurter.dev — no key, soft fair-use limits, ideal for prototypes and low-volume production.
  name: Public Hosted (Free)
- description: Run lineofflight/frankfurter via Docker; no application-level rate limit.
  name: Self-Hosted FOSS
- description: Drop the Frankfurter MCP server into any Claude / agent stack for natural-language FX access.
  name: MCP Tooling
tags:
- Currency Exchange
- Foreign Exchange
- FX
- Open Source
- MIT
- Self-Hosted
- Public APIs
use_cases:
- description: Embed blended FX rates into invoicing, payouts, and conversion.
  name: Treasury and Payments Pricing
- description: Convert displayed prices into the visitor's currency on page load.
  name: E-commerce Storefront Localization
- description: Backfill historical FX into BI dashboards and finance reports.
  name: Reporting and Analytics
- description: Sync ISO 4217 currency tables and provider metadata into ERPs.
  name: Reference Data Maintenance
- description: Equip Claude and other MCP-capable agents with the official Frankfurter MCP server (get_rates, convert, list_currencies, list_providers).
  name: AI Assistant Tooling
- description: Self-host inside a VPC for compliance-sensitive workloads.
  name: Private FX Service
- description: Long historical series for FX econometric studies.
  name: Academic and Research
website: https://frankfurter.dev
---
