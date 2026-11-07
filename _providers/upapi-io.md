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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Upapi Io Agentic Access
  operation_count: 103
  slug: upapi-io-agentic-access
  summary_line: 103 operations · 63 acting
api_count: 1
apis:
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Communication API from upapi-io — 1 operation(s) for communication.
  name: upapi-io Communication API
  slug: upapi-io-communication-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Data API from upapi-io — 6 operation(s) for data.
  name: upapi-io Data API
  slug: upapi-io-data-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Developer Tools API from upapi-io — 17 operation(s) for developer tools.
  name: upapi-io Developer Tools API
  slug: upapi-io-developer-tools-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Finance API from upapi-io — 2 operation(s) for finance.
  name: upapi-io Finance API
  slug: upapi-io-finance-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Maps API from upapi-io — 3 operation(s) for maps.
  name: upapi-io Maps API
  slug: upapi-io-maps-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Media API from upapi-io — 4 operation(s) for media.
  name: upapi-io Media API
  slug: upapi-io-media-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Search API from upapi-io — 4 operation(s) for search.
  name: upapi-io Search API
  slug: upapi-io-search-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The SEO tools API from upapi-io — 5 operation(s) for seo tools.
  name: upapi-io SEO tools API
  slug: upapi-io-seo-tools-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Social Media API from upapi-io — 50 operation(s) for social media.
  name: upapi-io Social Media API
  slug: upapi-io-social-media-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Tools API from upapi-io — 7 operation(s) for tools.
  name: upapi-io Tools API
  slug: upapi-io-tools-api
- baseURL: https://api.upapi.io
  baseurl_source: declared
  description: The Utility API from upapi-io — 4 operation(s) for utility.
  name: upapi-io Utility API
  slug: upapi-io-utility-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/upapi-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/upapi-io/agentic-access/upapi-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/upapi-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/upapi-io/rate-limits/upapi-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/upapi-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/upapi-io/plans/upapi-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/upapi-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/rules/upapi-io-rules.yml
  title: ''
  type: Spectral
  url: rules/upapi-io-rules.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/json-ld/upapi-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/upapi-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/upapi-io/vocabulary/upapi-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/upapi-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/data-model/upapi-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upapi-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/upapi-io/changelog/upapi-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/upapi-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/conventions/upapi-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/upapi-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/conventions/upapi-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/upapi-io-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://upapi.io/terms
- group: auth
  href: https://artifacts.apis.io/upapi-io/authentication/upapi-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upapi-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/lifecycle/upapi-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/upapi-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/errors/upapi-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/upapi-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/upapi-io/conformance/upapi-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upapi-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/upapi-io/llms/upapi-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upapi-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-voicelabs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-voicelabs-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-joinmarka-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-joinmarka-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-getuptimely-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-getuptimely-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-dodomain-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-dodomain-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-aishorty-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upapi-io-aishorty-security.txt
- group: agent
  href: https://artifacts.apis.io/upapi-io/well-known/upapi-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upapi-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/upapi-io/hosts/upapi-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upapi-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/upapi-io/vendors/upapi-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upapi-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/upapi-io/packages/upapi-io-packages.yml
  title: ''
  type: Packages
  url: packages/upapi-io-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://upapi.io/apis/media
- group: operate
  title: ''
  type: ChangeLog
  url: https://upapi.io/docs/changelog
- group: auth
  href: https://artifacts.apis.io/upapi-io/security/upapi-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/upapi-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/upapi-io/security/upapi-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upapi-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upapi.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.upapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://upapi.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://upapi.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://upapi.io/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://app.upapi.io/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevinoSolutions/upapi-mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://upapi.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.upapi.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.upapi.io/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upapi.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upapi.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upapi.io/privacy
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@upapi/sdk
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://upapi.io/openapi.json
  - status: null
    url: https://api.upapi.io/openapi.json
  - status: 401
    url: https://app.upapi.io/api/mcp
  - status: 401
    url: https://api.upapi.io/graphql
  - status: 401
    url: https://api.upapi.io/mcp
  - status: 200
    url: https://upapi.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: upAPI is an API marketplace platform that provides a single API key and gateway to access over 60 production APIs across categories such as media, finance, social media, and more. It offers weighted‑unit billing, per‑operation pricing, and supports multiple programming languages. The service includes a developer portal, documentation, pricing, and support, and is hosted at upapi.io with its API endpoint at api.upapi.io.
image: https://upapi.io/opengraph-image?83e8f20bd27f96b7
jsonld:
- class_count: 1
  name: Upapi Io Context
  property_count: 1
  slug: upapi-io-context
layout: provider
modified: '2026-10-31'
name: upapi-io
nav: Providers
network: true
overview: 'upapi-io publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Communication API, Data API, Developer Tools API, and 8 more. Tagged areas include API Marketplace, Developer Tools, Data, Automation, and Integration.


  The upapi-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  upapi-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 40 more developer resources.'
plans:
- name: Upapi Io Plans Pricing
  plan_count: 4
  slug: upapi-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Upapi Io Rate Limits
  slug: upapi-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: upapi-io API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: upapi-io-rules
scopes:
- name: Upapi Io Scopes
  scope_count: 0
  slug: upapi-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 46.9
    discoverability: 67.0
    operational_transparency: 44.7
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Upapi Io Authentication
  slug: upapi-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Upapi Io Domain Security
  slug: upapi-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Upapi Io Vulnerability Disclosure
  slug: upapi-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: upapi-io
tags:
- API Marketplace
- Developer Tools
- Data
- Automation
- Integration
website: https://upapi.io/
---
