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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Ireceipt Pro Agentic Access
  operation_count: 17
  slug: ireceipt-pro-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.ireceipt.pro/v1
  baseurl_source: declared
  description: Get JPG image
  name: ireceipt-pro /jpg API
  slug: ireceipt-pro-jpg-api
- baseURL: https://api.ireceipt.pro/v1
  baseurl_source: declared
  description: Get PDF file
  name: ireceipt-pro /pdf API
  slug: ireceipt-pro-pdf-api
- baseURL: https://api.ireceipt.pro/v1
  baseurl_source: declared
  description: Check the status of the API
  name: ireceipt-pro /ping API
  slug: ireceipt-pro-ping-api
- baseURL: https://api.ireceipt.pro/v1
  baseurl_source: declared
  description: Get PNG image
  name: ireceipt-pro /png API
  slug: ireceipt-pro-png-api
- baseURL: https://api.ireceipt.pro/v1
  baseurl_source: declared
  description: Get WEBP image
  name: ireceipt-pro /webp API
  slug: ireceipt-pro-webp-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/ireceipt-pro/agentic-access/ireceipt-pro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ireceipt-pro-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ireceipt-pro/rules/ireceipt-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/ireceipt-pro-rules.yml
- group: design
  href: https://artifacts.apis.io/ireceipt-pro/json-ld/ireceipt-pro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ireceipt-pro-context.jsonld
- group: design
  href: https://artifacts.apis.io/ireceipt-pro/vocabulary/ireceipt-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ireceipt-pro-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ireceipt-pro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ireceipt-pro/data-model/ireceipt-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ireceipt-pro-data-model.yml
- group: design
  href: https://artifacts.apis.io/ireceipt-pro/errors/ireceipt-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ireceipt-pro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ireceipt-pro/conformance/ireceipt-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ireceipt-pro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ireceipt-pro/llms/ireceipt-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ireceipt-pro-llms.txt
- group: other
  href: https://artifacts.apis.io/ireceipt-pro/hosts/ireceipt-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ireceipt-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/ireceipt-pro/vendors/ireceipt-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ireceipt-pro-vendors.yml
- group: build
  href: https://artifacts.apis.io/ireceipt-pro/packages/ireceipt-pro-packages.yml
  title: ''
  type: SDKs
  url: packages/ireceipt-pro-packages.yml
- group: build
  href: https://artifacts.apis.io/ireceipt-pro/packages/ireceipt-pro-packages.yml
  title: ''
  type: Packages
  url: packages/ireceipt-pro-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ireceipt.pro/docs/license.md
- group: docs
  title: ''
  type: APIReference
  url: https://api.ireceipt.pro
- group: auth
  href: https://artifacts.apis.io/ireceipt-pro/authentication/ireceipt-pro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ireceipt-pro-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ireceipt-pro/security/ireceipt-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ireceipt-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ireceipt.pro/
- group: start
  title: ''
  type: GettingStarted
  url: https://ireceipt.pro/quickstart
created: '2026-10-30'
description: iReceipt PRO provides a PDF and image generation API that lets developers create PDFs, JPGs, PNGs, and WEBP files from templates. It offers a library of over 250 ready‑made templates for invoices, certificates, gift cards, tickets, and more, plus the ability to upload custom designs. The service includes a free trial, SDKs for JavaScript/TypeScript, and a sandbox for testing. Documentation includes quickstart guides, API reference, and pricing information.
image: https://ireceipt.pro/assets/images/og-image.png
json_schemas:
- name: BasicRequestBody
  property_count: 3
  slug: ireceipt-pro-basic-request-body
jsonld:
- class_count: 3
  name: Ireceipt Pro Context
  property_count: 5
  slug: ireceipt-pro-context
layout: provider
modified: '2026-10-30'
name: ireceipt-pro
nav: Providers
network: true
overview: 'ireceipt-pro publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including /jpg API, /pdf API, /ping API, and 2 more. Tagged areas include Company, PDF, Image Generation, and Templates.


  The ireceipt-pro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ireceipt-pro''s developer surface includes documentation, API reference, authentication, getting-started guide, and 15 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Ireceipt Pro Rate Limits
  slug: ireceipt-pro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: ireceipt-pro API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: ireceipt-pro-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 54.0
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ireceipt-pro/ireceipt-pro-2026-11-03T134032.png
security:
- kind: authentication
  name: Ireceipt Pro Authentication
  slug: ireceipt-pro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ireceipt Pro Domain Security
  slug: ireceipt-pro-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: generate-pdf
  slug: ireceipt-pro-generate-pdf
- name: ireceipt-pro-jpg-generate-public
  slug: ireceipt-pro-jpg-generate-public
slug: ireceipt-pro
tags:
- Company
- PDF
- Image Generation
- Templates
website: https://ireceipt.pro/
---
