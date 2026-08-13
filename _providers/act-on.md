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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: OAuth 2.0 REST API for Act-On marketing automation — contacts and lists, segments, email messages and campaigns, media and creative assets, landing pages and forms, subscriptions, custom data, and rep
  name: Act-On REST API
  slug: act-on-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://act-on.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.act-on.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.act-on.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.act-on.com/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.act-on.com/reference/request-a-developer-account
- group: operate
  title: ''
  type: StatusPage
  url: https://status.act-on.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/act-on-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/act-on-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/act-on-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/act-on-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/act-on-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/act-on-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/act-on-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/act-on-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/act-on-domain-security.yml
created: '2026-07-17'
description: Act-On Software is a cloud-based marketing automation platform used by B2B and B2C marketing teams for email marketing, lead generation and nurturing, landing pages and forms, website visitor tracking, lead scoring and segmentation, custom data, and campaign reporting. Act-On exposes a documented OAuth 2.0 REST API (base https://restapi.actonsoftware.com, versioned under /api/1) covering contacts and lists, segments, messages and email campaigns, media and creative assets, landing pages and forms, subscription management, custom data ingestion, and reporting. Added to the API Evangelist network from a Norwest Venture Partners portfolio lead and enriched from Act-On's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/act-on.png
layout: provider
mcp_servers:
- description: ''
  name: act-on-mcp.yml
  slug: act-on-mcpyml
modified: '2026-07-17'
name: Act-On
nav: Providers
network: true
overview: 'Act-On publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Automation, Email Marketing, and Email.


  Act-On''s developer surface includes documentation, API reference, getting-started guide, authentication, and 11 more developer resources.'
random_paper: 98
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 19.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/act-on/refs/heads/main/screenshots/act-on-2026-07-25T181520.png
security:
- kind: authentication
  name: Act On Authentication
  slug: act-on-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Act On Domain Security
  slug: act-on-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: act-on
tags:
- Company
- Marketing
- Marketing Automation
- Email Marketing
- Email
- Marketing Technology
- Lead Generation
- Campaign Management
- API
website: https://act-on.com
---
