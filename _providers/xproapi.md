---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xproapi Agentic Access
  operation_count: 19
  slug: xproapi-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://xproapi.com/api
  baseurl_source: spec
  description: The default API from Xproapi — 2 operation(s) for default.
  name: Xproapi Default API
  slug: xproapi-default-api
- baseURL: https://xproapi.com/api
  baseurl_source: spec
  description: The Follow, Followings API from Xproapi — 3 operation(s) for follow, followings.
  name: Xproapi Follow, Followings API
  slug: xproapi-follow-followings-api
- baseURL: https://xproapi.com/api
  baseurl_source: spec
  description: The Tweet Activity API from Xproapi — 8 operation(s) for tweet activity.
  name: Xproapi Tweet Activity API
  slug: xproapi-tweet-activity-api
- baseURL: https://xproapi.com/api
  baseurl_source: spec
  description: The Tweets API from Xproapi — 1 operation(s) for tweets.
  name: Xproapi Tweets API
  slug: xproapi-tweets-api
- baseURL: https://xproapi.com/api
  baseurl_source: spec
  description: The Users API from Xproapi — 5 operation(s) for users.
  name: Xproapi Users API
  slug: xproapi-users-api
artifact_total: 9
asyncapis:
- description: ''
  name: Xproapi Webhooks
  slug: xproapi-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/xproapi/agentic-access/xproapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xproapi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/xproapi/rules/xproapi-rules.yml
  title: ''
  type: Spectral
  url: rules/xproapi-rules.yml
- group: design
  href: https://artifacts.apis.io/xproapi/asyncapi/xproapi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/xproapi-webhooks.yml
- group: design
  href: https://artifacts.apis.io/xproapi/conformance/xproapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xproapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xproapi/llms/xproapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xproapi-llms.txt
- group: other
  href: https://artifacts.apis.io/xproapi/hosts/xproapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xproapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/xproapi/vendors/xproapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xproapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/xproapi/packages/xproapi-packages.yml
  title: ''
  type: Packages
  url: packages/xproapi-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xproapi.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://xproapi.com/sdks/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xproapi.com/privacy
- group: start
  title: ''
  type: Login
  url: https://xproapi.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xproapi-LLC
- group: company
  title: ''
  type: Blog
  url: https://xproapi.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://xproapi.com/blog/getting-started-track-your-first-x-account-in-five-minutes
- group: auth
  href: https://artifacts.apis.io/xproapi/security/xproapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xproapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xproapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://xproapi.com/docs
created: '2026-10-14'
description: Xproapi provides a developer API that monitors X (formerly Twitter) accounts, tracking who they follow and who follows them. It offers daily checks, alerts via Telegram, Discord, or email, and delivers follower/following data through a RESTful API. The service includes pricing tiers, a blog with updates, and clear terms and privacy policies.
layout: provider
modified: '2026-10-14'
name: Xproapi
nav: Providers
network: true
overview: 'Xproapi publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Default API, Follow, Followings API, Tweet Activity API, and 2 more. Tagged areas include Company, X, Social, Monitoring, and Data.


  The Xproapi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Xproapi''s developer surface includes engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Xproapi API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: xproapi-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 28.6
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 19.0
    discoverability: 60.7
    operational_transparency: 10.5
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/xproapi/xproapi-2026-11-03T150311.png
security:
- kind: domain-security
  name: Xproapi Domain Security
  slug: xproapi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: xproapi
tags:
- Company
- X
- Social
- Monitoring
- Data
website: https://xproapi.com
---
