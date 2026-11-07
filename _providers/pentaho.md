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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Pentaho API as documented publicly: 33 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Pentaho API
  slug: pentaho-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/pentaho/rules/pentaho-rules.yml
  title: ''
  type: Spectral
  url: rules/pentaho-rules.yml
- group: design
  href: https://artifacts.apis.io/pentaho/json-ld/pentaho-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pentaho-context.jsonld
- group: design
  href: https://artifacts.apis.io/pentaho/vocabulary/pentaho-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pentaho-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pentaho/data-model/pentaho-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pentaho-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pentaho/changelog/pentaho-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pentaho-changelog.yml
- group: auth
  href: https://artifacts.apis.io/pentaho/security/pentaho-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pentaho-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pentaho/authentication/pentaho-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pentaho-authentication.yml
- group: design
  href: https://artifacts.apis.io/pentaho/conformance/pentaho-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pentaho-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pentaho/llms/pentaho-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pentaho-llms.txt
- group: agent
  href: https://artifacts.apis.io/pentaho/well-known/pentaho-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pentaho-well-known.yml
- group: other
  href: https://artifacts.apis.io/pentaho/hosts/pentaho-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pentaho-hosts.yml
- group: other
  href: https://artifacts.apis.io/pentaho/vendors/pentaho-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pentaho-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pentaho.com/pdia-try-pdia/getting-started-with-analyzer-interactive-reports-and-dashboard-designer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pentaho.com/
- group: auth
  href: https://artifacts.apis.io/pentaho/security/pentaho-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pentaho-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pentaho/security/pentaho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pentaho-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pentaho.com
created: '2026-10-26'
description: Pentaho offers a scalable data integration and intelligence platform that includes Pentaho Data Integration, Business Analytics, Embedded Analytics, and AI‑focused solutions. It provides governed pipelines, real‑time insights, and compliance features for organizations handling complex data. The platform serves enterprises across industries such as financial services, insurance, healthcare, manufacturing, and government.
json_schemas:
- name: GetPdiaDataIntegrationPdiJobEntriesReferenceOverviewSparkSub
  property_count: 1
  slug: pentaho-get-pdia-data-integration-pdi-job-entries-reference-overview-spark-sub
- name: GetPdiaDataIntegrationPdiTransformationStepsReferenceOvervie
  property_count: 1
  slug: pentaho-get-pdia-data-integration-pdi-transformation-steps-reference-overvie
- name: GetPdiaDataIntegrationPdiTransformationStepsReferenceOvervie2
  property_count: 1
  slug: pentaho-get-pdia-data-integration-pdi-transformation-steps-reference-overvie2
- name: GetPdiaDataIntegrationPdiTransformationStepsReferenceOvervie3
  property_count: 1
  slug: pentaho-get-pdia-data-integration-pdi-transformation-steps-reference-overvie3
- name: GetPdiaDataIntegrationPdiTransformationStepsReferenceOvervie4
  property_count: 1
  slug: pentaho-get-pdia-data-integration-pdi-transformation-steps-reference-overvie4
- name: GetPdiaDataIntegrationPdiTransformationStepsReferenceOvervie6
  property_count: 1
  slug: pentaho-get-pdia-data-integration-pdi-transformation-steps-reference-overvie6
jsonld:
- class_count: 7
  name: Pentaho Context
  property_count: 2
  slug: pentaho-context
layout: provider
modified: '2026-10-26'
name: Pentaho
nav: Providers
network: true
overview: 'Pentaho is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, Business Analytics, Embedded Analytics, Artificial Intelligence, and Financial Services.


  The Pentaho catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pentaho''s developer surface includes changelog, authentication, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Pentaho API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: pentaho-rules
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 22.6
    developer_ergonomics: 22.6
    discoverability: 60.7
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
    score: 16.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/pentaho/pentaho-2026-11-03T141110.png
security:
- kind: authentication
  name: Pentaho Authentication
  slug: pentaho-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pentaho Domain Security
  slug: pentaho-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pentaho Vulnerability Disclosure
  slug: pentaho-vulnerability-disclosure
  summary_line: no policy recorded
slug: pentaho
tags:
- Data Integration
- Business Analytics
- Embedded Analytics
- Artificial Intelligence
- Financial Services
- Healthcare
- Manufacturing
- Government
website: https://pentaho.com
---
