---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.5
  scored_at: '2026-09-14'
api_count: 3
apis:
- description: The APILayer marketplace gateway at api.apilayer.com fronts the third-party APIs listed on marketplace.apilayer.com (Bank Data, Tax Data and others) behind a single subscription. Authentication here i
  name: APILayer Marketplace API
  slug: apilayer-api
- baseURL: https://api.exchangerate.host
  baseurl_source: declared
  description: Real-time and historical foreign exchange rates for 168 world currencies, with live quotes, single-day historical rates, date-range time frames, change queries and currency conversion. Five GET endpoi
  name: ExchangeRate.host API
  slug: exchangerate-host-api
- baseURL: https://api.exchangeratesapi.io/v1
  baseurl_source: declared
  description: 'Foreign exchange rate data for 170 world currencies drawn from 15+ sources: latest rates, single-date historical rates, time series, fluctuation between two dates, currency conversion and a supported-'
  name: Exchange Rates API
  slug: exchange-rates-api
- baseURL: https://api.ipapi.com/api
  baseurl_source: declared
  description: Real-time IP to geolocation lookup returning location, connection, timezone, currency and optional threat-assessment data for an IPv4 or IPv6 address, plus a /check endpoint that resolves the caller's
  name: ipapi
  slug: ipapi
artifact_total: 38
common:
- group: company
  title: ''
  type: Website
  url: https://apilayer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apilayer.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/apilayer/docs/api-layer-hub
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apilayer.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://apilayer.com/developers/suite/
- group: start
  title: ''
  type: SignUp
  url: https://app.apilayer.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.apilayer.com/login
- group: operate
  title: ''
  type: Support
  url: https://apilayer.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://apilayer.com/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/hgjA78638n
- group: operate
  title: ''
  type: FAQ
  url: https://apilayer.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.apilayer.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/apilayer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apilayer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ideracorp.com/legal/APILayer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ideracorp.com/en/legal/privacypolicy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/llms/apilayer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apilayer-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://apilayer.com/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/packages/apilayer-packages.yml
  title: ''
  type: Packages
  url: packages/apilayer-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/packages/apilayer-packages.yml
  title: ''
  type: SDKs
  url: packages/apilayer-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/well-known/apilayer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apilayer-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/mcp/apilayer-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apilayer-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/mcp/apilayer-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apilayer-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/authentication/apilayer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apilayer-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/scopes/apilayer-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apilayer-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/conformance/apilayer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apilayer-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/errors/apilayer-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/apilayer-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/lifecycle/apilayer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apilayer-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/lifecycle/apilayer-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/apilayer-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/changelog/apilayer-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apilayer-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/conventions/apilayer-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apilayer-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/data-model/apilayer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apilayer-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/plans/apilayer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apilayer-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/rate-limits/apilayer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apilayer-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/finops/apilayer-finops.yml
  title: ''
  type: FinOps
  url: finops/apilayer-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/vocabulary/apilayer-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/apilayer-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/rules/apilayer-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/apilayer-jsonschema-spectral-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/examples/apilayer-api-example.json
  title: ''
  type: Examples
  url: examples/apilayer-api-example.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/security/apilayer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apilayer-domain-security.yml
created: '2025-03-01'
description: APILayer is an API marketplace and hub, an Idera, Inc. brand headquartered in Vienna, Austria, that publishes and operates a portfolio of self-service REST data APIs alongside a gateway marketplace of third-party APIs. The house products cover IP geolocation (IPstack, ipapi), foreign exchange (Fixer, Currencylayer, ExchangeRate.host, Exchange Rates API), weather (Weatherstack), market data (Marketstack), news (Mediastack), aviation (Aviationstack), scraping and SERP (Scrapestack, Serpstack), and validation utilities (Numverify, Mailboxlayer, Vatlayer, Userstack, Countrylayer, Positionstack, Pdflayer, Screenshotlayer). One account and one dashboard cover every product, each product is keyed and billed separately, and every API has a free plan. APILayer publishes 22 OpenAPI documents from its own SwaggerHub organization, an llms.txt, and an OAuth-protected hosted MCP server.
examples:
- key_count: 9
  name: Apilayer Api Example
  slug: apilayer-api-example
