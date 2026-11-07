---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Email verification API documented at InboxVet docs.
  name: InboxVet API
  slug: inboxvet-api
- description: 'inboxvet-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: inboxvet-com API
  slug: inboxvet-com-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/inboxvet-com/plans/inboxvet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inboxvet-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/inboxvet-com/rules/inboxvet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/inboxvet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/inboxvet-com/json-ld/inboxvet-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/inboxvet-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/inboxvet-com/vocabulary/inboxvet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inboxvet-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/inboxvet-com/data-model/inboxvet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inboxvet-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/inboxvet-com/conformance/inboxvet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inboxvet-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/inboxvet-com/llms/inboxvet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inboxvet-com-llms.txt
- group: other
  href: https://artifacts.apis.io/inboxvet-com/hosts/inboxvet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inboxvet-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inboxvet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inboxvet.com/privacy
- group: start
  title: ''
  type: Login
  url: https://inboxvet.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inboxvet
- group: auth
  href: https://artifacts.apis.io/inboxvet-com/security/inboxvet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inboxvet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inboxvet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://inboxvet.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://inboxvet.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://inboxvet.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://inboxvet.com/blog
- group: operate
  title: ''
  type: Support
  url: https://inboxvet.com/contact
coverage:
  checked: '2026-10-31'
  detail: Docs are public HTML with no downloadable OpenAPI/Swagger spec.
  evidence:
  - status: 200
    url: https://inboxvet.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: InboxVet provides a real‑time email verification API that helps developers and marketers clean email lists, improve deliverability, and reduce bounce rates. The service boasts 99.6% accuracy with sub‑100 ms response times, supporting bulk uploads and single‑email checks. InboxVet’s platform includes tools for blacklist monitoring, DMARC monitoring, and email server testing, positioning it as a comprehensive email hygiene solution for SaaS applications and marketing teams.
image: https://inboxvet.com/og-image.png
json_schemas:
- name: PostApiValidateBatchRequest
  property_count: 2
  slug: inboxvet-com-post-api-validate-batch-request
- name: PostApiValidateBatchResponse
  property_count: 3
  slug: inboxvet-com-post-api-validate-batch-response
- name: PostApiValidateRequest
  property_count: 2
  slug: inboxvet-com-post-api-validate-request
jsonld:
- class_count: 3
  name: Inboxvet Com Context
  property_count: 6
  slug: inboxvet-com-context
layout: provider
modified: '2026-10-31'
name: inboxvet-com
nav: Providers
network: true
overview: 'inboxvet-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Verification, Software-as-a-Service, and Marketing.


  The inboxvet-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  inboxvet-com''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Inboxvet Com Plans Pricing
  plan_count: 9
  slug: inboxvet-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: inboxvet-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: inboxvet-com-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.8
    catalog_earned_first_party: 12.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 34.6
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/inboxvet-com/inboxvet-com-2026-11-03T133728.png
security:
- kind: domain-security
  name: Inboxvet Com Domain Security
  slug: inboxvet-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inboxvet-com
tags:
- Company
- Email Verification
- Software-as-a-Service
- Marketing
website: https://inboxvet.com/
---
