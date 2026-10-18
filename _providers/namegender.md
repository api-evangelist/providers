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
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-10-17'
api_count: 2
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
artifact_total: 16
asyncapis:
- description: ''
  name: Namegender Webhooks
  slug: namegender-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/rules/namegender-rules.yml
  title: ''
  type: Spectral
  url: rules/namegender-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/json-ld/namegender-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/namegender-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/vocabulary/namegender-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/namegender-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/conventions/namegender-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/namegender-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/conventions/namegender-conventions.yml
  title: ''
  type: Conventions
  url: conventions/namegender-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/conformance/namegender-conformance.yml
  title: ''
  type: Conformance
  url: conformance/namegender-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/plans/namegender-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/namegender-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/asyncapi/namegender-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/namegender-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/data-model/namegender-data-model.yml
  title: ''
  type: DataModel
  url: data-model/namegender-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/cli/namegender-cli.yml
  title: ''
  type: CLI
  url: cli/namegender-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/changelog/namegender-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/namegender-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://namegender.com/changelog#security
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/lifecycle/namegender-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/namegender-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/lifecycle/namegender-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/namegender-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/errors/namegender-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/namegender-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/llms/namegender-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/namegender-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/well-known/namegender-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/namegender-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/well-known/namegender-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/namegender-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/hosts/namegender-hosts.yml
  title: ''
  type: Hosts
  url: hosts/namegender-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/packages/namegender-packages.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/security/namegender-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/namegender-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namegender/refs/heads/main/security/namegender-domain-security.yml
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
random_paper: 12
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
  composite: 59.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 69.1
    developer_ergonomics: 50.0
    discoverability: 60.7
    operational_transparency: 57.9
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
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
