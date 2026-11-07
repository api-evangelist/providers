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
    error_semantics: false
    event_surface_described: true
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
  score: 19.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://demo.gotenberg.dev
  baseurl_source: declared
  description: 'Gotenberg API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Gotenberg API
  slug: gotenberg-api
artifact_total: 7
asyncapis:
- description: ''
  name: Gotenberg Webhooks
  slug: gotenberg-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://gotenberg.dev/docs
- group: design
  href: https://artifacts.apis.io/gotenberg/rules/gotenberg-rules.yml
  title: ''
  type: Spectral
  url: rules/gotenberg-rules.yml
- group: design
  href: https://artifacts.apis.io/gotenberg/json-ld/gotenberg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gotenberg-context.jsonld
- group: design
  href: https://artifacts.apis.io/gotenberg/vocabulary/gotenberg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gotenberg-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gotenberg/asyncapi/gotenberg-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gotenberg-webhooks.yml
- group: design
  href: https://artifacts.apis.io/gotenberg/data-model/gotenberg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gotenberg-data-model.yml
- group: design
  href: https://artifacts.apis.io/gotenberg/conformance/gotenberg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gotenberg-conformance.yml
- group: other
  href: https://artifacts.apis.io/gotenberg/hosts/gotenberg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gotenberg-hosts.yml
- group: other
  href: https://artifacts.apis.io/gotenberg/vendors/gotenberg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gotenberg-vendors.yml
- group: build
  href: https://artifacts.apis.io/gotenberg/packages/gotenberg-packages.yml
  title: ''
  type: SDKs
  url: packages/gotenberg-packages.yml
- group: build
  href: https://artifacts.apis.io/gotenberg/packages/gotenberg-packages.yml
  title: ''
  type: Packages
  url: packages/gotenberg-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gotenberg
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/gotenberg/gotenberg/releases/tag/v8.0.0
- group: company
  title: ''
  type: Blog
  url: https://gotenberg.dev/blog
- group: auth
  href: https://artifacts.apis.io/gotenberg/security/gotenberg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gotenberg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gotenberg.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://gotenberg.dev/docs/getting-started/introduction
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/gotenberg/gotenberg
- group: start
  title: ''
  type: GettingStarted
  url: https://gotenberg.dev/docs/getting-started/introduction
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/gotenberg/gotenberg
created: '2026-10-27'
description: Gotenberg provides a Docker-based API for converting documents to PDF and other formats. It offers a simple HTTP interface where users can POST files like HTML, Markdown, or Office documents and receive a generated PDF. The service runs as a container, making it easy to self‑host, and supports features such as merging PDFs, adding headers/footers, and applying custom CSS. Documentation, examples, and a quick‑start guide are available on its website.
image: https://gotenberg.dev/img/og-image.png
json_schemas:
- name: PostFormsRequest
  property_count: 1
  slug: gotenberg-post-forms-request
- name: PostFormsResponse
  property_count: 3
  slug: gotenberg-post-forms-response
jsonld:
- class_count: 2
  name: Gotenberg Context
  property_count: 1
  slug: gotenberg-context
layout: provider
modified: '2026-10-27'
name: Gotenberg
nav: Providers
network: true
overview: 'Gotenberg is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, Docker, Conversion, and Open Source.


  The Gotenberg catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gotenberg''s developer surface includes documentation, changelog, engineering blog, getting-started guide, and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Gotenberg API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: gotenberg-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 28.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 24.9
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gotenberg/gotenberg-2026-11-03T132947.png
security:
- kind: domain-security
  name: Gotenberg Domain Security
  slug: gotenberg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: gotenberg
tags:
- PDF
- Docker
- Conversion
- Open Source
website: https://gotenberg.dev/
---
