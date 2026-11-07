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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: CitizenLeap provides a study aid platform for citizenship test preparation across multiple countries, offering free lessons, quizzes, and a premium tier with timed mock exams and AI tutoring.
  name: CitizenLeap API
  slug: citizenleap-api
- baseURL: https://api.citizenleap.com
  baseurl_source: declared
  description: 'Civica API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Civica API
  slug: citizenleap-com-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/citizenleap-com/rules/citizenleap-com-rules.yml
  title: ''
  type: Spectral
  url: rules/citizenleap-com-rules.yml
- group: design
  href: https://artifacts.apis.io/citizenleap-com/json-ld/citizenleap-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citizenleap-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/citizenleap-com/vocabulary/citizenleap-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citizenleap-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/citizenleap-com/data-model/citizenleap-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citizenleap-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/citizenleap-com/errors/citizenleap-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/citizenleap-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/citizenleap-com/conformance/citizenleap-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citizenleap-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citizenleap-com/llms/citizenleap-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citizenleap-com-llms.txt
- group: other
  href: https://artifacts.apis.io/citizenleap-com/hosts/citizenleap-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citizenleap-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citizenleap-com/vendors/citizenleap-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citizenleap-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citizenleap.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citizenleap.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.citizenleap.com/
- group: auth
  href: https://artifacts.apis.io/citizenleap-com/security/citizenleap-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citizenleap-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citizenleap.com/
coverage:
  checked: '2026-11-04'
  detail: Developer portal pages are rendered with JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://dev.citizenleap.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Civica provides an independent study aid for citizenship and naturalisation test preparation across eight countries, offering free lessons, level‑based quizzes, and practice questions. It also offers a premium tier with timed mock exams, audio, and AI tutoring. Owned by Saaram Labs, Civica emphasizes that it is not affiliated with any government or official test provider.
image: https://citizenleap.com/og-image.png
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: citizenleap-com-post-mcp-request
jsonld:
- class_count: 2
  name: Citizenleap Com Context
  property_count: 5
  slug: citizenleap-com-context
layout: provider
modified: '2026-11-03'
name: Civica
nav: Providers
network: true
overview: 'Civica is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Citizenship, Test Prep, Software-as-a-Service, and Civica.


  The Civica catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Civica''s developer surface includes documentation and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Civica API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: citizenleap-com-rules
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citizenleap Com Domain Security
  slug: citizenleap-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citizenleap-com
tags:
- Education
- Citizenship
- Test Prep
- Software-as-a-Service
- Civica
website: https://citizenleap.com/
---
