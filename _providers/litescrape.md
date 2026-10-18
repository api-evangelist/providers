---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Litescrape Agentic Access
  operation_count: 23
  slug: litescrape-agentic-access
  summary_line: 23 operations · 1 acting
api_count: 2
apis:
- description: Hosted Model Context Protocol server (Streamable HTTP, protocol 2025-06-18) exposing ten search, maps, reviews and web-fetch tools backed by the Litescrape API; google_search, bing_search, duckduckgo_
  name: Litescrape MCP Server
  slug: litescrape-mcp-server
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Apple API from Litescrape — 2 operation(s) for apple.
  name: Litescrape Apple API
  slug: litescrape-apple-api
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Bing API from Litescrape — 2 operation(s) for bing.
  name: Litescrape Bing API
  slug: litescrape-bing-api
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Duckduckgo API from Litescrape — 2 operation(s) for duckduckgo.
  name: Litescrape Duckduckgo API
  slug: litescrape-duckduckgo-api
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Google API from Litescrape — 11 operation(s) for google.
  name: Litescrape Google API
  slug: litescrape-google-api
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Tripadvisor API from Litescrape — 3 operation(s) for tripadvisor.
  name: Litescrape Tripadvisor API
  slug: litescrape-tripadvisor-api
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Yelp API from Litescrape — 2 operation(s) for yelp.
  name: Litescrape Yelp API
  slug: litescrape-yelp-api
- baseURL: https://api.litescrape.com
  baseurl_source: declared
  description: The Zeroclick API from Litescrape — 1 operation(s) for zeroclick.
  name: Litescrape Zeroclick API
  slug: litescrape-zeroclick-api
artifact_total: 17
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/agentic-access/litescrape-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/litescrape-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/rate-limits/litescrape-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/litescrape-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/plans/litescrape-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/litescrape-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/rules/litescrape-rules.yml
  title: ''
  type: Spectral
  url: rules/litescrape-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/json-ld/litescrape-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/litescrape-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/vocabulary/litescrape-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/litescrape-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/data-model/litescrape-data-model.yml
  title: ''
  type: DataModel
  url: data-model/litescrape-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/changelog/litescrape-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/litescrape-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/conventions/litescrape-conventions.yml
  title: ''
  type: Conventions
  url: conventions/litescrape-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/litescrape/litescrape-mcp-server/blob/main/SECURITY.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/security/litescrape-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/litescrape-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/authentication/litescrape-authentication.yml
  title: ''
  type: Authentication
  url: authentication/litescrape-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://litescrape.com/terms
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/lifecycle/litescrape-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/litescrape-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/errors/litescrape-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/litescrape-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/conformance/litescrape-conformance.yml
  title: ''
  type: Conformance
  url: conformance/litescrape-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/overlays/litescrape-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/litescrape-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/llms/litescrape-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/litescrape-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/mcp/litescrape-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/litescrape-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/mcp/litescrape-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/litescrape-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/well-known/litescrape-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/litescrape-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/hosts/litescrape-hosts.yml
  title: ''
  type: Hosts
  url: hosts/litescrape-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/vendors/litescrape-vendors.yml
  title: ''
  type: Vendors
  url: vendors/litescrape-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/packages/litescrape-packages.yml
  title: ''
  type: SDKs
  url: packages/litescrape-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/packages/litescrape-packages.yml
  title: ''
  type: Packages
  url: packages/litescrape-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/security/litescrape-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/litescrape-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://litescrape.com
- group: docs
  title: ''
  type: Documentation
  url: https://litescrape.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://litescrape.com/docs/reference
- group: company
  title: ''
  type: Blog
  url: https://litescrape.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://litescrape.com/pricing
- group: other
  title: ''
  type: Playground
  url: https://litescrape.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://litescrape.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://litescrape.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/litescrape
created: '2026-10-07'
description: Litescrape is a search-results and web-data API from Litescrape LLC (Sheridan, Wyoming) that returns structured JSON from Google Search, Google AI Overview and AI Mode, Google Maps and reviews, Google Shopping, Bing, DuckDuckGo, Apple Maps, Yelp, Tripadvisor, Google Play and the Apple App Store, plus a browser-rendered Fetch and Screenshot API, billed at a flat $0.15 per 1,000 requests on prepaid credits with no subscription. It ships Python and TypeScript SDKs, an n8n node, a hosted MCP server at mcp.litescrape.com with a free keyless allowance, and a ZeroClick agent storefront at agents.litescrape.com that publishes its OpenAPI.
image: https://litescrape.com/litescrape-og.png
jsonld:
- class_count: 1
  name: Litescrape Context
  property_count: 6
  slug: litescrape-context
layout: provider
mcp_servers:
- description: Official Litescrape MCP server. The hosted Streamable HTTP endpoint answered an unauthenticated initialize (serverInfo litescrape-mcp-server 0.3.0, protocolVersion 2025-06-18, capabilities.tools.listC
  name: Litescrape MCP Server
  slug: litescrape-mcp-server
modified: '2026-10-07'
name: Litescrape
nav: Providers
network: true
overview: 'Litescrape publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apple API, Bing API, Duckduckgo API, and 5 more. Tagged areas include Company, SERP API, Web Scraping, Search, and Google Maps.


  The Litescrape catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Litescrape''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Litescrape Plans Pricing
  plan_count: 1
  slug: litescrape-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Litescrape Rate Limits
  slug: litescrape-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Litescrape API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: litescrape-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 63.8
    catalog_earned_first_party: 16.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 54.5
    developer_ergonomics: 47.0
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/litescrape/refs/heads/main/screenshots/litescrape-2026-10-11T110526.png
security:
- kind: authentication
  name: Litescrape Authentication
  slug: litescrape-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Litescrape Domain Security
  slug: litescrape-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Litescrape Vulnerability Disclosure
  slug: litescrape-vulnerability-disclosure
  summary_line: contact published
slug: litescrape
tags:
- Company
- SERP API
- Web Scraping
- Search
- Google Maps
- Reviews
- Web Data
- MCP
website: https://litescrape.com
---
