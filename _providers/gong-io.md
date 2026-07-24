---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 12
apis:
- description: Gong's primary REST API for reading and writing platform data — calls, users, stats, library content, settings, workspaces, permissions, data privacy, CRM data, audit logs, and engagement. Authenticat
  name: Gong Public API
  slug: public-api
- description: Endpoints for retrieving call metadata, transcripts, media URLs, extensive filtering, and adding new calls (recordings and metadata) from external telephony and conferencing platforms.
  name: Gong Calls API
  slug: calls-api
- description: Endpoints for listing and managing Gong users, their roles, manager relationships, and metadata used for permissioning and reporting.
  name: Gong Users API
  slug: users-api
- description: Aggregated statistics for activity, interaction, and rep-level metrics — used to back dashboards, scorecards, and external BI integrations.
  name: Gong Stats API
  slug: stats-api
- description: Endpoints for browsing Gong libraries and folders, retrieving call lists inside a folder, and managing the curated learning content shared across teams.
  name: Gong Library API
  slug: library-api
- description: Read and update tenant-level configuration — trackers, scorecards, and tracking settings used by Gong to score calls and surface signals.
  name: Gong Settings API
  slug: settings-api
- description: Manage Gong workspaces — the isolation boundary used for multi-tenant or multi-business-unit Gong deployments.
  name: Gong Workspaces API
  slug: workspaces-api
- description: Endpoints for listing and managing permission profiles and access controls applied to Gong users and content.
  name: Gong Permissions API
  slug: permissions-api
- description: Endpoints supporting GDPR / CCPA workflows — locate, export, and purge personal data stored in Gong on behalf of an individual.
  name: Gong Data Privacy API
  slug: data-privacy-api
- description: Endpoints for reading CRM object schema and data Gong has ingested from connected CRMs (Salesforce, HubSpot, Dynamics), and for pushing engagement activity back into the CRM context.
  name: Gong CRM API
  slug: crm-api
- description: Audit log endpoints for retrieving user activity, configuration changes, and access events used in compliance and SIEM workflows.
  name: Gong Logs API
  slug: logs-api
- description: Engagement endpoints surfacing email and meeting touchpoints between reps and prospects, used for activity analytics and pipeline hygiene.
  name: Gong Engagement API
  slug: engagement-api
artifact_total: 17
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/gong-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gong-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gong.io
- group: docs
  title: ''
  type: Documentation
  url: https://app.gong.io/settings/api/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app.gong.io/settings/api/documentation
- group: operate
  title: ''
  type: Help
  url: https://app.gong.io/help
- group: start
  title: ''
  type: GettingStarted
  url: https://app.gong.io/help/docs/api
- group: start
  title: ''
  type: Login
  url: https://app.gong.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gong.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.gong.io/blog
- group: operate
  title: ''
  type: Status
  url: https://status.gong.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gong.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gong.io/terms-of-service
- group: auth
  title: ''
  type: Trust
  url: https://www.gong.io/trust-center
- group: auth
  title: ''
  type: Security
  url: https://www.gong.io/trust-center/security
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gong-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gong-io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/gong_io
created: '2026-05-23'
description: Gong is the Revenue AI platform that captures customer interactions across phone, web conferencing, and email, then applies conversation intelligence and generative AI to coach reps, forecast pipeline, and surface deal risk. Gong exposes a REST API at api.gong.io covering Calls, Users, Stats, Library, Settings, Workspaces, Permissions, Data Privacy, CRM, Logs, Engagement, and webhook-style automation rules, plus an outbound data integrations program for pushing call recordings, transcripts, and metadata into Gong from third-party telephony and conferencing systems.
finops:
- name: Gong Io Finops
  service_category: API
  slug: gong-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gong-io.png
layout: provider
modified: '2026-05-23'
name: Gong
nav: Providers
network: true
overview: 'Gong publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Revenue Intelligence, Conversation Intelligence, Sales, AI, and CRM.


  Gong''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, status page, GitHub presence, and 11 more developer resources.'
plans:
- name: Gong Io Plans Pricing
  plan_count: 1
  slug: gong-io-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 2
  name: Gong Io Rate Limits
  slug: gong-io-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gong-io/refs/heads/main/screenshots/gong-io-2026-06-20T182025.png
security:
- kind: domain-security
  name: Gong Io Domain Security
  slug: gong-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gong Io Trust Center
  slug: gong-io-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, CSA STAR
slug: gong-io
tags:
- Revenue Intelligence
- Conversation Intelligence
- Sales
- AI
- CRM
- Coaching
- Forecasting
website: https://www.gong.io
---
