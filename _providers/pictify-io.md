---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Pictify Io Agentic Access
  operation_count: 31
  slug: pictify-io-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: Batch rendering operations
  name: pictify-io Batch API
  slug: pictify-io-batch-api
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: Data binding for auto-rendering
  name: pictify-io Bindings API
  slug: pictify-io-bindings-api
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: GIF generation and capture
  name: pictify-io GIFs API
  slug: pictify-io-gifs-api
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: Image generation endpoints
  name: pictify-io Images API
  slug: pictify-io-images-api
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: PDF generation
  name: pictify-io PDFs API
  slug: pictify-io-pdfs-api
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: Template management
  name: pictify-io Templates API
  slug: pictify-io-templates-api
- baseURL: https://api.pictify.io
  baseurl_source: declared
  description: Webhook subscription management
  name: pictify-io Webhooks API
  slug: pictify-io-webhooks-api
artifact_total: 27
asyncapis:
- description: ''
  name: Pictify Io Webhooks
  slug: pictify-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/pictify-io/agentic-access/pictify-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pictify-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/pictify-io/plans/pictify-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pictify-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/rules/pictify-io-rules.yml
  title: ''
  type: Spectral
  url: rules/pictify-io-rules.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/json-ld/pictify-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pictify-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/pictify-io/vocabulary/pictify-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pictify-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pictify-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/asyncapi/pictify-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pictify-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/data-model/pictify-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pictify-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pictify-io/changelog/pictify-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pictify-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/pictify-io/authentication/pictify-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pictify-io-authentication.yml
- group: operate
  href: https://artifacts.apis.io/pictify-io/lifecycle/pictify-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/pictify-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/lifecycle/pictify-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pictify-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/errors/pictify-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pictify-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pictify-io/conformance/pictify-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pictify-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pictify-io/llms/pictify-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pictify-io-llms.txt
- group: other
  href: https://artifacts.apis.io/pictify-io/a2a/pictify-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pictify-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/pictify-io/well-known/pictify-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pictify-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/pictify-io/hosts/pictify-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pictify-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/pictify-io/vendors/pictify-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pictify-io-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pictify.io/resources/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.yoursite.com/webhooks/pictify
- group: auth
  href: https://artifacts.apis.io/pictify-io/security/pictify-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pictify-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pictify.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pictify.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pictify.io/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pictify.io/quickstart
- group: company
  title: ''
  type: Blog
  url: https://pictify.io/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://pictify.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://pictify.io/signup
- group: start
  title: ''
  type: Login
  url: https://pictify.io/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pictify.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pictify.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pictify.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pictify-io
created: '2026-10-31'
description: Pictify provides an API-first templated media platform that generates images, PDFs, GIFs, and videos from HTML templates. Users can supply data via code, spreadsheets, webhooks, or AI agents to produce personalized certificates, badges, reports, or videos. The service offers free tier access, SDKs for Node and Python, and integrations with Zapier, Make, n8n, plus an MCP server for AI agents. It supports batch rendering, per-row status tracking, and CDN-hosted outputs.
image: https://pictify.io/og/v2/home.png
json_schemas:
- name: GetTemplatesResponse
  property_count: 2
  slug: pictify-io-get-templates-response
- name: GetTemplatesUidRenderResponse
  property_count: 6
  slug: pictify-io-get-templates-uid-render-response
- name: PostGifCaptureRequest
  property_count: 5
  slug: pictify-io-post-gif-capture-request
- name: PostGifRequest
  property_count: 7
  slug: pictify-io-post-gif-request
- name: PostTemplatesRequest
  property_count: 6
  slug: pictify-io-post-templates-request
- name: PostTemplatesResponse
  property_count: 2
  slug: pictify-io-post-templates-response
jsonld:
- class_count: 18
  name: Pictify Io Context
  property_count: 81
  slug: pictify-io-context
layout: provider
modified: '2026-10-31'
name: pictify-io
nav: Providers
network: true
overview: 'pictify-io publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Bindings API, GIFs API, and 4 more. Tagged areas include Company, Media, API, Templating, and Automation.


  The pictify-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  pictify-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Pictify Io Plans Pricing
  plan_count: 5
  slug: pictify-io-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Pictify Io Rate Limits
  slug: pictify-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: pictify-io API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: pictify-io-rules
scopes:
- name: Pictify Io Scopes
  scope_count: 0
  slug: pictify-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.7
    catalog_earned_first_party: 0.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 58.1
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 71.6
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
  name: Pictify Io Authentication
  slug: pictify-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pictify Io Domain Security
  slug: pictify-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 5
skills:
- name: pictify-io-batch-render
  slug: pictify-io-batch-render
- name: pictify-io-generate-and-retrieve-image
  slug: pictify-io-generate-and-retrieve-image
- name: pictify-io-generate-pdf-with-presets
  slug: pictify-io-generate-pdf-with-presets
- name: pictify-io-manage-webhook-subscriptions
  slug: pictify-io-manage-webhook-subscriptions
- name: pictify
  slug: pictify-io-pictify
slug: pictify-io
tags:
- Company
- Media
- API
- Templating
- Automation
website: https://pictify.io/
---
