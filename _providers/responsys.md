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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Responsys REST API (v1.3) manages profile lists and recipients, profile extension tables, supplemental data tables, campaigns and campaign schedules, programs, folders, the content library, trigge
  name: Oracle Responsys REST API
  slug: oracle-responsys-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/responsys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cx/marketing/campaign-management/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-rest-api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-rest-api/rest-endpoints.html
- group: other
  title: ''
  type: SOAP
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-soap-api/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/responsys-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/responsys-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/responsys-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/responsys-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/responsys-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/responsys-llms.txt
created: '2026-07-17'
description: Oracle Responsys (Oracle Responsys Campaign Management) is a B2C cross-channel marketing orchestration platform, originally founded as Responsys and acquired by Oracle in 2014, now part of Oracle Marketing. It lets marketing teams design and deliver targeted, personalized customer experiences across email, mobile push, SMS, display, and web channels, unifying data from disparate sources into precisely targeted audiences delivered in near real-time. Responsys exposes a REST API (v1.3) and a legacy SOAP API for managing profile lists and recipients, profile extension tables, supplemental tables, campaigns, programs, folders, the content library, triggered email/SMS/push messages, events, and account settings. This profile catalogs the public Oracle Responsys developer surface for the API Evangelist network.
image: https://docs.oracle.com/en/cloud/saas/marketing/responsys.html
layout: provider
mcp_servers:
- description: ''
  name: responsys-mcp.yml
  slug: responsys-mcpyml
modified: '2026-07-20'
name: Responsys
nav: Providers
network: true
overview: 'Responsys publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Email Marketing, Marketing Automation, and Campaign Management.


  Responsys'' developer surface includes documentation, API reference, authentication, and 9 more developer resources.'
random_paper: 30
score:
  band: emerging
  composite: 15.4
  delta: -2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Responsys Authentication
  slug: responsys-authentication
  summary_line: token · 1 scheme
- kind: domain-security
  name: Responsys Domain Security
  slug: responsys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: responsys
tags:
- Company
- Marketing
- Email Marketing
- Marketing Automation
- Campaign Management
- Cross-Channel Marketing
- Customer Engagement
- Oracle
- Martech
website: https://www.oracle.com/cx/marketing/campaign-management/
---
