---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Johnson And Johnson Agentic Access
  operation_count: 3
  slug: johnson-and-johnson-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Manage connected glucose monitoring devices.
  name: Johnson & Johnson Devices API
  slug: johnson-and-johnson-devices-api
- description: Manage and retrieve blood glucose reading data.
  name: Johnson & Johnson Glucose Readings API
  slug: johnson-and-johnson-glucose-readings-api
- description: Access patient profile and health information.
  name: Johnson & Johnson Patients API
  slug: johnson-and-johnson-patients-api
artifact_total: 10
collections:
- collection_type: open
  name: Johnson & Johnson LifeScan API
  slug: open-johnson-and-johnson-lifescan-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/johnson-and-johnson-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/johnson-and-johnson-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/johnson-and-johnson-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.jnj.com/
- group: start
  title: ''
  type: Portal
  url: https://github.com/johnsonandjohnson
created: '2026-03-21'
description: Johnson & Johnson is a multinational pharmaceutical and medical devices corporation. Operating today as Johnson & Johnson Innovative Medicine and MedTech, J&J has historically connected health platforms and APIs through subsidiaries such as LifeScan (OneTouch blood glucose monitoring), which was divested to Platinum Equity in 2018 and continues to operate the LifeScan developer portal referenced here. Consumer health brands (Tylenol, Listerine, Neutrogena, Band-Aid) were spun out as Kenvue in 2023 and are tracked in a separate kenvue index.
finops:
- name: Johnson And Johnson Finops
  service_category: Healthcare / Enterprise Integration
  slug: johnson-and-johnson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/johnson-and-johnson.png
layout: provider
modified: '2026-05-19'
name: Johnson & Johnson
nav: Providers
network: true
overview: 'Johnson & Johnson publishes 3 APIs on the [APIs.io](https://apis.io/) network: Devices API, Glucose Readings API, and Patients API. Tagged areas include Healthcare, Medical Devices, Diabetes, Blood Glucose, and Pharmaceuticals.


  Johnson & Johnson''s developer surface includes authentication, developer portal, and 3 more developer resources.'
plans:
- name: Johnson And Johnson Plans Pricing
  plan_count: 1
  slug: johnson-and-johnson-plans-pricing
press:
- date: '2026-05-25'
  title: 'J&J Uses AI Agents: 10 Ways to Use AI [In-Depth Analysis] ...'
  url: https://www.klover.ai/johnson-johnson-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/
- date: '2026-05-25'
  title: Johnson & Johnson Advances Polyphonic™ AI Fund for ...
  url: https://www.jnjmedtech.com/en-US/news/press-releases/johnson-johnson-advances-polyphonic-ai-fund-surgery-data-driven-healthcar/
- date: '2026-05-25'
  title: 6 ways Johnson & Johnson is using AI to help advance ...
  url: https://www.jnj.com/innovation/artificial-intelligence-in-healthcare
- date: '2026-05-25'
  title: We're using AI and other innovative technology in new ...
  url: https://www.facebook.com/jnj/posts/were-using-ai-and-other-innovative-technology-in-new-ways-to-advance-healthcaref/1761545181191612/
- date: '2026-05-25'
  title: JNJ Innovation - News & Events
  url: https://jnjinnovation.com/news
random_paper: 10
rate_limits:
- limit_count: 1
  name: Johnson And Johnson Rate Limits
  slug: johnson-and-johnson-rate-limits
score:
  band: thin
  composite: 31.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/johnson-and-johnson/refs/heads/main/screenshots/johnson-and-johnson-2026-06-20T183753.png
security:
- kind: authentication
  name: Johnson And Johnson Authentication
  slug: johnson-and-johnson-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Johnson And Johnson Domain Security
  slug: johnson-and-johnson-domain-security
  summary_line: TLSv1.3 · DMARC
slug: johnson-and-johnson
tags:
- Healthcare
- Medical Devices
- Diabetes
- Blood Glucose
- Pharmaceuticals
- Fortune 100
website: https://www.jnj.com/
---
