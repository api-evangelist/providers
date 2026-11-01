---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 20
  human_in_the_loop: 2
  name: Pdfs Build Agentic Access
  operation_count: 38
  slug: pdfs-build-agentic-access
  summary_line: 38 operations · 20 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Render PDFs from templates, manage templates, webhooks, embedded editor sessions and delegated agent access.
  name: pdfs.build API
  slug: pdfs-build-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Let your customers connect their own AI assistant (over MCP) to the templates under their tenant scope. Requires the Platform plan, the organization opt-in, and an API key owned by an organization own
  name: pdfs-build Delegated agents API
  slug: pdfs-build-delegated-agents-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: 'Exchange an API key for a short-lived, template-scoped session token that mounts the editor in your product with `@pdfsbuild/react`. Requires the Platform (or a custom) plan. Guide: https://pdfs.build'
  name: pdfs-build Embedded editor API
  slug: pdfs-build-embedded-editor-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Templates addressed by their generated internal id. Supported, but new integrations should use `/v2`.
  name: pdfs-build Legacy v1 API
  slug: pdfs-build-legacy-v1-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Status and download for async renders.
  name: pdfs-build Render jobs API
  slug: pdfs-build-render-jobs-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Audit trail of every render — API, app, and MCP.
  name: pdfs-build Render logs API
  slug: pdfs-build-render-logs-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Compile a published template with your data. Synchronous renders return the PDF; async renders return a job handle and notify webhooks.
  name: pdfs-build Rendering API
  slug: pdfs-build-rendering-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: 'The pdfs.build design library over the API: list the designs, preview one, and copy one into your organization in a single call. The Odoo module''s "Add designs for Odoo" button uses these.'
  name: pdfs-build Template gallery API
  slug: pdfs-build-template-gallery-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Create, inspect, publish and rename templates. Only published templates can be rendered over the API.
  name: pdfs-build Templates API
  slug: pdfs-build-templates-api
- baseURL: https://api.pdfs.build
  baseurl_source: declared
  description: Outbound endpoints notified when API renders complete or fail. Creating, rotating and testing require a paid plan; listing, updating, deleting and reading deliveries do not.
  name: pdfs-build Webhooks API
  slug: pdfs-build-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Pdfs Build Webhooks
  slug: pdfs-build-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/pdfs-build/agentic-access/pdfs-build-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfs-build-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/pdfs-build/plans/pdfs-build-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pdfs-build-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pdfs-build/rules/pdfs-build-rules.yml
  title: ''
  type: Spectral
  url: rules/pdfs-build-rules.yml
- group: design
  href: https://artifacts.apis.io/pdfs-build/json-ld/pdfs-build-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pdfs-build-context.jsonld
- group: design
  href: https://artifacts.apis.io/pdfs-build/vocabulary/pdfs-build-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pdfs-build-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pdfs-build/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pdfs-build/asyncapi/pdfs-build-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pdfs-build-webhooks.yml
- group: design
  href: https://artifacts.apis.io/pdfs-build/data-model/pdfs-build-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pdfs-build-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://pdfs.build/security/
- group: auth
  href: https://artifacts.apis.io/pdfs-build/authentication/pdfs-build-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pdfs-build-authentication.yml
- group: design
  href: https://artifacts.apis.io/pdfs-build/errors/pdfs-build-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pdfs-build-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pdfs-build/conformance/pdfs-build-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pdfs-build-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pdfs-build/llms/pdfs-build-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pdfs-build-llms.txt
- group: other
  href: https://artifacts.apis.io/pdfs-build/hosts/pdfs-build-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pdfs-build-hosts.yml
- group: other
  href: https://artifacts.apis.io/pdfs-build/vendors/pdfs-build-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pdfs-build-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://pdfs.build/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pdfs-build
- group: operate
  title: ''
  type: ChangeLog
  url: https://pdfs.build/templates/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://pdfs.build/blog/getting-started/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.pdfs.build</code
- group: docs
  title: ''
  type: APIReference
  url: https://pdfs.build/llms.txt
- group: auth
  href: https://artifacts.apis.io/pdfs-build/security/pdfs-build-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pdfs-build-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pdfs-build/security/pdfs-build-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pdfs-build-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pdfs-build/security/pdfs-build-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pdfs-build-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pdfs.build/
- group: docs
  title: ''
  type: Documentation
  url: https://pdfs.build/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://pdfs.build/pricing/
- group: company
  title: ''
  type: Blog
  url: https://pdfs.build/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pdfs.build/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pdfs.build/privacy/
created: '2026-10-30'
description: pdfs-build provides a PDF Template Engine and Rendering API that allows developers to generate PDFs from templates, data, or AI-described documents. The service offers a range of templates for invoices, price quotes, receipts, tax invoices, and more, with options for white-label integration, React SDKs, and embedded editors. It includes a free trial and tiered pricing plans, and its documentation covers API usage, pricing, alternatives, and a blog with updates.
image: https://pdfs.build/og-image.png
jsonld:
- class_count: 42
  name: Pdfs Build Context
  property_count: 89
  slug: pdfs-build-context
layout: provider
modified: '2026-10-30'
name: pdfs-build
nav: Providers
network: true
overview: 'pdfs-build publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Delegated agents API, Embedded editor API, Legacy v1 API, and 7 more. Tagged areas include PDF, API, TemplateEngine, Rendering, and SaaS.


  The pdfs-build catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  pdfs-build''s developer surface includes authentication, changelog, getting-started guide, API reference, documentation, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Pdfs Build Plans Pricing
  plan_count: 4
  slug: pdfs-build-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: pdfs-build API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: pdfs-build-rules
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 79.5
    catalog_earned_first_party: 0.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 75.8
    contract_governance: 79.1
    contract_quality: 64.6
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 39.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pdfs Build Authentication
  slug: pdfs-build-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pdfs Build Domain Security
  slug: pdfs-build-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pdfs Build Vulnerability Disclosure
  slug: pdfs-build-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Pdfs Build Trust Center
  slug: pdfs-build-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: pdfs-build-main
  slug: pdfs-build-main
slug: pdfs-build
tags:
- PDF
- API
- TemplateEngine
- Rendering
- SaaS
- DocumentGeneration
website: https://pdfs.build/
---
