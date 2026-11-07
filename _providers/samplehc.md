---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
api_count: 2
apis:
- description: API for executing SQL queries on healthcare documents.
  name: SampleHC API
  slug: samplehc-api-2
- description: 'Sample API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Sample API
  slug: samplehc-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/samplehc/rules/samplehc-rules.yml
  title: ''
  type: Spectral
  url: rules/samplehc-rules.yml
- group: design
  href: https://artifacts.apis.io/samplehc/json-ld/samplehc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/samplehc-context.jsonld
- group: design
  href: https://artifacts.apis.io/samplehc/vocabulary/samplehc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/samplehc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/samplehc/data-model/samplehc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/samplehc-data-model.yml
- group: operate
  href: https://artifacts.apis.io/samplehc/changelog/samplehc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/samplehc-changelog.yml
- group: auth
  href: https://artifacts.apis.io/samplehc/authentication/samplehc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/samplehc-authentication.yml
- group: design
  href: https://artifacts.apis.io/samplehc/conformance/samplehc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/samplehc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/samplehc/llms/samplehc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/samplehc-llms.txt
- group: other
  href: https://artifacts.apis.io/samplehc/a2a/samplehc-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/samplehc-a2a.yml
- group: agent
  href: https://artifacts.apis.io/samplehc/well-known/samplehc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samplehc-well-known.yml
- group: other
  href: https://artifacts.apis.io/samplehc/hosts/samplehc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/samplehc-hosts.yml
- group: other
  href: https://artifacts.apis.io/samplehc/vendors/samplehc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/samplehc-vendors.yml
- group: build
  href: https://artifacts.apis.io/samplehc/packages/samplehc-packages.yml
  title: ''
  type: SDKs
  url: packages/samplehc-packages.yml
- group: build
  href: https://artifacts.apis.io/samplehc/packages/samplehc-packages.yml
  title: ''
  type: Packages
  url: packages/samplehc-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.samplehc.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.samplehc.com/news
- group: start
  title: ''
  type: Login
  url: https://app.samplehc.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.samplehc.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.samplehc.com/api-reference/v1/execute-sql-query
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.samplehc.com/workflows/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.samplehc.com/
- group: auth
  href: https://artifacts.apis.io/samplehc/security/samplehc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samplehc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://samplehc.com/
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are rendered HTML with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.samplehc.com/api-reference/v1/execute-sql-query
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Sample Healthcare provides AI-powered document workflow solutions for the healthcare industry. Their platform automates extraction, classification, and analysis of medical records, enabling clinical and operational teams to work up to ten times faster. By leveraging large language model copilots, Sample helps organizations streamline patient intake, prior authorization, and revenue cycle management, improving efficiency, accuracy, and patient care.
image: https://cdn.prod.website-files.com/67bc7a2c4469024abe1d8c1b/67c02f859239ca0fbdcbe7ef_Screenshot%202025-02-27%20at%2010.24.48.webp
json_schemas:
- name: GetApiV1SqlResponse
  property_count: 1
  slug: samplehc-get-api-v1-sql-response
- name: PostApiV1SqlResponse
  property_count: 1
  slug: samplehc-post-api-v1-sql-response
jsonld:
- class_count: 2
  name: Samplehc Context
  property_count: 1
  slug: samplehc-context
layout: provider
modified: '2026-10-18'
name: Sample
nav: Providers
network: true
overview: 'Sample is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, Document Automation, LLM, and Software-as-a-Service.


  The Sample catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sample''s developer surface includes changelog, authentication, API reference, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Sample API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: samplehc-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 33.3
    discoverability: 65.2
    operational_transparency: 26.3
  previous_composite: 31.4
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
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/samplehc/samplehc-2026-11-03T142659.png
security:
- kind: authentication
  name: Samplehc Authentication
  slug: samplehc-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Samplehc Domain Security
  slug: samplehc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: samplehc
tags:
- Healthcare
- Artificial Intelligence
- Document Automation
- LLM
- Software-as-a-Service
website: https://samplehc.com/
---
