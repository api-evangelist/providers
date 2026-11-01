---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Twine Integrations API provides endpoints for HR and payroll automation integration.
  name: Twine API
  slug: twine-api-2
- baseURL: https://api.twine.se
  baseurl_source: declared
  description: 'Twine Integrations API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Twine Integrations API
  slug: twine-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/twine/rules/twine-rules.yml
  title: ''
  type: Spectral
  url: rules/twine-rules.yml
- group: design
  href: https://artifacts.apis.io/twine/json-ld/twine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/twine-context.jsonld
- group: design
  href: https://artifacts.apis.io/twine/vocabulary/twine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/twine-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/twine/data-model/twine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/twine-data-model.yml
- group: operate
  href: https://artifacts.apis.io/twine/changelog/twine-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/twine-changelog.yml
- group: design
  href: https://artifacts.apis.io/twine/conventions/twine-conventions.yml
  title: ''
  type: Conventions
  url: conventions/twine-conventions.yml
- group: auth
  href: https://artifacts.apis.io/twine/authentication/twine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twine-authentication.yml
- group: design
  href: https://artifacts.apis.io/twine/conformance/twine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twine-conformance.yml
- group: agent
  href: https://artifacts.apis.io/twine/llms/twine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twine-llms.txt
- group: other
  href: https://artifacts.apis.io/twine/a2a/twine-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/twine-a2a.yml
- group: auth
  href: https://artifacts.apis.io/twine/well-known/twine-app-stage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/twine-app-stage-security.txt
- group: auth
  href: https://artifacts.apis.io/twine/well-known/twine-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/twine-app-security.txt
- group: agent
  href: https://artifacts.apis.io/twine/well-known/twine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/twine-well-known.yml
- group: other
  href: https://artifacts.apis.io/twine/hosts/twine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/twine-hosts.yml
- group: other
  href: https://artifacts.apis.io/twine/vendors/twine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/twine-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.twine.se/blogg/webhooks
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.twine.se/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.twine.se/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.twine.se/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.twine.se/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/twine/security/twine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://twine.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.twine.se/
- group: company
  title: ''
  type: Blog
  url: https://www.twine.se/blogg
- group: operate
  title: ''
  type: Support
  url: https://www.twine.se/kontakta-oss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twine.se/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.twine.se/terms-of-service
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 200
    url: https://docs.twine.se/api-reference/introduction
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Twine Integrations is a Nordic integration partner specializing in HR and payroll automation. They provide a platform that connects and synchronizes HR and payroll systems across the region, enabling efficient data access and process automation. Their solutions help businesses save time and resources while ensuring compliance and data security.
image: http://static1.squarespace.com/static/63cec8699b6d396be083ed8b/t/66cca37e84ff6667f5edcfb0/1724687234196/twine%2Bvertical%2B%2528kopia%2529.jpg?format=1500w
json_schemas:
- name: GetV1OrgJobsJobidResponse
  property_count: 2
  slug: twine-get-v1-org-jobs-jobid-response
- name: PatchV1OrgSystemIntegrationsIdRequest
  property_count: 7
  slug: twine-patch-v1-org-system-integrations-id-request
- name: PostV1OrgDomainMappingsRequest
  property_count: 7
  slug: twine-post-v1-org-domain-mappings-request
- name: PostV1OrgResponse
  property_count: 2
  slug: twine-post-v1-org-response
- name: PostV1OrgSystemIntegrationsRequest
  property_count: 11
  slug: twine-post-v1-org-system-integrations-request
- name: PutV1OrgSystemIntegrationsIdRequest
  property_count: 4
  slug: twine-put-v1-org-system-integrations-id-request
jsonld:
- class_count: 12
  name: Twine Context
  property_count: 25
  slug: twine-context
layout: provider
modified: '2026-10-19'
name: Twine Integrations
nav: Providers
network: true
overview: 'Twine Integrations is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Payroll, Integration, and Nordic.


  The Twine Integrations catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Twine Integrations'' developer surface includes changelog, authentication, API reference, documentation, engineering blog, support, and 21 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Twine Integrations API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: twine-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Twine Authentication
  slug: twine-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Twine Domain Security
  slug: twine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: twine
tags:
- Company
- Human Resources
- Payroll
- Integration
- Nordic
website: https://twine.se/
---
