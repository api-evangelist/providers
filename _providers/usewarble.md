---
access_model:
  confidence: low
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.usewarble.com
  baseurl_source: declared
  description: 'Warble API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Warble API
  slug: usewarble-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/usewarble/plans/usewarble-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usewarble-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usewarble/rules/usewarble-rules.yml
  title: ''
  type: Spectral
  url: rules/usewarble-rules.yml
- group: design
  href: https://artifacts.apis.io/usewarble/json-ld/usewarble-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usewarble-context.jsonld
- group: design
  href: https://artifacts.apis.io/usewarble/vocabulary/usewarble-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usewarble-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usewarble/data-model/usewarble-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usewarble-data-model.yml
- group: design
  href: https://artifacts.apis.io/usewarble/conformance/usewarble-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usewarble-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usewarble/llms/usewarble-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usewarble-llms.txt
- group: agent
  href: https://artifacts.apis.io/usewarble/well-known/usewarble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usewarble-well-known.yml
- group: other
  href: https://artifacts.apis.io/usewarble/hosts/usewarble-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usewarble-hosts.yml
- group: other
  href: https://artifacts.apis.io/usewarble/vendors/usewarble-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usewarble-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://usewarble.com/sign-up?nosite=1
- group: auth
  href: https://artifacts.apis.io/usewarble/security/usewarble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usewarble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usewarble.com
- group: docs
  title: ''
  type: Documentation
  url: https://usewarble.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://usewarble.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://usewarble.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usewarble.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usewarble.com/privacy
- group: other
  title: ''
  type: SignIn
  url: https://usewarble.com/sign-in
- group: company
  title: ''
  type: About
  url: https://usewarble.com/about
coverage:
  checked: '2026-11-02'
  detail: Developer documentation at https://usewarble.com/developers is a JavaScript‑rendered single‑page app, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://usewarble.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Warble provides an AI‑powered social media manager tailored for small businesses. It reads a website, learns the brand’s voice, and automatically generates a month’s worth of posts which can be reviewed, scheduled, and published across multiple channels. Plans include a free trial, a Basic tier with 120 credits per month, and a Pro tier offering API and MCP access for deeper integration.
image: https://usewarble.com/opengraph-image.png
json_schemas:
- name: GetApiV1AdTemplatesResponse
  property_count: 1
  slug: usewarble-get-api-v1-ad-templates-response
- name: GetApiV1WorkspacesResponse
  property_count: 1
  slug: usewarble-get-api-v1-workspaces-response
- name: PatchApiV1PostsIdRequest
  property_count: 3
  slug: usewarble-patch-api-v1-posts-id-request
- name: PostApiV1AdsResponse
  property_count: 6
  slug: usewarble-post-api-v1-ads-response
- name: PostApiV1PostsRequest
  property_count: 5
  slug: usewarble-post-api-v1-posts-request
- name: PostApiV1UploadsIdCompleteResponse
  property_count: 5
  slug: usewarble-post-api-v1-uploads-id-complete-response
jsonld:
- class_count: 32
  name: Usewarble Context
  property_count: 46
  slug: usewarble-context
layout: provider
modified: '2026-11-02'
name: Warble
nav: Providers
network: true
overview: 'Warble is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Social Media, Small Business, and Automation.


  The Warble catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Warble''s developer surface includes signup flow, documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Usewarble Plans Pricing
  plan_count: 3
  slug: usewarble-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Warble API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 2
  slug: usewarble-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 6.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usewarble Domain Security
  slug: usewarble-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usewarble
tags:
- Company
- Artificial Intelligence
- Social Media
- Small Business
- Automation
website: https://usewarble.com
---
