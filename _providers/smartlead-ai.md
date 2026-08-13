---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Smartlead Ai Agentic Access
  operation_count: 5
  slug: smartlead-ai-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 9
apis:
- description: REST endpoints to create, list, fetch, update, schedule, pause, resume, and delete email campaigns, plus manage sequences, A/B variants, and sender account assignments inside a campaign.
  name: Smartlead Campaigns API
  slug: campaigns-api
- description: Endpoints to add leads to a campaign in bulk, fetch leads, update lead status (interested, replied, unsubscribed), search leads globally, and manage lead categories.
  name: Smartlead Leads API
  slug: leads-api
- description: Endpoints to add, list, update, and remove sender mailboxes (SMTP, Gmail, Outlook), assign them to campaigns, and track per-account sending limits and warmup state.
  name: Smartlead Email Accounts API
  slug: email-accounts-api
- description: Endpoints for managing Smartlead's deliverability warmup engine — enabling warmup per mailbox, configuring ramp settings, and reading warmup reputation and stats.
  name: Smartlead Email Warmup API
  slug: email-warmup-api
- description: CRUD endpoints for campaign-scoped webhook subscriptions covering lead events (sent, opened, clicked, replied, bounced, unsubscribed) used to stream Smartlead activity to external systems.
  name: Smartlead Webhooks API
  slug: webhooks-api
- description: Endpoints for campaign and account-level analytics — sent, open, click, reply, bounce, and unsubscribe metrics aggregated over time ranges.
  name: Smartlead Analytics API
  slug: analytics-api
- description: Endpoints for agency users to provision and manage white-labeled client accounts, assign permissions, and meter usage across multiple end customers.
  name: Smartlead Client Management API
  slug: client-management-api
- description: Retrieve campaign performance metrics.
  name: Smartlead Campaign Statistics API
  slug: smartlead-ai-campaign-statistics-api
- description: Manage Smartlead email campaigns.
  name: Smartlead Campaigns API
  slug: smartlead-ai-campaigns-api
artifact_total: 16
collections:
- collection_type: open
  name: Smartlead API
  slug: open-smartlead-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartlead-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartlead-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartlead-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartlead.ai
- group: other
  title: ''
  type: App
  url: https://app.smartlead.ai
- group: docs
  title: ''
  type: Documentation
  url: https://api.smartlead.ai/reference
- group: docs
  title: ''
  type: APIReference
  url: https://api.smartlead.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.smartlead.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartlead.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.smartlead.ai/blog
- group: start
  title: ''
  type: Signup
  url: https://app.smartlead.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.smartlead.ai/login
- group: operate
  title: ''
  type: Help
  url: https://help.smartlead.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartlead.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartlead.ai/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartleadhq
- group: company
  title: ''
  type: Twitter
  url: https://x.com/smartlead_ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@smartlead
- group: agent
  title: ''
  type: LlmsText
  url: https://api.smartlead.ai/llms.txt
created: '2026-05-23'
description: Smartlead is cold email infrastructure for outbound sales and lead generation, focused on inbox deliverability through unlimited mailbox rotation, automated warmup, and a unified master inbox. Smartlead exposes a REST API at server.smartlead.ai/api/v1 covering campaigns, leads, email accounts, email warmup, webhooks, analytics, and client management, with API key authentication via query parameter.
finops:
- name: Smartlead Ai Finops
  service_category: API
  slug: smartlead-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartlead-ai.png
layout: provider
modified: '2026-05-23'
name: Smartlead
nav: Providers
network: true
overview: 'Smartlead publishes 2 APIs on the [APIs.io](https://apis.io/) network: Campaign Statistics API and Campaigns API. Tagged areas include Cold Email, Outbound, Sales, Deliverability, and Email Warmup.


  Smartlead''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Smartlead Ai Plans Pricing
  plan_count: 1
  slug: smartlead-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Smartlead Ai Rate Limits
  slug: smartlead-ai-rate-limits
score:
  band: developing
  composite: 47.9
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 57.8
    developer_ergonomics: 39.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartlead-ai/refs/heads/main/screenshots/smartlead-ai-2026-06-20T194043.png
security:
- kind: authentication
  name: Smartlead Ai Authentication
  slug: smartlead-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smartlead Ai Domain Security
  slug: smartlead-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartlead-ai
tags:
- Cold Email
- Outbound
- Sales
- Deliverability
- Email Warmup
- Automation
- Sequences
website: https://www.smartlead.ai
---
