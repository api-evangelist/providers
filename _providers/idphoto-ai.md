---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Idphoto Ai Agentic Access
  operation_count: 34
  slug: idphoto-ai-agentic-access
  summary_line: 34 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api-us.idphotoapp.com
  baseurl_source: declared
  description: The ID Photo API V1 API from idphoto-ai — 5 operation(s) for id photo api v1.
  name: idphoto-ai ID Photo API V1 API
  slug: idphoto-ai-id-photo-api-v1-api
- baseURL: https://api-us.idphotoapp.com
  baseurl_source: declared
  description: The ID Photo API V2 API from idphoto-ai — 25 operation(s) for id photo api v2.
  name: idphoto-ai ID Photo API V2 API
  slug: idphoto-ai-id-photo-api-v2-api
- baseURL: https://api-us.idphotoapp.com
  baseurl_source: declared
  description: The misc API from idphoto-ai — 4 operation(s) for misc.
  name: idphoto-ai Misc API
  slug: idphoto-ai-misc-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/idphoto-ai/agentic-access/idphoto-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/idphoto-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/idphoto-ai/plans/idphoto-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/idphoto-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/idphoto-ai/rules/idphoto-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/idphoto-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/idphoto-ai/json-ld/idphoto-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/idphoto-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/idphoto-ai/vocabulary/idphoto-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/idphoto-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/idphoto-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/idphoto-ai/data-model/idphoto-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/idphoto-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/idphoto-ai/errors/idphoto-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/idphoto-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/idphoto-ai/conformance/idphoto-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/idphoto-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/idphoto-ai/llms/idphoto-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/idphoto-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/idphoto-ai/hosts/idphoto-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/idphoto-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/idphoto-ai/vendors/idphoto-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/idphoto-ai-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://idphoto.ai/blog/automate-employee-badge-photos-for-hr-onboarding.html
- group: auth
  href: https://artifacts.apis.io/idphoto-ai/security/idphoto-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/idphoto-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://idphoto.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.idphoto.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://idphoto.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://idphoto.ai/docs/api-reference/passport-photo-api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://idphoto.ai/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://idphoto.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://idphoto.ai/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://idphoto.ai/blog/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.idphoto.ai/
created: '2026-10-30'
description: IDPhoto.ai provides an AI-powered API that generates passport, visa, and other identity document photos from a single portrait image. The service automatically removes backgrounds, crops to the exact specifications of over 300 photo standards across more than 200 countries, and performs quality checks to ensure compliance. Designed for integration into mobile apps, kiosks, travel platforms, and any system needing fast, accurate ID-photo processing, with pricing starting at $0.20 per photo.
image: https://idphoto.ai/imgs/og-image.png
json_schemas:
- name: AIEditIn
  property_count: 5
  slug: idphoto-ai-aiedit-in
- name: IdPhotoForSignedUrl
  property_count: 7
  slug: idphoto-ai-id-photo-for-signed-url
- name: IdPhotoIn
  property_count: 15
  slug: idphoto-ai-id-photo-in
- name: IdPhotoOut
  property_count: 20
  slug: idphoto-ai-id-photo-out
- name: PhotoEnhanceIn
  property_count: 7
  slug: idphoto-ai-photo-enhance-in
- name: ReMakePhotoIn
  property_count: 8
  slug: idphoto-ai-re-make-photo-in
jsonld:
- class_count: 40
  name: Idphoto Ai Context
  property_count: 86
  slug: idphoto-ai-context
layout: provider
modified: '2026-10-30'
name: idphoto-ai
nav: Providers
network: true
overview: 'idphoto-ai publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: ID Photo API V1 API, ID Photo API V2 API, and Misc API. Tagged areas include Artificial Intelligence, Photos, Identity, Passport, and Visa.


  The idphoto-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  idphoto-ai''s developer surface includes getting-started guide, documentation, API reference, pricing, engineering blog, signup flow, and 17 more developer resources.'
plans:
- name: Idphoto Ai Plans Pricing
  plan_count: 1
  slug: idphoto-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Idphoto Ai Rate Limits
  slug: idphoto-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: idphoto-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: idphoto-ai-rules
scopes:
- name: Idphoto Ai Scopes
  scope_count: 0
  slug: idphoto-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 50.1
    developer_ergonomics: 26.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/idphoto-ai/idphoto-ai-2026-11-03T133633.png
security:
- kind: authentication
  name: Idphoto Ai Authentication
  slug: idphoto-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Idphoto Ai Domain Security
  slug: idphoto-ai-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: make-id-photo
  slug: idphoto-ai-make-id-photo
slug: idphoto-ai
tags:
- Artificial Intelligence
- Photos
- Identity
- Passport
- Visa
- Image Processing
website: https://idphoto.ai/
---
