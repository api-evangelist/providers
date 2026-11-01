---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 78.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Blinkpdf Io Agentic Access
  operation_count: 32
  slug: blinkpdf-io-agentic-access
  summary_line: 32 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: The authenticated caller account and billing tier
  name: blinkpdf-io Account API
  slug: blinkpdf-io-account-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Canvas sheets and paginated stream sections composed into a PDF
  name: blinkpdf-io Compose API
  slug: blinkpdf-io-compose-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Machine-readable API entry point
  name: blinkpdf-io Discovery API
  slug: blinkpdf-io-discovery-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: The Docs API from blinkpdf-io — 1 operation(s) for docs.
  name: blinkpdf-io Docs API
  slug: blinkpdf-io-docs-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Fill an AcroForm by name
  name: blinkpdf-io Fill API
  slug: blinkpdf-io-fill-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Hosted font catalog and Google Fonts capability discovery
  name: blinkpdf-io Fonts API
  slug: blinkpdf-io-fonts-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Liveness and readiness probes
  name: blinkpdf-io Health API
  slug: blinkpdf-io-health-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Layout documents — a Markdown body confined to one writing rect on every page, with caller-positioned text, images, and calibration frames, an optional full-sheet background, and a printer calibration
  name: blinkpdf-io Layout Document API
  slug: blinkpdf-io-layoutdocument-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Merge, split, reorder, and rotate the pages of existing PDFs
  name: blinkpdf-io Pages API
  slug: blinkpdf-io-pages-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: 'Read a native PDF: its text in reading order as Markdown and with the box of every line, its headings, lists, and tables, and the values of its form fields'
  name: blinkpdf-io Read API
  slug: blinkpdf-io-read-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Markdown-to-PDF rendering
  name: blinkpdf-io Render API
  slug: blinkpdf-io-render-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Sandwich documents — a first-page header (logo, professional identity, subject/context data) and a last-page footer (signature, name) wrapping a Markdown body
  name: blinkpdf-io Sandwich Document API
  slug: blinkpdf-io-sandwichdocument-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Stamp text, images, and codes onto the pages of an existing PDF, over or under its content
  name: blinkpdf-io Stamp API
  slug: blinkpdf-io-stamp-api
- baseURL: https://api.blinkpdf.io
  baseurl_source: declared
  description: Stored AcroForm template library
  name: blinkpdf-io Templates API
  slug: blinkpdf-io-templates-api
artifact_total: 31
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blinkpdf.io/
- group: agent
  href: https://artifacts.apis.io/blinkpdf-io/agentic-access/blinkpdf-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blinkpdf-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/blinkpdf-io/rate-limits/blinkpdf-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blinkpdf-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/blinkpdf-io/plans/blinkpdf-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blinkpdf-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/rules/blinkpdf-io-rules.yml
  title: ''
  type: Spectral
  url: rules/blinkpdf-io-rules.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/json-ld/blinkpdf-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blinkpdf-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/vocabulary/blinkpdf-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blinkpdf-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blinkpdf-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/data-model/blinkpdf-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blinkpdf-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/conventions/blinkpdf-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blinkpdf-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/conventions/blinkpdf-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blinkpdf-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/blinkpdf-io/authentication/blinkpdf-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blinkpdf-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/errors/blinkpdf-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blinkpdf-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blinkpdf-io/conformance/blinkpdf-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blinkpdf-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blinkpdf-io/llms/blinkpdf-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blinkpdf-io-llms.txt
- group: other
  href: https://artifacts.apis.io/blinkpdf-io/a2a/blinkpdf-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blinkpdf-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/blinkpdf-io/well-known/blinkpdf-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blinkpdf-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/blinkpdf-io/hosts/blinkpdf-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blinkpdf-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/blinkpdf-io/vendors/blinkpdf-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blinkpdf-io-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blinkpdf.io/quickstart
- group: auth
  href: https://artifacts.apis.io/blinkpdf-io/security/blinkpdf-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blinkpdf-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkpdf.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.blinkpdf.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://blinkpdf.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blinkpdf.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blinkpdf.io/terms-of-service/
created: '2026-10-30'
description: BlinkPDF.io provides a simple API to convert, merge, split, and manipulate PDF documents programmatically. Developers can integrate PDF processing into web, mobile, or desktop applications without needing heavy client-side libraries. Features include PDF to image conversion, OCR support, watermarking, encryption, and batch processing, all accessible via RESTful endpoints with JSON responses. The service emphasizes security, scalability, and ease of use, offering tiered pricing and comprehensive documentation for quick onboarding.
image: https://blinkpdf.io/images/og-card.png
json_schemas:
- name: AcroForm.Definition
  property_count: 2
  slug: blinkpdf-io-acro-form-definition
- name: AcroForm.Inspection
  property_count: 5
  slug: blinkpdf-io-acro-form-inspection
- name: Compose.ValidateOk
  property_count: 3
  slug: blinkpdf-io-compose-validate-ok
- name: Render.ValidateOk
  property_count: 3
  slug: blinkpdf-io-render-validate-ok
- name: Template.layout-document.Body
  property_count: 12
  slug: blinkpdf-io-template-layout-document-body
- name: Template.sandwich-document.Body
  property_count: 10
  slug: blinkpdf-io-template-sandwich-document-body
jsonld:
- class_count: 120
  name: Blinkpdf Io Context
  property_count: 26
  slug: blinkpdf-io-context
layout: provider
modified: '2026-10-30'
name: blinkpdf-io
nav: Providers
network: true
overview: 'blinkpdf-io publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Compose API, Discovery API, and 11 more. Tagged areas include PDF, DocumentProcessing, API, SaaS, and Automation.


  The blinkpdf-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  blinkpdf-io''s developer surface includes documentation, authentication, getting-started guide, API reference, pricing, and 21 more developer resources.'
plans:
- name: Blinkpdf Io Plans Pricing
  plan_count: 4
  slug: blinkpdf-io-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Blinkpdf Io Rate Limits
  slug: blinkpdf-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: blinkpdf-io API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: blinkpdf-io-rules
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 64.6
    developer_ergonomics: 46.9
    discoverability: 66.1
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blinkpdf Io Authentication
  slug: blinkpdf-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blinkpdf Io Domain Security
  slug: blinkpdf-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: blinkpdf-io-compose-pdf
  slug: blinkpdf-io-compose-pdf
- name: blinkpdf-io-fill-form
  slug: blinkpdf-io-fill-form
- name: blinkpdf-io-layout-document-render
  slug: blinkpdf-io-layout-document-render
- name: blinkpdf-io-sandwich-document-render-and-validate
  slug: blinkpdf-io-sandwich-document-render-and-validate
slug: blinkpdf-io
tags:
- PDF
- DocumentProcessing
- API
- SaaS
- Automation
website: https://blinkpdf.io/
---
