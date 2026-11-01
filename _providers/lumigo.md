---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Programmatic access to the Lumigo observability platform, authenticated with an API token (x-api-key header) generated in Lumigo Settings. Host confirmed live (returns 401 without credentials); no pub
  name: Lumigo API
  slug: lumigo-api
artifact_total: 9
asyncapis:
- description: ''
  name: Lumigo Webhooks
  slug: lumigo-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/lumigo/plans/lumigo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lumigo-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://lumigo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lumigo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lumigo.io/
- group: company
  title: ''
  type: Blog
  url: https://lumigo.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lumigo.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://platform.lumigo.io/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumigo.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumigo.io/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://lumigo.io/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumigo-io
- group: operate
  title: ''
  type: Support
  url: https://lumigo.io/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lumigo.io/
- group: auth
  title: ''
  type: Compliance
  url: https://lumigo.io/security/
- group: build
  href: https://artifacts.apis.io/lumigo/packages/lumigo-packages.yml
  title: ''
  type: Packages
  url: packages/lumigo-packages.yml
- group: build
  href: https://artifacts.apis.io/lumigo/packages/lumigo-packages.yml
  title: ''
  type: SDKs
  url: packages/lumigo-packages.yml
- group: build
  href: https://artifacts.apis.io/lumigo/cli/lumigo-cli.yml
  title: ''
  type: CLI
  url: cli/lumigo-cli.yml
- group: agent
  href: https://artifacts.apis.io/lumigo/mcp/lumigo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lumigo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lumigo/llms/lumigo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lumigo-llms.txt
- group: design
  href: https://artifacts.apis.io/lumigo/asyncapi/lumigo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lumigo-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/lumigo/authentication/lumigo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lumigo-authentication.yml
- group: design
  href: https://artifacts.apis.io/lumigo/conformance/lumigo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lumigo-conformance.yml
- group: design
  href: https://artifacts.apis.io/lumigo/lifecycle/lumigo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lumigo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lumigo/conventions/lumigo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lumigo-conventions.yml
- group: operate
  href: https://artifacts.apis.io/lumigo/changelog/lumigo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lumigo-changelog.yml
- group: auth
  href: https://artifacts.apis.io/lumigo/security/lumigo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lumigo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lumigo/security/lumigo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumigo-domain-security.yml
created: '2026-07-17'
description: Lumigo is an observability and troubleshooting platform for microservices and serverless environments. It provides distributed tracing, logs, and metrics with automatic, no-code instrumentation for AWS Lambda, Amazon ECS, AWS AppSync, API Gateway, Kubernetes, and OpenTelemetry workloads. Lumigo captures full request/response payloads for end-to-end traces, maps service dependencies, and offers an AI Copilot (with an IDE MCP server) to investigate and resolve production issues. First-party tracers and OpenTelemetry distributions ship for Node.js, Python, Java, Go, and .NET, alongside a CLI, a Serverless Framework plugin, CDK constructs, and a Kubernetes operator. Lumigo was surfaced as a portfolio company of Wing Venture Capital.
finops:
- has_sources: true
  method: derived
  name: Lumigo Finops
  primary_unit: subscription
  service_category: ''
  slug: lumigo-finops
  template: false
image: https://avatars.githubusercontent.com/u/38886022?v=4
layout: provider
mcp_servers:
- description: Lumigo Copilot MCP server for IDE integration. Lets agents in VS Code (GitHub Copilot), Cursor, JetBrains, Eclipse, and Xcode investigate and resolve production issues from the editor via natural-lang
  name: Lumigo MCP Server
  slug: lumigo-copilot
modified: '2026-07-20'
name: Lumigo
nav: Providers
network: true
overview: 'Lumigo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Monitoring, Serverless, and Distributed Tracing.


  The Lumigo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lumigo''s developer surface includes documentation, engineering blog, pricing, support, CLI, authentication, changelog, and 20 more developer resources.'
plans:
- name: Lumigo Plans Pricing
  plan_count: 6
  slug: lumigo-plans-pricing
- name: Lumigo Price Estimates
  plan_count: 0
  slug: lumigo-price-estimates
random_paper: 5
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 52.4
    discoverability: 65.0
    operational_transparency: 55.3
  previous_composite: 50.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lumigo/lumigo-2026-07-25T225711.png
security:
- kind: authentication
  name: Lumigo Authentication
  slug: lumigo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lumigo Domain Security
  slug: lumigo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Lumigo Trust Center
  slug: lumigo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: lumigo
tags:
- Company
- Observability
- Monitoring
- Serverless
- Distributed Tracing
- OpenTelemetry
- AWS Lambda
- Microservices
- Logs
website: https://lumigo.io/
---
