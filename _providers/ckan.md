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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: http://demo.ckan.org
  baseurl_source: declared
  description: The Action API from CKAN — 2 operation(s) for action.
  name: CKAN Action API
  slug: ckan-action-api
- baseURL: http://demo.ckan.org
  baseurl_source: declared
  description: The CKAN API API from CKAN — 1 operation(s) for ckan api.
  name: CKAN CKAN API
  slug: ckan-ckan-api-api
- baseURL: http://demo.ckan.org
  baseurl_source: declared
  description: The Search API from CKAN — 1 operation(s) for search.
  name: CKAN Search API
  slug: ckan-search-api
- baseURL: http://demo.ckan.org
  baseurl_source: declared
  description: The Solr API from CKAN — 3 operation(s) for solr.
  name: CKAN Solr API
  slug: ckan-solr-api
artifact_total: 10
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ckan.org/en/2.12/maintaining/getting-started.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/rules/ckan-rules.yml
  title: ''
  type: Spectral
  url: rules/ckan-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/json-ld/ckan-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ckan-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/vocabulary/ckan-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ckan-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/data-model/ckan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ckan-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/changelog/ckan-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ckan-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/conformance/ckan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ckan-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/hosts/ckan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ckan-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/vendors/ckan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ckan-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/packages/ckan-packages.yml
  title: ''
  type: SDKs
  url: packages/ckan-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/packages/ckan-packages.yml
  title: ''
  type: Packages
  url: packages/ckan-packages.yml
- group: start
  title: ''
  type: Login
  url: https://ckan.org/accounts/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ckan/refs/heads/main/security/ckan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ckan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ckan.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/2.12/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ckan.org/en/2.12/api/index.html
- group: company
  title: ''
  type: Blog
  url: https://ckan.org/blog
- group: operate
  title: ''
  type: Support
  url: https://ckan.org/faq
coverage:
  checked: '2026-10-13'
  detail: The CKAN documentation provides API guides but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://docs.ckan.org/en/2.12/api/index.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: CKAN is an open-source data management system that powers data portals and hubs worldwide. It enables organizations to publish, share, and use data efficiently, supporting governments, enterprises, and communities across the globe. CKAN provides robust features for data cataloging, API access, and community-driven extensions, fostering open data initiatives and transparency.
image: https://ckan.org/media/images/CKAN-Website-Launch_G0ZlBCH.original.png
json_schemas:
- name: GetApiActionActionidResponse
  property_count: 1
  slug: ckan-get-api-action-actionid-response
- name: GetApiSearchDatasetResponse
  property_count: 1
  slug: ckan-get-api-search-dataset-response
- name: GetResponse
  property_count: 3
  slug: ckan-get-response
jsonld:
- class_count: 3
  name: Ckan Context
  property_count: 5
  slug: ckan-context
layout: provider
modified: '2026-10-13'
name: CKAN
nav: Providers
network: true
overview: 'CKAN is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Action API, CKAN API, Search API, and 1 more. Tagged areas include Open Source, Data-Management, Government, and Community.


  The CKAN catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CKAN''s developer surface includes getting-started guide, changelog, documentation, API reference, engineering blog, support, and 12 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: CKAN API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 1
  slug: ckan-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Ckan Domain Security
  slug: ckan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ckan
tags:
- Open Source
- Data-Management
- Government
- Community
website: https://ckan.org
---
