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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.membranelabs.com/api/lending
  baseurl_source: declared
  description: 'Membrane API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Membrane API
  slug: membranelabs-com-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/membranelabs-com/well-known/membranelabs-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/membranelabs-com-status-security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://membranelabs.com/privacy-policy/
- group: other
  href: https://artifacts.apis.io/membranelabs-com/vendors/membranelabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/membranelabs-com-vendors.yml
- group: design
  href: https://artifacts.apis.io/membranelabs-com/rules/membranelabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/membranelabs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/membranelabs-com/json-ld/membranelabs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/membranelabs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/membranelabs-com/vocabulary/membranelabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/membranelabs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/membranelabs-com/data-model/membranelabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/membranelabs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/membranelabs-com/conventions/membranelabs-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/membranelabs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/membranelabs-com/conventions/membranelabs-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/membranelabs-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/membranelabs-com/conformance/membranelabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/membranelabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/membranelabs-com/llms/membranelabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/membranelabs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/membranelabs-com/well-known/membranelabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/membranelabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/membranelabs-com/hosts/membranelabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/membranelabs-com-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.membranelabs.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.membranelabs.com/assets-and-prices/pricing-feed
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.membranelabs.com/release-notes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.membranelabs.com/
- group: auth
  href: https://artifacts.apis.io/membranelabs-com/security/membranelabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/membranelabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://membranelabs.com/
created: '2026-10-22'
description: 'Membrane is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by electric-capital) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetV2LoansLoanidFeesFeeidResponse
  property_count: 15
  slug: membranelabs-com-get-v2-loans-loanid-fees-feeid-response
- name: GetV2LoansLoanidFeesResponse
  property_count: 3
  slug: membranelabs-com-get-v2-loans-loanid-fees-response
- name: PatchV2LoansLoanidFeesFeeidRequest
  property_count: 6
  slug: membranelabs-com-patch-v2-loans-loanid-fees-feeid-request
- name: PostV1PaymentOffPlatformRequest
  property_count: 6
  slug: membranelabs-com-post-v1-payment-off-platform-request
- name: PostV2LoansLoanidFeesRequest
  property_count: 7
  slug: membranelabs-com-post-v2-loans-loanid-fees-request
- name: PostV2LoansLoanidWaiversRequest
  property_count: 3
  slug: membranelabs-com-post-v2-loans-loanid-waivers-request
jsonld:
- class_count: 23
  name: Membranelabs Com Context
  property_count: 28
  slug: membranelabs-com-context
layout: provider
modified: '2026-10-22'
name: Membrane
nav: Providers
network: true
overview: 'Membrane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Membrane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Membrane''s developer surface includes pricing, changelog, documentation, and 16 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Membrane API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 2
  slug: membranelabs-com-rules
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.9
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/membranelabs-com/membranelabs-com-2026-11-03T135447.png
security:
- kind: domain-security
  name: Membranelabs Com Domain Security
  slug: membranelabs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: membranelabs-com
tags:
- Company
website: https://membranelabs.com/
---
