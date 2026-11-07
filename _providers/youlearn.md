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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'YouLearn API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: YouLearn API
  slug: youlearn-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/youlearn/well-known/youlearn-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/youlearn-vercel-security.txt
- group: other
  href: https://artifacts.apis.io/youlearn/vendors/youlearn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/youlearn-vendors.yml
- group: design
  href: https://artifacts.apis.io/youlearn/rules/youlearn-rules.yml
  title: ''
  type: Spectral
  url: rules/youlearn-rules.yml
- group: design
  href: https://artifacts.apis.io/youlearn/json-ld/youlearn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/youlearn-context.jsonld
- group: design
  href: https://artifacts.apis.io/youlearn/vocabulary/youlearn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/youlearn-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/youlearn/data-model/youlearn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/youlearn-data-model.yml
- group: design
  href: https://artifacts.apis.io/youlearn/conformance/youlearn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/youlearn-conformance.yml
- group: agent
  href: https://artifacts.apis.io/youlearn/well-known/youlearn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/youlearn-well-known.yml
- group: other
  href: https://artifacts.apis.io/youlearn/hosts/youlearn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/youlearn-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.youlearn.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.youlearn.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.youlearn.ai/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://vercel.com/docs/getting-started-with-vercel.md?from=llms-txt
- group: docs
  title: ''
  type: Documentation
  url: https://dev.youlearn.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://vercel.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/youlearn/security/youlearn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/youlearn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://youlearn.ai
created: '2026-10-24'
description: 'YouLearn is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by true-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/assets/XivrxXuIUuSjflrSGDEo0UF5eg.png
json_schemas:
- name: PostV1BillingBuyRequest
  property_count: 2
  slug: youlearn-post-v1-billing-buy-request
- name: PostV1BillingBuyResponse
  property_count: 3
  slug: youlearn-post-v1-billing-buy-response
- name: PostV1RegistrarDomainsPriceRequest
  property_count: 1
  slug: youlearn-post-v1-registrar-domains-price-request
- name: PostV1RegistrarDomainsSearchRequest
  property_count: 1
  slug: youlearn-post-v1-registrar-domains-search-request
jsonld:
- class_count: 4
  name: Youlearn Context
  property_count: 6
  slug: youlearn-context
layout: provider
modified: '2026-10-24'
name: YouLearn
nav: Providers
network: true
overview: 'YouLearn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Artificial Intelligence, Tutoring, and Learning.


  The YouLearn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  YouLearn''s developer surface includes getting-started guide, documentation, API reference, and 14 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: YouLearn API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: youlearn-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.1
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/youlearn/youlearn-2026-11-03T150342.png
security:
- kind: domain-security
  name: Youlearn Domain Security
  slug: youlearn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: youlearn
tags:
- Company
- Education
- Artificial Intelligence
- Tutoring
- Learning
website: https://youlearn.ai
---
