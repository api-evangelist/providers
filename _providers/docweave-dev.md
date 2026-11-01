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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Docweave PDF generation and reading API (REST) as documented.
  name: PDF Generation API
  slug: pdf-generation-api
- description: 'docweave-dev API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: docweave-dev API
  slug: docweave-dev-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/docweave-dev/rules/docweave-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/docweave-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/docweave-dev/json-ld/docweave-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docweave-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/docweave-dev/vocabulary/docweave-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docweave-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/docweave-dev/data-model/docweave-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docweave-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/docweave-dev/conventions/docweave-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/docweave-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/docweave-dev/conventions/docweave-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/docweave-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/docweave-dev/conformance/docweave-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docweave-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docweave-dev/llms/docweave-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docweave-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/docweave-dev/mcp/docweave-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/docweave-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/docweave-dev/mcp/docweave-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docweave-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/docweave-dev/hosts/docweave-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docweave-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/docweave-dev/vendors/docweave-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docweave-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/docweave-dev/packages/docweave-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/docweave-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/docweave-dev/packages/docweave-dev-packages.yml
  title: ''
  type: Packages
  url: packages/docweave-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/docweave-dev/security/docweave-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docweave-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docweave.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docweave.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docweave.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docweave.dev/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docweave.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://docweave.dev/signup
- group: company
  title: ''
  type: Blog
  url: https://docweave.dev/blog
created: '2026-10-30'
description: Docweave provides an MCP‑native PDF generation API designed for AI agents and developers. With a single REST or MCP call, users can turn HTML, a URL, or a JSON‑based template into a pixel‑perfect PDF, and also read PDFs back into clean text or markdown. The service offers transparent per‑document pricing, a free tier of 50 PDFs per month, and no credit‑card requirement. It includes features such as batch processing, merging, async rendering, watermarks, headers/footers, and Google Font support. Documentation, quick‑start guides, and SDK examples are available on the site.
image: https://docweave.dev/opengraph-image?691dde07023f6af7
json_schemas:
- name: Docweave Dev Mcp
  property_count: 0
  slug: docweave-dev-mcp
- name: PostApiV1PdfAsyncRequest
  property_count: 3
  slug: docweave-dev-post-api-v1-pdf-async-request
- name: PostApiV1PdfAsyncResponse
  property_count: 2
  slug: docweave-dev-post-api-v1-pdf-async-response
- name: PostApiV1PdfBatchRequest
  property_count: 1
  slug: docweave-dev-post-api-v1-pdf-batch-request
- name: PostApiV1PdfMergeRequest
  property_count: 2
  slug: docweave-dev-post-api-v1-pdf-merge-request
- name: PostApiV1PdfRequest
  property_count: 2
  slug: docweave-dev-post-api-v1-pdf-request
- name: PostApiV1ReadRequest
  property_count: 2
  slug: docweave-dev-post-api-v1-read-request
jsonld:
- class_count: 8
  name: Docweave Dev Context
  property_count: 9
  slug: docweave-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at docweave.dev.
  name: docweave-dev MCP Server
  slug: docweave-dev-mcp-yml
modified: '2026-10-30'
name: docweave-dev
nav: Providers
network: true
overview: 'docweave-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, Generation, API, AI, and Developers.


  The docweave-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  docweave-dev''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: docweave-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: docweave-dev-rules
scopes:
- name: Docweave Dev Scopes
  scope_count: 0
  slug: docweave-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.7
    catalog_earned_first_party: 0.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 79.1
    contract_quality: 51.4
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docweave Dev Authentication
  slug: docweave-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Docweave Dev Domain Security
  slug: docweave-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docweave-dev
tags:
- PDF
- Generation
- API
- AI
- Developers
website: https://docweave.dev/
---
