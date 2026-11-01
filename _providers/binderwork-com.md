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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Binderwork API provides endpoints for workspace creation, document management and AI‑driven features. See the developer guides at https://binderwork.com/guides.
  name: Binderwork API
  slug: binderwork-api
- baseURL: https://localhost:4410/api/v1
  baseurl_source: declared
  description: Every action in Binderwork. The workspace comes from the credential, so paths carry no workspace ID. Writes take an Idempotency-Key header.
  name: Binderwork API V1 API
  slug: binderwork-api-v1-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/binderwork-com/plans/binderwork-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/binderwork-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/binderwork-com/rules/binderwork-com-rules.yml
  title: ''
  type: Spectral
  url: rules/binderwork-com-rules.yml
- group: design
  href: https://artifacts.apis.io/binderwork-com/json-ld/binderwork-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/binderwork-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/binderwork-com/vocabulary/binderwork-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/binderwork-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/binderwork-com/data-model/binderwork-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/binderwork-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/binderwork-com/changelog/binderwork-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/binderwork-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/binderwork-com/security/binderwork-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/binderwork-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/binderwork-com/errors/binderwork-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/binderwork-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/binderwork-com/conformance/binderwork-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/binderwork-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/binderwork-com/llms/binderwork-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/binderwork-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/binderwork-com/well-known/binderwork-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/binderwork-com-security.txt
- group: auth
  href: https://artifacts.apis.io/binderwork-com/well-known/binderwork-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/binderwork-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/binderwork-com/well-known/binderwork-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/binderwork-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/binderwork-com/hosts/binderwork-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/binderwork-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/binderwork-com/vendors/binderwork-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/binderwork-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://binderwork.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://binderwork.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/binderwork-com/security/binderwork-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/binderwork-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/binderwork-com/security/binderwork-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/binderwork-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://binderwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://binderwork.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://binderwork.com/demo
- group: operate
  title: ''
  type: Support
  url: https://binderwork.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://binderwork.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://binderwork.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://binderwork.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/binderwork/workspace
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.binderwork.com/mcp
  - status: 200
    url: https://binderwork.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Binderwork provides an AI‑native, open‑source platform that serves as an alternative to DocuSign and DocSend. It enables users to share decks, collect signatures, and manage documents directly within AI chat interfaces like ChatGPT or Claude. The service is free, open‑source under AGPL‑3.0, and offers features such as analytics on deck views, automated signing workflows, and integrations for hiring and fundraising processes. Binderwork aims to streamline startup operations by combining document management, e‑signatures, and AI‑driven assistance in a single platform.
image: https://binderwork.com/opengraph-image?ffb4e181c104f216
json_schemas:
- name: ApprovalRequired
  property_count: 7
  slug: binderwork-com-approval-required
- name: Json
  property_count: 0
  slug: binderwork-com-json
jsonld:
- class_count: 2
  name: Binderwork Com Context
  property_count: 14
  slug: binderwork-com-context
layout: provider
modified: '2026-10-30'
name: binderwork-com
nav: Providers
network: true
overview: 'binderwork-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Binderwork API V1 API, and 1 more. Tagged areas include AI, OpenSource, DocumentManagement, ESignature, and StartupTools.


  The binderwork-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  binderwork-com''s developer surface includes changelog, API reference, documentation, getting-started guide, support, pricing, and 21 more developer resources.'
plans:
- name: Binderwork Com Plans Pricing
  plan_count: 1
  slug: binderwork-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: binderwork-com API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: binderwork-com-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 76.9
    catalog_earned_first_party: 0.0
    catalog_gap: 38.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 79.1
    contract_quality: 46.7
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Binderwork Com Domain Security
  slug: binderwork-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Binderwork Com Vulnerability Disclosure
  slug: binderwork-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: binderwork-com
tags:
- AI
- OpenSource
- DocumentManagement
- ESignature
- StartupTools
website: https://binderwork.com/
---
