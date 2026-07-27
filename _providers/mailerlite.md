---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 70.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Mailerlite Agentic Access
  operation_count: 21
  slug: mailerlite-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 9
apis:
- description: The MailerLite Classic API serves legacy MailerLite Classic accounts. New integrations should target the current API at connect.mailerlite.com.
  name: MailerLite Classic API (Legacy)
  slug: mailerlite-classic-api
- description: The Automations API from MailerLite — 1 operation(s) for automations.
  name: MailerLite Automations API
  slug: mailerlite-automations-api
- description: The Campaigns API from MailerLite — 2 operation(s) for campaigns.
  name: MailerLite Campaigns API
  slug: mailerlite-campaigns-api
- description: The Fields API from MailerLite — 1 operation(s) for fields.
  name: MailerLite Fields API
  slug: mailerlite-fields-api
- description: The Forms API from MailerLite — 1 operation(s) for forms.
  name: MailerLite Forms API
  slug: mailerlite-forms-api
- description: The Groups API from MailerLite — 2 operation(s) for groups.
  name: MailerLite Groups API
  slug: mailerlite-groups-api
- description: The Segments API from MailerLite — 1 operation(s) for segments.
  name: MailerLite Segments API
  slug: mailerlite-segments-api
- description: The Subscribers API from MailerLite — 4 operation(s) for subscribers.
  name: MailerLite Subscribers API
  slug: mailerlite-subscribers-api
- description: The Webhooks API from MailerLite — 2 operation(s) for webhooks.
  name: MailerLite Webhooks API
  slug: mailerlite-webhooks-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of MailerLite's outbound webhook surface. MailerLite delivers event notifications by issuing HTTP POST requests with a JSON body to a callback URL the customer registers throu
  name: MailerLite Webhooks
  slug: mailerlite-webhooks-asyncapi
collections:
- collection_type: open
  name: MailerLite API
  slug: open-mailerlite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailerlite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailerlite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailerlite-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailerlite-international
- group: company
  title: ''
  type: Website
  url: https://www.mailerlite.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.mailerlite.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailerlite
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailerlite.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/mailerlite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailerlite-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailerlite-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/mailerlite/canny-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/mailerlite/mailerlite-skills
created: '2026-05-08'
description: MailerLite is an email marketing and automation platform. The current REST API exposes subscribers, groups, segments, fields, campaigns, automations, forms, webhooks, and more, with a deprecated Classic API still serving legacy accounts.
finops:
- name: Mailerlite Finops
  service_category: Email Marketing
  slug: mailerlite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailerlite.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: MailerLite
nav: Providers
network: true
overview: 'MailerLite publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Automations API, Campaigns API, Fields API, and 5 more. Tagged areas include Email Marketing, Automation, Newsletters, and Subscribers.


  The MailerLite catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MailerLite''s developer surface includes authentication, developer portal, pricing, and 10 more developer resources.'
plans:
- name: Mailerlite Plans Pricing
  plan_count: 4
  slug: mailerlite-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 1
  name: Mailerlite Rate Limits
  slug: mailerlite-rate-limits
rules:
- name: MailerLite API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: mailerlite-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.6
  delta: 3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 28.3
    discoverability: 87.5
    governance: 52.6
    operational_transparency: 26.3
  previous_composite: 46.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailerlite/refs/heads/main/screenshots/mailerlite-2026-06-20T184854.png
security:
- kind: authentication
  name: Mailerlite Authentication
  slug: mailerlite-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailerlite Domain Security
  slug: mailerlite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: MailerLite
  slug: mailerlite
slug: mailerlite
tags:
- Email Marketing
- Automation
- Newsletters
- Subscribers
website: https://www.mailerlite.com/
---
