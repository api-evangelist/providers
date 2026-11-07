---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Alma Food Agentic Access
  operation_count: 7
  slug: alma-food-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://www.alma.food
  baseurl_source: declared
  description: Public files agents should fetch first
  name: Alma Discovery API
  slug: alma-food-discovery-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/alma-food/agentic-access/alma-food-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alma-food-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/alma-food/rules/alma-food-rules.yml
  title: ''
  type: Spectral
  url: rules/alma-food-rules.yml
- group: design
  href: https://artifacts.apis.io/alma-food/vocabulary/alma-food-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alma-food-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/alma-food/conformance/alma-food-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alma-food-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alma-food/llms/alma-food-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alma-food-llms.txt
- group: agent
  href: https://artifacts.apis.io/alma-food/well-known/alma-food-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alma-food-well-known.yml
- group: other
  href: https://artifacts.apis.io/alma-food/hosts/alma-food-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alma-food-hosts.yml
- group: other
  href: https://artifacts.apis.io/alma-food/vendors/alma-food-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alma-food-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.alma.food/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.alma.food/developers
- group: auth
  href: https://artifacts.apis.io/alma-food/scopes/alma-food-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/alma-food-scopes.yml
- group: auth
  href: https://artifacts.apis.io/alma-food/authentication/alma-food-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alma-food-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alma-food/security/alma-food-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alma-food-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alma.food/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alma.food/help
- group: operate
  title: ''
  type: Support
  url: https://www.alma.food/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alma.food/privacy-and-terms
created: '2026-11-01'
description: Alma is an AI‑powered nutrition coach and food tracking platform that helps users understand the impact of every meal on their health goals. The service offers personalized meal logging, goal‑based recommendations, and a conversational interface that answers nutrition questions. Alma provides plans for weight loss, muscle building, sport performance, and overall health, integrating with health data and offering insights through its web and mobile apps.
image: https://www.alma.food/og-image.jpg
layout: provider
modified: '2026-11-01'
name: Alma
nav: Providers
network: true
overview: 'Alma publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Discovery API. Tagged areas include Nutrition, Artificial Intelligence, Health, Food Tracking, and Personalization.


  The Alma catalog on APIs.io includes 1 Spectral governance ruleset.


  Alma''s developer surface includes engineering blog, API reference, authentication, documentation, support, and 12 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Alma API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: alma-food-rules
scopes:
- name: Alma Food Scopes
  scope_count: 2
  slug: alma-food-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 43.5
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alma Food Authentication
  slug: alma-food-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Alma Food Domain Security
  slug: alma-food-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alma-food
tags:
- Nutrition
- Artificial Intelligence
- Health
- Food Tracking
- Personalization
- Company
website: https://alma.food/
---
