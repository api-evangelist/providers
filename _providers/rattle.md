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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.gorattle.com
- group: start
  title: ''
  type: Login
  url: https://app.gorattle.com/
- group: operate
  title: ''
  type: Support
  url: https://help.gorattle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.gorattle.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.gorattle.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.gorattle.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gorattle.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gorattle.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gorattle.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.gorattle.com/en/collections/7377751-weekly-release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rattle-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rattle-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://help.gorattle.com/llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/rattle-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rattle-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rattle-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gorattle.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rattle-domain-security.yml
coverage:
  checked: '2026-08-13'
  detail: Rattle (and its successor brand Von) ships only an end-user Slack/Teams app over a customer's own Salesforce tenant — api.gorattle.com does not resolve at all, and api.vonlabs.ai answers as a bare nginx origin that 404s /openapi.json, /swagger.json, /docs, /redoc, /api-docs, /mcp and every /.well-known path, so there is no developer portal, API reference, SDK, webhook catalog or machine-readable contract anywhere on either brand.
  evidence:
  - status: 404
    url: https://api.vonlabs.ai/openapi.json
  - status: 404
    url: https://www.gorattle.com/api
  - status: 404
    url: https://www.gorattle.com/developers
  - status: 404
    url: https://vonlabs.ai/.well-known/agent-card.json
  - status: 200
    url: https://help.gorattle.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Rattle is a sales-execution and revenue-workflow platform that positions itself as "the AI layer your CRM always needed," connecting Salesforce with Slack and Microsoft Teams so revenue teams can automate RevOps workflows, keep CRM data accurate, and surface deal insights in real time. AI features — Wizard, Smart Context, Meeting Intelligence, Deal Rooms, Board and Leaderboard — drive alerts, field auto-update, deal-risk assessment and call summarization from inside the chat client. In May 2026 the company rebranded its forward product to Von (vonlabs.ai), an "AI RevOps teammate" that connects to CRM, call recordings and the data warehouse; Rattle remains fully supported for existing customers. Rattle is backed by GV (Google Ventures), Insight Partners, Sequoia and Lightspeed. As of this enrichment pass neither Rattle nor Von exposes a public developer API, SDK, webhook catalog or API reference — probes of api.gorattle.com, api.vonlabs.ai and every documented host returned no
  machine-readable contract — so this profile captures the company's public web, help-center, release-note, security/compliance and operational-transparency surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rattle.png
layout: provider
modified: '2026-08-13'
name: Rattle
nav: Providers
network: true
overview: 'Rattle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, RevOps, CRM, and Salesforce.


  Rattle''s developer surface includes support, documentation, signup flow, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Rattle Plans Pricing
  plan_count: 0
  slug: rattle-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Rattle Rate Limits
  slug: rattle-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: -1.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 25.5
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Rattle Domain Security
  slug: rattle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Rattle Trust Center
  slug: rattle-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: rattle
tags:
- Company
- Sales
- RevOps
- CRM
- Salesforce
- Slack
- Microsoft Teams
- Sales Automation
- Revenue Intelligence
- Workflow Automation
- Artificial Intelligence
website: https://www.gorattle.com
---
