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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for HL7 and FHIR integration services provided by Saga IT.
  name: Saga IT HL7/FHIR API
  slug: saga-it-hl7-fhir-api
- description: 'Saga IT API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Saga IT API
  slug: saga-it-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/saga-it/rules/saga-it-rules.yml
  title: ''
  type: Spectral
  url: rules/saga-it-rules.yml
- group: design
  href: https://artifacts.apis.io/saga-it/json-ld/saga-it-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/saga-it-context.jsonld
- group: design
  href: https://artifacts.apis.io/saga-it/vocabulary/saga-it-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/saga-it-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/saga-it/data-model/saga-it-data-model.yml
  title: ''
  type: DataModel
  url: data-model/saga-it-data-model.yml
- group: build
  href: https://artifacts.apis.io/saga-it/cli/saga-it-cli.yml
  title: ''
  type: CLI
  url: cli/saga-it-cli.yml
- group: auth
  href: https://artifacts.apis.io/saga-it/security/saga-it-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/saga-it-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/saga-it/authentication/saga-it-authentication.yml
  title: ''
  type: Authentication
  url: authentication/saga-it-authentication.yml
- group: design
  href: https://artifacts.apis.io/saga-it/conformance/saga-it-conformance.yml
  title: ''
  type: Conformance
  url: conformance/saga-it-conformance.yml
- group: agent
  href: https://artifacts.apis.io/saga-it/llms/saga-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/saga-it-llms.txt
- group: auth
  href: https://artifacts.apis.io/saga-it/well-known/saga-it-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/saga-it-security.txt
- group: agent
  href: https://artifacts.apis.io/saga-it/well-known/saga-it-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/saga-it-well-known.yml
- group: other
  href: https://artifacts.apis.io/saga-it/hosts/saga-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saga-it-hosts.yml
- group: other
  href: https://artifacts.apis.io/saga-it/vendors/saga-it-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saga-it-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saga-it.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SagaHealthcareIT
- group: docs
  title: ''
  type: Documentation
  url: https://saga-it.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/kayyagari/ballista/releases
- group: company
  title: ''
  type: Blog
  url: https://saga-it.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://saga-it.com/docs/hl7/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://saga-it.com/docs/mirthsync/cli/setup
- group: auth
  href: https://artifacts.apis.io/saga-it/security/saga-it-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/saga-it-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/saga-it/security/saga-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saga-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saga-it.com/
coverage:
  checked: '2026-10-21'
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://saga-it.com/docs/hl7/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Saga IT is a US‑based healthcare IT consulting and engineering firm specializing in interoperability solutions such as HL7, FHIR, DICOM, and EHR integration. They provide custom software development, cloud hosting, cybersecurity, and compliance services for healthcare organizations, helping clients integrate with major EHR platforms like Epic, Cerner, and MEDITECH while ensuring HIPAA‑compliant architectures.
image: https://saga-it.com/api/og?title=Healthcare%20IT%20Consulting%20%26%20Engineering%20Firm&subtitle=A%20healthcare%20IT%20consulting%20firm%3A%20HL7%2C%20FHIR%20and%20Mirth%20integration%2C%20custom%20clinical%20apps%2C%20and%20HIPAA-compliant%20cloud%20architecture%2C%20nationwide%20from%20Florida.
json_schemas:
- name: GetConditionResponse
  property_count: 1
  slug: saga-it-get-condition-response
- name: GetMedicationrequestResponse
  property_count: 1
  slug: saga-it-get-medicationrequest-response
- name: GetSagahealthcareitMirthsyncReleasesDownloadMirthsyncVersion
  property_count: 1
  slug: saga-it-get-sagahealthcareit-mirthsync-releases-download-mirthsync-version
- name: PostCdsServicesRequest
  property_count: 1
  slug: saga-it-post-cds-services-request
- name: PostCdsServicesSepsisRiskRequest
  property_count: 1
  slug: saga-it-post-cds-services-sepsis-risk-request
- name: PostQueryRequest
  property_count: 4
  slug: saga-it-post-query-request
jsonld:
- class_count: 9
  name: Saga It Context
  property_count: 6
  slug: saga-it-context
layout: provider
modified: '2026-10-21'
name: Saga IT
nav: Providers
network: true
overview: 'Saga IT is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, IT Consulting, Interoperability, and Cloud Services.


  The Saga IT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Saga IT''s developer surface includes CLI, authentication, documentation, changelog, engineering blog, API reference, getting-started guide, and 16 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Saga IT API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: saga-it-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 34.5
    discoverability: 64.3
    operational_transparency: 21.1
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
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/saga-it/saga-it-2026-11-03T142639.png
security:
- kind: authentication
  name: Saga It Authentication
  slug: saga-it-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Saga It Domain Security
  slug: saga-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Saga It Vulnerability Disclosure
  slug: saga-it-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: saga-it
tags:
- Company
- Healthcare
- IT Consulting
- Interoperability
- Cloud Services
website: https://saga-it.com/
---
