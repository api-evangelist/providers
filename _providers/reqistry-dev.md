---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 3
  name: Reqistry Dev Agentic Access
  operation_count: 66
  slug: reqistry-dev-agentic-access
  summary_line: 66 operations · 31 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Reqistry provides a public JSON API for catalog search, categories, and API details, offering endpoints for searching APIs, retrieving categories, and accessing API metadata without authentication.
  name: Reqistry API
  slug: reqistry-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The AgentKeys API from reqistry-dev — 3 operation(s) for agentkeys.
  name: reqistry-dev Agent Keys API
  slug: reqistry-dev-agentkeys-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The API Detail API from reqistry-dev — 4 operation(s) for api detail.
  name: reqistry-dev API Detail API
  slug: reqistry-dev-api-detail-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Anonymous device authentication (v1)
  name: reqistry-dev Auth API
  slug: reqistry-dev-auth-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: User API bookmarks (v1)
  name: reqistry-dev Bookmarks API
  slug: reqistry-dev-bookmarks-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Browse and list API categories
  name: reqistry-dev Categories API
  slug: reqistry-dev-categories-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The Contact API from reqistry-dev — 1 operation(s) for contact.
  name: reqistry-dev Contact API
  slug: reqistry-dev-contact-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: API discovery — recently added, recommendations
  name: reqistry-dev Discover API
  slug: reqistry-dev-discover-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: User API folders (v1)
  name: reqistry-dev Folders API
  slug: reqistry-dev-folders-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Trust scores, stack, comparison, change feed, and curated collections
  name: reqistry-dev Growth API
  slug: reqistry-dev-growth-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Server health and status
  name: reqistry-dev Health API
  slug: reqistry-dev-health-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: URL metadata extraction
  name: reqistry-dev Metadata API
  slug: reqistry-dev-metadata-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: FCM token management, preferences, and notification event tracking
  name: reqistry-dev Notifications API
  slug: reqistry-dev-notifications-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The Projects API from reqistry-dev — 2 operation(s) for projects.
  name: reqistry-dev Projects API
  slug: reqistry-dev-projects-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The Public APIs — Mobile Client API API from reqistry-dev — 1 operation(s) for public apis — mobile client api.
  name: reqistry-dev Public APIs — Mobile Client API
  slug: reqistry-dev-public-apis-mobile-client-api-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: FCM token management for push notifications
  name: reqistry-dev Push Notifications API
  slug: reqistry-dev-push-notifications-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The Reports API from reqistry-dev — 1 operation(s) for reports.
  name: reqistry-dev Reports API
  slug: reqistry-dev-reports-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Full-text search across the API catalog
  name: reqistry-dev Search API
  slug: reqistry-dev-search-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Submit an API for review
  name: reqistry-dev Submit API
  slug: reqistry-dev-submit-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: Page event tracking
  name: reqistry-dev Tracking API
  slug: reqistry-dev-tracking-api
- baseURL: https://api.reqistry.dev
  baseurl_source: declared
  description: The Watchlists API from reqistry-dev — 2 operation(s) for watchlists.
  name: reqistry-dev Watchlists API
  slug: reqistry-dev-watchlists-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/reqistry-dev/agentic-access/reqistry-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reqistry-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/reqistry-dev/rate-limits/reqistry-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reqistry-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/reqistry-dev/plans/reqistry-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reqistry-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/reqistry-dev/rules/reqistry-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/reqistry-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/reqistry-dev/json-ld/reqistry-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/reqistry-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/reqistry-dev/vocabulary/reqistry-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reqistry-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/reqistry-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/reqistry-dev/data-model/reqistry-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reqistry-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/reqistry-dev/changelog/reqistry-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/reqistry-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/reqistry-dev/conventions/reqistry-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reqistry-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/reqistry-dev/authentication/reqistry-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reqistry-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/reqistry-dev/errors/reqistry-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reqistry-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reqistry-dev/conformance/reqistry-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reqistry-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/reqistry-dev/llms/reqistry-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reqistry-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/reqistry-dev/hosts/reqistry-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reqistry-dev-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://reqistry.dev/categories/security
- group: company
  title: ''
  type: Newsroom
  url: https://reqistry.dev/apis/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://reqistry.dev/changelog
- group: auth
  href: https://artifacts.apis.io/reqistry-dev/security/reqistry-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reqistry-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reqistry.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reqistry.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://api.reqistry.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reqistry.dev/quickstart
- group: operate
  title: ''
  type: Support
  url: https://reqistry.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reqistry.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reqistry.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.reqistry.dev/pricing
coverage:
  checked: '2026-10-31'
  detail: The OpenAPI spec at https://api.reqistry.dev/openapi.json is a placeholder with localhost servers and does not belong to Reqistry.
  evidence:
  - status: 200
    url: https://api.reqistry.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Reqistry is an API intelligence platform for builders and agents, offering a searchable catalog of over 3,000 public APIs across dozens of categories. It provides a free public JSON API for searching, comparing, and retrieving detailed metadata about APIs, including health scores, authentication methods, pricing, and rate limits. The service includes a developer portal with documentation, quickstart guides, and an MCP server for agent integration. Users can monitor API changes, receive alerts, and explore pricing plans. The platform aims to help developers choose reliable APIs and stay informed about updates.
image: https://reqistry.dev/reqistry.svg
jsonld:
- class_count: 76
  name: Reqistry Dev Context
  property_count: 146
  slug: reqistry-dev-context
layout: provider
modified: '2026-10-31'
name: reqistry-dev
nav: Providers
network: true
overview: 'reqistry-dev publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Keys API, API Detail API, Auth API, and 18 more. Tagged areas include Company, Catalog, Intelligence, Builder, and Agents.


  The reqistry-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  reqistry-dev''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 20 more developer resources.'
plans:
- name: Reqistry Dev Plans Pricing
  plan_count: 1
  slug: reqistry-dev-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Reqistry Dev Rate Limits
  slug: reqistry-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: reqistry-dev API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: reqistry-dev-rules
scopes:
- name: Reqistry Dev Scopes
  scope_count: 0
  slug: reqistry-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 73.8
    catalog_earned_first_party: 20.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 52.5
    developer_ergonomics: 35.0
    discoverability: 67.0
    operational_transparency: 44.7
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reqistry-dev/reqistry-dev-2026-11-03T142202.png
security:
- kind: authentication
  name: Reqistry Dev Authentication
  slug: reqistry-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Reqistry Dev Domain Security
  slug: reqistry-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: search-apis
  slug: search-apis
slug: reqistry-dev
tags:
- Company
- Catalog
- Intelligence
- Builder
- Agents
website: https://reqistry.dev/
---
