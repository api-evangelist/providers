---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Datanem Com Agentic Access
  operation_count: 7
  slug: datanem-com-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://datanem.com
  baseurl_source: declared
  description: Submitting documents and reading the results.
  name: Datanem Extraction API
  slug: datanem-com-extraction-api
- baseURL: https://datanem.com
  baseurl_source: declared
  description: Built-in document types and saved column designs.
  name: Datanem Templates API
  slug: datanem-com-templates-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/datanem-com/data-model/datanem-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datanem-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/datanem-com/agentic-access/datanem-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datanem-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/datanem-com/plans/datanem-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datanem-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datanem-com/rules/datanem-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datanem-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datanem-com/vocabulary/datanem-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datanem-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/datanem-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/datanem-com/errors/datanem-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datanem-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datanem-com/conformance/datanem-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datanem-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datanem-com/llms/datanem-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datanem-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/datanem-com/well-known/datanem-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datanem-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datanem-com/hosts/datanem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datanem-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datanem-com/vendors/datanem-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datanem-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datanem.com/terms
- group: auth
  title: ''
  type: Security
  url: https://datanem.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datanem.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://datanem.com/pricing
- group: start
  title: ''
  type: Login
  url: https://datanem.com/signin
- group: auth
  href: https://artifacts.apis.io/datanem-com/authentication/datanem-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datanem-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/datanem-com/security/datanem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datanem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datanem.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://datanem.com/openapi.json
  - status: 401
    url: https://datanem.com/mcp
  - status: 200
    url: https://datanem.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Datanem provides a service that lets users photograph invoices, delivery notes, or forms and receive a structured spreadsheet output. It extracts columns from documents using OCR and AI, supporting export to Excel, CSV, SQL, JSON and more. Free tier offers one anonymous document processing, with paid plans for higher volume and features. The platform stores files in EU-only buckets and deletes them after 30 days, ensuring privacy. Founded in the UK, Datanem aims to simplify data extraction from physical documents for businesses and individuals.
image: https://datanem.com/og/default.png
json_schemas:
- name: JobStatus
  property_count: 0
  slug: datanem-com-job-status
- name: NamedId
  property_count: 0
  slug: datanem-com-named-id
- name: Results
  property_count: 0
  slug: datanem-com-results
layout: provider
modified: '2026-11-05'
name: Datanem
nav: Providers
network: true
overview: 'Datanem publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Extraction API and Templates API. Tagged areas include Data Extraction, OCR, Document Processing, Spreadsheet Export, and United Kingdom.


  The Datanem catalog on APIs.io includes 1 Spectral governance ruleset.


  Datanem''s developer surface includes pricing, authentication, and 18 more developer resources.'
plans:
- name: Datanem Com Plans Pricing
  plan_count: 4
  slug: datanem-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Datanem API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: datanem-com-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 55.7
    developer_ergonomics: 13.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datanem Com Authentication
  slug: datanem-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Datanem Com Domain Security
  slug: datanem-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: datanem-com-extract-documents
  slug: datanem-com-extract-documents
slug: datanem-com
tags:
- Data Extraction
- OCR
- Document Processing
- Spreadsheet Export
- United Kingdom
website: https://datanem.com/
---
