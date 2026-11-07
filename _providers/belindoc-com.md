---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://belindoc.com/api
  baseurl_source: declared
  description: 'Belin Doc API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Belin Doc API
  slug: belindoc-com-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/belindoc-com/plans/belindoc-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/belindoc-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/belindoc-com/rules/belindoc-com-rules.yml
  title: ''
  type: Spectral
  url: rules/belindoc-com-rules.yml
- group: design
  href: https://artifacts.apis.io/belindoc-com/json-ld/belindoc-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/belindoc-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/belindoc-com/vocabulary/belindoc-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/belindoc-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/belindoc-com/data-model/belindoc-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/belindoc-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/belindoc-com/authentication/belindoc-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/belindoc-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/belindoc-com/conformance/belindoc-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/belindoc-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/belindoc-com/llms/belindoc-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/belindoc-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/belindoc-com/mcp/belindoc-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/belindoc-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/belindoc-com/well-known/belindoc-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/belindoc-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/belindoc-com/hosts/belindoc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belindoc-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/belindoc-com/vendors/belindoc-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belindoc-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/belindoc-com/packages/belindoc-com-packages.yml
  title: ''
  type: SDKs
  url: packages/belindoc-com-packages.yml
- group: build
  href: https://artifacts.apis.io/belindoc-com/packages/belindoc-com-packages.yml
  title: ''
  type: Packages
  url: packages/belindoc-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://belindoc.com/changelog
- group: auth
  href: https://artifacts.apis.io/belindoc-com/security/belindoc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belindoc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belindoc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://belindoc.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://belindoc.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://belindoc.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://belindoc.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://belindoc.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://belindoc.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://belindoc.com/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://mcp.belindoc.com/api/mcp
  - status: 200
    url: https://belindoc.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Belin Doc provides a free, unlimited AI-powered document translation service that supports PDF, DOCX, EPUB, PPTX, Excel, and many other formats. Powered by top-tier AI models such as Gemini, ChatGPT, Claude, and DeepSeek, it preserves original layout and formatting while translating content into over 60 languages. The platform offers zero-cost translation with no registration, privacy-focused data handling that deletes files within 24 hours, and additional tools like OCR for scanned PDFs. Belin Doc aims to be the world’s largest free document translation tool, continuously updating models and features.
image: https://belindoc.com/lg2.png
json_schemas:
- name: PostApiExternalTranslateBatchpresigneduploadurlRequest
  property_count: 1
  slug: belindoc-com-post-api-external-translate-batchpresigneduploadurl-request
- name: PostApiExternalTranslateGettranslates3DownloadurlRequest
  property_count: 2
  slug: belindoc-com-post-api-external-translate-gettranslates3-downloadurl-request
- name: PostApiExternalTranslateGettranslates3DownloadurlResponse
  property_count: 2
  slug: belindoc-com-post-api-external-translate-gettranslates3-downloadurl-response
- name: PostApiExternalTranslateSearchtranslatefilebybatchnoResponse
  property_count: 2
  slug: belindoc-com-post-api-external-translate-searchtranslatefilebybatchno-response
- name: PutApiExternalTranslateBatchsubmittranslatetaskRequest
  property_count: 4
  slug: belindoc-com-put-api-external-translate-batchsubmittranslatetask-request
- name: PutApiExternalTranslateBatchsubmittranslatetaskResponse
  property_count: 2
  slug: belindoc-com-put-api-external-translate-batchsubmittranslatetask-response
jsonld:
- class_count: 7
  name: Belindoc Com Context
  property_count: 10
  slug: belindoc-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.belindoc.com.
  name: Belin Doc MCP Server
  slug: belindoc-com-mcp-yml
modified: '2026-11-02'
name: Belin Doc
nav: Providers
network: true
overview: 'Belin Doc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Document Translation, Free, PDF, and Multilingual.


  The Belin Doc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Belin Doc''s developer surface includes authentication, changelog, documentation, API reference, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Belindoc Com Plans Pricing
  plan_count: 2
  slug: belindoc-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Belin Doc API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: belindoc-com-rules
scopes:
- name: Belindoc Com Scopes
  scope_count: 0
  slug: belindoc-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Belindoc Com Authentication
  slug: belindoc-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Belindoc Com Domain Security
  slug: belindoc-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: belindoc-com
tags:
- Artificial Intelligence
- Document Translation
- Free
- PDF
- Multilingual
website: https://belindoc.com/
---
