---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Html2Img Com Agentic Access
  operation_count: 1
  slug: html2img-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Convert HTML, CSS or URLs to PNG or PDF via a REST API.
  name: HTML to Image API
  slug: html-to-image-api
- baseURL: https://app.html2img.com/api
  baseurl_source: declared
  description: Convert HTML, CSS or any public URL into a PNG image or a vector PDF, rendered in real headless Chrome. JSON in, a CDN URL out.
  name: HTML to Image API API
  slug: html-to-image-api-api
artifact_total: 18
asyncapis:
- description: ''
  name: Html2Img Com Webhooks
  slug: html2img-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/html2img-com/rules/html2img-com-rules.yml
  title: ''
  type: Spectral
  url: rules/html2img-com-rules.yml
- group: design
  href: https://artifacts.apis.io/html2img-com/json-ld/html2img-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/html2img-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/html2img-com/vocabulary/html2img-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/html2img-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/html2img-com/asyncapi/html2img-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/html2img-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/html2img-com/conformance/html2img-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/html2img-com-conformance.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://html2img.com/docs/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://html2img.com/llms.txt
- group: commercial
  href: https://artifacts.apis.io/html2img-com/plans/html2img-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/html2img-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/html2img-com/data-model/html2img-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/html2img-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/html2img-com/authentication/html2img-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/html2img-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/html2img-com/errors/html2img-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/html2img-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/html2img-com/llms/html2img-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/html2img-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/html2img-com/well-known/html2img-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/html2img-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/html2img-com/hosts/html2img-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/html2img-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/html2img-com/vendors/html2img-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/html2img-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/html2img-com/packages/html2img-com-packages.yml
  title: ''
  type: SDKs
  url: packages/html2img-com-packages.yml
- group: build
  href: https://artifacts.apis.io/html2img-com/packages/html2img-com-packages.yml
  title: ''
  type: Packages
  url: packages/html2img-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://html2img.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://html2img.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.html2img.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/html2img/
- group: auth
  href: https://artifacts.apis.io/html2img-com/security/html2img-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/html2img-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://html2img.com/
- group: docs
  title: ''
  type: Documentation
  url: https://html2img.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://html2img.com/pricing/
created: '2026-10-30'
description: HTML to Image provides a REST API that converts HTML, CSS, or any public URL into PNG images or PDF documents using real headless Chrome. It offers a free tier with 50 renders, multiple language guides, and named templates for invoices, social cards, and more, targeting developers needing on‑demand screenshot or PDF generation.
image: https://html2img.com/og/home.png
json_schemas:
- name: Account
  property_count: 7
  slug: html2img-com-account
- name: Health
  property_count: 2
  slug: html2img-com-health
- name: HtmlRequest
  property_count: 11
  slug: html2img-com-html-request
- name: ScreenshotRequest
  property_count: 12
  slug: html2img-com-screenshot-request
- name: TemplateRequest
  property_count: 2
  slug: html2img-com-template-request
jsonld:
- class_count: 8
  name: Html2Img Com Context
  property_count: 30
  slug: html2img-com-context
layout: provider
modified: '2026-10-30'
name: html2img-com
nav: Providers
network: true
overview: 'html2img-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including HTML to Image API API, and 1 more. Tagged areas include Company, API, Screenshot, PDF, and Rendering.


  The html2img-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  html2img-com''s developer surface includes getting-started guide, API reference, authentication, documentation, pricing, and 20 more developer resources.'
plans:
- name: Html2Img Com Plans Pricing
  plan_count: 7
  slug: html2img-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: html2img-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: html2img-com-rules
scopes:
- name: Html2Img Com Scopes
  scope_count: 0
  slug: html2img-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Html2Img Com Authentication
  slug: html2img-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Html2Img Com Domain Security
  slug: html2img-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: render-html
  slug: html2img-com-render-html
- name: render-template
  slug: html2img-com-render-template
- name: screenshot-url
  slug: html2img-com-screenshot-url
slug: html2img-com
tags:
- Company
- API
- Screenshot
- PDF
- Rendering
- HeadlessChrome
website: https://html2img.com/
---
