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
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Sudomock Com Agentic Access
  operation_count: 53
  slug: sudomock-com-agentic-access
  summary_line: 53 operations · 30 acting
api_count: 1
apis:
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Read the current account, its plan and its remaining credits.
  name: sudomock-com Account API
  slug: sudomock-com-account-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Isolate a subject from its background as a standalone step.
  name: sudomock-com Background removal API
  slug: sudomock-com-background-removal-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Upload and manage the fonts available to text layers.
  name: sudomock-com Fonts API
  slug: sudomock-com-fonts-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Poll queued renders and read their results.
  name: sudomock-com Jobs API
  slug: sudomock-com-jobs-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Turn a product photo into a reusable mockup, then render artwork onto it.
  name: sudomock-com Photo mockups API
  slug: sudomock-com-photo-mockups-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Turn a Photoshop file into a reusable mockup, then render it.
  name: sudomock-com PSD mockups API
  slug: sudomock-com-psd-mockups-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Open an embedded editor session and read what the customer produced in it.
  name: sudomock-com Studio API
  slug: sudomock-com-studio-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Render a mockup as a short video.
  name: sudomock-com Video mockups API
  slug: sudomock-com-video-mockups-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Inspect, replay and retry what those endpoints received.
  name: sudomock-com Webhook deliveries API
  slug: sudomock-com-webhook-deliveries-api
- baseURL: https://api.sudomock.com
  baseurl_source: declared
  description: Register signed endpoints and manage their secrets.
  name: sudomock-com Webhook endpoints API
  slug: sudomock-com-webhook-endpoints-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/sudomock-com/agentic-access/sudomock-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sudomock-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/sudomock-com/rate-limits/sudomock-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sudomock-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sudomock-com/rules/sudomock-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sudomock-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sudomock-com/json-ld/sudomock-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sudomock-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sudomock-com/vocabulary/sudomock-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sudomock-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sudomock-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sudomock-com/data-model/sudomock-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sudomock-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/sudomock-com/conventions/sudomock-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sudomock-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/sudomock-com/conventions/sudomock-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sudomock-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sudomock-com/authentication/sudomock-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sudomock-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/sudomock-com/conformance/sudomock-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sudomock-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sudomock-com/llms/sudomock-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sudomock-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/sudomock-com/well-known/sudomock-com-sudomock-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sudomock-com-sudomock-security.txt
- group: auth
  href: https://artifacts.apis.io/sudomock-com/well-known/sudomock-com-n8n-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sudomock-com-n8n-security.txt
- group: agent
  href: https://artifacts.apis.io/sudomock-com/well-known/sudomock-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sudomock-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sudomock-com/hosts/sudomock-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sudomock-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sudomock-com/vendors/sudomock-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sudomock-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/sudomock-com/packages/sudomock-com-packages.yml
  title: ''
  type: SDKs
  url: packages/sudomock-com-packages.yml
- group: build
  href: https://artifacts.apis.io/sudomock-com/packages/sudomock-com-packages.yml
  title: ''
  type: Packages
  url: packages/sudomock-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sudomock.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://sudomock.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sudomock.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://sudomock.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://sudomock.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://sudomock.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://sudomock.com/docs/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sudomock.com</span
- group: docs
  title: ''
  type: APIReference
  url: https://sudomock.com/docs/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/sudomock-com/security/sudomock-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sudomock-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sudomock.com/
created: '2026-10-31'
description: SudoMock provides a RESTful mockup rendering API that transforms PSD templates and product photos into realistic product images. Developers can integrate the service via simple HTTP calls or official SDKs for Node and Python. The platform supports bulk mockup generation, async rendering, webhooks, and no‑code integrations with Shopify, WooCommerce, and other e‑commerce platforms. With a free tier of 500 credits and paid plans for higher volume, SudoMock enables automated product photography for print‑on‑demand businesses, designers, and developers.
image: https://sudomock.com/og-image.png
json_schemas:
- name: CreateSessionRequest
  property_count: 9
  slug: sudomock-com-create-session-request
- name: FontResponse
  property_count: 11
  slug: sudomock-com-font-response
- name: JobStatusResponse
  property_count: 13
  slug: sudomock-com-job-status-response
- name: RenderRequest
  property_count: 8
  slug: sudomock-com-render-request
- name: VideoRenderRequest
  property_count: 6
  slug: sudomock-com-video-render-request
- name: WebhookDeliveryDetailResponse
  property_count: 14
  slug: sudomock-com-webhook-delivery-detail-response
jsonld:
- class_count: 120
  name: Sudomock Com Context
  property_count: 257
  slug: sudomock-com-context
layout: provider
modified: '2026-10-31'
name: sudomock-com
nav: Providers
network: true
overview: 'sudomock-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Background removal API, Fonts API, and 7 more. Tagged areas include Mockup, API, PSD, E-commerce, and Automation.


  The sudomock-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sudomock-com''s developer surface includes authentication, changelog, engineering blog, getting-started guide, API reference, and 25 more developer resources.'
plans:
- name: Sudomock Com Plans Pricing
  plan_count: 0
  slug: sudomock-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Sudomock Com Rate Limits
  slug: sudomock-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: sudomock-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: sudomock-com-rules
scopes:
- name: Sudomock Com Scopes
  scope_count: 0
  slug: sudomock-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 58.8
    developer_ergonomics: 66.0
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
  name: Sudomock Com Authentication
  slug: sudomock-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sudomock Com Domain Security
  slug: sudomock-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: upload-render
  slug: sudomock-com-upload-render
slug: sudomock-com
tags:
- Mockup
- API
- PSD
- E-commerce
- Automation
website: https://sudomock.com/
---
