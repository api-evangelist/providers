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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://crm-odata-v1.prospect365.com
  baseurl_source: declared
  description: 'Prospect CRM API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Prospect CRM API
  slug: prospect-crm-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/prospect-crm/vendors/prospect-crm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prospect-crm-vendors.yml
- group: design
  href: https://artifacts.apis.io/prospect-crm/rules/prospect-crm-rules.yml
  title: ''
  type: Spectral
  url: rules/prospect-crm-rules.yml
- group: design
  href: https://artifacts.apis.io/prospect-crm/json-ld/prospect-crm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prospect-crm-context.jsonld
- group: design
  href: https://artifacts.apis.io/prospect-crm/vocabulary/prospect-crm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prospect-crm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/prospect-crm/data-model/prospect-crm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prospect-crm-data-model.yml
- group: design
  href: https://artifacts.apis.io/prospect-crm/conformance/prospect-crm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prospect-crm-conformance.yml
- group: auth
  href: https://artifacts.apis.io/prospect-crm/well-known/prospect-crm-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospect-crm-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/prospect-crm/well-known/prospect-crm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prospect-crm-well-known.yml
- group: other
  href: https://artifacts.apis.io/prospect-crm/hosts/prospect-crm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prospect-crm-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prospect365.com/en/articles/1689197-getting-started-with-business-intelligence-tools-like-power-bi
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prospectsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.prospect365.com/assets/favicon
- group: auth
  href: https://artifacts.apis.io/prospect-crm/security/prospect-crm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prospect-crm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prospectsoft.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation is available as markdown but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.prospect365.com/en/articles/2455275-get-started-with-the-odata-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Prospect CRM is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostNotepadsRequest
  property_count: 3
  slug: prospect-crm-post-notepads-request
jsonld:
- class_count: 1
  name: Prospect Crm Context
  property_count: 3
  slug: prospect-crm-context
layout: provider
modified: '2026-10-28'
name: Prospect CRM
nav: Providers
network: true
overview: 'Prospect CRM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Prospect CRM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Prospect CRM''s developer surface includes getting-started guide, documentation, and 12 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Prospect CRM API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: prospect-crm-rules
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.2
    catalog_earned_first_party: 0.0
    catalog_gap: 73.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 31.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Prospect Crm Authentication
  slug: prospect-crm-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Prospect Crm Domain Security
  slug: prospect-crm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: prospect-crm
tags:
- Company
website: https://prospectsoft.com/
---
