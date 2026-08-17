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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/involveai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.involve.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://city.involve.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://city.involve.ai/knowledge-base
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/involveai
- group: operate
  title: ''
  type: Support
  url: https://city.involve.ai/help-and-tech-support-40
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Involve-AI
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/involveai-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/involveai-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Involve.AI was renamed into Jeeva AI and its product surface decommissioned — app.involve.ai is NXDOMAIN, api.involve.ai answers Cloudflare 530 with no origin behind it, and www.involve.ai answers 522 on every path except the root, which is a redirect rule pointing at www.jeeva.ai.
  evidence:
  - status: 530
    url: https://api.involve.ai/
  - status: 522
    url: https://www.involve.ai/pricing
  - status: 301
    url: https://www.involve.ai/
  - status: 404
    url: https://city.involve.ai/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/involve-ai
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Involve.AI was an AI-driven customer intelligence platform for customer success and revenue teams. It unified data from CRM, support, product-usage, and billing systems to calculate customer health scores and power an Early Warning System that predicted churn and surfaced renewal and upsell opportunities, with a 9Factor model scoring qualitative and quantitative signals. Founded as a Techstars-backed startup, Involve.AI was renamed into Jeeva.ai rather than shut down — the GitHub organization login is still Involve-AI while its display name is now Jeeva AI, and involve.ai redirects to jeeva.ai. The product surface is retired: app.involve.ai no longer resolves, the involve.ai web origin answers Cloudflare 522 on every path but the root redirect, and api.involve.ai answers 530 with no origin behind it. Only the customer knowledge base at city.involve.ai survives. Involve.AI never published a developer API — it took admin-granted read access into a customer''s source systems (Salesforce,
  Zendesk, Snowflake, Azure SQL, Pendo) through a no-code Data Mapping tool and returned health scores through configured write-backs into the system of action — so this profile documents company identity and a retirement record rather than an API surface.'
image: https://uploads-us-west-2.insided.com/involve-en/attachment/70ee02e8-dba6-4699-b6ec-894a6c75b81a.png
layout: provider
modified: '2026-08-13'
name: Involve.AI
nav: Providers
network: true
overview: 'Involve.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Intelligence, Customer Success, Customer Health Score, and Churn Prediction.


  Involve.AI''s developer surface includes documentation, support, and 7 more developer resources.'
plans:
- name: Involveai Plans Pricing
  plan_count: 0
  slug: involveai-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 0
  name: Involveai Rate Limits
  slug: involveai-rate-limits
score:
  band: minimal
  composite: 8.8
  delta: 1.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/involveai/refs/heads/main/screenshots/involveai-2026-07-25T222808.png
security:
- kind: domain-security
  name: Involveai Domain Security
  slug: involveai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: involveai
tags:
- Company
- Customer Intelligence
- Customer Success
- Customer Health Score
- Churn Prediction
- Artificial Intelligence
- SaaS
- Revenue Operations
website: https://www.involve.ai/
---
