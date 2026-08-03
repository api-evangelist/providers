---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Beeceptor Agentic Access
  operation_count: 29
  slug: beeceptor-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 5
apis:
- description: Beeceptor's management API provides programmatic access to create and manage mock endpoints, rules, and traffic inspection on Scale and Enterprise plans. It enables teams to automate mock server provi
  name: Beeceptor API
  slug: beeceptor
- description: The Endpoint Settings API from Beeceptor — 5 operation(s) for endpoint settings.
  name: Beeceptor Endpoint Settings API
  slug: beeceptor-endpoint-settings-api
- description: The Mock Rules API from Beeceptor — 4 operation(s) for mock rules.
  name: Beeceptor Mock Rules API
  slug: beeceptor-mock-rules-api
- description: The Request History API from Beeceptor — 3 operation(s) for request history.
  name: Beeceptor Request History API
  slug: beeceptor-request-history-api
- description: The State Store API from Beeceptor — 2 operation(s) for state store.
  name: Beeceptor State Store API
  slug: beeceptor-state-store-api
artifact_total: 27
collections:
- collection_type: open
  name: Beeceptor API
  slug: open-beeceptor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beeceptor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beeceptor-domain-security.yml
- group: auth
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
- name: Beeceptor Finops
  service_category: API Mocking
  slug: beeceptor-finops
graphqls:
- description: ''
  name: Beeceptor GraphQL API
  slug: beeceptor-graphql
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
modified: '2026-05-04'
name: Beeceptor
nav: Providers
network: true
overview: 'Beeceptor publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Endpoint Settings API, Mock Rules API, Request History API, and 1 more. Tagged areas include API Mocking, Automation, Debugging, HTTP Proxy, and Integrations.


  Beeceptor''s developer surface includes authentication, developer portal, pricing, FAQ, engineering blog, and 8 more developer resources.'
plans:
- name: Beeceptor Plans Pricing
  plan_count: 1
  slug: beeceptor-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Beeceptor Rate Limits
  slug: beeceptor-rate-limits
score:
  band: developing
  composite: 43.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beeceptor/refs/heads/main/screenshots/beeceptor-2026-06-20T173119.png
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
- Integrations
- Mock Servers
- Platform
- Testing
- Webhooks
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
