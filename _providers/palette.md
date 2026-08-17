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
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://palettehq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.palettehq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://palettehq.com/plans
- group: company
  title: ''
  type: Blog
  url: https://palettehq.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.palettehq.com/#/login
- group: operate
  title: ''
  type: Support
  url: https://palettehq.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://palettehq.com/terms-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://palette.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://palettehq.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/palette-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palette-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/palette-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://palettehq.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/palette-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaletteHQ
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/palette-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/palette-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: Palette's only documentation host, doc.palettehq.com, historically 302'd to https://app.palettehq.com/#/login — the reference required an active tenant — and it now returns CloudFront 502 "Failed to contact the origin" on every path, while the API host api.palettehq.com is a dangling CNAME to an NXDOMAIN Elastic Beanstalk environment, so the API that Palette monitors as a component on its own status page has no reachable reference at all.
  evidence:
  - status: 502
    url: https://doc.palettehq.com/
  - status: 404
    url: https://palettehq.com/openapi.json
  - status: 404
    url: https://palettehq.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Palette (Palette HQ) is a sales commission and incentive compensation management platform that automates the calculation, tracking, and payout of sales commissions in real time. It lets revenue operations and finance teams design complex commission plans, run scenario analysis and forecasting, give reps live visibility into earnings through performance dashboards, and keep audit trails for compliance. Palette connects to CRMs (Salesforce, HubSpot, Pipedrive, Close, Outreach, Bullhorn, Sellsy), billing systems (Stripe, Chargebee, QuickBooks, Xero, NetSuite, Pennylane), and data warehouses (Snowflake, BigQuery, Redshift) via one-click integrations rather than a public developer API. The company is SOC 2 Type II compliant and backed by Bain Capital Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/palette.png
layout: provider
modified: '2026-08-13'
name: Palette
nav: Providers
network: true
overview: 'Palette is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Sales Compensation, Commission Management, and Revenue Operations.


  Palette''s developer surface includes documentation, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Palette Plans Pricing
  plan_count: 3
  slug: palette-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Palette Rate Limits
  slug: palette-rate-limits
score:
  band: thin
  composite: 29.1
  delta: 7.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 22.1
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/palette/refs/heads/main/screenshots/palette-2026-08-07T191317.png
security:
- kind: domain-security
  name: Palette Domain Security
  slug: palette-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Palette Vulnerability Disclosure
  slug: palette-vulnerability-disclosure
  summary_line: disclosure policy published
slug: palette
tags:
- Company
- Ai Apps
- Sales Compensation
- Commission Management
- Revenue Operations
- Sales
- FinOps
- SaaS
website: https://palettehq.com/
---
