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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adludio-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/adludio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adludio-llms.txt
- group: company
  title: ''
  type: Website
  url: https://adludio.com/
coverage:
  checked: '2026-08-12'
  detail: ADLUDIO LIMITED (UK company 08227542) went into administration on 2024-08-23 and into creditors voluntary liquidation on 2025-08-28; adludio.com now 301-redirects to permate.com, a different company, and no Adludio host or developer surface survives.
  evidence:
  - status: 301
    url: https://adludio.com/
  - status: 301
    url: https://adludio.com/openapi.json
  - status: 404
    url: https://adludio.webflow.io/
  - status: 200
    url: https://find-and-update.company-information.service.gov.uk/company/08227542/insolvency
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=adludio
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Adludio was an AI-powered interactive mobile advertising company founded in 2015 in London by Paul Coggins (originally Future Ad Labs). Its "Sensory Ad Science" platform built rich, interactive mobile ad units using touch, motion and haptic interaction, sold on a cost-per-engagement rather than CPM model, with brand clients including Nike, Microsoft, Coca-Cola and Estee Lauder. The company was backed by Balderton Capital. Adludio is now defunct: ADLUDIO LIMITED (UK company number 08227542) entered administration on 2024-08-23 and moved into creditors voluntary liquidation on 2025-08-28. The adludio.com domain 301-redirects to permate.com (an unrelated partnership-automation platform), no api/docs/developer subdomain resolves, and the residual adludio.webflow.io marketing mirror now returns 404. Adludio never published a public API, developer portal or machine-readable contract; the only surviving developer artifacts are four abandoned first-party npm packages under the @adludio
  scope (interactive ad-runtime building blocks, not API clients), none released since 2019.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adludio.png
layout: provider
modified: '2026-08-12'
name: adludio
nav: Providers
network: true
overview: adludio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile Advertising, and Marketing Technology.
random_paper: 142
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adludio/refs/heads/main/screenshots/adludio-2026-07-25T181639.png
security:
- kind: domain-security
  name: Adludio Domain Security
  slug: adludio-domain-security
  summary_line: TLSv1.3
slug: adludio
tags:
- Company
- Advertising
- AdTech
- Mobile Advertising
- Marketing Technology
- Interactive Advertising
- Creative
website: https://adludio.com/
---
