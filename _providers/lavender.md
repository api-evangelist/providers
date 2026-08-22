---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.lavender.ai
- group: company
  title: ''
  type: Blog
  url: https://www.lavender.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.lavender.ai/blog?category=Product+Help
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lavender.ai/coach#pricing
- group: start
  title: ''
  type: SignUp
  url: https://install.lavender.ai
- group: start
  title: ''
  type: Login
  url: https://dashboard.lavender.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lavender.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lavender.ai/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.lavender.ai/privacy
- group: design
  title: ''
  type: Conformance
  url: conformance/lavender-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/lavender-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lavender-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lavender-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lavender-llms.txt
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/lavenderhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itslavenderduh/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@itslavenderduh/videos
coverage:
  checked: '2026-08-13'
  detail: 'Lavender ships only end-user software — a Chrome/Outlook extension, a dashboard and a Salesforce integration — and exposes no developer surface at all: contract discovery across www, api, app, dashboard and docs subdomains found no OpenAPI, GraphQL, MCP or agent card, and docs.lavender.ai is a dangling Stoplight host (CNAME ingress.stoplight.io) that Cloudflare answers with error 1014.'
  evidence:
  - status: 404
    url: https://api.lavender.ai/openapi.json
  - status: 404
    url: https://www.lavender.ai/.well-known/agent-card.json
  - status: 403
    url: https://docs.lavender.ai/openapi.json
  - note: Soft 200 — SPA catch-all returning text/html for every path, not a spec. Recorded so a later round does not read it as a contract.
    status: 200
    url: https://app.lavender.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Lavender is an AI email intelligence company for sales teams. Its Email Coach is a browser extension and Outlook add-in that scores and coaches outbound sales email in real time — subject line, structure, tone, length and personalization — using models trained on billions of sales emails, and its newer product Ora is an AI sales agent that drafts email and pushes reasoned prospect research into Salesforce CRM records. Lavender is distributed as an end-user extension and a Salesforce integration rather than as a public developer API: as of this profile the company publishes no developer portal, no API reference, no OpenAPI definition, and no client SDKs. It is SOC 2 Type 2 certified and GDPR compliant. Lavender is backed by Norwest Venture Partners.'
image: https://cdn.prod.website-files.com/658433a0cbce340e298ba330/658433a0cbce340e298ba44f_webclip.jpg
layout: provider
modified: '2026-08-13'
name: Lavender
nav: Providers
network: true
overview: 'Lavender is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Email, Artificial Intelligence, and Sales Enablement.


  Lavender''s developer surface includes engineering blog, support, pricing, signup flow, YouTube channel, and 12 more developer resources.'
plans:
- name: Lavender Plans Pricing
  plan_count: 0
  slug: lavender-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 19.7
  delta: -0.5
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.2
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lavender/refs/heads/main/screenshots/lavender-2026-07-25T224733.png
security:
- kind: domain-security
  name: Lavender Domain Security
  slug: lavender-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lavender Trust Center
  slug: lavender-trust-center
  summary_line: trust center published
slug: lavender
tags:
- Company
- Sales
- Email
- Artificial Intelligence
- Sales Enablement
- Sales Engagement
- CRM
- Browser Extension
- Productivity
website: https://www.lavender.ai
---
