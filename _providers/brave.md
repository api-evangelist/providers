---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Brave Agentic Access
  operation_count: 11
  slug: brave-agentic-access
  summary_line: 11 operations
api_count: 10
apis:
- description: API for managing and reporting on Brave Ads campaigns. Enables advertisers to retrieve campaign details and performance data for privacy-preserving native browser ads and search ads. Supports customiz
  name: Brave Ads API
  slug: brave-ads-api
- description: Campaign management and hierarchy endpoints
  name: Brave campaigns API
  slug: brave-campaigns-api
- description: Image search endpoints
  name: Brave images API
  slug: brave-images-api
- description: Local place of interest endpoints
  name: Brave local API
  slug: brave-local-api
- description: News search endpoints
  name: Brave news API
  slug: brave-news-api
- description: Campaign performance reporting endpoints
  name: Brave reporting API
  slug: brave-reporting-api
- description: Spellcheck endpoints
  name: Brave spellcheck API
  slug: brave-spellcheck-api
- description: Autosuggest endpoints
  name: Brave suggest API
  slug: brave-suggest-api
- description: Video search endpoints
  name: Brave videos API
  slug: brave-videos-api
- description: Web search endpoints
  name: Brave web API
  slug: brave-web-api
artifact_total: 26
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/brave/brave-search-mcp-server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/brave/brave-search-mcp-server/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/brave/brave-search-mcp-server/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brave-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brave-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brave-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://brave.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-dashboard.search.brave.com/app/documentation/web-search/get-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/brave
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brave-software
- group: company
  title: ''
  type: Blog
  url: https://brave.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://brave.com/search/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brave.app
- group: other
  title: ''
  type: X
  url: https://x.com/brave
- group: commercial
  title: ''
  type: Plans
  url: plans/brave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brave-finops.yml
created: '2026-06-13'
description: Brave is a privacy-first browser company offering developer APIs for anonymous web search and privacy-preserving advertising. The Brave Search API provides real-time search results from an independent index of over 30 billion pages, designed for AI and LLM applications with schema-enriched results and citation- grounded answer completions. The Brave Ads API enables advertisers to manage campaigns and access performance reporting data for privacy-respecting native browser and search ads.
examples:
- key_count: 3
  name: Spellcheck Response
  slug: spellcheck-response
- key_count: 3
  name: Suggest Response
  slug: suggest-response
- key_count: 5
  name: Web Search Response
  slug: web-search-response
finops:
- name: Brave Finops
  service_category: ''
  slug: brave-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brave.png
json_schemas:
- name: Campaign
  property_count: 7
  slug: campaign
- name: SuggestResponse
  property_count: 3
  slug: suggest-response
- name: WebSearchResponse
  property_count: 5
  slug: web-search-response
jsonld:
- class_count: 34
  name: Brave Ads Context
  property_count: 0
  slug: brave-ads-context
- class_count: 51
  name: Brave Search Context
  property_count: 0
  slug: brave-search-context
layout: provider
modified: '2026-06-13'
name: Brave
nav: Providers
network: true
overview: 'Brave publishes 9 APIs on the [APIs.io](https://apis.io/) network, including campaigns API, images API, local API, and 6 more. Tagged areas include Search, Advertising, Privacy, Browser, and AI.


  The Brave catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Brave''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Brave Plans Pricing
  plan_count: 4
  slug: brave-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 0
  name: Brave Rate Limits
  slug: brave-rate-limits
rules:
- name: Brave API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: brave-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brave/refs/heads/main/screenshots/brave-2026-06-20T173636.png
security:
- kind: authentication
  name: Brave Authentication
  slug: brave-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Brave Domain Security
  slug: brave-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Brave Vulnerability Disclosure
  slug: brave-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: brave
tags:
- Search
- Advertising
- Privacy
- Browser
- AI
- LLM
website: https://brave.com
---
