---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.astravue.com
  baseurl_source: declared
  description: 'Astravue API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Astravue API
  slug: astravue-com-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/astravue-com/vendors/astravue-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astravue-com-vendors.yml
- group: operate
  href: https://artifacts.apis.io/astravue-com/rate-limits/astravue-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/astravue-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/astravue-com/plans/astravue-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astravue-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/astravue-com/rules/astravue-com-rules.yml
  title: ''
  type: Spectral
  url: rules/astravue-com-rules.yml
- group: design
  href: https://artifacts.apis.io/astravue-com/json-ld/astravue-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/astravue-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/astravue-com/vocabulary/astravue-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astravue-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/astravue-com/data-model/astravue-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astravue-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/astravue-com/authentication/astravue-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/astravue-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/astravue-com/conformance/astravue-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astravue-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astravue-com/llms/astravue-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astravue-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/astravue-com/well-known/astravue-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astravue-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/astravue-com/hosts/astravue-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astravue-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.astravue.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://astravue.com/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.astravue.com/portal/en/kb/onboarding-with-astravue
- group: docs
  title: ''
  type: Documentation
  url: https://docs.astravue.com/
- group: auth
  href: https://artifacts.apis.io/astravue-com/security/astravue-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astravue-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astravue.com/
- group: company
  title: ''
  type: Blog
  url: https://astravue.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://astravue.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astravue.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astravue.com/privacy-policy/
created: '2026-11-01'
description: Astravue provides project profitability software tailored for agencies and professional services firms. The platform delivers real-time margin visibility per project, automatically flags idle capacity, surfaces unbilled hours, and catches scope-creep the moment it occurs. With dashboards, forecasting tools, and integrations to popular workflows, Astravue helps firms maximize revenue, control costs, and prevent budget overruns.
image: https://astravue.com/wp-content/uploads/2026/10/1_1-512px-_-512-px.jpg-1.jpeg
json_schemas:
- name: GetV1TasksCommentsResponse
  property_count: 5
  slug: astravue-com-get-v1-tasks-comments-response
- name: PostV1SpacesProjectsResponse
  property_count: 22
  slug: astravue-com-post-v1-spaces-projects-response
- name: PostV1SpacesProjectsTasksResponse
  property_count: 22
  slug: astravue-com-post-v1-spaces-projects-tasks-response
- name: PostV1TimeTrackProjectsTasksManualResponse
  property_count: 5
  slug: astravue-com-post-v1-time-track-projects-tasks-manual-response
- name: PostV1TimeTrackProjectsTasksRangeResponse
  property_count: 5
  slug: astravue-com-post-v1-time-track-projects-tasks-range-response
- name: PutV1SpacesProjectsResponse
  property_count: 22
  slug: astravue-com-put-v1-spaces-projects-response
jsonld:
- class_count: 34
  name: Astravue Com Context
  property_count: 82
  slug: astravue-com-context
layout: provider
modified: '2026-11-01'
name: Astravue
nav: Providers
network: true
overview: 'Astravue is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, Profitability, Software-as-a-Service, Agencies, and Professional Services.


  The Astravue catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Astravue''s developer surface includes authentication, support, changelog, getting-started guide, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Astravue Com Plans Pricing
  plan_count: 3
  slug: astravue-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Astravue Com Rate Limits
  slug: astravue-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Astravue API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: astravue-com-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 45.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
security:
- kind: authentication
  name: Astravue Com Authentication
  slug: astravue-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Astravue Com Domain Security
  slug: astravue-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: astravue-com
tags:
- Project Management
- Profitability
- Software-as-a-Service
- Agencies
- Professional Services
website: https://astravue.com/
---
