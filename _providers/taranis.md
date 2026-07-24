---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: 'Leaf-level crop intelligence delivered through the AcreForward platform using submillimeter aerial imagery and computer vision to detect weeds, insect damage, disease pressure, nutrient deficiencies, '
  name: Taranis Crop Intelligence
  slug: taranis-crop-intelligence
- description: Field health imagery, agronomic insights, and Yield Impact reporting that convert leaf-level observations into measurable bushel and yield outcomes, surfaced through the Taranis web dashboard and mobi
  name: Taranis Imagery and Insights
  slug: taranis-imagery-insights
- description: Generative AI agronomy engine that contextualizes Taranis leaf-level data with weather, machinery, and research data to generate product, nutrient, and input recommendations. Exposed as an in-platform
  name: Taranis Ag Assistant
  slug: taranis-ag-assistant
- description: Channel and data partnerships (e.g., Syngenta Crop Protection, Ag Partners / Nutrien) and ingestion of machinery and weather data that power AcreForward. These are commercial and operational integrati
  name: Taranis Platform Integrations
  slug: taranis-platform-integrations
artifact_total: 9
collections:
- collection_type: open
  name: Taranis API
  slug: open-taranis
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taranis-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taranis-visual
- group: company
  title: ''
  type: Website
  url: https://www.taranis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.taranis.ag/portal/en/kb
- group: commercial
  title: ''
  type: Plans
  url: plans/taranis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taranis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taranis-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.taranis.com/feed/
created: '2026-06-20'
description: Taranis is an AI-powered crop intelligence company that delivers full-service, leaf-level aerial scouting for agricultural advisors, retailers, and growers. Its AcreForward platform captures submillimeter drone and satellite imagery and applies computer vision and generative AI (Ag Assistant) to detect weeds, pests, disease, nutrient deficiencies, and stand counts, turning insights into measurable yield outcomes. Taranis is delivered as a closed SaaS platform (web dashboard and mobile apps); no public or partner developer API is documented as of this writing.
finops:
- name: Taranis Finops
  service_category: Analytics
  slug: taranis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taranis.png
layout: provider
modified: '2026-06-20'
name: Taranis
nav: Providers
network: true
overview: 'Taranis publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Crop Intelligence, Imagery and Insights, Ag Assistant, and 1 more. Tagged areas include Agriculture, AgTech, Crop Intelligence, Computer Vision, and Aerial Scouting.


  Taranis'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Taranis Plans Pricing
  plan_count: 2
  slug: taranis-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Taranis Rate Limits
  slug: taranis-rate-limits
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 37.7
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taranis/refs/heads/main/screenshots/taranis-2026-06-20T194922.png
security:
- kind: domain-security
  name: Taranis Domain Security
  slug: taranis-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: taranis
tags:
- Agriculture
- AgTech
- Crop Intelligence
- Computer Vision
- Aerial Scouting
- Precision Agriculture
website: https://www.taranis.com/
---
