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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: RESTful API for the Incident IQ K-12 ITSM and asset management platform. Resources include tickets, assets, users, locations, views, and categories. Requests require SiteId, Authorization (bearer toke
  name: Incident IQ API v1.0
  slug: incident-iq-api-v10
artifact_total: 4
asyncapis:
- description: ''
  name: Incident Iq Webhooks
  slug: incident-iq-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.incidentiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apihub.incidentiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apihub.incidentiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apihub.incidentiq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.incidentiq.com/platform/api
- group: operate
  title: ''
  type: Support
  url: https://www.incidentiq.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.incidentiq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.incidentiq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.incidentiq.com/pricing
- group: start
  title: ''
  type: Login
  url: https://login.incidentiq.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.incidentiq.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.incidentiq.com/terms-of-use
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.incidentiq.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.incidentiq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/incidentiq
- group: auth
  title: ''
  type: Authentication
  url: authentication/incident-iq-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/incident-iq-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/incident-iq-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/incident-iq-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/incident-iq-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incident-iq-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/incident-iq-llms.txt
created: '2026-07-17'
description: Incident IQ is a K-12-purpose-built IT service management (ITSM) and asset management platform used by school districts to run help desk ticketing, device and technology asset tracking, facilities and HR service delivery, and operational analytics. Its RESTful API (v1.0) lets districts and partners build custom integrations across the district ecosystem — connecting billing and ticketing, pushing tickets to third-party service providers, exporting analytics to visualization tools, and syncing systems. Requests are authenticated with SiteId, Authorization, and Client (ApiClient) headers issued from Administration > Developer Tools, and events can be pushed to external systems via rule-triggered webhooks.
image: https://www.incidentiq.com/
layout: provider
modified: '2026-07-19'
name: Incident IQ
nav: Providers
network: true
overview: 'Incident IQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edtech, IT Service Management, Asset Management, and Help Desk.


  The Incident IQ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Incident IQ''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 31.4
  delta: -13.8
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 45.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/incident-iq/refs/heads/main/screenshots/incident-iq-2026-07-25T222224.png
security:
- kind: authentication
  name: Incident Iq Authentication
  slug: incident-iq-authentication
  summary_line: http/oauth1 · 4 schemes
- kind: domain-security
  name: Incident Iq Domain Security
  slug: incident-iq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: incident-iq
tags:
- Company
- Edtech
- IT Service Management
- Asset Management
- Help Desk
- Ticketing
- K-12
- Education
- Webhooks
- REST
website: https://www.incidentiq.com/
---
