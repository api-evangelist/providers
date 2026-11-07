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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Prismareviews Agentic Access
  operation_count: 19
  slug: prismareviews-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: Connect platform accounts by OAuth, credentials or listing URL, or with a connect link.
  name: Prisma Reviews Connections API
  slug: prismareviews-connections-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: The places, apps, shops and listings that receive reviews.
  name: Prisma Reviews Locations API
  slug: prismareviews-locations-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: How each platform connects, the fields it needs and whether your workspace can connect it.
  name: Prisma Reviews Platforms API
  slug: prismareviews-platforms-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: Publish and delete replies through each platform's official API.
  name: Prisma Reviews Replies API
  slug: prismareviews-replies-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: Reviews from every connected location, in one JSON shape.
  name: Prisma Reviews Reviews API
  slug: prismareviews-reviews-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: Review statistics per workspace, location or platform.
  name: Prisma Reviews Stats API
  slug: prismareviews-stats-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: Your plan and this month's usage.
  name: Prisma Reviews Usage API
  slug: prismareviews-usage-api
- baseURL: https://api.prismareviews.com
  baseurl_source: declared
  description: Signed event deliveries to your HTTPS endpoints.
  name: Prisma Reviews Webhooks API
  slug: prismareviews-webhooks-api
artifact_total: 29
asyncapis:
- description: ''
  name: Prismareviews Webhooks
  slug: prismareviews-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/prismareviews/agentic-access/prismareviews-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prismareviews-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/prismareviews/rate-limits/prismareviews-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prismareviews-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/prismareviews/plans/prismareviews-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prismareviews-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/rules/prismareviews-rules.yml
  title: ''
  type: Spectral
  url: rules/prismareviews-rules.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/json-ld/prismareviews-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prismareviews-context.jsonld
- group: design
  href: https://artifacts.apis.io/prismareviews/vocabulary/prismareviews-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prismareviews-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/prismareviews/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/asyncapi/prismareviews-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/prismareviews-webhooks.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/data-model/prismareviews-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prismareviews-data-model.yml
- group: operate
  href: https://artifacts.apis.io/prismareviews/changelog/prismareviews-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/prismareviews-changelog.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/conventions/prismareviews-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/prismareviews-conventions.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/conventions/prismareviews-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prismareviews-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://prismareviews.com/security
- group: auth
  href: https://artifacts.apis.io/prismareviews/authentication/prismareviews-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prismareviews-authentication.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/errors/prismareviews-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prismareviews-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prismareviews/conformance/prismareviews-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prismareviews-conformance.yml
- group: agent
  href: https://artifacts.apis.io/prismareviews/llms/prismareviews-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prismareviews-llms.txt
- group: agent
  href: https://artifacts.apis.io/prismareviews/mcp/prismareviews-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prismareviews-mcp.yml
- group: agent
  href: https://artifacts.apis.io/prismareviews/well-known/prismareviews-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prismareviews-well-known.yml
- group: other
  href: https://artifacts.apis.io/prismareviews/hosts/prismareviews-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prismareviews-hosts.yml
- group: other
  href: https://artifacts.apis.io/prismareviews/vendors/prismareviews-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prismareviews-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prismareviews.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://prismareviews.com/status
- group: auth
  title: ''
  type: Security
  url: https://prismareviews.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prismareviews.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://prismareviews.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://prismareviews.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://app.prismareviews.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://prismareviews.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/prismareviews/security/prismareviews-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/prismareviews-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/prismareviews/security/prismareviews-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prismareviews-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prismareviews/security/prismareviews-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prismareviews-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prismareviews.com/
- group: docs
  title: ''
  type: Documentation
  url: https://prismareviews.com/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://prismareviews.com/openapi.json
  - status: 401
    url: https://api.prismareviews.com/mcp
  - status: 200
    url: https://prismareviews.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Prisma Reviews is a unified reviews API built by Sopa Lab SL in Madrid, Spain. It aggregates reviews from Google, App Store, Google Play, Tripadvisor, Booking.com, Yelp, Trustpilot and more, providing a single API and webhook to read, monitor and reply to reviews. The service operates under GDPR, offers free tier for two locations and paid plans starting at €49, and is independent of the platforms it connects to.
image: https://prismareviews.com/og/index.png
json_schemas:
- name: Location
  property_count: 12
  slug: prismareviews-location
- name: PlatformId
  property_count: 0
  slug: prismareviews-platform-id
- name: Platform
  property_count: 12
  slug: prismareviews-platform
- name: Review
  property_count: 12
  slug: prismareviews-review
- name: Stats
  property_count: 12
  slug: prismareviews-stats
- name: Usage
  property_count: 7
  slug: prismareviews-usage
jsonld:
- class_count: 24
  name: Prismareviews Context
  property_count: 67
  slug: prismareviews-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.prismareviews.com requiring an API key.
  name: Prisma Reviews MCP Server
  slug: prismareviews-mcp-yml
modified: '2026-11-02'
name: Prisma Reviews
nav: Providers
network: true
overview: 'Prisma Reviews publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connections API, Locations API, Platforms API, and 5 more. Tagged areas include Company, Reviews, Software-as-a-Service, GDPR, and Spain.


  The Prisma Reviews catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Prisma Reviews'' developer surface includes changelog, authentication, pricing, signup flow, getting-started guide, documentation, and 28 more developer resources.'
plans:
- name: Prismareviews Plans Pricing
  plan_count: 5
  slug: prismareviews-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 11
  name: Prismareviews Rate Limits
  slug: prismareviews-rate-limits
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: Prisma Reviews API Rules
  rule_count: 72
  severity_counts:
    error: 66
    hint: 0
    info: 2
    warn: 4
  slug: prismareviews-rules
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 76.0
    developer_ergonomics: 24.4
    discoverability: 65.0
    operational_transparency: 60.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Prismareviews Authentication
  slug: prismareviews-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Prismareviews Domain Security
  slug: prismareviews-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prismareviews Vulnerability Disclosure
  slug: prismareviews-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Prismareviews Trust Center
  slug: prismareviews-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 4
skills:
- name: prismareviews-create-and-delete-connection
  slug: prismareviews-create-and-delete-connection
- name: prismareviews-locations-refresh
  slug: prismareviews-locations-refresh
- name: prismareviews-manage-reply
  slug: prismareviews-manage-reply
- name: prismareviews-webhook-management
  slug: prismareviews-webhook-management
slug: prismareviews
tags:
- Company
- Reviews
- Software-as-a-Service
- GDPR
- Spain
website: https://prismareviews.com/
---
