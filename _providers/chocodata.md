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
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chocodata Agentic Access
  operation_count: 11
  slug: chocodata-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The Amazon API from Chocodata — 3 operation(s) for amazon.
  name: Chocodata Amazon API
  slug: chocodata-amazon-api
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The Chocodata API from Chocodata — 1 operation(s) for chocodata.
  name: Chocodata Chocodata API
  slug: chocodata-chocodata-api
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The Reddit API from Chocodata — 1 operation(s) for reddit.
  name: Chocodata Reddit API
  slug: chocodata-reddit-api
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The Universal API from Chocodata — 1 operation(s) for universal.
  name: Chocodata Universal API
  slug: chocodata-universal-api
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The Youtube API from Chocodata — 2 operation(s) for youtube.
  name: Chocodata Youtube API
  slug: chocodata-youtube-api
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The App Store API from Chocodata — 2 operation(s) for app store.
  name: Chocodata App Store API
  slug: chocodata-app-store-api
- baseURL: https://api.chocodata.com
  baseurl_source: declared
  description: The Google Play API from Chocodata — 1 operation(s) for google play.
  name: Chocodata Google Play API
  slug: chocodata-google-play-api
artifact_total: 20
asyncapis:
- description: ''
  name: Chocodata Webhooks
  slug: chocodata-webhooks
common:
- group: other
  href: https://artifacts.apis.io/chocodata/capabilities/chocodata-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chocodata-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://chocodata.com
- group: auth
  href: https://artifacts.apis.io/chocodata/security/chocodata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chocodata-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chocodata/authentication/chocodata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chocodata-authentication.yml
- group: build
  href: https://artifacts.apis.io/chocodata/packages/chocodata-packages.yml
  title: ''
  type: Packages
  url: packages/chocodata-packages.yml
- group: build
  href: https://artifacts.apis.io/chocodata/packages/chocodata-packages.yml
  title: ''
  type: SDKs
  url: packages/chocodata-packages.yml
- group: agent
  href: https://artifacts.apis.io/chocodata/well-known/chocodata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chocodata-well-known.yml
- group: agent
  href: https://artifacts.apis.io/chocodata/mcp/chocodata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chocodata-mcp.yml
- group: build
  href: https://artifacts.apis.io/chocodata/mcp/chocodata-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/chocodata-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/chocodata/llms/chocodata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chocodata-llms.txt
- group: other
  href: https://artifacts.apis.io/chocodata/overlays/chocodata-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/chocodata-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/chocodata/conformance/chocodata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chocodata-conformance.yml
- group: design
  href: https://artifacts.apis.io/chocodata/errors/chocodata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chocodata-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chocodata/lifecycle/chocodata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chocodata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://chocodata.com/status
- group: operate
  href: https://artifacts.apis.io/chocodata/lifecycle/chocodata-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/chocodata-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/chocodata/conventions/chocodata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chocodata-conventions.yml
- group: operate
  href: https://artifacts.apis.io/chocodata/changelog/chocodata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chocodata-changelog.yml
- group: build
  href: https://artifacts.apis.io/chocodata/cli/chocodata-cli.yml
  title: ''
  type: CLI
  url: cli/chocodata-cli.yml
- group: design
  href: https://artifacts.apis.io/chocodata/asyncapi/chocodata-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chocodata-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/chocodata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/chocodata/agentic-access/chocodata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chocodata-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/chocodata/plans/chocodata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chocodata-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chocodata/rate-limits/chocodata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chocodata-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://chocodata.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://chocodata.com/docs/endpoint-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://chocodata.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://chocodata.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chocodata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chocodata.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.chocodata.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.chocodata.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChocoData-com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.chocodata.com
- group: start
  title: ''
  type: Console
  url: https://app.chocodata.com
created: '2026-07-16'
description: Web-scraping REST API that returns structured JSON from a large catalog of target sites (e-commerce, search engines, social, real estate, finance, and more), with proxies, CAPTCHA, and anti-bot handling managed server-side. Ships an OpenAPI 3.1 contract, official Node/Python/Go SDKs, a CLI, an npm-distributed stdio MCP server (chocodata-mcp), live llms.txt manifests with markdown twins of every docs page, and an ai-plugin.json discovery manifest. Bills only for successful (2xx) responses.
finops:
- has_sources: true
  method: derived
  name: Chocodata Finops
  primary_unit: 1,000 successful requests
  service_category: ''
  slug: chocodata-finops
  template: false
image: https://chocodata.com/logo-512.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server requiring an API key; 12 tools listed.
  name: Chocodata MCP Server
  slug: chocodata
modified: '2026-09-03'
name: Chocodata
nav: Providers
network: true
overview: 'Chocodata publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Amazon API, Chocodata API, Reddit API, and 4 more. Tagged areas include Web Scraping, Data Extraction, SERP, E-Commerce Data, and social-media-data.


  The Chocodata catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chocodata''s developer surface includes authentication, changelog, CLI, documentation, API reference, getting-started guide, pricing, and 28 more developer resources.'
plans:
- name: Chocodata Plans Pricing
  plan_count: 5
  slug: chocodata-plans-pricing
- name: Chocodata Price Estimates
  plan_count: 0
  slug: chocodata-price-estimates
random_paper: 22
rate_limits:
- limit_count: 4
  name: Chocodata Rate Limits
  slug: chocodata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Chocodata API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 2
  slug: chocodata-rules
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 56.3
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 81.6
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chocodata/chocodata-2026-07-25T205249.png
security:
- kind: authentication
  name: Chocodata Authentication
  slug: chocodata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chocodata Domain Security
  slug: chocodata-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: chocodata-batch-scraping
  slug: chocodata-batch-scraping
- name: chocodata-scrape-product
  slug: chocodata-scrape-product
- name: chocodata-universal-scrape
  slug: chocodata-universal-scrape
slug: chocodata
tags:
- Web Scraping
- Data Extraction
- SERP
- E-Commerce Data
- social-media-data
- Proxy
- MCP
- Agent-Native
- structured-json
website: https://chocodata.com
---
