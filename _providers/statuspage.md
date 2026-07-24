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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 47.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Statuspage Agentic Access
  operation_count: 29
  slug: statuspage-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 4
apis:
- description: REST API for managing Statuspage pages, components, component groups, incidents, incident templates, scheduled maintenances, metrics, subscribers, users, and page access groups. Authentication uses an
  name: Statuspage Manage API
  slug: manage-api
- description: Public, read-only REST API exposed by every Statuspage at /api/v2 that returns current status, components, incidents, maintenances, and uptime data as JSON. Useful for embedding status data in applica
  name: Statuspage Status API (v2)
  slug: status-api
- description: 'Outbound webhook notifications Statuspage POSTs to subscriber endpoints for component status changes, incident lifecycle updates, and scheduled maintenance lifecycle updates. Subscribers must respond '
  name: Statuspage Webhook Notifications
  slug: webhooks
- description: The Pages API from Statuspage — 17 operation(s) for pages.
  name: Statuspage Pages API
  slug: statuspage-pages-api
artifact_total: 13
asyncapis:
- description: AsyncAPI description of the webhook notifications that Atlassian Statuspage delivers to subscriber endpoints. Statuspage POSTs a JSON body to a customer-configured URL whenever a component changes sta
  name: Statuspage Webhook Notifications
  slug: statuspage-webhooks-asyncapi
collections:
- collection_type: open
  name: Statuspage REST API
  slug: open-statuspage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/statuspage-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/statuspage-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/statuspage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/statuspage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/statuspage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StatusPage
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statuspage
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/statuspage
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.statuspage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://support.atlassian.com/statuspage/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/statuspage/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.atlassian.com/software/statuspage/try
- group: start
  title: ''
  type: Login
  url: https://manage.statuspage.io/login
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/statuspage/
- group: other
  title: ''
  type: Parent Company
  url: https://www.atlassian.com/
created: '2026-05-11'
description: Statuspage by Atlassian is a hosted status page and incident communication platform that helps companies communicate real-time service status, incident updates, scheduled maintenance, and component health to customers and internal stakeholders. It supports public and private pages, audience-specific pages, subscriber notifications via email, SMS, webhooks, Slack, and Teams, and 150+ third-party component integrations. The Statuspage REST API provides programmatic access to pages, components, incidents, maintenances, metrics, subscribers, and users authenticated with an OAuth-prefixed API key.
graphqls:
- description: 'This conceptual GraphQL schema represents the Atlassian Statuspage REST API surface, which provides programmatic access to hosted status pages and incident communication. The REST API is available at '
  name: Atlassian Statuspage GraphQL Schema
  slug: statuspage-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/statuspage.png
layout: provider
modified: '2026-05-30'
name: Statuspage
nav: Providers
network: true
overview: 'Statuspage publishes 2 APIs on the [APIs.io](https://apis.io/) network: Webhook Notifications and Pages API. Tagged areas include Status Page, Incident Communication, Incident Management, Uptime, and Reliability.


  The Statuspage catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Statuspage''s developer surface includes authentication, documentation, pricing, signup flow, support, and 10 more developer resources.'
random_paper: 18
rules:
- name: Statuspage API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: statuspage-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 58.4
    developer_ergonomics: 32.6
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 5.3
  previous_composite: 41.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/statuspage/refs/heads/main/screenshots/statuspage-2026-06-20T194529.png
security:
- kind: authentication
  name: Statuspage Authentication
  slug: statuspage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Statuspage Domain Security
  slug: statuspage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Statuspage Vulnerability Disclosure
  slug: statuspage-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Statuspage Trust Center
  slug: statuspage-trust-center
  summary_line: FedRAMP
slug: statuspage
tags:
- Status Page
- Incident Communication
- Incident Management
- Uptime
- Reliability
- Atlassian
website: https://www.atlassian.com/software/statuspage
---
