---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Docuqueue Com Agentic Access
  operation_count: 35
  slug: docuqueue-com-agentic-access
  summary_line: 35 operations · 19 acting
api_count: 1
apis:
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Batch API from docuqueue-com — 4 operation(s) for batch.
  name: docuqueue-com Batch API
  slug: docuqueue-com-batch-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Conversion API from docuqueue-com — 4 operation(s) for conversion.
  name: docuqueue-com Conversion API
  slug: docuqueue-com-conversion-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Document Generation API from docuqueue-com — 1 operation(s) for document generation.
  name: docuqueue-com Document Generation API
  slug: docuqueue-com-document-generation-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Forms API from docuqueue-com — 5 operation(s) for forms.
  name: docuqueue-com Forms API
  slug: docuqueue-com-forms-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Research API from docuqueue-com — 2 operation(s) for research.
  name: docuqueue-com Research API
  slug: docuqueue-com-research-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Shared Documents API from docuqueue-com — 2 operation(s) for shared documents.
  name: docuqueue-com Shared Documents API
  slug: docuqueue-com-shared-documents-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Sharing API from docuqueue-com — 2 operation(s) for sharing.
  name: docuqueue-com Sharing API
  slug: docuqueue-com-sharing-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The System API from docuqueue-com — 1 operation(s) for system.
  name: docuqueue-com System API
  slug: docuqueue-com-system-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Templates API from docuqueue-com — 8 operation(s) for templates.
  name: docuqueue-com Templates API
  slug: docuqueue-com-templates-api
- baseURL: https://docuqueue.com/api/v1
  baseurl_source: declared
  description: The Upload API from docuqueue-com — 1 operation(s) for upload.
  name: docuqueue-com Upload API
  slug: docuqueue-com-upload-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/docuqueue-com/agentic-access/docuqueue-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docuqueue-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/docuqueue-com/plans/docuqueue-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docuqueue-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docuqueue-com/rules/docuqueue-com-rules.yml
  title: ''
  type: Spectral
  url: rules/docuqueue-com-rules.yml
- group: design
  href: https://artifacts.apis.io/docuqueue-com/json-ld/docuqueue-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docuqueue-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/docuqueue-com/vocabulary/docuqueue-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docuqueue-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/docuqueue-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/docuqueue-com/data-model/docuqueue-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docuqueue-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/docuqueue-com/authentication/docuqueue-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docuqueue-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/docuqueue-com/errors/docuqueue-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docuqueue-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docuqueue-com/conformance/docuqueue-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docuqueue-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docuqueue-com/llms/docuqueue-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docuqueue-com-llms.txt
- group: other
  href: https://artifacts.apis.io/docuqueue-com/a2a/docuqueue-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/docuqueue-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/docuqueue-com/mcp/docuqueue-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docuqueue-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/docuqueue-com/well-known/docuqueue-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docuqueue-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/docuqueue-com/hosts/docuqueue-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docuqueue-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/docuqueue-com/packages/docuqueue-com-packages.yml
  title: ''
  type: SDKs
  url: packages/docuqueue-com-packages.yml
- group: build
  href: https://artifacts.apis.io/docuqueue-com/packages/docuqueue-com-packages.yml
  title: ''
  type: Packages
  url: packages/docuqueue-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://docuqueue.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docuqueue.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://docuqueue.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docuqueue.com/docs/mcp-setup
- group: auth
  href: https://artifacts.apis.io/docuqueue-com/security/docuqueue-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docuqueue-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docuqueue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docuqueue.com/docs/document-generation
- group: docs
  title: ''
  type: APIReference
  url: https://docuqueue.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://docuqueue.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docuqueue.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docuqueue.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@docuqueue.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dvcoolarun
created: '2026-10-30'
description: DocuQueue is an AI‑powered document automation platform designed for the agent era. It offers a REST API and MCP integration that lets developers generate, fill, and batch PDFs, contracts, invoices, certificates, and other documents on demand. Built by Arun in India, the service provides a free tier with initial credits and scales with usage, targeting legal, sales, HR, real‑estate, and other enterprise workflows.
image: https://docuqueue.com/legal/assets/docuqueue-logo-192.png
json_schemas:
- name: BatchStatusResponse
  property_count: 8
  slug: docuqueue-com-batch-status-response
- name: ConvertResponse
  property_count: 5
  slug: docuqueue-com-convert-response
- name: FormDetailResponse
  property_count: 11
  slug: docuqueue-com-form-detail-response
- name: FormUploadResponse
  property_count: 7
  slug: docuqueue-com-form-upload-response
- name: TemplateResponse
  property_count: 13
  slug: docuqueue-com-template-response
- name: UploadResponse
  property_count: 6
  slug: docuqueue-com-upload-response
jsonld:
- class_count: 38
  name: Docuqueue Com Context
  property_count: 71
  slug: docuqueue-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docuqueue.com.
  name: docuqueue-com MCP Server
  slug: docuqueue-com-mcp-yml
modified: '2026-10-30'
name: docuqueue-com
nav: Providers
network: true
overview: 'docuqueue-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Conversion API, Document Generation API, and 7 more. Tagged areas include Company, AI, DocumentAutomation, PDF, and RESTAPI.


  The docuqueue-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  docuqueue-com''s developer surface includes authentication, changelog, engineering blog, getting-started guide, documentation, API reference, pricing, and 23 more developer resources.'
plans:
- name: Docuqueue Com Plans Pricing
  plan_count: 4
  slug: docuqueue-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Docuqueue Com Rate Limits
  slug: docuqueue-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: docuqueue-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: docuqueue-com-rules
scopes:
- name: Docuqueue Com Scopes
  scope_count: 0
  slug: docuqueue-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 53.9
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docuqueue Com Authentication
  slug: docuqueue-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Docuqueue Com Domain Security
  slug: docuqueue-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: convert-urls
  slug: convert-urls
slug: docuqueue-com
tags:
- Company
- AI
- DocumentAutomation
- PDF
- RESTAPI
- MCP
website: https://docuqueue.com/
---
