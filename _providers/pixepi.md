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
    error_semantics: verified
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
  score: 21.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: External developer API for Pixepi tools providing PDF, image and text processing.
  name: Pixepi API
  slug: pixepi-api
- baseURL: https://api.pixepi.com
  baseurl_source: declared
  description: The Apps API from Pixepi — 11 operation(s) for apps.
  name: Pixepi Apps API
  slug: pixepi-apps-api
- baseURL: https://api.pixepi.com
  baseurl_source: declared
  description: The Jobs API from Pixepi — 2 operation(s) for jobs.
  name: Pixepi Jobs API
  slug: pixepi-jobs-api
- baseURL: https://api.pixepi.com
  baseurl_source: declared
  description: The Usage API from Pixepi — 1 operation(s) for usage.
  name: Pixepi Usage API
  slug: pixepi-usage-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/rules/pixepi-rules.yml
  title: ''
  type: Spectral
  url: rules/pixepi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/json-ld/pixepi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pixepi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/vocabulary/pixepi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pixepi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/conformance/pixepi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pixepi-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/data-model/pixepi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pixepi-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/errors/pixepi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pixepi-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/hosts/pixepi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pixepi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/vendors/pixepi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pixepi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pixepi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pixepi.com/privacy
- group: start
  title: ''
  type: Login
  url: https://pixepi.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://pixepi.com/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pixepi/refs/heads/main/security/pixepi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixepi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pixepi.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.pixepi.com/api/v1
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://pixepi.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Pixepi provides practical online tools for PDFs, images, text and more, allowing users to process files via HTTP APIs without installing software or signing up. The platform offers a range of utilities such as PDF conversion, image manipulation, and OCR, accessible through a bearer‑key secured REST API. It targets developers needing quick, free‑tier access to common document processing tasks.
image: https://pixepi.com/og-image.png?app=core
json_schemas:
- name: Job
  property_count: 5
  slug: pixepi-job
jsonld:
- class_count: 2
  name: Pixepi Context
  property_count: 9
  slug: pixepi-context
layout: provider
modified: '2026-10-15'
name: Pixepi
nav: Providers
network: true
overview: 'Pixepi publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Jobs API, Usage API, and 1 more. Tagged areas include Company, Tools, PDF, and Image.


  The Pixepi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pixepi''s developer surface includes API reference, documentation, and 13 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Pixepi API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: pixepi-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Pixepi Domain Security
  slug: pixepi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pixepi
tags:
- Company
- Tools
- PDF
- Image
website: https://pixepi.com
---
