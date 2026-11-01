---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Snaplab Dev Agentic Access
  operation_count: 21
  slug: snaplab-dev-agentic-access
  summary_line: 21 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://snaplab.dev
  baseurl_source: declared
  description: API keys, plan and usage.
  name: snaplab-dev Account API
  slug: snaplab-dev-account-api
- baseURL: https://snaplab.dev
  baseurl_source: declared
  description: Stripe checkout, portal and webhook.
  name: snaplab-dev Billing API
  slug: snaplab-dev-billing-api
- baseURL: https://snaplab.dev
  baseurl_source: declared
  description: Stored renders, served from public `/i/c/{id}` URLs.
  name: snaplab-dev Captures API
  slug: snaplab-dev-captures-api
- baseURL: https://snaplab.dev
  baseurl_source: declared
  description: Key-less public endpoints behind the free tool pages.
  name: snaplab-dev Free tools API
  slug: snaplab-dev-free-tools-api
- baseURL: https://snaplab.dev
  baseurl_source: declared
  description: Turn URLs and HTML into images and PDFs.
  name: snaplab-dev Rendering API
  slug: snaplab-dev-rendering-api
- baseURL: https://snaplab.dev
  baseurl_source: declared
  description: Unauthenticated service health.
  name: snaplab-dev System API
  slug: snaplab-dev-system-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/snaplab-dev/agentic-access/snaplab-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snaplab-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/snaplab-dev/rules/snaplab-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/snaplab-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/snaplab-dev/json-ld/snaplab-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snaplab-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/snaplab-dev/vocabulary/snaplab-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snaplab-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/snaplab-dev/data-model/snaplab-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snaplab-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/snaplab-dev/errors/snaplab-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snaplab-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snaplab-dev/conformance/snaplab-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snaplab-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/snaplab-dev/llms/snaplab-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snaplab-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/snaplab-dev/hosts/snaplab-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snaplab-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/snaplab-dev/vendors/snaplab-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snaplab-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/snaplab-dev/packages/snaplab-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/snaplab-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/snaplab-dev/packages/snaplab-dev-packages.yml
  title: ''
  type: Packages
  url: packages/snaplab-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/snaplab-dev/authentication/snaplab-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snaplab-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/snaplab-dev/security/snaplab-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snaplab-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snaplab.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://snaplab.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://snaplab.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://snaplab.dev/docs#quickstart
- group: company
  title: ''
  type: Blog
  url: https://snaplab.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snaplab.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snaplab.dev/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://snaplab.dev/openapi.json
  - status: 401
    url: https://snaplab.dev/mcp
  - status: 200
    url: https://snaplab.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Snaplab provides a screenshot, PDF, and Open Graph image generation API. It renders web pages via real Chromium, offering options like full‑page capture, ad blocking, dark mode, mobile emulation, and signed URLs. The service includes free tools, rate‑limited free tier, and paid plans for higher volume, targeting developers needing visual QA, social previews, invoices, and archived page snapshots.
image: https://snaplab.dev/og.png
json_schemas:
- name: ApiKey
  property_count: 6
  slug: snaplab-dev-api-key
- name: CaptureRequest
  property_count: 2
  slug: snaplab-dev-capture-request
- name: Capture
  property_count: 22
  slug: snaplab-dev-capture
- name: HostedRender
  property_count: 8
  slug: snaplab-dev-hosted-render
- name: ImageOptions
  property_count: 14
  slug: snaplab-dev-image-options
- name: RenderOptions
  property_count: 32
  slug: snaplab-dev-render-options
jsonld:
- class_count: 10
  name: Snaplab Dev Context
  property_count: 64
  slug: snaplab-dev-context
layout: provider
modified: '2026-10-31'
name: snaplab-dev
nav: Providers
network: true
overview: 'snaplab-dev publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Captures API, and 3 more. Tagged areas include Company, Screenshot, PDF, OpenGraph, and API.


  The snaplab-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  snaplab-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: snaplab-dev API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: snaplab-dev-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 58.9
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 0.0
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
  name: Snaplab Dev Authentication
  slug: snaplab-dev-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Snaplab Dev Domain Security
  slug: snaplab-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: snaplab-dev
tags:
- Company
- Screenshot
- PDF
- OpenGraph
- API
website: https://snaplab.dev/
---
