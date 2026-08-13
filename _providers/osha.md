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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Access OSHA enforcement data including inspections, violations, and penalties through the Department of Labor's API.
  name: OSHA Enforcement Data API
  slug: osha-enforcement-data
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osha-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osha
- group: company
  title: ''
  type: Website
  url: https://www.osha.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.osha.gov/data/
- group: operate
  title: ''
  type: Support
  url: https://www.osha.gov/contactus/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.osha.gov/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.osha.gov/rss.xml
created: '2026-03-16'
description: Occupational Safety and Health Administration - U.S. federal agency responsible for setting and enforcing workplace safety and health standards. OSHA provides data APIs for accessing enforcement, inspection, and injury data.
finops:
- name: Osha Finops
  service_category: API
  slug: osha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/osha.png
layout: provider
modified: '2026-03-16'
name: OSHA
nav: Providers
network: true
overview: 'OSHA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Government, Health Standards, Regulatory, and Workplace Safety.


  OSHA''s developer surface includes documentation, support, engineering blog, and 4 more developer resources.'
plans:
- name: Osha Plans Pricing
  plan_count: 3
  slug: osha-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Osha Rate Limits
  slug: osha-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Osha Domain Security
  slug: osha-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: osha
tags:
- Compliance
- Government
- Health Standards
- Regulatory
- Workplace Safety
website: https://www.osha.gov/
---
