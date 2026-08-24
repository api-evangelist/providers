---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cat Agentic Access
  operation_count: 6
  slug: cat-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: The CAT Caterpillar Telematics API API from CAT — 1 operation(s) for cat caterpillar telematics api.
  name: CAT CAT Caterpillar Telematics API API
  slug: cat-cat-caterpillar-telematics-api-api
- description: The Equipment API from CAT — 5 operation(s) for equipment.
  name: CAT Equipment API
  slug: cat-equipment-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CAT Caterpillar Telematics CAT Caterpillar Telematics API API
  slug: open-cat-cat-caterpillar-telematics-api-api
- collection_type: open
  name: CAT Caterpillar Telematics CAT Caterpillar Telematics API Equipment API
  slug: open-cat-equipment-api
- collection_type: open
  name: CAT Caterpillar Telematics API
  slug: open-cat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cat-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caterpillar-inc
- group: start
  title: ''
  type: Portal
  url: https://digital.cat.com/
- group: company
  title: ''
  type: Website
  url: https://www.cat.com/
- group: start
  title: ''
  type: Login
  url: https://digital.cat.com/
- group: other
  title: ''
  type: Applications
  url: https://digital.cat.com/applications
- group: operate
  title: ''
  type: FAQ
  url: https://digital.cat.com/knowledge-hub/faq
- group: company
  title: ''
  type: News
  url: https://digital.cat.com/news-announcements-list
- group: operate
  title: ''
  type: ChangeLog
  url: https://digital.cat.com/release-notes-manager
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digital.cat.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digital.cat.com/privacy
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.caterpillar.com/en/investors.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.caterpillar.com/en/news.html
- group: company
  title: ''
  type: Careers
  url: https://www.caterpillar.com/en/careers.html
created: '2025-01-07'
description: 'CAT is the brand name and ticker symbol for Caterpillar Inc. (NYSE: CAT), the world''s leading manufacturer of construction and mining equipment, off-highway diesel and natural gas engines, industrial gas turbines, and diesel-electric locomotives. Cat Digital publishes a public API catalog at digital.cat.com that exposes fleet, asset, telematics, and fuel data APIs built on the Cat Connect and VisionLink platforms.'
features:
- name: Fleet Management
- name: Asset Telematics
- name: VisionLink
- name: Cat Connect
- name: Fuel Data
- name: Utilization
- name: Hours and Odometer
- name: Location and Geofencing
- name: Equipment Health
- name: Service and Maintenance
- name: Parts Catalog
- name: Dealer Integrations
finops:
- name: Cat Finops
  service_category: API
  slug: cat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cat.png
layout: provider
modified: '2026-05-19'
name: CAT
nav: Providers
network: true
overview: 'CAT publishes 2 APIs on the [APIs.io](https://apis.io/) network: CAT Caterpillar Telematics API API and Equipment API. Tagged areas include Construction, Engines, Equipment, Heavy Equipment, and Locomotives.


  CAT''s developer surface includes developer portal, FAQ, product news, changelog, and 11 more developer resources.'
plans:
- name: Cat Plans Pricing
  plan_count: 3
  slug: cat-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Cat Rate Limits
  slug: cat-rate-limits
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 0.0
    contract_quality: 45.5
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cat/refs/heads/main/screenshots/cat-2026-06-20T174039.png
security:
- kind: domain-security
  name: Cat Domain Security
  slug: cat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cat
tags:
- Construction
- Engines
- Equipment
- Heavy Equipment
- Locomotives
- Manufacturing
- Mining
- Telematics
use_cases:
- name: Construction Site Fleet Tracking
- name: Mining Fleet Optimization
- name: Fuel Consumption Analytics
- name: Predictive Maintenance
- name: Dealer Parts Ordering
- name: Telematics Integration
website: https://www.cat.com/
---
