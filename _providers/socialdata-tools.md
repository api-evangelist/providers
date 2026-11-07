---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Socialdata Tools Agentic Access
  operation_count: 144
  slug: socialdata-tools-agentic-access
  summary_line: 144 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for retrieving data from Twitter
  name: socialdata-tools Data API
  slug: socialdata-tools-data-api-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for creating and managing your monitors
  name: socialdata-tools Monitoring API
  slug: socialdata-tools-monitoring-api-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for validating social actions Twitter
  name: socialdata-tools Social Actions API
  slug: socialdata-tools-social-actions-api-api
- baseURL: https://api.socialdata.tools
  baseurl_source: declared
  description: Endpoints for managing your SocialData account
  name: socialdata-tools SocialData Account Management API
  slug: socialdata-tools-socialdata-account-management-api
artifact_total: 22
asyncapis:
- description: ''
  name: Socialdata Tools Webhooks
  slug: socialdata-tools-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/socialdata-tools/agentic-access/socialdata-tools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/socialdata-tools-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/socialdata-tools/rate-limits/socialdata-tools-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/socialdata-tools-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/socialdata-tools/plans/socialdata-tools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socialdata-tools-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/socialdata-tools/rules/socialdata-tools-rules.yml
  title: ''
  type: Spectral
  url: rules/socialdata-tools-rules.yml
- group: design
  href: https://artifacts.apis.io/socialdata-tools/json-ld/socialdata-tools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/socialdata-tools-context.jsonld
- group: design
  href: https://artifacts.apis.io/socialdata-tools/vocabulary/socialdata-tools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/socialdata-tools-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/socialdata-tools/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/socialdata-tools/asyncapi/socialdata-tools-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/socialdata-tools-webhooks.yml
- group: design
  href: https://artifacts.apis.io/socialdata-tools/data-model/socialdata-tools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/socialdata-tools-data-model.yml
- group: auth
  href: https://artifacts.apis.io/socialdata-tools/authentication/socialdata-tools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socialdata-tools-authentication.yml
- group: design
  href: https://artifacts.apis.io/socialdata-tools/errors/socialdata-tools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/socialdata-tools-problem-types.yml
- group: design
  href: https://artifacts.apis.io/socialdata-tools/conformance/socialdata-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socialdata-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socialdata-tools/llms/socialdata-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialdata-tools-llms.txt
- group: agent
  href: https://artifacts.apis.io/socialdata-tools/well-known/socialdata-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/socialdata-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/socialdata-tools/hosts/socialdata-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialdata-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/socialdata-tools/vendors/socialdata-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/socialdata-tools-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://socialdata.tools/login
- group: docs
  title: ''
  type: APIReference
  url: https://docs.socialdata.tools/reference/get-user-profile/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.socialdata.tools</span
- group: auth
  href: https://artifacts.apis.io/socialdata-tools/security/socialdata-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialdata-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialdata.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socialdata.tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socialdata.tools/getting-started/overview/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.socialdata.tools/getting-started/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.socialdata.tools/getting-started/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.socialdata.tools/getting-started/rate-limits/
- group: design
  title: ''
  type: Errors
  url: https://docs.socialdata.tools/getting-started/errors/
- group: operate
  title: ''
  type: Support
  url: https://docs.socialdata.tools/getting-started/getting-help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialdata.tools/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialdata.tools/legal/privacy-policy
created: '2026-10-31'
description: SocialData Tools provides a public API for accessing X (formerly Twitter) data on a per‑result pricing model. Users can retrieve profiles, tweets, followers, mentions, and related analytics via simple REST endpoints without needing OAuth or complex SDKs. The service emphasizes ease‑of‑use, transparent pricing ($0.20 per 1,000 results), and instant access for developers, data scientists, and AI assistants. It offers comprehensive documentation, quick‑start guides, and a sandbox for testing. The platform aims to democratize public social media data for research, monitoring, and application development.
image: https://socialdata.tools/og/OGCard-Main.png
json_schemas:
- name: Community
  property_count: 13
  slug: socialdata-tools-community
- name: MonitorEvent
  property_count: 4
  slug: socialdata-tools-monitor-event
- name: Monitor
  property_count: 7
  slug: socialdata-tools-monitor
- name: Tweet
  property_count: 27
  slug: socialdata-tools-tweet
- name: TweetWithMarkdown
  property_count: 30
  slug: socialdata-tools-tweet-with-markdown
- name: User
  property_count: 18
  slug: socialdata-tools-user
jsonld:
- class_count: 22
  name: Socialdata Tools Context
  property_count: 93
  slug: socialdata-tools-context
layout: provider
modified: '2026-10-31'
name: socialdata-tools
nav: Providers
network: true
overview: 'socialdata-tools publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Monitoring API, Social Actions API, and 1 more. Tagged areas include Company, Social Media, Data, and Public APIs.


  The socialdata-tools catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  socialdata-tools'' developer surface includes authentication, API reference, documentation, getting-started guide, pricing, support, and 24 more developer resources.'
plans:
- name: Socialdata Tools Plans Pricing
  plan_count: 8
  slug: socialdata-tools-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Socialdata Tools Rate Limits
  slug: socialdata-tools-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: socialdata-tools API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: socialdata-tools-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 74.3
    developer_ergonomics: 29.2
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/socialdata-tools/socialdata-tools-2026-11-03T143422.png
security:
- kind: authentication
  name: Socialdata Tools Authentication
  slug: socialdata-tools-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Socialdata Tools Domain Security
  slug: socialdata-tools-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: get-tweet
  slug: get-tweet
- name: get-user-profile
  slug: get-user-profile
- name: socialdata-tools-create-user-tweets-monitor
  slug: socialdata-tools-create-user-tweets-monitor
- name: socialdata-tools-fetch-user-tweets
  slug: socialdata-tools-fetch-user-tweets
slug: socialdata-tools
tags:
- Company
- Social Media
- Data
- Public APIs
website: https://socialdata.tools/
---
