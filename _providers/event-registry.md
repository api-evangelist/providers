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
    agent_skills: true
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Event Registry Agentic Access
  operation_count: 14
  slug: event-registry-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 1
apis:
- baseURL: https://eventregistry.org/api/v1
  baseurl_source: declared
  description: Search and retrieve individual news articles from 150,000+ global sources.
  name: Event Registry Articles API
  slug: event-registry-articles-api
- baseURL: https://eventregistry.org/api/v1
  baseurl_source: declared
  description: Search and retrieve clustered news events (deduplicated story groups).
  name: Event Registry Events API
  slug: event-registry-events-api
- baseURL: https://eventregistry.org/api/v1
  baseurl_source: declared
  description: Resolve entity names to URIs for use in search filters.
  name: Event Registry Suggest API
  slug: event-registry-suggest-api
- baseURL: https://eventregistry.org/api/v1
  baseurl_source: declared
  description: Retrieve content matching user-defined topic page configurations.
  name: Event Registry Topic Pages API
  slug: event-registry-topic-pages-api
- baseURL: https://eventregistry.org/api/v1
  baseurl_source: declared
  description: Monitor API token quota and usage.
  name: Event Registry Usage API
  slug: event-registry-usage-api
artifact_total: 26
collections:
- collection_type: open
  name: Event Registry (NewsAPI.ai) Articles API
  slug: open-event-registry-articles-api
- collection_type: open
  name: Event Registry (NewsAPI.ai) Articles Events API
  slug: open-event-registry-events-api
- collection_type: open
  name: Event Registry (NewsAPI.ai) Articles Suggest API
  slug: open-event-registry-suggest-api
- collection_type: open
  name: Event Registry (NewsAPI.ai) Articles Topic Pages API
  slug: open-event-registry-topic-pages-api
- collection_type: open
  name: Event Registry (NewsAPI.ai) Articles Usage API
  slug: open-event-registry-usage-api
common:
- group: other
  href: https://artifacts.apis.io/event-registry/capabilities/event-registry-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/event-registry-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/EventRegistry/newsapi-mcp/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/event-registry/agentic-access/event-registry-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/event-registry-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/event-registry/security/event-registry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/event-registry-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/event-registry/authentication/event-registry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/event-registry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://eventregistry.org
- group: docs
  title: ''
  type: Documentation
  url: https://newsapi.ai/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/EventRegistry
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/event-registry/
- group: company
  title: ''
  type: Blog
  url: https://newsapi.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://newsapi.ai/plans
- group: other
  title: ''
  type: X
  url: https://x.com/event_registry
- group: commercial
  href: https://artifacts.apis.io/event-registry/plans/event-registry-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/event-registry-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/event-registry/rate-limits/event-registry-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/event-registry-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/event-registry/finops/event-registry-finops.yml
  title: ''
  type: FinOps
  url: finops/event-registry-finops.yml
- group: build
  href: https://artifacts.apis.io/event-registry/packages/event-registry-packages.yml
  title: ''
  type: Packages
  url: packages/event-registry-packages.yml
- group: build
  href: https://artifacts.apis.io/event-registry/packages/event-registry-packages.yml
  title: ''
  type: SDKs
  url: packages/event-registry-packages.yml
- group: agent
  href: https://artifacts.apis.io/event-registry/mcp/event-registry-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/event-registry-mcp.yml
- group: build
  href: https://artifacts.apis.io/event-registry/mcp/event-registry-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/event-registry-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/event-registry/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/event-registry/llms/event-registry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/event-registry-llms.txt
- group: design
  href: https://artifacts.apis.io/event-registry/conventions/event-registry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/event-registry-conventions.yml
- group: design
  href: https://artifacts.apis.io/event-registry/errors/event-registry-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/event-registry-problem-types.yml
- group: design
  href: https://artifacts.apis.io/event-registry/data-model/event-registry-data-model.yml
  title: ''
  type: DataModel
  url: data-model/event-registry-data-model.yml
- group: design
  href: https://artifacts.apis.io/event-registry/lifecycle/event-registry-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/event-registry-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/event-registry/conformance/event-registry-conformance.yml
  title: ''
  type: Conformance
  url: conformance/event-registry-conformance.yml
- group: operate
  href: https://artifacts.apis.io/event-registry/changelog/event-registry-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/event-registry-changelog.yml
- group: start
  href: https://artifacts.apis.io/event-registry/sandbox/event-registry-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/event-registry-sandbox.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newsapi.ai/terms
- group: start
  title: ''
  type: SignUp
  url: https://newsapi.ai/register
- group: docs
  title: ''
  type: APIReference
  url: https://newsapi.ai/documentation
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/EventRegistry/newsapi-mcp
created: 2026-06-13
description: Event Registry (NewsAPI.ai) is the world's leading news intelligence platform providing a REST API for accessing global news articles, trending topics, event detection, named entities, sentiment analysis, and media monitoring across 150,000+ sources in 60+ languages, with historical archive access dating back to 2014.
examples:
- key_count: 4
  name: Search Articles
  slug: search-articles
- key_count: 4
  name: Search Events
  slug: search-events
- key_count: 5
  name: Suggest Concepts
  slug: suggest-concepts
finops:
- has_sources: true
  method: derived
  name: Event Registry Finops
  primary_unit: tokens
  service_category: ''
  slug: event-registry-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/event-registry.png
json_schemas:
- name: Article
  property_count: 19
  slug: article
- name: Event
  property_count: 14
  slug: event
jsonld:
- class_count: 40
  name: context Context
  property_count: 1
  slug: context
layout: provider
mcp_servers:
- description: 'Event Registry publishes a first-party Model Context Protocol server, newsapi-mcp, that wraps the Event Registry REST API for LLM clients. It is a LOCAL STDIO server: there is no hosted endpoint an ag'
  name: NewsAPI.ai MCP Server
  slug: newsapi
modified: 2026-08-13
name: Event Registry
nav: Providers
network: true
overview: 'Event Registry publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Events API, Suggest API, and 2 more. Tagged areas include News, Media Monitoring, News Intelligence, Event Detection, and Named Entity Recognition.


  The Event Registry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Event Registry''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, sandbox, signup flow, and 25 more developer resources.'
plans:
- name: Event Registry Plans Pricing
  plan_count: 3
  slug: event-registry-plans-pricing
- name: Event Registry Price Estimates
  plan_count: 0
  slug: event-registry-price-estimates
random_paper: 16
rate_limits:
- limit_count: 2
  name: Event Registry Rate Limits
  slug: event-registry-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Event Registry — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: event-registry-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 33
    catalog_earned: 71.3
    catalog_earned_first_party: 20.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.5
  facets:
    access_clarity: 73.7
    contract_governance: 14.4
    contract_quality: 57.8
    developer_ergonomics: 53.6
    discoverability: 65.0
    operational_transparency: 42.1
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/event-registry/event-registry-2026-06-20T180857.png
security:
- kind: authentication
  name: Event Registry Authentication
  slug: event-registry-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Event Registry Domain Security
  slug: event-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: news
  slug: event-registry-news-research
slug: event-registry
tags:
- News
- Media Monitoring
- News Intelligence
- Event Detection
- Named Entity Recognition
- Sentiment Analysis
- Media Analytics
- News API
website: https://eventregistry.org
---
