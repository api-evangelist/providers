---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.omophub.com
  baseurl_source: declared
  description: 'OMOPHub API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: OMOPHub API
  slug: omophub-api
artifact_total: 13
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://omophub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://omophub.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://omophub.com/blog
- group: operate
  href: https://artifacts.apis.io/omophub/rate-limits/omophub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/omophub-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/omophub/plans/omophub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/omophub-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/omophub/rules/omophub-rules.yml
  title: ''
  type: Spectral
  url: rules/omophub-rules.yml
- group: design
  href: https://artifacts.apis.io/omophub/json-ld/omophub-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/omophub-context.jsonld
- group: design
  href: https://artifacts.apis.io/omophub/vocabulary/omophub-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/omophub-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/omophub/data-model/omophub-data-model.yml
  title: ''
  type: DataModel
  url: data-model/omophub-data-model.yml
- group: design
  href: https://artifacts.apis.io/omophub/conventions/omophub-conventions.yml
  title: ''
  type: Conventions
  url: conventions/omophub-conventions.yml
- group: auth
  href: https://artifacts.apis.io/omophub/authentication/omophub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/omophub-authentication.yml
- group: design
  href: https://artifacts.apis.io/omophub/conformance/omophub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/omophub-conformance.yml
- group: agent
  href: https://artifacts.apis.io/omophub/llms/omophub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omophub-llms.txt
- group: other
  href: https://artifacts.apis.io/omophub/a2a/omophub-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/omophub-a2a.yml
- group: agent
  href: https://artifacts.apis.io/omophub/well-known/omophub-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/omophub-well-known.yml
- group: other
  href: https://artifacts.apis.io/omophub/hosts/omophub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omophub-hosts.yml
- group: other
  href: https://artifacts.apis.io/omophub/vendors/omophub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/omophub-vendors.yml
- group: build
  href: https://artifacts.apis.io/omophub/packages/omophub-packages.yml
  title: ''
  type: SDKs
  url: packages/omophub-packages.yml
- group: build
  href: https://artifacts.apis.io/omophub/packages/omophub-packages.yml
  title: ''
  type: Packages
  url: packages/omophub-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://omophub.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://omophub.com/changelog
- group: auth
  href: https://artifacts.apis.io/omophub/security/omophub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omophub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omophub.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.omophub.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.omophub.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.omophub.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://dashboard.omophub.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omophub
coverage:
  checked: '2026-10-23'
  detail: Documentation site renders content via JavaScript, preventing retrieval of a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.omophub.com/api-reference/introduction
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: OMOPHub provides a platform that enables the integration, transformation, and analysis of healthcare data using the OMOP Common Data Model. It offers APIs for data ingestion, cohort definition, and analytics, supporting researchers and clinicians in generating real‑world evidence. The service includes comprehensive documentation, authentication mechanisms, and compliance with healthcare data standards, facilitating secure and scalable access to standardized health datasets.
image: https://omophub.com/og-cover.png
json_schemas:
- name: GetV1DomainsResponse
  property_count: 3
  slug: omophub-get-v1-domains-response
- name: PostFhirR4Response
  property_count: 2
  slug: omophub-post-fhir-r4-response
- name: PostV1FhirResolveBatchResponse
  property_count: 2
  slug: omophub-post-v1-fhir-resolve-batch-response
- name: PostV1SearchBulkRequest
  property_count: 2
  slug: omophub-post-v1-search-bulk-request
- name: PostV1SearchBulkResponse
  property_count: 3
  slug: omophub-post-v1-search-bulk-response
- name: PostV1SearchSimilarRequest
  property_count: 9
  slug: omophub-post-v1-search-similar-request
jsonld:
- class_count: 22
  name: Omophub Context
  property_count: 31
  slug: omophub-context
layout: provider
modified: '2026-10-23'
name: OMOPHub
nav: Providers
network: true
overview: 'OMOPHub is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Data Integration, and OMOP.


  The OMOPHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OMOPHub''s developer surface includes engineering blog, authentication, pricing, changelog, documentation, API reference, getting-started guide, and 21 more developer resources.'
plans:
- name: Omophub Plans Pricing
  plan_count: 4
  slug: omophub-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Omophub Rate Limits
  slug: omophub-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: OMOPHub API Rules
  rule_count: 46
  severity_counts:
    error: 40
    hint: 0
    info: 4
    warn: 2
  slug: omophub-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 25.9
    developer_ergonomics: 36.9
    discoverability: 64.3
    operational_transparency: 42.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.9
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/omophub/omophub-2026-11-03T140541.png
security:
- kind: authentication
  name: Omophub Authentication
  slug: omophub-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Omophub Domain Security
  slug: omophub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omophub
tags:
- Company
- Healthcare
- Data Integration
- OMOP
website: https://omophub.com
---
