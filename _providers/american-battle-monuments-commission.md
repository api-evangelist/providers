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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The ABMC We Remember portal provides a searchable database of more than 200,000 fallen U.S. service members buried or commemorated at American military cemeteries abroad. Includes World War II Registr
  name: ABMC We Remember Burial Search
  slug: we-remember
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-battle-monuments-commission-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usabmc
- group: company
  title: ''
  type: Website
  url: https://www.abmc.gov/
- group: start
  title: ''
  type: Portal
  url: https://weremember.abmc.gov/
created: '2024-11-21'
description: The American Battle Monuments Commission (ABMC), established by Congress in 1923, commemorates the service, achievements, and sacrifice of U.S. Armed Forces. ABMC administers and maintains 26 American military cemeteries and 31 memorials, monuments, and markers on foreign soil. The commission maintains a searchable database of more than 200,000 fallen service members buried or commemorated abroad, accessible via the We Remember burial search portal. ABMC is working on a data roadmap to provide open datasets on data.gov per the Foundations for Evidence-based Policymaking Act (2019).
features:
- description: Searchable database of more than 200,000 fallen service members buried or commemorated at ABMC cemeteries and memorials abroad, searchable by name and cemetery.
  name: Burial Search Database
- description: Database of U.S. servicemembers who lost their lives during World War II, accessible via the ABMC WWII Registry portal.
  name: World War II Registry
- description: Registry of U.S. servicemembers who gave their lives during the Korean War, searchable through the We Remember portal.
  name: Korean War Honor Roll
- description: Information about 26 American military cemeteries and 31 memorials, monuments, and markers on foreign soil including virtual 360-degree tours.
  name: Cemetery and Memorial Information
- description: ABMC is developing a data roadmap to provide access to datasets hosted on data.gov per the Foundations for Evidence-based Policymaking Act (2019), with a designated Chief Data Officer.
  name: Open Data Roadmap
finops:
- name: American Battle Monuments Commission Finops
  service_category: API
  slug: american-battle-monuments-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-battle-monuments-commission.png
layout: provider
modified: '2026-04-19'
name: American Battle Monuments Commission
nav: Providers
network: true
overview: 'American Battle Monuments Commission publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Military, Veterans, World War II, and Memorial.


  American Battle Monuments Commission''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: American Battle Monuments Commission Plans Pricing
  plan_count: 3
  slug: american-battle-monuments-commission-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: American Battle Monuments Commission Rate Limits
  slug: american-battle-monuments-commission-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -1.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.0
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-battle-monuments-commission/refs/heads/main/screenshots/american-battle-monuments-commission-2026-06-20T171913.png
security:
- kind: domain-security
  name: American Battle Monuments Commission Domain Security
  slug: american-battle-monuments-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: american-battle-monuments-commission
tags:
- Federal Government
- Military
- Veterans
- World War II
- Memorial
- Open Data
use_cases:
- description: Families and descendants search for fallen service members buried at ABMC cemeteries to locate burial information and plan visits.
  name: Family Research
- description: Historians, researchers, and educators access burial and memorial records for World War II, Korean War, and other conflicts.
  name: Historical Research
- description: ABMC administrators and partner organizations use cemetery and memorial data for ceremony planning and site maintenance.
  name: Memorial Planning
website: https://www.abmc.gov/
---
