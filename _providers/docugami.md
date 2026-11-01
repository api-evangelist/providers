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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.docugami.com
  baseurl_source: declared
  description: 'Docugami API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: Docugami API
  slug: docugami-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/docugami/rules/docugami-rules.yml
  title: ''
  type: Spectral
  url: rules/docugami-rules.yml
- group: design
  href: https://artifacts.apis.io/docugami/json-ld/docugami-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docugami-context.jsonld
- group: design
  href: https://artifacts.apis.io/docugami/vocabulary/docugami-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docugami-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/docugami/data-model/docugami-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docugami-data-model.yml
- group: design
  href: https://artifacts.apis.io/docugami/conformance/docugami-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docugami-conformance.yml
- group: other
  href: https://artifacts.apis.io/docugami/hosts/docugami-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docugami-hosts.yml
- group: other
  href: https://artifacts.apis.io/docugami/vendors/docugami-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docugami-vendors.yml
- group: build
  href: https://artifacts.apis.io/docugami/packages/docugami-packages.yml
  title: ''
  type: SDKs
  url: packages/docugami-packages.yml
- group: build
  href: https://artifacts.apis.io/docugami/packages/docugami-packages.yml
  title: ''
  type: Packages
  url: packages/docugami-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docugami.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.docugami.com/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docugami.com/privacy?hsLang=en
- group: company
  title: ''
  type: Newsroom
  url: https://www.docugami.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.docugami.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.docugami.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.docugami.com/
- group: auth
  href: https://artifacts.apis.io/docugami/security/docugami-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docugami-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.docugami.com/
coverage:
  checked: '2026-10-23'
  detail: The main website renders content via JavaScript, preventing machine‑readable discovery of API specifications.
  evidence:
  - status: 200
    url: https://www.docugami.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Docugami provides an AI-powered document automation platform that transforms unstructured business documents into actionable knowledge graphs. Their technology enables enterprises to extract, organize, and act on data locked in contracts, reports, and other files, supporting use cases such as contract lifecycle management, data extraction, and workflow automation. By leveraging proprietary AI, Docugami helps reduce manual effort, improve compliance, and accelerate decision‑making across industries.
image: https://www.docugami.com/hubfs/System%20of%20Action%20Slide%20(2).png
json_schemas:
- name: GetDocsetsDocsetidPropertiesPropertyidDocumentsDocumentidRes
  property_count: 5
  slug: docugami-get-docsets-docsetid-properties-propertyid-documents-documentid-res
- name: GetDocumentsIdResponse
  property_count: 12
  slug: docugami-get-documents-id-response
- name: GetProjectsIdResponse
  property_count: 8
  slug: docugami-get-projects-id-response
- name: GetV1Preview1DocumentsBn0Px5Iaym7ZResponse
  property_count: 3
  slug: docugami-get-v1-preview1-documents-bn0-px5-iaym7-zresponse
- name: GetWebhooksIdResponse
  property_count: 8
  slug: docugami-get-webhooks-id-response
- name: PostDocumentsTemporaryurlRequest
  property_count: 4
  slug: docugami-post-documents-temporaryurl-request
jsonld:
- class_count: 10
  name: Docugami Context
  property_count: 32
  slug: docugami-context
layout: provider
modified: '2026-10-23'
name: Docugami
nav: Providers
network: true
overview: 'Docugami is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Document Automation, Enterprise, and Contract Management.


  The Docugami catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Docugami''s developer surface includes support, engineering blog, documentation, and 15 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Docugami API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: docugami-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 23.8
    discoverability: 69.6
    operational_transparency: 0.0
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docugami Domain Security
  slug: docugami-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docugami
tags:
- Company
- Artificial Intelligence
- Document Automation
- Enterprise
- Contract Management
website: https://www.docugami.com/
---
