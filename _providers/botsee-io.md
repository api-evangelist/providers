---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://botsee.io
  baseurl_source: declared
  description: BotSee API for monitoring AI visibility
  name: BotSee API
  slug: botsee-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/botsee-io/rate-limits/botsee-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/botsee-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/botsee-io/json-ld/botsee-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botsee-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/botsee-io/vocabulary/botsee-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botsee-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botsee-io/data-model/botsee-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botsee-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/botsee-io/authentication/botsee-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botsee-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/botsee-io/conformance/botsee-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botsee-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botsee-io/llms/botsee-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botsee-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/botsee-io/well-known/botsee-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botsee-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/botsee-io/hosts/botsee-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botsee-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/botsee-io/vendors/botsee-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botsee-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botsee.io/privacy
- group: start
  title: ''
  type: Login
  url: https://botsee.io/login
- group: company
  title: ''
  type: Blog
  url: https://botsee.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://botsee.io/docs#skill
- group: docs
  title: ''
  type: APIReference
  url: https://botsee.io/docs
- group: auth
  href: https://artifacts.apis.io/botsee-io/security/botsee-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botsee-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botsee.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://botsee.io/mcp
  - status: 200
    url: https://botsee.io/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Botsee.io provides AI visibility auditing tools for ChatGPT, Claude, and other LLMs, offering a GEO API for agents to monitor how AI assistants reference your brand. The platform includes dashboards, charts, and a suite of APIs for developers and agencies to integrate AI visibility data into their products, enabling insights into mentions, competitor recommendations, and regional visibility trends.
image: https://botsee.io/images/botsee-og-image.png
jsonld:
- class_count: 8
  name: Botsee Io Context
  property_count: 35
  slug: botsee-io-context
layout: provider
modified: '2026-10-30'
name: botsee-io
nav: Providers
network: true
overview: 'botsee-io is listed with 1 API on the [APIs.io](https://apis.io/) network: BotSee API. Tagged areas include Company, Artificial Intelligence, Visibility, Analytics, and LLM.


  The botsee-io catalog on APIs.io includes 1 JSON-LD context.


  botsee-io''s developer surface includes authentication, engineering blog, getting-started guide, API reference, and 13 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Botsee Io Rate Limits
  slug: botsee-io-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.3
    catalog_earned_first_party: 8.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 35.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/botsee-io/botsee-io-2026-11-03T122343.png
security:
- kind: authentication
  name: Botsee Io Authentication
  slug: botsee-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Botsee Io Domain Security
  slug: botsee-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: botsee-io-skill
  slug: botsee-io-skill
slug: botsee-io
tags:
- Company
- Artificial Intelligence
- Visibility
- Analytics
- LLM
website: https://botsee.io/
---
