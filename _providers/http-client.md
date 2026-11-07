---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: JetBrains HTTP Client lets developers compose, edit, and execute HTTP, gRPC, WebSocket, and GraphQL requests directly within IntelliJ-based IDEs using .http and .rest files, with environment variables
  name: HTTP Client
  slug: http-client
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/http-client/plans/http-client-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/http-client-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/http-client/rate-limits/http-client-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/http-client-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/http-client/finops/http-client-finops.yml
  title: ''
  type: FinOps
  url: finops/http-client-finops.yml
- group: auth
  href: https://artifacts.apis.io/http-client/security/http-client-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/http-client-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/http-client/security/http-client-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/http-client-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JetBrains
- group: other
  title: ''
  type: Company
  url: https://www.jetbrains.com
- group: company
  title: ''
  type: Blog
  url: https://blog.jetbrains.com/idea/feed/
created: '2026-03-27'
description: HTTP Client is JetBrains' built-in tool for creating, editing, and executing HTTP requests directly from the IDE. Requests are stored in .http and .rest files alongside source code, with code highlighting, completion for hosts and methods, code folding, inline documentation, and live templates accelerating composition. The client supports HTTP/1.1 and HTTP/2 requests, gRPC unary and server-streaming calls, WebSocket connections, GraphQL operations, server-sent events, and imports from cURL and Postman collections. Environment files define reusable variables across global, request, and secured scopes; the cookie jar, request history, run/debug configurations, and Services tool window response viewer round out a workflow tightly integrated with the IntelliJ-based IDE family.
finops:
- has_sources: false
  method: generated
  name: Http Client Finops
  primary_unit: request
  service_category: API
  slug: http-client-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/http-client.png
layout: provider
modified: '2026-04-28'
name: HTTP Client
nav: Providers
network: true
overview: 'HTTP Client is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Clients, Developer Tools, HTTP Client, and IDE Extension.


  HTTP Client''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Http Client Plans Pricing
  plan_count: 3
  slug: http-client-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Http Client Rate Limits
  slug: http-client-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 14.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/http-client/http-client-2026-06-20T182910.png
security:
- kind: domain-security
  name: Http Client Domain Security
  slug: http-client-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Http Client Vulnerability Disclosure
  slug: http-client-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: http-client
tags:
- API Testing
- Clients
- Developer Tools
- HTTP Client
- IDE Extension
- IntelliJ
- JetBrains
- REST Client
website: https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html
---
