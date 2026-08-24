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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Member-facing data export of glucose/CGM, activity, zones, and nutrition logs as CSV downloads from the Levels member portal. This is a UI download only; no programmatic/public API endpoint is documen
  name: Levels Data Export
  slug: levels-data-export
- description: Inbound connectivity that lets members link Apple Health and wearable data and upload prior labs, DEXA scans, and health records into the Levels app. These are in-app integrations, not an outbound pub
  name: Levels Health Data Integrations
  slug: levels-health-data-integrations
- description: A "Partner With Us" program for clinics and partners surfaced in the Levels site footer. No partner-facing developer API, OAuth flow, or documented endpoints are published; engagement is via a contact
  name: Levels Partner Program
  slug: levels-partner-program
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Levels
  slug: open-levels-health
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levels-health-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/levels-health
- group: company
  title: ''
  type: Website
  url: https://www.levelshealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.levels.com
- group: commercial
  title: ''
  type: Plans
  url: plans/levels-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/levels-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/levels-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.levelshealth.com/rss/
created: '2026-06-20'
description: Levels is a continuous glucose monitoring (CGM) metabolic-health app that pairs glucose sensors with lab testing and personalized guidance. The platform is a consumer product delivered through iOS, Android, and a member web portal; it consumes health data (Apple Health, wearables, uploaded labs) but does not publish a documented public or partner developer API as of this catalog date.
finops:
- name: Levels Health Finops
  service_category: Health and Wellness
  slug: levels-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/levels-health.png
layout: provider
modified: '2026-06-20'
name: Levels
nav: Providers
network: true
overview: 'Levels publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data Export, Health Data Integrations, and Partner Program. Tagged areas include Metabolic Health, CGM, Continuous Glucose Monitoring, Health, and Wellness.


  Levels'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Levels Health Plans Pricing
  plan_count: 4
  slug: levels-health-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Levels Health Rate Limits
  slug: levels-health-rate-limits
score:
  band: emerging
  composite: 25.9
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 28.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/levels-health/refs/heads/main/screenshots/levels-health-2026-06-20T184436.png
security:
- kind: domain-security
  name: Levels Health Domain Security
  slug: levels-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: levels-health
tags:
- Metabolic Health
- CGM
- Continuous Glucose Monitoring
- Health
- Wellness
website: https://www.levelshealth.com
---
