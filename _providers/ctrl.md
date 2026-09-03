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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ctrl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getctrl.co
- group: company
  title: ''
  type: Blog
  url: https://www.getctrl.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getctrl.co/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/ctrl-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/ctrl-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ctrl-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ctrl-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getctrl.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getctrl.co/privacy-policy
coverage:
  checked: '2026-08-13'
  detail: Ctrl was absorbed into Sana Labs on 2024-10-30; the marketing site is now a live archive whose own homepage answers 200 with a 404 body, api.getctrl.co has never resolved, and the former application host app.getctrl.co has been taken over by an unrelated Indonesian gambling portal.
  evidence:
  - status: 200
    url: https://www.getctrl.co/
  - status: 200
    url: https://app.getctrl.co/
  - status: 404
    url: https://www.getctrl.co/.well-known/agent-card.json
  - status: 404
    url: https://www.getctrl.co/openapi.json
  - status: 404
    url: https://www.getctrl.co/llms.txt
  reason: defunct
  state: none
created: '2026-07-17'
description: Ctrl (Ctrl, Inc., a Delaware corporation) is an AI-powered workspace for revenue and sales teams that consolidates the tools and data a rep needs — CRM, email, calendar, and messaging — into a single actionable view. Founded in 2021 by Omri Sagzan and Aviv Nahum and based in Tel Aviv and London, Ctrl automates the manual work of updating records across apps such as HubSpot, Salesforce, Google Workspace, and Slack, and helps teams codify and replicate their winning sales playbooks. The company raised a $9M seed round led by LocalGlobe and Earlybird in 2023 and was acquired by Sana Labs in October 2024. Ctrl is a UI/workspace product surfaced as an Earlybird portfolio company; it publishes no public developer API, OpenAPI, or SDKs.
image: https://cdn.prod.website-files.com/625d8e920c535704a599b545/62ab32f217ec4d3c47eda994_Screenshot%202022-06-16%20164043.png
layout: provider
modified: '2026-08-13'
name: Ctrl
nav: Providers
network: true
overview: 'Ctrl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Revenue Operations, CRM, and Productivity.


  Ctrl''s developer surface includes engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Ctrl Plans Pricing
  plan_count: 3
  slug: ctrl-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ctrl/refs/heads/main/screenshots/ctrl-2026-07-25T210854.png
security:
- kind: domain-security
  name: Ctrl Domain Security
  slug: ctrl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ctrl
tags:
- Company
- Sales
- Revenue Operations
- CRM
- Productivity
- Workspace
- Automation
- Artificial Intelligence
- Software-as-a-Service
website: https://www.getctrl.co
---
