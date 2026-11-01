---
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://namegender.com
  baseurl_source: spec
  description: Credit balance and key status.
  name: NameGender Account API
  slug: namegender-account-api
- baseURL: https://namegender.com
  baseurl_source: spec
  description: Upload a CSV or XLSX file and download it back with gender columns added.
  name: NameGender Batches API
  slug: namegender-batches-api
- baseURL: https://namegender.com
  baseurl_source: spec
  description: Name, email and username lookups.
  name: NameGender Gender API
  slug: namegender-gender-api
- baseURL: https://namegender.com
  baseurl_source: spec
  description: Requests NameGender sends to your server when a file job finishes or credits run low.
  name: NameGender Webhooks API
  slug: namegender-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Namegender Webhooks
  slug: namegender-webhooks
common:
- group: design
  href: https://artifacts.apis.io/namegender/rules/namegender-rules.yml
  title: ''
  type: Spectral
  url: rules/namegender-rules.yml
- group: design
  href: https://artifacts.apis.io/namegender/json-ld/namegender-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/namegender-context.jsonld
- group: design
  href: https://artifacts.apis.io/namegender/vocabulary/namegender-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/namegender-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/namegender/conventions/namegender-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/namegender-conventions.yml
- group: design
  href: https://artifacts.apis.io/namegender/conventions/namegender-conventions.yml
  title: ''
  type: Conventions
  url: conventions/namegender-conventions.yml
- group: design
  href: https://artifacts.apis.io/namegender/conformance/namegender-conformance.yml
  title: ''
  type: Conformance
  url: conformance/namegender-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/namegender/plans/namegender-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/namegender-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/namegender/asyncapi/namegender-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/namegender-webhooks.yml
- group: design
  href: https://artifacts.apis.io/namegender/data-model/namegender-data-model.yml
  title: ''
  type: DataModel
  url: data-model/namegender-data-model.yml
- group: build
  href: https://artifacts.apis.io/namegender/cli/namegender-cli.yml
  title: ''
  type: CLI
  url: cli/namegender-cli.yml
- group: operate
  href: https://artifacts.apis.io/namegender/changelog/namegender-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/namegender-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://namegender.com/changelog#security
- group: operate
  href: https://artifacts.apis.io/namegender/lifecycle/namegender-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/namegender-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/namegender/lifecycle/namegender-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/namegender-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/namegender/errors/namegender-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/namegender-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/namegender/llms/namegender-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/namegender-llms.txt
- group: auth
  href: https://artifacts.apis.io/namegender/well-known/namegender-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/namegender-security.txt
- group: agent
  href: https://artifacts.apis.io/namegender/well-known/namegender-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/namegender-well-known.yml
- group: other
  href: https://artifacts.apis.io/namegender/hosts/namegender-hosts.yml
  title: ''
  type: Hosts
  url: hosts/namegender-hosts.yml
- group: build
  href: https://artifacts.apis.io/namegender/packages/namegender-packages.yml
  title: ''
  type: Packages
  url: packages/namegender-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://namegender.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://namegender.com/status
- group: build
  title: ''
  type: SDKs
  url: https://namegender.com/client-libraries
- group: operate
  title: ''
  type: ChangeLog
  url: https://namegender.com/changelog
- group: auth
  href: https://artifacts.apis.io/namegender/security/namegender-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/namegender-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/namegender/security/namegender-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/namegender-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://namegender.com/apis.json
- group: docs
  title: ''
  type: Documentation
  url: https://namegender.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://namegender.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://namegender.com/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://namegender.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://namegender.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://namegender.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://namegender.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://namegender.com/blog
created: '2026-10-06'
description: NameGender provides a gender detection API that returns gender, probability, and supporting evidence for first names, full names, emails, or usernames. It supports multiple languages and countries, offers a free tier with 100 daily credits, and includes detailed documentation, pricing, client libraries, and research resources.
finops:
- has_sources: true
  method: derived
  name: Namegender Finops
  primary_unit: seat
  service_category: ''
  slug: namegender-finops
  template: false
json_schemas:
- name: AccountResponse
  property_count: 7
  slug: namegender-account-response
- name: BatchJob
  property_count: 19
  slug: namegender-batch-job
- name: BulkRequest
  property_count: 7
  slug: namegender-bulk-request
- name: BulkResponse
  property_count: 0
  slug: namegender-bulk-response
- name: CountriesResponse
  property_count: 9
  slug: namegender-countries-response
- name: SingleResponse
  property_count: 0
  slug: namegender-single-response
jsonld:
- class_count: 11
  name: Namegender Context
  property_count: 65
  slug: namegender-context
layout: provider
modified: '2026-10-06'
name: NameGender
nav: Providers
network: true
overview: 'NameGender publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batches API, Gender API, and 1 more. Tagged areas include Gender, Name, Data Enrichment, Demographics, and Bulk.


  The NameGender catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  NameGender''s developer surface includes CLI, changelog, support, documentation, API reference, getting-started guide, pricing, and 28 more developer resources.'
plans:
- name: Namegender Plans Pricing
  plan_count: 13
  slug: namegender-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: NameGender API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: namegender-rules
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 12.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 73.5
    developer_ergonomics: 50.0
    discoverability: 53.6
    operational_transparency: 57.9
  previous_composite: 60.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Namegender Domain Security
  slug: namegender-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Namegender Vulnerability Disclosure
  slug: namegender-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: namegender
tags:
- Gender
- Name
- Data Enrichment
- Demographics
- Bulk
website: https://namegender.com/apis.json
---
