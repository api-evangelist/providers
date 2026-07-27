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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Tally Agentic Access
  operation_count: 26
  slug: tally-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 8
apis:
- description: REST API for managing forms and fetching/deleting submissions. Bearer token auth using API keys created from the workspace dashboard. Free on every Tally plan including the Free tier.
  name: Tally REST API
  slug: rest
- description: JavaScript embed library exposing Tally.openPopup, Tally.closePopup, Tally.loadEmbeds and event listeners for form load, page view, submission and popup close.
  name: Tally Embed JS
  slug: embed
- description: The Forms API from Tally — 3 operation(s) for forms.
  name: Tally Forms API
  slug: tally-forms-api
- description: The Organization API from Tally — 4 operation(s) for organization.
  name: Tally Organization API
  slug: tally-organization-api
- description: The Submissions API from Tally — 2 operation(s) for submissions.
  name: Tally Submissions API
  slug: tally-submissions-api
- description: The Users API from Tally — 1 operation(s) for users.
  name: Tally Users API
  slug: tally-users-api
- description: The Webhooks API from Tally — 4 operation(s) for webhooks.
  name: Tally Webhooks API
  slug: tally-webhooks-api
- description: The Workspaces API from Tally — 2 operation(s) for workspaces.
  name: Tally Workspaces API
  slug: tally-workspaces-api
artifact_total: 15
collections:
- collection_type: open
  name: Tally REST API
  slug: open-tally
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tally-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tally-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tally-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withtally
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meettally
- group: company
  title: ''
  type: Website
  url: https://tally.so/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tally.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://tally.so/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://tally.so/help
- group: commercial
  title: ''
  type: Plans
  url: plans/tally-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tally-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tally-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://tally.so/llms.txt
created: '2026-05-08'
description: Tally is a Notion-style form and survey builder offering unlimited forms and submissions on its free plan. The Tally API exposes forms, submissions and webhooks programmatically and is free to use across all plans (including Free). Tally also publishes a JS embed library and an MCP server for AI integration.
finops:
- name: Tally Finops
  service_category: Forms / Surveys
  slug: tally-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tally.png
layout: provider
modified: '2026-05-08'
name: Tally
nav: Providers
network: true
overview: 'Tally publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Forms API, Organization API, Submissions API, and 3 more. Tagged areas include Forms, Surveys, No-Code, Free, and Notion-style.


  Tally''s developer surface includes authentication, documentation, pricing, and 10 more developer resources.'
plans:
- name: Tally Plans Pricing
  plan_count: 3
  slug: tally-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Tally Rate Limits
  slug: tally-rate-limits
score:
  band: thin
  composite: 41.0
  delta: 3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.3
    developer_ergonomics: 23.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tally/refs/heads/main/screenshots/tally-2026-06-20T194908.png
security:
- kind: authentication
  name: Tally Authentication
  slug: tally-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tally Domain Security
  slug: tally-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tally
tags:
- Forms
- Surveys
- No-Code
- Free
- Notion-style
- Webhooks
- MCP
website: https://tally.so/
---
