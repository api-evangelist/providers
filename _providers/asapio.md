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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: API for ASAPIO Integration Add‑on connecting SAP to cloud platforms.
  name: ASAPIO Integration API
  slug: asapio-integration-api
- description: The Connectionset API from ASAPIO — 1 operation(s) for connectionset.
  name: ASAPIO Connectionset API
  slug: asapio-connectionset-api
- description: The Connectorset API from ASAPIO — 1 operation(s) for connectorset.
  name: ASAPIO Connectorset API
  slug: asapio-connectorset-api
- description: The Interfaceset API from ASAPIO — 1 operation(s) for interfaceset.
  name: ASAPIO Interfaceset API
  slug: asapio-interfaceset-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/rules/asapio-rules.yml
  title: ''
  type: Spectral
  url: rules/asapio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/json-ld/asapio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asapio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/vocabulary/asapio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asapio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/data-model/asapio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asapio-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/changelog/asapio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/asapio-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/conformance/asapio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asapio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/llms/asapio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asapio-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/hosts/asapio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asapio-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asapio.com/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asapio.com/privacy.php
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asapio/refs/heads/main/security/asapio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asapio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asapio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asapio.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://asapio.com/docs/getting-started.html
- group: docs
  title: ''
  type: APIReference
  url: https://asapio.com/docs/asyncapi/index.html
- group: operate
  title: ''
  type: Support
  url: https://asapio.com/contact.php
- group: company
  title: ''
  type: Blog
  url: https://asapio.com/blog/
coverage:
  checked: '2026-10-16'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 0
    url: https://api.asapio.com/openapi.json
  - status: 404
    url: https://docs.asapio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: ASAPIO is an SAP Silver Partner specializing in SAP-to-cloud integration since 2003. The company provides the ASAPIO Integration Add‑on that connects SAP S/4HANA and ECC to major cloud platforms such as Azure, AWS, Google Cloud, Kafka, and Solace in real‑time without custom ABAP. Trusted by over 350 enterprises, ASAPIO offers pre‑built connectors, event‑driven architecture, and comprehensive documentation for developers and integrators.
json_schemas:
- name: GetConnectionsetResponse
  property_count: 6
  slug: asapio-get-connectionset-response
- name: GetConnectorsetResponse
  property_count: 9
  slug: asapio-get-connectorset-response
- name: GetInterfacesetResponse
  property_count: 13
  slug: asapio-get-interfaceset-response
jsonld:
- class_count: 3
  name: Asapio Context
  property_count: 20
  slug: asapio-context
layout: provider
modified: '2026-10-16'
name: ASAPIO
nav: Providers
network: true
overview: 'ASAPIO is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Connectionset API, Connectorset API, Interfaceset API, and 1 more. Tagged areas include Company, SAP, Integration, Cloud, and Enterprise.


  The ASAPIO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ASAPIO''s developer surface includes changelog, documentation, getting-started guide, API reference, support, engineering blog, and 11 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: ASAPIO API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: asapio-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 44.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.1
    contract_governance: 22.0
    contract_quality: 20.9
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Asapio Domain Security
  slug: asapio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asapio
tags:
- Company
- SAP
- Integration
- Cloud
- Enterprise
website: https://asapio.com/
---
