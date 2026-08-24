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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for the Unravel data observability platform. Query and collect data from your monitored clusters and workspaces over HTTP/HTTPS with JSON requests and responses. Endpoint groups cover applica
  name: Unravel REST API
  slug: unravel-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Unravel Data Systems Webhooks
  slug: unravel-data-systems-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unravel-data-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unraveldata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unraveldata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.unraveldata.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.unraveldata.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unraveldata-org
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unraveldata.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unraveldata.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unraveldata.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.unraveldata.com/contact-us/
- group: auth
  title: ''
  type: TrustCenter
  url: security/unravel-data-systems-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.unraveldata.com/privacy-security-faq/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unravel-data-systems-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unravel-data-systems-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/unravel-data-systems-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unravel-data-systems-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unravel-data-systems-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unravel-data-systems-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unravel-data-systems-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unravel-data-systems-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/unravel-data-systems-cli.yml
- group: start
  title: ''
  type: Login
  url: https://customers.unraveldata.com/login
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unravel-data-systems-webhooks.yml
created: '2026-07-17'
description: Unravel Data Systems is an AI-powered data observability and FinOps platform that helps data teams optimize performance, cost, and reliability across modern data stacks including Databricks, Snowflake, BigQuery, Amazon EMR, and Cloudera. The self-hosted and SaaS platform exposes a REST API (JSON over HTTP, session-token authentication via /signIn, RBAC-scoped) for querying application performance, cluster operations, chargeback, anomaly detection, and pipeline data collected by its observability engine.
image: https://cdn.prod.website-files.com/69c4c9c7f795b263782ef5be/69c754b2bfc0db573c3c6e36_9869e478efb1fecc6dafa9f6cb79fb13_global-og-image.jpg
layout: provider
modified: '2026-07-21'
name: Unravel Data Systems
nav: Providers
network: true
overview: 'Unravel Data Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Observability, FinOps, DataOps, Databricks, and Snowflake.


  The Unravel Data Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unravel Data Systems'' developer surface includes documentation, engineering blog, support, pricing, authentication, changelog, CLI, and 16 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 42.4
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 42.4
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unravel-data-systems/refs/heads/main/screenshots/unravel-data-systems-2026-08-17T082628.png
security:
- kind: authentication
  name: Unravel Data Systems Authentication
  slug: unravel-data-systems-authentication
  summary_line: sessionToken · 2 schemes
- kind: domain-security
  name: Unravel Data Systems Domain Security
  slug: unravel-data-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unravel Data Systems Trust Center
  slug: unravel-data-systems-trust-center
  summary_line: SOC 2 Type II
slug: unravel-data-systems
tags:
- Data Observability
- FinOps
- DataOps
- Databricks
- Snowflake
- BigQuery
- Cost Optimization
- Performance
website: https://www.unraveldata.com/
---
