---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Desearch Ai Agentic Access
  operation_count: 60
  slug: desearch-ai-agentic-access
  summary_line: 60 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The AI Search API from desearch-ai — 3 operation(s) for ai search.
  name: desearch-ai AI Search API
  slug: desearch-ai-ai-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The Company Search API from desearch-ai — 9 operation(s) for company search.
  name: desearch-ai Company Search API
  slug: desearch-ai-company-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The Facebook Search API from desearch-ai — 6 operation(s) for facebook search.
  name: desearch-ai Facebook Search API
  slug: desearch-ai-facebook-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The Instagram Search API from desearch-ai — 6 operation(s) for instagram search.
  name: desearch-ai Instagram Search API
  slug: desearch-ai-instagram-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The Network Stats API from desearch-ai — 3 operation(s) for network stats.
  name: desearch-ai Network Stats API
  slug: desearch-ai-network-stats-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The People Search API from desearch-ai — 13 operation(s) for people search.
  name: desearch-ai People Search API
  slug: desearch-ai-people-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The Search API from desearch-ai — 1 operation(s) for search.
  name: desearch-ai Search API
  slug: desearch-ai-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The TikTok Search API from desearch-ai — 7 operation(s) for tiktok search.
  name: desearch-ai TikTok Search API
  slug: desearch-ai-tiktok-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The Web Search API from desearch-ai — 3 operation(s) for web search.
  name: desearch-ai Web Search API
  slug: desearch-ai-web-search-api
- baseURL: https://api.desearch.ai
  baseurl_source: declared
  description: The X Search API from desearch-ai — 9 operation(s) for x search.
  name: desearch-ai X Search API
  slug: desearch-ai-x-search-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/desearch-ai/agentic-access/desearch-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/desearch-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/desearch-ai/plans/desearch-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/desearch-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/rules/desearch-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/desearch-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/json-ld/desearch-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/desearch-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/desearch-ai/vocabulary/desearch-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/desearch-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/desearch-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/data-model/desearch-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/desearch-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/conventions/desearch-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/desearch-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/conventions/desearch-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/desearch-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.desearch.ai/security
- group: auth
  href: https://artifacts.apis.io/desearch-ai/authentication/desearch-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/desearch-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/errors/desearch-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/desearch-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/desearch-ai/conformance/desearch-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/desearch-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/desearch-ai/llms/desearch-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/desearch-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/desearch-ai/hosts/desearch-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/desearch-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/desearch-ai/vendors/desearch-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/desearch-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/desearch-ai/packages/desearch-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/desearch-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/desearch-ai/packages/desearch-ai-packages.yml
  title: ''
  type: Packages
  url: packages/desearch-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.desearch.ai/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.desearch.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.desearch.ai/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/desearch-ai/security/desearch-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/desearch-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/desearch-ai/security/desearch-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/desearch-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/desearch-ai/security/desearch-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desearch-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://desearch.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.desearch.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.desearch.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.desearch.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.desearch.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Desearch-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.desearch.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.desearch.ai/privacy
created: '2026-10-30'
description: Desearch is a search API for AI agents on Bittensor. Subnet 22 builds Desearch's web index, and Desearch runs the search API on top of it. It returns current, source-linked context from the web and X (Twitter). One API key covers AI Search, Web Search, Extract, and X Search, so an agent can search, read pages, pull X data, or get an answer grounded in the returned sources.
image: https://www.desearch.ai/logo.png
json_schemas:
- name: CompanySearchRequest
  property_count: 9
  slug: desearch-ai-company-search-request
- name: CompanyTask
  property_count: 26
  slug: desearch-ai-company-task
- name: PeopleTask
  property_count: 25
  slug: desearch-ai-people-task
- name: ResponseData
  property_count: 8
  slug: desearch-ai-response-data
- name: ScraperStreamingSynapseRequest
  property_count: 15
  slug: desearch-ai-scraper-streaming-synapse-request
- name: TwitterScraperTweet
  property_count: 31
  slug: desearch-ai-twitter-scraper-tweet
jsonld:
- class_count: 120
  name: Desearch Ai Context
  property_count: 313
  slug: desearch-ai-context
layout: provider
modified: '2026-10-30'
name: desearch-ai
nav: Providers
network: true
overview: 'desearch-ai publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Search API, Company Search API, Facebook Search API, and 7 more. Tagged areas include Artificial Intelligence, Search, Web, Bittensor, and Company.


  The desearch-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  desearch-ai''s developer surface includes authentication, API reference, documentation, pricing, engineering blog, support, and 26 more developer resources.'
plans:
- name: Desearch Ai Plans Pricing
  plan_count: 10
  slug: desearch-ai-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: desearch-ai API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: desearch-ai-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 65.6
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/desearch-ai/desearch-ai-2026-11-03T130541.png
security:
- kind: authentication
  name: Desearch Ai Authentication
  slug: desearch-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Desearch Ai Domain Security
  slug: desearch-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Desearch Ai Vulnerability Disclosure
  slug: desearch-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Desearch Ai Trust Center
  slug: desearch-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 1
skills:
- name: search
  slug: desearch-ai-search
slug: desearch-ai
tags:
- Artificial Intelligence
- Search
- Web
- Bittensor
- Company
website: https://desearch.ai/
---
