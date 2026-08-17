---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Avenue Webhooks
  slug: avenue-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avenue-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avenue-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/avenue-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/avenue-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/avenue-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avenue-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Avenue-Alerting
- group: company
  title: ''
  type: Website
  url: https://avenue.app/
- group: company
  title: ''
  type: Blog
  url: https://avenue.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://avenue.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avenue.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avenue.app/privacy-policy
coverage:
  checked: '2026-08-14'
  detail: Avenue was acquired by Clay in January 2025 and the product is gone — the application host app.useavenue.com, which the live site's "Log in" button still points at, returns HTTP 404 "Application not found" from Railway on every path, and the Intercom help center at docs.useavenue.com returns HTTP 403 (Cloudflare error 1014), leaving only a frozen Framer marketing site footered "© 2024 Avenue".
  evidence:
  - status: 404
    url: https://app.useavenue.com/signin
  - status: 403
    url: https://docs.useavenue.com/
  - status: 404
    url: https://avenue.app/openapi.json
  - status: 404
    url: https://avenue.app/.well-known/agent-card.json
  - status: 200
    url: https://avenue.app/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Avenue is an operations observability and workflow-automation platform that helps operations, RevOps, and support teams detect problems and act on them in real time. It connects to the tools and databases a business already runs on (Postgres, Google Sheets, Salesforce, Zendesk, Slack, Linear, Asana, Notion), watches for issues using custom rules and thresholds, and routes alerts into a shared task queue where teams triage and resolve them. A drag-and-drop playbook builder and an operational AI copilot automate routine responses, while metrics track resolution over time. Avenue is used by operations leaders at marketplaces, fintech, and healthcare companies. It was founded in 2021 by Justin Bleuel and Jeff Barg, and was backed by Y Combinator, Slack Fund, Accel, Flexport, Lachy Groom, and Elad Gil. Avenue was acquired by Clay in January 2025 and the product has since been wound down: the marketing site at avenue.app is still served but frozen at "© 2024 Avenue", the application
  host app.useavenue.com returns HTTP 404 "Application not found", and the Intercom help center at docs.useavenue.com returns HTTP 403. Avenue never published a public API, OpenAPI specification, SDK, MCP server, or agent card; the only developer- facing surface it documented was inbound and outbound webhooks.'
image: https://framerusercontent.com/images/P7bVoSUqmRbIfCE0DPeHoRKwyA.png
layout: provider
modified: '2026-08-14'
name: Avenue
nav: Providers
network: true
overview: 'Avenue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Operations, Observability, and Workflow Automation.


  The Avenue catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avenue''s developer surface includes engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Avenue Plans Pricing
  plan_count: 2
  slug: avenue-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 0
  name: Avenue Rate Limits
  slug: avenue-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 19.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/avenue/refs/heads/main/screenshots/avenue-2026-07-25T201920.png
security:
- kind: domain-security
  name: Avenue Domain Security
  slug: avenue-domain-security
  summary_line: TLSv1.3 · HSTS
slug: avenue
tags:
- Company
- Cloud Saas
- Operations
- Observability
- Workflow Automation
- Alerting
- RevOps
- Task Queue
website: https://avenue.app/
---
