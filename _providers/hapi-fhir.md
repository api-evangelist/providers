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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: http://your-server-base
  baseurl_source: declared
  description: The Fhir API from HAPI FHIR — 1 operation(s) for fhir.
  name: HAPI FHIR Fhir API
  slug: hapi-fhir-fhir-api
- baseURL: http://your-server-base
  baseurl_source: declared
  description: The Patient API from HAPI FHIR — 2 operation(s) for patient.
  name: HAPI FHIR Patient API
  slug: hapi-fhir-patient-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/rules/hapi-fhir-rules.yml
  title: ''
  type: Spectral
  url: rules/hapi-fhir-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/json-ld/hapi-fhir-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hapi-fhir-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/vocabulary/hapi-fhir-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hapi-fhir-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/data-model/hapi-fhir-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hapi-fhir-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/cli/hapi-fhir-cli.yml
  title: ''
  type: CLI
  url: cli/hapi-fhir-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/changelog/hapi-fhir-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hapi-fhir-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/conformance/hapi-fhir-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hapi-fhir-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/hosts/hapi-fhir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hapi-fhir-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/packages/hapi-fhir-packages.yml
  title: ''
  type: SDKs
  url: packages/hapi-fhir-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/packages/hapi-fhir-packages.yml
  title: ''
  type: Packages
  url: packages/hapi-fhir-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://hapifhir.io/hapi-fhir/apidocs/hapi-fhir-base/
- group: start
  title: ''
  type: GettingStarted
  url: https://hapifhir.io/hapi-fhir/docs/getting_started/introduction.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hapi-fhir/refs/heads/main/security/hapi-fhir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hapi-fhir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hapifhir.io
- group: docs
  title: ''
  type: Documentation
  url: https://hapifhir.io/hapi-fhir/
- group: company
  title: ''
  type: Blog
  url: https://hapifhir.io/hapi-fhir/blog/
- group: operate
  title: ''
  type: Support
  url: https://smilecdr.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jamesagnew/hapi-fhir
coverage:
  checked: '2026-10-14'
  detail: The provider's documentation site lists API reference but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: timeout
    url: https://api.hapifhir.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: HAPI FHIR provides an open-source implementation of the HL7 FHIR (Fast Healthcare Interoperability Resources) standard for Java. It enables developers to quickly build and deploy FHIR‑based clinical data repositories, offering RESTful APIs, a powerful server framework, and extensive tooling for validation, searching, and transaction processing. The project powers numerous health‑IT solutions and is maintained by the community and Smile CDR, delivering a robust, scalable platform for interoperable healthcare data exchange.
image: https://hapifhir.io/hapi-fhir/images/logos/raccoon-forwards.png
json_schemas:
- name: PostPatientRequest
  property_count: 1
  slug: hapi-fhir-post-patient-request
- name: PostPatientResponse
  property_count: 1
  slug: hapi-fhir-post-patient-response
- name: PutPatientPatientidRequest
  property_count: 1
  slug: hapi-fhir-put-patient-patientid-request
jsonld:
- class_count: 3
  name: Hapi Fhir Context
  property_count: 3
  slug: hapi-fhir-context
layout: provider
modified: '2026-10-13'
name: HAPI FHIR
nav: Providers
network: true
overview: 'HAPI FHIR is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Fhir API and Patient API. Tagged areas include Healthcare, Interoperability, Open Source, Java, and FHIR.


  The HAPI FHIR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HAPI FHIR''s developer surface includes CLI, changelog, API reference, getting-started guide, documentation, engineering blog, support, and 11 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: HAPI FHIR API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: hapi-fhir-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 19.4
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Hapi Fhir Domain Security
  slug: hapi-fhir-domain-security
  summary_line: TLSv1.2 · HSTS
slug: hapi-fhir
tags:
- Healthcare
- Interoperability
- Open Source
- Java
- FHIR
website: https://hapifhir.io
---
