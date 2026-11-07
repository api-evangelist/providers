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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Docspeed Ai Agentic Access
  operation_count: 44
  slug: docspeed-ai-agentic-access
  summary_line: 44 operations · 34 acting
api_count: 1
apis:
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: Agent creation and tool discovery APIs.
  name: Docspeed Agents API
  slug: docspeed-ai-agents-api
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: Single and multi-document chat endpoints.
  name: Docspeed Chat API
  slug: docspeed-ai-chat-api
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: Schema-driven and specialized extraction APIs.
  name: Docspeed Extraction API
  slug: docspeed-ai-extraction-api
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: File upload, retrieval, and page image access.
  name: Docspeed Files API
  slug: docspeed-ai-files-api
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: The Generation API from Docspeed — 3 operation(s) for generation.
  name: Docspeed Generation API
  slug: docspeed-ai-generation-api
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: Async job status and result retrieval endpoints.
  name: Docspeed Jobs API
  slug: docspeed-ai-jobs-api
- baseURL: https://api.docspeed.ai
  baseurl_source: declared
  description: Core parsing, layout, OCR, classify, and split operations.
  name: Docspeed Processing API
  slug: docspeed-ai-processing-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/docspeed-ai/agentic-access/docspeed-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docspeed-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/docspeed-ai/rules/docspeed-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/docspeed-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/docspeed-ai/json-ld/docspeed-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docspeed-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/docspeed-ai/vocabulary/docspeed-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docspeed-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/docspeed-ai/data-model/docspeed-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docspeed-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/docspeed-ai/changelog/docspeed-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docspeed-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/docspeed-ai/authentication/docspeed-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docspeed-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/docspeed-ai/errors/docspeed-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docspeed-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docspeed-ai/conformance/docspeed-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docspeed-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docspeed-ai/well-known/docspeed-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docspeed-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/docspeed-ai/hosts/docspeed-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docspeed-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/docspeed-ai/vendors/docspeed-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docspeed-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docspeed.ai/terms
- group: start
  title: ''
  type: Sandbox
  url: https://www.docspeed.ai/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docspeed.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docspeed.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://api.docspeed.ai/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.docspeed.ai/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.docspeed.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://api.docspeed.ai/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://api.docspeed.ai/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/docspeed-ai/security/docspeed-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docspeed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docspeed.ai/
created: '2026-11-05'
description: Docspeed provides AP invoice extraction focused on Indian GST invoices for BPO and shared‑services teams. The service extracts GSTIN, vendor details, tax blocks, totals and line items and presents grounded, source‑linked evidence to speed exception handling. It is built for procurement and finance workflows that require structured, trusted data before production rollout.
image: https://www.docspeed.ai/docspeed-logo.svg
json_schemas:
- name: AskRequest
  property_count: 7
  slug: docspeed-ai-ask-request
- name: ClassificationResult
  property_count: 8
  slug: docspeed-ai-classification-result
- name: ClassifyRequest
  property_count: 6
  slug: docspeed-ai-classify-request
- name: ParseResponse
  property_count: 7
  slug: docspeed-ai-parse-response
- name: SchemaAutoRequest
  property_count: 5
  slug: docspeed-ai-schema-auto-request
- name: TableExtractRequest
  property_count: 5
  slug: docspeed-ai-table-extract-request
jsonld:
- class_count: 50
  name: Docspeed Ai Context
  property_count: 132
  slug: docspeed-ai-context
layout: provider
modified: '2026-11-05'
name: Docspeed
nav: Providers
network: true
overview: 'Docspeed publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Chat API, Extraction API, and 4 more. Tagged areas include AP Invoice Extraction, BPO, Shared Services, Document AI, and Financial Services.


  The Docspeed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Docspeed''s developer surface includes changelog, authentication, sandbox, pricing, documentation, engineering blog, getting-started guide, and 16 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Docspeed API Rules
  rule_count: 50
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 2
  slug: docspeed-ai-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 55.3
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docspeed Ai Authentication
  slug: docspeed-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Docspeed Ai Domain Security
  slug: docspeed-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docspeed-ai
tags:
- AP Invoice Extraction
- BPO
- Shared Services
- Document AI
- Financial Services
- Procurement Automation
website: https://docspeed.ai/
---
