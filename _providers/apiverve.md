---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 101
  human_in_the_loop: 0
  name: Apiverve Agentic Access
  operation_count: 367
  slug: apiverve-agentic-access
  summary_line: 367 operations · 101 acting
api_count: 1
apis:
- description: Single GraphQL endpoint that fans out to multiple APIs in one request. Explicitly labeled alpha / not for production.
  name: APIVerve GraphQL API (alpha)
  slug: apiverve-graphql-api-alpha
- description: 'Hosted remote MCP server (streamable HTTP) exposing every catalog endpoint as individual MCP tools with input/output schemas. Auth is negotiated: OAuth 2.0 by default or API key via x-api-key. New end'
  name: APIVerve MCP Server
  slug: apiverve-mcp-server
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The AI/Computer Vision API from APIVerve — 6 operation(s) for ai/computer vision.
  name: APIVerve AI/Computer Vision API
  slug: apiverve-ai-computer-vision-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Astrology API from APIVerve — 6 operation(s) for astrology.
  name: APIVerve Astrology API
  slug: apiverve-astrology-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Calendar API from APIVerve — 5 operation(s) for calendar.
  name: APIVerve Calendar API
  slug: apiverve-calendar-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Data Conversion API from APIVerve — 33 operation(s) for data conversion.
  name: APIVerve Data Conversion API
  slug: apiverve-data-conversion-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Data Generation API from APIVerve — 32 operation(s) for data generation.
  name: APIVerve Data Generation API
  slug: apiverve-data-generation-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Data Lookup API from APIVerve — 17 operation(s) for data lookup.
  name: APIVerve Data Lookup API
  slug: apiverve-data-lookup-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Data Processing API from APIVerve — 6 operation(s) for data processing.
  name: APIVerve Data Processing API
  slug: apiverve-data-processing-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Data Scraping API from APIVerve — 5 operation(s) for data scraping.
  name: APIVerve Data Scraping API
  slug: apiverve-data-scraping-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Data Validation API from APIVerve — 9 operation(s) for data validation.
  name: APIVerve Data Validation API
  slug: apiverve-data-validation-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Documents API from APIVerve — 3 operation(s) for documents.
  name: APIVerve Documents API
  slug: apiverve-documents-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Domain Data API from APIVerve — 18 operation(s) for domain data.
  name: APIVerve Domain Data API
  slug: apiverve-domain-data-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Entertainment API from APIVerve — 24 operation(s) for entertainment.
  name: APIVerve Entertainment API
  slug: apiverve-entertainment-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Finance API from APIVerve — 49 operation(s) for finance.
  name: APIVerve Finance API
  slug: apiverve-finance-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Food API from APIVerve — 3 operation(s) for food.
  name: APIVerve Food API
  slug: apiverve-food-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Games API from APIVerve — 21 operation(s) for games.
  name: APIVerve Games API
  slug: apiverve-games-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Geography API from APIVerve — 13 operation(s) for geography.
  name: APIVerve Geography API
  slug: apiverve-geography-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Health/Wellness API from APIVerve — 2 operation(s) for health/wellness.
  name: APIVerve Health/Wellness API
  slug: apiverve-health-wellness-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Images API from APIVerve — 7 operation(s) for images.
  name: APIVerve Images API
  slug: apiverve-images-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Lifestyle API from APIVerve — 3 operation(s) for lifestyle.
  name: APIVerve Lifestyle API
  slug: apiverve-lifestyle-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Math/Calculations API from APIVerve — 8 operation(s) for math/calculations.
  name: APIVerve Math/Calculations API
  slug: apiverve-math-calculations-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Networking API from APIVerve — 14 operation(s) for networking.
  name: APIVerve Networking API
  slug: apiverve-networking-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The News API from APIVerve — 1 operation(s) for news.
  name: APIVerve News API
  slug: apiverve-news-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Parsers API from APIVerve — 4 operation(s) for parsers.
  name: APIVerve Parsers API
  slug: apiverve-parsers-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Reference Data API from APIVerve — 11 operation(s) for reference data.
  name: APIVerve Reference Data API
  slug: apiverve-reference-data-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Science API from APIVerve — 4 operation(s) for science.
  name: APIVerve Science API
  slug: apiverve-science-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Security API from APIVerve — 4 operation(s) for security.
  name: APIVerve Security API
  slug: apiverve-security-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Text Processing API from APIVerve — 45 operation(s) for text processing.
  name: APIVerve Text Processing API
  slug: apiverve-text-processing-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Transportation API from APIVerve — 6 operation(s) for transportation.
  name: APIVerve Transportation API
  slug: apiverve-transportation-api
- baseURL: https://api.apiverve.com/v1
  baseurl_source: declared
  description: The Weather API from APIVerve — 8 operation(s) for weather.
  name: APIVerve Weather API
  slug: apiverve-weather-api
