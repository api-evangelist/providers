---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: OpenTelemetry Protocol (OTLP) ingest endpoint for sending traces, metrics and logs into the Kosmos operational intelligence platform. Accepts OTLP over HTTP (primary) and gRPC (alternative), authentic
  name: Kosmos OTLP Ingest API
  slug: otlp-ingest
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://kosmoslabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kosmoslabs.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kosmoslabs.ai/product-documentation/readme
- group: company
  title: ''
  type: Blog
  url: https://kosmoslabs.ai/resources/blog/
- group: start
  title: ''
  type: SignUp
  url: https://kosmoslabs.ai/#contact
- group: start
  title: ''
  type: Login
  url: https://app.kosmoslabs.ai/
- group: operate
  title: ''
  type: Support
  url: mailto:support@kosmoslabs.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.kosmoslabs.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.kosmoslabs.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://kosmoslabs.ai/resources/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kosmoslabs.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kosmoslabs.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kosmosailabs/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kosmoslabs-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/kosmoslabs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kosmoslabs-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kosmoslabs-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kosmoslabs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kosmoslabs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kosmoslabs-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/kosmoslabs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kosmoslabs-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kosmoslabs-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kosmoslabs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kosmoslabs-vulnerability-disclosure.yml
created: '2026-07-17'
description: 'Kosmos AI Labs builds an operational intelligence platform that correlates signals across fragmented enterprise systems — Jira, Salesforce Service Cloud, GitHub, ServiceNow, Zendesk, Linear, Bitbucket, Azure DevOps, Pylon and OpenTelemetry — to surface Risk Events with ranked causes and supporting evidence for customer-impacting incidents. The platform operates on a "machines propose, humans confirm" trust model: it proposes root-cause analysis in under sixty seconds and a human confirms, building organizational memory that keeps incidents from recurring. Its public developer surface is an OpenTelemetry (OTLP) ingest API at ingest.kosmoslabs.ai accepting traces, metrics and logs over HTTP and gRPC, authenticated with a kos_-prefixed API key; every other system is connected through read-only OAuth integration scopes rather than a public REST API.'
image: https://kosmoslabs.ai/wp-content/themes/kosmoslabs/assets/images/logo.svg
layout: provider
modified: '2026-07-19'
name: Kosmos AI Labs
nav: Providers
network: true
overview: 'Kosmos AI Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Operational Intelligence, Observability, OpenTelemetry, and Incident Management.


  Kosmos AI Labs'' developer surface includes documentation, getting-started guide, engineering blog, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Kosmoslabs Rate Limits
  slug: kosmoslabs-rate-limits
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 29.2
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kosmoslabs/refs/heads/main/screenshots/kosmoslabs-2026-07-25T224239.png
security:
- kind: authentication
  name: Kosmoslabs Authentication
  slug: kosmoslabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kosmoslabs Domain Security
  slug: kosmoslabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kosmoslabs Vulnerability Disclosure
  slug: kosmoslabs-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kosmoslabs Trust Center
  slug: kosmoslabs-trust-center
  summary_line: trust center published
slug: kosmoslabs
tags:
- Company
- Operational Intelligence
- Observability
- OpenTelemetry
- Incident Management
- Root Cause Analysis
- AIOps
- Enterprise Software
website: https://kosmoslabs.ai
---
