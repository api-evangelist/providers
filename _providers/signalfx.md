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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The SignalFx REST API manages metadata and configuration objects in Splunk Observability Cloud / SignalFx: metrics and dimension metadata, detectors and alert muting rules, charts, dashboards and dash'
  name: SignalFx REST API
  slug: signalfx-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/signalfx-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signalfx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://advisory.splunk.com/report
- group: auth
  title: ''
  type: Compliance
  url: https://customertrust.splunk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.splunk.com/observability
- group: docs
  title: ''
  type: Documentation
  url: https://dev.splunk.com/observability/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.splunk.com/observability/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.splunk.com/observability/docs/apibasics/api_getting_started/
- group: company
  title: ''
  type: Blog
  url: https://www.splunk.com/en_us/blog/devops.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signalfx
- group: start
  title: ''
  type: SignUp
  url: https://www.splunk.com/en_us/products/observability.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.splunk.com/en_us/products/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splunk.com/en_us/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splunk.com/en_us/legal/privacy/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.splunk.com/en_us/support-and-services.html
- group: build
  title: ''
  type: Packages
  url: packages/signalfx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/signalfx-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signalfx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/signalfx-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signalfx-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/signalfx-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signalfx-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signalfx-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/signalfx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signalfx-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/signalfx-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signalfx-domain-security.yml
created: '2026-07-17'
description: SignalFx is a cloud monitoring and observability platform for modern infrastructure and microservices, founded in 2013 and acquired by Splunk in October 2019. It ingests high-resolution time-series metrics, events, and traces and applies real-time streaming analytics (the SignalFlow computation engine) to power dashboards, charts, detectors, and alerts. The platform is now delivered as Splunk Observability Cloud. SignalFx exposes a realm-based REST API (metadata, detectors, charts, dashboards, integrations, tokens, SLOs) at api.{realm}.signalfx.com, a data-ingest API at ingest.{realm}.signalfx.com, and a SignalFlow streaming API at stream.{realm}.signalfx.com, all authenticated with an X-SF-Token header. First-party client libraries ship for Go, Python, Node.js, Java, and Ruby.
image: https://avatars.githubusercontent.com/u/8532938?s=200&v=4
layout: provider
mcp_servers:
- description: ''
  name: signalfx-mcp.yml
  slug: signalfx-mcpyml
modified: '2026-07-21'
name: SignalFx
nav: Providers
network: true
overview: 'SignalFx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Monitoring, Metrics, and Time Series.


  SignalFx''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, support, and 20 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 36.4
  delta: -1.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 23.7
  previous_composite: 37.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Signalfx Authentication
  slug: signalfx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signalfx Domain Security
  slug: signalfx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Signalfx Vulnerability Disclosure
  slug: signalfx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Signalfx Trust Center
  slug: signalfx-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: signalfx
tags:
- Company
- Observability
- Monitoring
- Metrics
- Time Series
- APM
- Infrastructure Monitoring
- Alerting
- DevOps
- Splunk
website: https://dev.splunk.com/observability
---
