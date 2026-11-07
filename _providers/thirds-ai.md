---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted MCP server exposing thirds.ai tools (create_brand_kit, create_template, edit_template, publish_template, render, create_batch, get_status, and more) over Streamable HTTP with bearer-token auth.
  name: thirds.ai MCP Server
  slug: thirdsai-mcp-server
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Batches API from thirds.ai — 5 operation(s) for batches.
  name: thirds.ai Batches API
  slug: thirds-ai-batches-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Brand Kits API from thirds.ai — 4 operation(s) for brand kits.
  name: thirds.ai Brand Kits API
  slug: thirds-ai-brand-kits-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Carousels API from thirds.ai — 4 operation(s) for carousels.
  name: thirds.ai Carousels API
  slug: thirds-ai-carousels-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Downloads API from thirds.ai — 1 operation(s) for downloads.
  name: thirds.ai Downloads API
  slug: thirds-ai-downloads-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Image API from thirds.ai — 2 operation(s) for image.
  name: thirds.ai Image API
  slug: thirds-ai-image-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Image Assets API from thirds.ai — 3 operation(s) for image assets.
  name: thirds.ai Image Assets API
  slug: thirds-ai-image-assets-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Image Packs API from thirds.ai — 4 operation(s) for image packs.
  name: thirds.ai Image Packs API
  slug: thirds-ai-image-packs-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Keys API from thirds.ai — 2 operation(s) for keys.
  name: thirds.ai Keys API
  slug: thirds-ai-keys-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Me API from thirds.ai — 1 operation(s) for me.
  name: thirds.ai Me API
  slug: thirds-ai-me-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Openapi.json API from thirds.ai — 1 operation(s) for openapi.json.
  name: thirds.ai Openapi.json API
  slug: thirds-ai-openapi-json-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Pdf API from thirds.ai — 2 operation(s) for pdf.
  name: thirds.ai PDF API
  slug: thirds-ai-pdf-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Public Stats API from thirds.ai — 1 operation(s) for public stats.
  name: thirds.ai Public Stats API
  slug: thirds-ai-public-stats-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Template Builds API from thirds.ai — 7 operation(s) for template builds.
  name: thirds.ai Template Builds API
  slug: thirds-ai-template-builds-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Templates API from thirds.ai — 6 operation(s) for templates.
  name: thirds.ai Templates API
  slug: thirds-ai-templates-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Testimonials API from thirds.ai — 1 operation(s) for testimonials.
  name: thirds.ai Testimonials API
  slug: thirds-ai-testimonials-api
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: The Webhooks API from thirds.ai — 8 operation(s) for webhooks.
  name: thirds.ai Webhooks API
  slug: thirds-ai-webhooks-api
artifact_total: 31
asyncapis:
- description: ''
  name: Thirds Ai Webhooks
  slug: thirds-ai-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://thirds.ai/blog/feed.xml
- group: other
  href: https://artifacts.apis.io/thirds-ai/capabilities/thirds-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thirds-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/thirds-ai/overlays/thirds-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thirds-ai-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/thirds-ai/security/thirds-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thirds-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/thirds-ai/authentication/thirds-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thirds-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://thirds.ai
- group: docs
  title: ''
  type: Documentation
  url: https://thirds.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://thirds.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://thirds.ai/support
- group: company
  title: ''
  type: Blog
  url: https://thirds.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thirds.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thirds.ai/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://thirds.ai/changelog
- group: agent
  href: https://artifacts.apis.io/thirds-ai/llms/thirds-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thirds-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/thirds-ai/conventions/thirds-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thirds-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/thirds-ai/conventions/thirds-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/thirds-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/thirds-ai/conformance/thirds-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thirds-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/thirds-ai/lifecycle/thirds-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thirds-ai-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/thirds-ai/plans/thirds-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thirds-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/thirds-ai/rate-limits/thirds-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thirds-ai-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/thirds-ai/sandbox/thirds-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thirds-ai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/thirds-ai/errors/thirds-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thirds-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thirds-ai/data-model/thirds-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thirds-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/thirds-ai/asyncapi/thirds-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thirds-ai-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/thirds-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/thirds-ai/security/thirds-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thirds-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thirds-ai/security/thirds-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thirds-ai-vulnerability-disclosure.yml
created: '2026-09-18'
description: Turn one design into content at scale. thirds.ai makes editable templates from a text prompt, HTML, a picture, or gallery and renders PDFs and images via a web app, REST API, or hosted MCP server. Outputs are PDF, PNG, JPEG, and WebP.
finops:
- has_sources: true
  method: derived
  name: Thirds Ai Finops
  primary_unit: credit
  service_category: ''
  slug: thirds-ai-finops
  template: false
layout: provider
mcp_servers:
- description: Official hosted MCP server exposing thirds.ai PDF/image rendering, template, brand-kit and batch tools over Streamable HTTP with bearer-token auth. Uses the caller's existing account, credits and temp
  name: thirds.ai MCP Server
  slug: thirds-ai-mcp-server
modified: '2026-10-06'
name: thirds.ai
nav: Providers
network: true
overview: 'thirds.ai publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batches API, Brand Kits API, Carousels API, and 14 more. Tagged areas include pdf-automation, image-automation, Document Generation, HTML to PDF, and HTML to Image.


  The thirds.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  thirds.ai''s developer surface includes authentication, documentation, pricing, support, engineering blog, changelog, sandbox, and 20 more developer resources.'
plans:
- name: Thirds Ai Plans Pricing
  plan_count: 9
  slug: thirds-ai-plans-pricing
- name: Thirds Ai Price Estimates
  plan_count: 0
  slug: thirds-ai-price-estimates
random_paper: 13
rate_limits:
- limit_count: 5
  name: Thirds Ai Rate Limits
  slug: thirds-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: thirds.ai API Rules
  rule_count: 59
  severity_counts:
    error: 41
    hint: 0
    info: 8
    warn: 10
  slug: thirds-ai-rules
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.5
    catalog_earned_first_party: 24.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 56.5
    discoverability: 71.7
    operational_transparency: 65.8
  previous_composite: 59.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thirds-ai/thirds-ai-2026-10-11T130858.png
security:
- kind: authentication
  name: Thirds Ai Authentication
  slug: thirds-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Thirds Ai Domain Security
  slug: thirds-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thirds Ai Vulnerability Disclosure
  slug: thirds-ai-vulnerability-disclosure
  summary_line: contact published
skill_count: 4
skills:
- name: thirds-ai-ai-template-build
  slug: thirds-ai-ai-template-build
- name: thirds-ai-csv-batch
  slug: thirds-ai-csv-batch
- name: thirds-ai-html-to-pdf
  slug: thirds-ai-html-to-pdf
- name: thirds-ai-template-with-data
  slug: thirds-ai-template-with-data
slug: thirds-ai
tags:
- pdf-automation
- image-automation
- Document Generation
- HTML to PDF
- HTML to Image
- template-rendering
- Branded Content
- Developer Tools
- MCP Server
- Agent-Native
- marketing-ops
website: https://thirds.ai
---
