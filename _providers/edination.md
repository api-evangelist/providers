---
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
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: EdiNation provides a browser‑based EDI validation and translation API documented at the EdiFabric developer portal.
  name: EdiNation API
  slug: edination-api-2
- baseURL: https://api.edination.com
  baseurl_source: declared
  description: 'EdiNation API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: EdiNation API
  slug: edination-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/edination/plans/edination-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edination-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/edination/rules/edination-rules.yml
  title: ''
  type: Spectral
  url: rules/edination-rules.yml
- group: design
  href: https://artifacts.apis.io/edination/json-ld/edination-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/edination-context.jsonld
- group: design
  href: https://artifacts.apis.io/edination/vocabulary/edination-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/edination-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/edination/data-model/edination-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edination-data-model.yml
- group: operate
  href: https://artifacts.apis.io/edination/changelog/edination-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/edination-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.edifabric.com/edination/
- group: auth
  href: https://artifacts.apis.io/edination/authentication/edination-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edination-authentication.yml
- group: design
  href: https://artifacts.apis.io/edination/conformance/edination-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edination-conformance.yml
- group: agent
  href: https://artifacts.apis.io/edination/llms/edination-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edination-llms.txt
- group: other
  href: https://artifacts.apis.io/edination/hosts/edination-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edination-hosts.yml
- group: other
  href: https://artifacts.apis.io/edination/vendors/edination-vendors.yml
  title: ''
  type: Vendors
  url: vendors/edination-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EdiFabric
- group: start
  title: ''
  type: GettingStarted
  url: https://www.edifabric.com/docs/getting-started/introduction.html
- group: auth
  href: https://artifacts.apis.io/edination/security/edination-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/edination-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/edination/security/edination-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edination-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edination.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.edifabric.com/docs/edination/edination-your-local-edi-editor-in-the-browser.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.edifabric.com/edination/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edifabric.com/pricing.html?utm_source=edination&utm_medium=referral&utm_campaign=header-cta
- group: operate
  title: ''
  type: Support
  url: https://support.edifabric.com/hc/en-us/requests/new
coverage:
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.edifabric.com/docs/edifabric-cloud/x12-operations.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: EdiNation provides free X12 and HIPAA EDI validation, translation, and editing tools that run entirely in the browser using WebAssembly, ensuring that sensitive health information never leaves the client device. The platform offers a suite of utilities including EDI to JSON conversion, acknowledgment generation, and a comprehensive spec library covering X12, HIPAA, EDIFACT, HL7, NCPDP, and VDA standards, aimed at developers and healthcare organizations seeking secure, on‑premise EDI processing.
image: https://www.edifabric.com/edination/assets/img/edination-linkedin.png
json_schemas:
- name: PostEdifactReadResponse
  property_count: 3
  slug: edination-post-edifact-read-response
- name: PostEdifactValidateResponse
  property_count: 3
  slug: edination-post-edifact-validate-response
- name: PostNcpdpValidateRequest
  property_count: 4
  slug: edination-post-ncpdp-validate-request
- name: PostNcpdpWriteRequest
  property_count: 4
  slug: edination-post-ncpdp-write-request
- name: PostX12AckResponse
  property_count: 7
  slug: edination-post-x12-ack-response
- name: PostX12ReadResponse
  property_count: 7
  slug: edination-post-x12-read-response
jsonld:
- class_count: 19
  name: Edination Context
  property_count: 18
  slug: edination-context
layout: provider
modified: '2026-10-20'
name: EdiNation
nav: Providers
network: true
overview: 'EdiNation is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EDI, Healthcare, Validation, and Open Source.


  The EdiNation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EdiNation''s developer surface includes changelog, authentication, getting-started guide, documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Edination Plans Pricing
  plan_count: 3
  slug: edination-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: EdiNation API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: edination-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Edination Authentication
  slug: edination-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Edination Domain Security
  slug: edination-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Edination Trust Center
  slug: edination-trust-center
  summary_line: HIPAA
slug: edination
tags:
- Company
- EDI
- Healthcare
- Validation
- Open Source
website: https://edination.com/
---
