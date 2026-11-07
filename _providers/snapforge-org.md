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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://snapforge.org
  baseurl_source: declared
  description: 'snapforge-org API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: snapforge-org API
  slug: snapforge-org-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/snapforge-org/rules/snapforge-org-rules.yml
  title: ''
  type: Spectral
  url: rules/snapforge-org-rules.yml
- group: design
  href: https://artifacts.apis.io/snapforge-org/json-ld/snapforge-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snapforge-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/snapforge-org/vocabulary/snapforge-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snapforge-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/snapforge-org/data-model/snapforge-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snapforge-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/snapforge-org/conformance/snapforge-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snapforge-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/snapforge-org/llms/snapforge-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snapforge-org-llms.txt
- group: other
  href: https://artifacts.apis.io/snapforge-org/hosts/snapforge-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snapforge-org-hosts.yml
- group: build
  href: https://artifacts.apis.io/snapforge-org/packages/snapforge-org-packages.yml
  title: ''
  type: SDKs
  url: packages/snapforge-org-packages.yml
- group: build
  href: https://artifacts.apis.io/snapforge-org/packages/snapforge-org-packages.yml
  title: ''
  type: Packages
  url: packages/snapforge-org-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snapforge.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snapforge.org/privacy
- group: auth
  href: https://artifacts.apis.io/snapforge-org/security/snapforge-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snapforge-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snapforge.org/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host.
  evidence:
  - status: 404
    url: https://api.snapforge.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: SnapForge provides a Screenshots, PDFs and Markdown API designed for AI agents. It converts any URL or HTML into pixel-perfect screenshots, print-ready PDFs, or clean Markdown suitable for large language models. The service includes native Model Context Protocol (MCP) integration, allowing seamless tool usage within AI agents like Claude, Cursor, and others. Pricing tiers include a free trial with 100 renders and paid plans for higher volume, and the platform offers comprehensive documentation, examples, and a privacy policy.
image: https://snapforge.org/logo.png
json_schemas:
- name: GetV1UsageResponse
  property_count: 3
  slug: snapforge-org-get-v1-usage-response
- name: PostSignupResponse
  property_count: 3
  slug: snapforge-org-post-signup-response
- name: PostV1MarkdownResponse
  property_count: 6
  slug: snapforge-org-post-v1-markdown-response
- name: PostV1PdfRequest
  property_count: 7
  slug: snapforge-org-post-v1-pdf-request
- name: PostV1ScreenshotRequest
  property_count: 10
  slug: snapforge-org-post-v1-screenshot-request
- name: PostV1ScreenshotResponse
  property_count: 1
  slug: snapforge-org-post-v1-screenshot-response
jsonld:
- class_count: 9
  name: Snapforge Org Context
  property_count: 21
  slug: snapforge-org-context
layout: provider
modified: '2026-10-31'
name: snapforge-org
nav: Providers
network: true
overview: 'snapforge-org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Screenshots, PDF, Markdown, and MCP.


  The snapforge-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: snapforge-org API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: snapforge-org-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 7.1
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 21.8
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/snapforge-org/snapforge-org-2026-11-03T143405.png
security:
- kind: domain-security
  name: Snapforge Org Domain Security
  slug: snapforge-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snapforge-org
tags:
- Artificial Intelligence
- Screenshots
- PDF
- Markdown
- MCP
website: https://snapforge.org/
---