artifact_total: 43
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.apiverve.com/rss.xml
- group: agent
  href: https://artifacts.apis.io/apiverve/agentic-access/apiverve-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apiverve-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/apiverve/security/apiverve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiverve-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/apiverve/authentication/apiverve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiverve-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://apiverve.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.apiverve.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apiverve.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apiverve.com/api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apiverve.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://apiverve.com/contact
- group: company
  title: ''
  type: Blog
  url: https://apiverve.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiverve
- group: operate
  title: ''
  type: Roadmap
  url: https://apiverve.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://apiverve.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.apiverve.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evlarsoft.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evlarsoft.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/apiverve
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apiverve.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://apiverve.com/changelog
- group: build
  href: https://artifacts.apis.io/apiverve/packages/apiverve-packages.yml
  title: ''
  type: Packages
  url: packages/apiverve-packages.yml
- group: build
  href: https://artifacts.apis.io/apiverve/packages/apiverve-packages.yml
  title: ''
  type: SDKs
  url: packages/apiverve-packages.yml
- group: build
  href: https://artifacts.apis.io/apiverve/cli/apiverve-cli.yml
  title: ''
  type: CLI
  url: cli/apiverve-cli.yml
- group: agent
  href: https://artifacts.apis.io/apiverve/well-known/apiverve-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiverve-well-known.yml
- group: agent
  href: https://artifacts.apis.io/apiverve/llms/apiverve-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiverve-llms.txt
- group: design
  href: https://artifacts.apis.io/apiverve/conformance/apiverve-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiverve-conformance.yml
- group: design
  href: https://artifacts.apis.io/apiverve/errors/apiverve-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiverve-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apiverve/lifecycle/apiverve-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apiverve-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/apiverve/rate-limits/apiverve-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apiverve-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apiverve/plans/apiverve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apiverve-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apiverve/conventions/apiverve-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apiverve-conventions.yml
- group: start
  href: https://artifacts.apis.io/apiverve/sandbox/apiverve-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apiverve-sandbox.yml
- group: design
  href: https://artifacts.apis.io/apiverve/components/apiverve-components.yml
  title: ''
  type: Components
  url: components/apiverve-components.yml
- group: other
  href: https://artifacts.apis.io/apiverve/overlays/apiverve-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiverve-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/apiverve/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/apiverve/mcp/apiverve-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apiverve-tool-crosswalk.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://evlarsoft.com/legal/subprocessors
- group: operate
  title: ''
  type: IncidentNotification
  url: https://evlarsoft.com/legal/data-processing
created: '2026-09-19'
description: An agent-native API marketplace exposing 300+ (367+ enumerated) ready-made REST APIs behind a single API key with a uniform JSON envelope. Offers REST, an alpha GraphQL gateway, OpenAPI + Postman contracts, a self-hosted apis.json, an llms.txt, and a hosted remote MCP server that turns the whole catalog into agent tools.
finops:
- has_sources: true
  method: derived
  name: Apiverve Finops
  primary_unit: credits
  service_category: ''
  slug: apiverve-finops
  template: false
image: https://apiverve.com/images/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: APIVerve MCP Server
  slug: mcp
modified: '2026-10-06'
name: APIVerve
nav: Providers
network: true
overview: 'APIVerve publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI/Computer Vision API, Astrology API, Calendar API, and 28 more. Tagged areas include API Marketplace, REST, JSON, GraphQL, and OpenAPI.


  The APIVerve catalog on APIs.io includes 1 Spectral governance ruleset.


  APIVerve''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Apiverve Plans Pricing
  plan_count: 5
  slug: apiverve-plans-pricing
- name: Apiverve Price Estimates
  plan_count: 0
  slug: apiverve-price-estimates
random_paper: 2
rate_limits:
- limit_count: 0
  name: Apiverve Rate Limits
  slug: apiverve-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: APIVerve API Rules
  rule_count: 64
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 4
  slug: apiverve-rules
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.8
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 60.1
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 64.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apiverve/apiverve-2026-10-11T095934.png
security:
- kind: authentication
  name: Apiverve Authentication
  slug: apiverve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apiverve Domain Security
  slug: apiverve-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 3
skills:
- name: Domain intelligence sweep with APIVerve
  slug: apiverve-domain-intelligence
- name: IP risk & geolocation check with APIVerve
  slug: apiverve-ip-risk-check
- name: Validate a signup with APIVerve
  slug: apiverve-validate-signup
slug: apiverve
tags:
- API Marketplace
- REST
- JSON
- GraphQL
- OpenAPI
- Postman
- MCP
- Llms.txt
- Agent-Native
- APIKeys
- IP Geolocation
- DNS
- WHOIS
- SSL
- Email Verification
- Phone Validation
- Exchange Rates
- metals prices
- Weather
- Geocoding
- Text Processing
- Developer Tools
website: https://apiverve.com
---
