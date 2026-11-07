---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Beeceptor Agentic Access
  operation_count: 29
  slug: beeceptor-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 1
apis:
- description: Beeceptor's management API provides programmatic access to create and manage mock endpoints, rules, and traffic inspection on Scale and Enterprise plans. It enables teams to automate mock server provi
  name: Beeceptor API
  slug: beeceptor
- baseURL: https://api.beeceptor.com/api
  baseurl_source: spec
  description: The Endpoint Settings API from Beeceptor — 5 operation(s) for endpoint settings.
  name: Beeceptor Endpoint Settings API
  slug: beeceptor-endpoint-settings-api
- baseURL: https://api.beeceptor.com/api
  baseurl_source: spec
  description: The Mock Rules API from Beeceptor — 4 operation(s) for mock rules.
  name: Beeceptor Mock Rules API
  slug: beeceptor-mock-rules-api
- baseURL: https://api.beeceptor.com/api
  baseurl_source: spec
  description: The Request History API from Beeceptor — 3 operation(s) for request history.
  name: Beeceptor Request History API
  slug: beeceptor-request-history-api
- baseURL: https://api.beeceptor.com/api
  baseurl_source: spec
  description: The State Store API from Beeceptor — 2 operation(s) for state store.
  name: Beeceptor State Store API
  slug: beeceptor-state-store-api
artifact_total: 32
collections:
- collection_type: open
  name: Beeceptor Endpoint Settings API
  slug: open-beeceptor-endpoint-settings-api
- collection_type: open
  name: Beeceptor Endpoint Settings Mock Rules API
  slug: open-beeceptor-mock-rules-api
- collection_type: open
  name: Beeceptor Endpoint Settings Request History API
  slug: open-beeceptor-request-history-api
- collection_type: open
  name: Beeceptor Endpoint Settings State Store API
  slug: open-beeceptor-state-store-api
- collection_type: open
  name: Beeceptor API
  slug: open-beeceptor
common:
- group: operate
  href: https://artifacts.apis.io/beeceptor/rate-limits/beeceptor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/beeceptor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/beeceptor/finops/beeceptor-finops.yml
  title: ''
  type: FinOps
  url: finops/beeceptor-finops.yml
- group: agent
  href: https://artifacts.apis.io/beeceptor/agentic-access/beeceptor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beeceptor-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/beeceptor/security/beeceptor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beeceptor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/beeceptor/authentication/beeceptor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beeceptor-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beeceptor
- group: company
  title: ''
  type: Website
  url: https://beeceptor.com
- group: start
  title: ''
  type: Portal
  url: https://app.beeceptor.com
- group: commercial
  title: ''
  type: Pricing
  url: https://beeceptor.com/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://beeceptor.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://beeceptor.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://beeceptorstatus.statuspage.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beeceptor.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beeceptor.com/terms-of-service/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beeceptor
- group: commercial
  title: ''
  type: Plans
  url: ''
created: '2025-01-08'
description: Beeceptor is an API mocking, HTTP debugging, and proxy platform that lets developers create mock servers instantly without any coding. It supports REST, SOAP, GraphQL, and gRPC mocking, provides real-time HTTP traffic inspection, webhook testing, local tunneling, and AI-powered spec generation. Teams use Beeceptor to unblock frontend, backend, and QA workflows by simulating APIs before they are built or while avoiding dependencies on live services.
features:
- 'Beeceptor: free public API'
- Free for personal mock APIs (1 endpoint, 50 requests/day). Paid plans from $10/mo.
- 'Public URL: https://beeceptor.com/'
finops:
- has_sources: true
  method: generated
  name: Beeceptor Finops
  primary_unit: ''
  service_category: API Mocking
  slug: beeceptor-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beeceptor.png
integrations:
- description: Inspect and debug Shopify webhook payloads by tunneling webhook deliveries through Beeceptor for local development and testing.
  name: Shopify
- description: Test Stripe webhook events and payment API callbacks using Beeceptor local tunneling and traffic inspection.
  name: Stripe
- description: Debug email delivery webhook callbacks and event notifications from Sendgrid using Beeceptor HTTP inspection and mock responses.
  name: Sendgrid
- description: Integrate Beeceptor programmatic API (Scale plan and above) into CI/CD pipelines to automate mock provisioning and teardown during testing.
  name: CI/CD Pipelines
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.beeceptor.com over HTTP.
  name: Beeceptor MCP Server
  slug: beeceptor
modified: '2026-05-04'
name: Beeceptor
nav: Providers
network: true
overview: 'Beeceptor publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Endpoint Settings API, Mock Rules API, Request History API, and 2 more. Tagged areas include API Mocking, Automation, Debugging, HTTP Proxy, and Integration.


  The Beeceptor catalog on APIs.io includes 1 Spectral governance ruleset.


  Beeceptor''s developer surface includes authentication, developer portal, pricing, FAQ, engineering blog, and 10 more developer resources.'
plans:
- name: Beeceptor Plans Pricing
  plan_count: 1
  slug: beeceptor-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Beeceptor Rate Limits
  slug: beeceptor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Beeceptor API Rules
  rule_count: 54
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 2
  slug: beeceptor-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 51.7
    developer_ergonomics: 50.0
    discoverability: 60.0
    operational_transparency: 23.7
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
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
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/beeceptor/beeceptor-2026-06-20T173119.png
security:
- kind: authentication
  name: Beeceptor Authentication
  slug: beeceptor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Beeceptor Domain Security
  slug: beeceptor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beeceptor
tags:
- API Mocking
- Automation
- Debugging
- HTTP Proxy
- Integration
- Mock Servers
- Platform
- Testing
- Webhook
use_cases:
- description: Build and test frontend applications against mock APIs without waiting for backend APIs to be ready, removing cross-team blocking dependencies.
  name: Frontend Development
- description: Mock downstream microservices and third-party APIs to test API behavior under various conditions including timeouts and error states.
  name: Backend Development
- description: Access mock servers to enable parallel mobile development without backend dependencies, accelerating the mobile app development cycle.
  name: Mobile Development
- description: Simulate edge cases, rate limits, latencies, and rarely reachable code paths to achieve comprehensive test coverage without live API dependencies.
  name: QA Engineering
- description: Inspect and debug HTTP payloads for webhook consumers and producers from platforms like Shopify, Stripe, and Sendgrid using local tunneling.
  name: Webhook Testing
- description: Mimic external service behavior for predictable load test outcomes and reduce costs associated with third-party API usage during performance testing.
  name: Load Testing
- description: Collaborate with teammates by sharing intercepted requests and mock servers via permanent links for distributed team workflows.
  name: API Contract Sharing
website: https://beeceptor.com
---
