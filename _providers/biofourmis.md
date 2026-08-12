---
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biofourmis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biofourmis-llms.txt
- group: company
  title: ''
  type: Website
  url: https://biofourmis.com/
- group: company
  title: ''
  type: About
  url: https://biofourmis.com/about
- group: other
  title: ''
  type: Platform
  url: https://biofourmis.com/platform
- group: company
  title: ''
  type: Blog
  url: https://biofourmis.com/news-insights
- group: company
  title: ''
  type: BlogRSS
  url: https://biofourmis.com/news-insights/feed/
- group: operate
  title: ''
  type: Support
  url: https://biofourmis.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biofourmis.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biofourmis.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biofourmis/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/biofourmis
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/biofourmis_stock/
coverage:
  checked: '2026-08-07'
  detail: Biofourmis sells an enterprise in-home care platform and markets "EMR integration" on its platform page, but ships no developer portal, API reference or spec — every contract-discovery path on biofourmis.com hard-404s, there is no biofourmis GitHub org, and the API-named hosts in its certificate transparency history (dev-int-api, staging.solutionsapi, api.pmbeta) all resolve NXDOMAIN today.
  evidence:
  - status: 404
    url: https://biofourmis.com/openapi.json
  - status: 404
    url: https://biofourmis.com/.well-known/agent-card.json
  - status: 404
    url: https://biofourmis.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/biofourmis
  - status: 200
    url: https://biofourmis.com/platform
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: Biofourmis is a health technology company founded in 2015, with offices in Boston, Singapore and India, that partners with health systems, hospitals, payers and life science companies to deliver care in the home. Its platform combines medical-grade device connectivity, FDA-cleared algorithms and digital biomarkers, a patient mobile app and clinician dashboard, and 70+ dynamic care pathways to support Hospital at Home, Timely Discharge, SNF at Home and Remote Patient Monitoring programs. Biofourmis merged with CopilotIQ in October 2024 to form an end-to-end platform for AI-driven in-home care; ActiGraph acquired the Biofourmis life science business in January 2025. The company markets EMR integration and device-agnostic connectivity to enterprise healthcare customers, but publishes no public developer program, API reference or machine-readable API contract.
image: https://cdn.prod.website-files.com/641ded6681d1c50b3075e860/641ded6681d1c55e7b75e90c_Biofourmis%20webclip.png
layout: provider
modified: '2026-08-07'
name: Biofourmis
nav: Providers
network: true
overview: 'Biofourmis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Remote Patient Monitoring, and Hospital at Home.


  Biofourmis'' developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 43
score:
  band: minimal
  composite: 12.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biofourmis/refs/heads/main/screenshots/biofourmis-2026-08-07T162455.png
security:
- kind: domain-security
  name: Biofourmis Domain Security
  slug: biofourmis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biofourmis
tags:
- Company
- Healthcare
- Digital Health
- Remote Patient Monitoring
- Hospital at Home
- Care Delivery
- Life Sciences
- Health Technology
- Wearables
website: https://biofourmis.com/
---
