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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Retention API from brightback — 1 operation(s) for retention.
  name: brightback Retention API
  slug: brightback-retention-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Brightback (Chargebee ) Pre-cancel Retention API
  slug: open-brightback-retention-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/brightback-retention-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://www.chargebee.com/docs/retention/installing-chargebee-retention.html
- group: docs
  title: ''
  type: APIReference
  url: https://help.brightback.com/article/171-precancel-api
- group: operate
  title: ''
  type: Support
  url: https://help.brightback.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightback
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chargebee.com/
- group: company
  title: ''
  type: Website
  url: https://brightback.com
- group: build
  title: ''
  type: Packages
  url: packages/brightback-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brightback-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightback-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brightback-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brightback-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brightback-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brightback-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brightback-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brightback-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightback-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightback-domain-security.yml
created: '2026-07-17'
description: Brightback (now Chargebee Retention) is a churn-prevention and cancellation- experience platform for subscription businesses. When a customer clicks "cancel," Brightback intercepts the flow with a personalized, hosted save experience — targeted offers, surveys, and deflection paths — driven by customer and billing context passed from the merchant. Founded as a standalone SaaS backed by Point Nine and other investors, Brightback was acquired by Chargebee in 2021 and operates as Chargebee Retention. Developers integrate via the brightbackjs client library or a server-side pre-cancel API that returns a unique Cancel Session URL, with HMAC-SHA-512 signed requests for backend calls.
image: https://logo.clearbit.com/brightback.com
layout: provider
mcp_servers:
- description: ''
  name: brightback MCP Server
  slug: brightback-mcp-server
modified: '2026-07-18'
name: brightback
nav: Providers
network: true
overview: 'brightback publishes 1 API on the [APIs.io](https://apis.io/) network: Retention API. Tagged areas include Company, Churn Prevention, Customer Retention, Subscription, and Cancellation.


  brightback''s developer surface includes documentation, API reference, support, authentication, and 15 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 23.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 15.9
    developer_ergonomics: 36.3
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 23.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightback/refs/heads/main/screenshots/brightback-2026-07-25T203931.png
security:
- kind: authentication
  name: Brightback Authentication
  slug: brightback-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Brightback Domain Security
  slug: brightback-domain-security
  summary_line: TLSv1.2 · DMARC
slug: brightback
tags:
- Company
- Churn Prevention
- Customer Retention
- Subscription
- Cancellation
- Software-as-a-Service
website: https://brightback.com
---