features:
- description: Browse and integrate 100+ high-quality APIs across categories including geolocation, currency, weather, dev tools, and more.
  name: API Marketplace
- description: Single API key management across multiple APIs from the APILayer platform.
  name: Unified Authentication
- description: High-performance, reliable API infrastructure with global CDN for low-latency responses.
  name: Low Latency Infrastructure
- description: Centralized dashboard to manage API subscriptions, monitor usage, and access documentation.
  name: Developer Dashboard
- description: Real-time usage tracking and analytics across all subscribed APIs.
  name: Usage Analytics
finops:
- name: Apilayer Finops
  service_category: API
  slug: apilayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apilayer.png
integrations:
- description: IP geolocation API for geographic profiling and location intelligence.
  name: IPstack
- description: Real-time and historical currency exchange rate data API.
  name: Fixer
- description: Real-time weather data and forecasting API.
  name: Weatherstack
- description: Search engine results page scraping and SERP data API.
  name: Serpstack
- description: Live and historical news data API for media monitoring.
  name: Mediastack
- description: Global phone number validation and carrier lookup API.
  name: Numverify
- description: Real-time cryptocurrency exchange rate data API.
  name: Coinlayer
- description: HTML to PDF conversion and document generation API.
  name: Pdflayer
json_schemas:
- name: APILayer API
  property_count: 9
  slug: apilayer-api
json_structures:
- name: Apilayer Api Structure
  property_count: 9
  slug: apilayer-api-structure
jsonld:
- class_count: 12
  name: Apilayer Context
  property_count: 1
  slug: apilayer-context
layout: provider
mcp_servers:
- description: ''
  name: APILayer MCP Server
  slug: apilayer-mcp-server
modified: '2026-09-12'
name: APILayer
nav: Providers
network: true
overview: 'APILayer publishes 3 APIs on the [APIs.io](https://apis.io/) network: ExchangeRate.host API, Exchange Rates API, and ipapi. Tagged areas include API Marketplace, API Catalog, API Discovery, Developer Tools, and SaaS APIs.


  The APILayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APILayer''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, FAQ, engineering blog, and 35 more developer resources.'
plans:
- name: Apilayer Plans Pricing
  plan_count: 15
  slug: apilayer-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 8
  name: Apilayer Rate Limits
  slug: apilayer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APILayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apilayer-jsonschema-spectral-rules
scopes:
- name: Apilayer Scopes
  scope_count: 0
  slug: apilayer-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 89.3
    catalog_earned_first_party: 24.0
    catalog_gap: 25.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 43.2
    contract_quality: 64.6
    developer_ergonomics: 67.3
    discoverability: 81.5
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 67.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/screenshots/apilayer-2026-06-20T172242.png
security:
- kind: authentication
  name: Apilayer Authentication
  slug: apilayer-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Apilayer Domain Security
  slug: apilayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apilayer
solutions:
- description: Limited free tier for each API to explore and prototype integrations.
  name: Free Plan
- description: Entry-level paid plan with increased request limits for individual APIs.
  name: Basic Plan
- description: Higher volume plans for production applications requiring reliable API access.
  name: Professional Plan
- description: Custom volume and SLA guarantees for enterprise-scale API consumption.
  name: Enterprise Plan
tags:
- API Marketplace
- API Catalog
- API Discovery
- Developer Tools
- SaaS APIs
- Geolocation
- Currency
- Data APIs
use_cases:
- description: Determine user location, timezone, and geographic data from IP addresses using IPstack or IPapi.
  name: IP Geolocation
- description: Access real-time and historical currency exchange rates using Fixer or Currencylayer APIs.
  name: Currency Conversion
- description: Integrate real-time weather forecasts and historical weather data using Weatherstack.
  name: Weather Data
- description: Scrape search engine results programmatically using the Serpstack API.
  name: Search Engine Data
- description: Validate and look up phone number details globally using Numverify.
  name: Phone Validation
website: https://apilayer.com/
---
