---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://tvbeat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tvbeat.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tvbeat
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tvbeat-legal.snazzydocs.com/1.0/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tvbeat-legal.snazzydocs.com/1.0/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tvbeat-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/tvbeat/public/blob/master/docs/api.md
- group: company
  title: ''
  type: Blog
  url: https://blog.tvbeat.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.tvbeat.com/rss
- group: operate
  title: ''
  type: Support
  url: mailto:support@tvbeat.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/tvbeat-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tvbeat-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tvbeat-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tvbeat-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tvbeat-data-model.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tvbeat-json-schema.yml
- group: build
  title: ''
  type: Examples
  url: examples/tvbeat-examples.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tvbeat-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tvbeat-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tvbeat-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tvbeat-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tvbeat-llms.txt
created: '2026-07-17'
description: TVbeat is a London-based, Techstars-backed advertising technology company whose platform unifies linear television and streaming (CTV) advertising operations into a single system. It lets media owners and buyers forecast, plan, transact, optimize, and measure campaigns across audiences, yield, and operations, supporting multi-currency transacting (ratings, spots, impressions, and outcomes) and modern buying models — Direct, Programmatic, Self-Serve, and AI-driven — across both traditional linear spots and streaming inventory. TVbeat publishes a complete first-party API reference for its analytics API — three query endpoints signed with a custom TVBEAT-HMAC-SHA256 scheme, with two draft-04 JSON Schemas and example responses — in its own GitHub organization at github.com/tvbeat/public, but the API root it names (api.tvbeat.com) no longer resolves in public DNS and the document has not been modified since 2017. TVbeat ships no OpenAPI, SDK, CLI, MCP server or agent card, and its
  current documentation portal at docs.tvbeat.com is credential-gated.
examples:
- key_count: 2
  name: Tvbeat Breakdown Response Example
  slug: tvbeat-breakdown-response-example
- key_count: 3
  name: Tvbeat Dimensions Response Example
  slug: tvbeat-dimensions-response-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tvbeat.png
json_schemas:
- name: DataTypes.Query
  property_count: 5
  slug: tvbeat-breakdown-query
- name: DataTypes.Query
  property_count: 5
  slug: tvbeat-dimensions-search-query
layout: provider
modified: '2026-08-12'
name: TVbeat
nav: Providers
network: true
overview: 'TVbeat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Television, and Streaming.


  TVbeat''s developer surface includes documentation, API reference, engineering blog, support, authentication, code examples, changelog, and 15 more developer resources.'
plans:
- name: Tvbeat Plans Pricing
  plan_count: 0
  slug: tvbeat-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Tvbeat Rate Limits
  slug: tvbeat-rate-limits
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 17.6
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tvbeat Authentication
  slug: tvbeat-authentication
  summary_line: custom-hmac-signature · 1 scheme
- kind: domain-security
  name: Tvbeat Domain Security
  slug: tvbeat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tvbeat
tags:
- Company
- Advertising
- AdTech
- Television
- Streaming
- CTV
- Audience Measurement
- Analytics
- Media
website: https://tvbeat.com/
---
