---
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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for medical claims processing, as documented in the developer portal.
  name: ClaimRev API
  slug: claimrev-api-2
- description: 'Claim.Revolution API as documented publicly: 40 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Claim.Revolution API
  slug: claimrev-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/claimrev/plans/claimrev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claimrev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/claimrev/rules/claimrev-rules.yml
  title: ''
  type: Spectral
  url: rules/claimrev-rules.yml
- group: design
  href: https://artifacts.apis.io/claimrev/json-ld/claimrev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claimrev-context.jsonld
- group: design
  href: https://artifacts.apis.io/claimrev/vocabulary/claimrev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claimrev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claimrev/data-model/claimrev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claimrev-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.claimrev.com/security/
- group: design
  href: https://artifacts.apis.io/claimrev/conformance/claimrev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claimrev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claimrev/llms/claimrev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claimrev-llms.txt
- group: other
  href: https://artifacts.apis.io/claimrev/hosts/claimrev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claimrev-hosts.yml
- group: other
  href: https://artifacts.apis.io/claimrev/vendors/claimrev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claimrev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.claimrev.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.claimrev.com/changelog
- group: auth
  href: https://artifacts.apis.io/claimrev/security/claimrev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/claimrev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/claimrev/security/claimrev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claimrev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claimrev.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.claimrev.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.claimrev.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.claimrev.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.claimrev.com/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.claimrev.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.claimrev.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.claimrev.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claimrev.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claimrev.com/privacypolicy/
coverage:
  checked: '2026-10-27'
  detail: Developer portal provides HTML reference pages but no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 200
    url: https://developer.claimrev.com/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Claim.Revolution is a medical claims clearinghouse for providers, offering a platform that enables healthcare teams to submit cleaner claims, verify eligibility, track claim status, and manage revenue cycles. It supports high‑volume batch submissions, complex payer environments, and integrates with EMR systems like OpenEMR and Healthie. The service aims to reduce denials, accelerate payments, and provide real‑time insights into claim processing for clinics, billing companies, and tribal health programs.
image: https://www.claimrev.com/wp-content/uploads/2024/02/Stacked-Logo-e1722441851106.png
json_schemas:
- name: GetApiAimodelconfigV1ResolvemodelResponse
  property_count: 1
  slug: claimrev-get-api-aimodelconfig-v1-resolvemodel-response
- name: PostApiAttachment275V1IdStatusResponse
  property_count: 3
  slug: claimrev-post-api-attachment275-v1-id-status-response
- name: PostApiAttachment275V1SearchResponse
  property_count: 1
  slug: claimrev-post-api-attachment275-v1-search-response
- name: PostApiChildaccountV1ChildrenResponse
  property_count: 4
  slug: claimrev-post-api-childaccount-v1-children-response
- name: PostApiClaimviewV1SearchclaimsResponse
  property_count: 2
  slug: claimrev-post-api-claimview-v1-searchclaims-response
- name: PostApiInputfileV1Response
  property_count: 2
  slug: claimrev-post-api-inputfile-v1-response
- name: PostApiModuleV1CheckversionResponse
  property_count: 2
  slug: claimrev-post-api-module-v1-checkversion-response
- name: PostApiOcrreviewV1FlagocrreviewResponse
  property_count: 2
  slug: claimrev-post-api-ocrreview-v1-flagocrreview-response
- name: PostApiTicketsV1SearchResponse
  property_count: 1
  slug: claimrev-post-api-tickets-v1-search-response
jsonld:
- class_count: 6
  name: Claimrev Context
  property_count: 1
  slug: claimrev-context
layout: provider
modified: '2026-10-26'
name: Claim.Revolution
nav: Providers
network: true
overview: 'Claim.Revolution is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Claims, API, and Billing.


  The Claim.Revolution catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Claim.Revolution''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Claimrev Plans Pricing
  plan_count: 7
  slug: claimrev-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Claim.Revolution API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: claimrev-rules
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.0
    catalog_earned_first_party: 12.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 19.7
    contract_quality: 21.4
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 31
      marker_coverage: 100.0
      total: 31
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claimrev Domain Security
  slug: claimrev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Claimrev Trust Center
  slug: claimrev-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: claimrev
tags:
- Company
- Healthcare
- Claims
- API
- Billing
website: https://www.claimrev.com/
---
