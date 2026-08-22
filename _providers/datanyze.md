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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datanyze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datanyze.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Datanyze
- group: build
  title: ''
  type: Packages
  url: packages/datanyze-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/datanyze-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datanyze-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Datanyze ships only an end-user Chrome extension; its own sitemap lists 32,286 URLs and every one is a /market-share technographics page last modified 2021-04-21, with no developer, docs, or API page anywhere in it, and the live api.datanyze.com backend serves the extension only (every probed path returns a NestJS 404 and no specification).
  evidence:
  - status: 200
    url: https://www.datanyze.com/sitemap-index-1.xml
  - status: 404
    url: https://api.datanyze.com/openapi.json
  - status: 404
    url: https://api.datanyze.com/.well-known/agent-card.json
  - status: 404
    url: https://www.datanyze.com/.well-known/security.txt
  - status: 403
    url: https://www.datanyze.com/pricing
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Datanyze is a sales intelligence and technographic data provider owned by ZoomInfo. It offers a free browser (Chrome) extension that surfaces business contact information — work email addresses, direct-dial and mobile phone numbers, and company firmographics — for prospects on LinkedIn profiles and company websites. Datanyze pioneered "technographics," the practice of tracking the web technologies and software a company uses to power targeted B2B sales and marketing outreach. ZoomInfo acquired Datanyze in 2018 to deliver real-time technographic data to its customers. No public developer API is currently documented; this profile captures the company's discoverable web and security surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datanyze.png
layout: provider
modified: '2026-08-13'
name: Datanyze *
nav: Providers
network: true
overview: Datanyze * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Sales Intelligence, Technographics, and Data Enrichment.
plans:
- name: Datanyze Plans Pricing
  plan_count: 0
  slug: datanyze-plans-pricing
random_paper: 3
score:
  band: minimal
  composite: 6.1
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datanyze/refs/heads/main/screenshots/datanyze-2026-07-25T211344.png
security:
- kind: domain-security
  name: Datanyze Domain Security
  slug: datanyze-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datanyze
tags:
- Company
- Enterprise
- Sales Intelligence
- Technographics
- Data Enrichment
- Lead Generation
- Contact Data
- Marketing
- B2B
- Prospecting
website: https://www.datanyze.com/
---
