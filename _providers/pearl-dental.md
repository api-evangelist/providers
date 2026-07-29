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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Partner/OEM-gated cloud AI surface behind Second Opinion. When an imaging partner uploads a bitewing, periapical, panoramic, or CBCT radiograph, Pearl's cloud computer-vision service analyzes it and r
  name: Pearl Second Opinion Image Analysis API
  slug: pearl-dental-second-opinion-image-analysis-api
- description: Practice Intelligence pairs Pearl's diagnostic AI with full practice-management-system data to surface clinical quality, financial performance, appointment compliance, case acceptance, and per-provide
  name: Pearl Practice Intelligence Analytics API
  slug: pearl-dental-practice-intelligence-analytics-api
- description: 'The integration/enablement layer through which Pearl is provisioned inside third-party imaging and practice management systems - including as an authorized vendor in the Henry Schein One API Exchange '
  name: Pearl PMS Integration Exchange API
  slug: pearl-dental-pms-integration-exchange-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pearl-dental-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hellopearl
- group: company
  title: ''
  type: Website
  url: https://hellopearl.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.hellopearl.com
- group: start
  title: ''
  type: Portal
  url: https://management.hellopearl.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/pearl-dental-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://hellopearl.com/blog
created: '2026-07-05'
description: Pearl is a dental AI computer-vision company whose FDA-cleared products - Second Opinion (real-time pathology and restorative detection on 2D and 3D dental radiographs), Practice Intelligence (clinical and operational analytics over full practice-management-system data), and Precheck (AI insurance claim review) - are delivered by embedding Pearl's cloud AI into third-party imaging and practice management software rather than through a public, self-serve developer API. Pearl integrates natively with 40+ imaging/PMS platforms (DEXIS, Carestream, Planmeca Romexis, Dentsply Sirona Sidexis, Apteryx XVWeb, MiPACS, Open Dental, Dentrix, Eaglesoft, Curve, Denticon, Software of Excellence EXACT) and is an authorized vendor in the Henry Schein One API Exchange. There is no publicly documented, self-signup Pearl developer API, SDK, or OpenAPI reference; API access is partner/OEM-gated and arranged through Pearl's integrations and sales teams. The API surfaces below are modeled from Pearl's
  public product descriptions and integration architecture, not from published Pearl API reference documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pearl-dental.png
layout: provider
modified: '2026-07-05'
name: Pearl
nav: Providers
network: true
overview: 'Pearl publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Dental, Computer Vision, Radiology, and Medical Imaging.


  Pearl''s developer surface includes documentation, developer portal, engineering blog, and 4 more developer resources.'
plans:
- name: Pearl Dental Plans Pricing
  plan_count: 0
  slug: pearl-dental-plans-pricing
random_paper: 54
score:
  band: minimal
  composite: 10.0
  delta: -2.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Pearl Dental Domain Security
  slug: pearl-dental-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pearl-dental
tags:
- AI
- Dental
- Computer Vision
- Radiology
- Medical Imaging
- Pathology Detection
- Healthcare
- Partner Gated
website: https://hellopearl.com
---
