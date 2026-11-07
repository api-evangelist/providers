---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Daxoom Com Agentic Access
  operation_count: 23
  slug: daxoom-com-agentic-access
  summary_line: 23 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.daxoom.com
  baseurl_source: declared
  description: AI visibility analytics for your businesses
  name: Daxoom Analytics API
  slug: daxoom-com-analytics-api
- baseURL: https://api.daxoom.com
  baseurl_source: declared
  description: Manage your API keys
  name: Daxoom API Keys API
  slug: daxoom-com-api-keys-api
- baseURL: https://api.daxoom.com
  baseurl_source: declared
  description: Search and retrieve verified business profiles
  name: Daxoom Businesses API
  slug: daxoom-com-businesses-api
- baseURL: https://api.daxoom.com
  baseurl_source: declared
  description: Browse the business category catalog
  name: Daxoom Categories API
  slug: daxoom-com-categories-api
- baseURL: https://api.daxoom.com
  baseurl_source: declared
  description: Semantic and natural language search
  name: Daxoom Search API
  slug: daxoom-com-search-api
- baseURL: https://api.daxoom.com
  baseurl_source: declared
  description: Health checks and status
  name: Daxoom System API
  slug: daxoom-com-system-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/daxoom-com/agentic-access/daxoom-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/daxoom-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/daxoom-com/rules/daxoom-com-rules.yml
  title: ''
  type: Spectral
  url: rules/daxoom-com-rules.yml
- group: design
  href: https://artifacts.apis.io/daxoom-com/json-ld/daxoom-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/daxoom-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/daxoom-com/vocabulary/daxoom-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/daxoom-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/daxoom-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/daxoom-com/data-model/daxoom-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/daxoom-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/daxoom-com/errors/daxoom-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/daxoom-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/daxoom-com/conformance/daxoom-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daxoom-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daxoom-com/llms/daxoom-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daxoom-com-llms.txt
- group: other
  href: https://artifacts.apis.io/daxoom-com/hosts/daxoom-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daxoom-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/daxoom-com/vendors/daxoom-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daxoom-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daxoom.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://app.daxoom.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daxoom.com/privacy/
- group: docs
  title: ''
  type: APIReference
  url: https://daxoom.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/daxoom-com/authentication/daxoom-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daxoom-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/daxoom-com/security/daxoom-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daxoom-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.daxoom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.daxoom.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daxoom.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.daxoom.com/blog
created: '2026-11-05'
description: Daxoom helps local businesses publish verified menus, services, hours, prices, and AI‑ready facts so assistants and agents can answer customer questions from a source the business controls. It offers a public REST API, MCP server, and tools for AI agents to retrieve structured business data, with free and paid plans for developers.
image: https://www.daxoom.com/og-card.png
json_schemas:
- name: AnalyticsOverviewResponse
  property_count: 1
  slug: daxoom-com-analytics-overview-response
- name: ApiKeyInfo
  property_count: 8
  slug: daxoom-com-api-key-info
- name: BusinessSummary
  property_count: 17
  slug: daxoom-com-business-summary
- name: OfferingsResponse
  property_count: 1
  slug: daxoom-com-offerings-response
- name: Pagination
  property_count: 5
  slug: daxoom-com-pagination
- name: VisibilityReport
  property_count: 8
  slug: daxoom-com-visibility-report
jsonld:
- class_count: 33
  name: Daxoom Com Context
  property_count: 129
  slug: daxoom-com-context
layout: provider
modified: '2026-11-05'
name: Daxoom
nav: Providers
network: true
overview: 'Daxoom publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, API Keys API, Businesses API, and 3 more. Tagged areas include Local Business Data, AI Agents, Verified Profiles, POS Integration, and Analytics.


  The Daxoom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Daxoom''s developer surface includes signup flow, API reference, authentication, documentation, pricing, engineering blog, and 15 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Daxoom API Rules
  rule_count: 67
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 8
  slug: daxoom-com-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 64.8
    developer_ergonomics: 37.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Daxoom Com Authentication
  slug: daxoom-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Daxoom Com Domain Security
  slug: daxoom-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-business
  slug: daxoom-com-get-business
slug: daxoom-com
tags:
- Local Business Data
- AI Agents
- Verified Profiles
- POS Integration
- Analytics
website: https://www.daxoom.com/
---
