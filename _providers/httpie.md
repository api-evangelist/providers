---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Httpie Agentic Access
  operation_count: 2
  slug: httpie-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://httpie.io
  baseurl_source: spec
  description: The App API from HTTPie — 1 operation(s) for app.
  name: HTTPie App API
  slug: httpie-app-api
- baseURL: https://httpie.io
  baseurl_source: spec
  description: The Hello API from HTTPie — 1 operation(s) for hello.
  name: HTTPie Hello API
  slug: httpie-hello-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HTTPie App API
  slug: open-httpie-app-api
- collection_type: open
  name: HTTPie App Hello API
  slug: open-httpie-hello-api
- collection_type: open
  name: HTTPie API
  slug: open-httpie-httpie
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/httpie-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/httpie-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/httpie
- group: company
  title: ''
  type: Website
  url: https://httpie.io/
- group: docs
  title: ''
  type: Documentation
  url: https://httpie.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/httpie
- group: start
  title: ''
  type: Signup
  url: https://httpie.io/app
- group: company
  title: ''
  type: Blog
  url: https://httpie.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://httpie.io/pricing
created: '2025-01-08'
description: HTTPie is a user-friendly command-line and web-based HTTP client designed for testing, debugging, and interacting with APIs and HTTP services. It provides expressive syntax that mirrors actual HTTP requests, formatted and syntax-highlighted output, native JSON support, file uploads, form submissions, persistent sessions, multiple authentication schemes (basic, digest, bearer, .netrc, and an extensible plugin system covering OAuth, AWS, NTLM, and more), download mode similar to wget, HTTPS and proxy support, and cross-platform installation across Linux, macOS, Windows, and FreeBSD. The companion HTTPie web app and Desktop client layer a graphical interface over the same request and response model that the CLI exposes.
finops:
- name: Httpie Finops
  service_category: API
  slug: httpie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/httpie.png
json_schemas:
- name: HTTPie Request
  property_count: 8
  slug: request
- name: HTTPie Response
  property_count: 8
  slug: response
- name: HTTPie Session
  property_count: 6
  slug: session
jsonld:
- class_count: 22
  name: Httpie Context
  property_count: 0
  slug: httpie-context
layout: provider
modified: '2026-05-19'
name: HTTPie
nav: Providers
network: true
overview: 'HTTPie publishes 2 APIs on the [APIs.io](https://apis.io/) network: App API and Hello API. Tagged areas include API Client, API Testing, CLI, Clients, and Command Line.


  The HTTPie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HTTPie''s developer surface includes documentation, signup flow, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Httpie Plans Pricing
  plan_count: 3
  slug: httpie-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Httpie Rate Limits
  slug: httpie-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: HTTPie API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: httpie-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/httpie/refs/heads/main/screenshots/httpie-2026-06-20T182915.png
security:
- kind: domain-security
  name: Httpie Domain Security
  slug: httpie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: httpie
tags:
- API Client
- API Testing
- CLI
- Clients
- Command Line
- Developer Tools
- HTTP
- Open-Source
- Sessions
website: https://httpie.io/
---
