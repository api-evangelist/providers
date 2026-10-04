---
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
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.0
  scored_at: '2026-10-03'
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
artifact_total: 38
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/agentic-access/apiverve-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apiverve-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/security/apiverve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiverve-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/authentication/apiverve-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/packages/apiverve-packages.yml
  title: ''
  type: Packages
  url: packages/apiverve-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/packages/apiverve-packages.yml
  title: ''
  type: SDKs
  url: packages/apiverve-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/cli/apiverve-cli.yml
  title: ''
  type: CLI
  url: cli/apiverve-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/well-known/apiverve-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiverve-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/llms/apiverve-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiverve-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/conformance/apiverve-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiverve-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/errors/apiverve-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiverve-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/lifecycle/apiverve-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apiverve-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/rate-limits/apiverve-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apiverve-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/plans/apiverve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apiverve-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/conventions/apiverve-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apiverve-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/sandbox/apiverve-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apiverve-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/components/apiverve-components.yml
  title: ''
  type: Components
  url: components/apiverve-components.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/overlays/apiverve-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiverve-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apiverve/refs/heads/main/mcp/apiverve-tool-crosswalk.yml
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
image: https://apiverve.com/images/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: APIVerve MCP Server
  slug: apiverve-mcp-server
- description: ''
  name: MCP manifest
  slug: mcp-manifest
modified: '2026-09-20'
name: APIVerve
nav: Providers
network: true
overview: 'APIVerve publishes 31 APIs on the [APIs.io](https://apis.io/) network, including AI/Computer Vision API, Astrology API, Calendar API, and 28 more. Tagged areas include API Marketplace, REST, JSON, GraphQL, and OpenAPI.


  APIVerve''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Apiverve Plans Pricing
  plan_count: 5
  slug: apiverve-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Apiverve Rate Limits
  slug: apiverve-rate-limits
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 85.1
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 61.3
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
    score: 32.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Apiverve Authentication
  slug: apiverve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apiverve Domain Security
  slug: apiverve-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: apiverve
tags:
- API Marketplace
- REST
- JSON
- GraphQL
- OpenAPI
- Postman
- MCP
- llms-txt
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
