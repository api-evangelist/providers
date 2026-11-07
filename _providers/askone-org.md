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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for AskOne moderation platform, documented at https://askone.org/docs
  name: AskOne API
  slug: askone-api
- description: 'AskOne API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: AskOne API
  slug: askone-org-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/askone-org/rules/askone-org-rules.yml
  title: ''
  type: Spectral
  url: rules/askone-org-rules.yml
- group: design
  href: https://artifacts.apis.io/askone-org/json-ld/askone-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/askone-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/askone-org/vocabulary/askone-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/askone-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/askone-org/data-model/askone-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/askone-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/askone-org/conformance/askone-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/askone-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/askone-org/well-known/askone-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askone-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/askone-org/hosts/askone-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askone-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/askone-org/vendors/askone-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askone-org-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.askone.org/
- group: auth
  href: https://artifacts.apis.io/askone-org/security/askone-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askone-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askone.org/
- group: docs
  title: ''
  type: Documentation
  url: https://askone.org/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://askone.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://askone.org/sign-up
- group: other
  title: ''
  type: SignIn
  url: https://askone.org/sign-in
- group: operate
  title: ''
  type: Support
  url: https://askone.org/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askone.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askone.org/privacy
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://askone.org/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AskOne provides a free moderation platform for live Q&A sessions, allowing audiences to submit questions via phone without needing an account. It offers real‑time ranking, moderator controls, and AI assistance across multiple rooms, with flexible pricing for larger events and branding options. The service supports webinars, workshops, and all‑hands meetings, emphasizing ease of use and no‑cost moderation for basic usage.
image: https://askone.org/opengraph-image?1c1f00c55a918ed6
json_schemas:
- name: GetRoomsCodeResponse
  property_count: 3
  slug: askone-org-get-rooms-code-response
- name: GetRoomsCodeSurveysResponse
  property_count: 2
  slug: askone-org-get-rooms-code-surveys-response
- name: PostRoomsCodeSurveysRequest
  property_count: 12
  slug: askone-org-post-rooms-code-surveys-request
- name: PostRoomsCodeSurveysResponse
  property_count: 6
  slug: askone-org-post-rooms-code-surveys-response
- name: PostRoomsRequest
  property_count: 5
  slug: askone-org-post-rooms-request
- name: PostRoomsResponse
  property_count: 5
  slug: askone-org-post-rooms-response
jsonld:
- class_count: 8
  name: Askone Org Context
  property_count: 25
  slug: askone-org-context
layout: provider
modified: '2026-11-01'
name: AskOne
nav: Providers
network: true
overview: 'AskOne is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Moderation, LiveQ&A, Audience Engagement, WebinarTools, and FreePlatform.


  The AskOne catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AskOne''s developer surface includes documentation, pricing, signup flow, support, and 14 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: AskOne API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: askone-org-rules
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 29.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
- kind: domain-security
  name: Askone Org Domain Security
  slug: askone-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: askone-org
tags:
- Moderation
- LiveQ&A
- Audience Engagement
- WebinarTools
- FreePlatform
website: https://askone.org/
---
