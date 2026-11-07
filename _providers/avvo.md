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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Avvo API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Avvo API
  slug: avvo-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/avvo/rules/avvo-rules.yml
  title: ''
  type: Spectral
  url: rules/avvo-rules.yml
- group: design
  href: https://artifacts.apis.io/avvo/json-ld/avvo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avvo-context.jsonld
- group: design
  href: https://artifacts.apis.io/avvo/vocabulary/avvo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avvo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avvo/data-model/avvo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avvo-data-model.yml
- group: auth
  href: https://artifacts.apis.io/avvo/security/avvo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/avvo-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/avvo/conformance/avvo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avvo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avvo/llms/avvo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avvo-llms.txt
- group: auth
  href: https://artifacts.apis.io/avvo/well-known/avvo-stories-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avvo-stories-security.txt
- group: auth
  href: https://artifacts.apis.io/avvo/well-known/avvo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avvo-security.txt
- group: auth
  href: https://artifacts.apis.io/avvo/well-known/avvo-changelog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avvo-changelog-security.txt
- group: auth
  href: https://artifacts.apis.io/avvo/well-known/avvo-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avvo-api-security.txt
- group: agent
  href: https://artifacts.apis.io/avvo/well-known/avvo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avvo-well-known.yml
- group: other
  href: https://artifacts.apis.io/avvo/hosts/avvo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avvo-hosts.yml
- group: other
  href: https://artifacts.apis.io/avvo/vendors/avvo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avvo-vendors.yml
- group: build
  href: https://artifacts.apis.io/avvo/packages/avvo-packages.yml
  title: ''
  type: SDKs
  url: packages/avvo-packages.yml
- group: build
  href: https://artifacts.apis.io/avvo/packages/avvo-packages.yml
  title: ''
  type: Packages
  url: packages/avvo-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.avvo.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avvo.com/privacy-lawyer.html
- group: start
  title: ''
  type: Login
  url: https://www.avvo.com/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avvo
- group: auth
  href: https://artifacts.apis.io/avvo/security/avvo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avvo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avvo/security/avvo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avvo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avvo.com
created: '2026-10-22'
description: Avvo is an online legal services marketplace connecting consumers with attorneys across the United States. Founded in 2006, Avvo provides a searchable lawyer directory, free legal Q&A, client reviews, and a proprietary rating system to help users find and evaluate legal professionals. The platform also offers tools for lawyers to manage their online presence and attract clients.
image: https://images.avvo.com/production/images/social/Avvo_logo_share.png
json_schemas:
- name: GetApi5ReviewsCommentsReviewcommentidResponse
  property_count: 1
  slug: avvo-get-api5-reviews-comments-reviewcommentid-response
- name: GetApi5ReviewsResponse
  property_count: 2
  slug: avvo-get-api5-reviews-response
- name: GetApi5ReviewsReviewidCommentsResponse
  property_count: 2
  slug: avvo-get-api5-reviews-reviewid-comments-response
- name: GetApi5ReviewsReviewidResponse
  property_count: 2
  slug: avvo-get-api5-reviews-reviewid-response
- name: PostApi5ReviewsReviewidCommentsResponse
  property_count: 2
  slug: avvo-post-api5-reviews-reviewid-comments-response
- name: PutApi5ReviewsCommentsReviewcommentidResponse
  property_count: 1
  slug: avvo-put-api5-reviews-comments-reviewcommentid-response
jsonld:
- class_count: 10
  name: Avvo Context
  property_count: 5
  slug: avvo-context
layout: provider
modified: '2026-10-22'
name: Avvo
nav: Providers
network: true
overview: 'Avvo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Marketplace, Directory, Reviews, and Consumer Services.


  The Avvo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Avvo''s developer surface includes support and 22 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Avvo API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: avvo-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 23.2
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.2
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Avvo Domain Security
  slug: avvo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Avvo Vulnerability Disclosure
  slug: avvo-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: avvo
tags:
- Legal Tech
- Marketplace
- Directory
- Reviews
- Consumer Services
website: https://www.avvo.com
---
