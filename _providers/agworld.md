---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
api_count: 3
apis:
- description: Cloud farm-management platform for growers, agronomists, and ag retailers. Covers the Agworld Basics core, Planning, Scheduling, Precision (spray records), Insights (financial and agronomic), and Comp
  name: Agworld Farm Management Platform
  slug: platform
- description: Label, manufacturer, ingredient, and pest database powering product selection and compliance inside Agworld. Distributed publicly as the Greenbook product-label search database.
  name: Agworld DBX (Greenbook)
  slug: dbx
- description: Direct integrations with farm-equipment, weather, finance, BI, and compliance systems - including John Deere, Davis Weather Station, PIPA, Mobble, Shed, FSA Field Data, Figured, PowerBI, CalAg, Frames
  name: Agworld Integrations
  slug: integrations
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agworld-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.agworld.com/us/blog/
- group: company
  title: ''
  type: Website
  url: https://www.agworld.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.agworld.com/en/
- group: operate
  title: ''
  type: Contact
  url: https://agworld.com/us/contact
- group: other
  title: ''
  type: Parent
  url: https://www.telus.com/en/agriculture
created: '2026-05-23'
description: Agworld is a collaborative farm-management platform - now part of the Semios Group and majority-owned by Telus Agriculture & Consumer Goods - used by growers, agronomists, and ag retailers to plan, schedule, record, and report on field activities. The product surface covers planning, scheduling, precision spray records, agronomic and financial insights, and compliance reporting. Agworld integrates with John Deere, Climate-style monitor data via Agworld DBX, plus Figured, PowerBI, Shed, CalAg, Frames, CART by FarmReady, and Mobble. The companion DBX product is a label, manufacturer, ingredient, and pest database (Greenbook). Agworld does not publish an open public developer portal; partner integrations are arranged through their team.
finops:
- name: Agworld Finops
  service_category: API
  slug: agworld-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agworld.png
layout: provider
modified: '2026-05-23'
name: Agworld
nav: Providers
network: true
overview: 'Agworld publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Farm Management, Compliance, and Agronomy.


  Agworld''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Agworld Plans Pricing
  plan_count: 1
  slug: agworld-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Agworld Rate Limits
  slug: agworld-rate-limits
score:
  band: emerging
  composite: 17.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agworld/refs/heads/main/screenshots/agworld-2026-06-20T170515.png
security:
- kind: domain-security
  name: Agworld Domain Security
  slug: agworld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agworld
tags:
- Agriculture
- AgTech
- Farm Management
- Compliance
- Agronomy
- Telus
website: https://www.agworld.com/
---
