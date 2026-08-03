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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The ASCE Hazard Tool API provides a simple interface to query locations in the United States for environmental hazard data by geographic location. It provides site-specific hazard values used in struc
  name: ASCE Hazard Tool API
  slug: hazard-tool-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asce-amplify-domain-security.yml
- group: start
  title: ASCE Amplify Platform
  type: Portal
  url: https://amplify.asce.org/
- group: start
  title: ASCE Website
  type: Portal
  url: https://www.asce.org/
created: '2025-02-17'
description: ASCE Amplify is a platform created by the American Society of Civil Engineers (ASCE) that provides civil engineering data and advocacy tools. The platform includes the ASCE Hazard Tool API, which provides a simple interface to query locations in the United States for environmental hazard data by geographic location. The Hazard Tool API covers seismic, wind, snow, ice, flood, and other environmental hazard loads used in structural design per ASCE standards. ASCE Amplify also supports advocacy, connecting civil engineers with elected officials to advocate for infrastructure investment and sustainable practices.
features:
- description: Query any US location by latitude and longitude or address to retrieve site-specific environmental hazard values for structural design, including ASCE 7 seismic, wind, snow, and ice parameters.
  name: Geographic Hazard Lookup
- description: Retrieve seismic design parameters including Ss, S1, SMS, SM1, SDS, SD1, and spectral acceleration values per ASCE 7 for any US location.
  name: ASCE 7 Seismic Parameters
- description: Access design wind speed values for various risk categories and exposure categories per ASCE 7 for structural wind load calculations.
  name: Wind Speed Data
- description: Retrieve ground snow load values and ice storm data for design of roof structures and overhead transmission lines per ASCE 7.
  name: Snow and Ice Load Data
- description: Tools for ASCE members to contact elected officials and advocate for infrastructure funding, engineering standards, and professional issues.
  name: Civil Engineer Advocacy
finops:
- name: Asce Amplify Finops
  service_category: API
  slug: asce-amplify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asce-amplify.png
integrations:
- description: API values directly correspond to ASCE 7 Minimum Design Loads for Buildings and Other Structures, the primary reference standard for US structural engineering.
  name: ASCE 7 Standards
- description: Hazard parameters from the API align with International Building Code requirements that reference ASCE 7 for environmental load design values.
  name: IBC Building Codes
layout: provider
modified: '2026-04-19'
name: ASCE Amplify
nav: Providers
network: true
overview: 'ASCE Amplify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Civil Engineering, Hazard Data, Engineering Standards, and Infrastructure.


  ASCE Amplify''s developer surface includes developer portal and 2 more developer resources.'
plans:
- name: Asce Amplify Plans Pricing
  plan_count: 3
  slug: asce-amplify-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Asce Amplify Rate Limits
  slug: asce-amplify-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asce-amplify/refs/heads/main/screenshots/asce-amplify-2026-06-20T172456.png
security:
- kind: domain-security
  name: Asce Amplify Domain Security
  slug: asce-amplify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asce-amplify
tags:
- Civil Engineering
- Hazard Data
- Engineering Standards
- Infrastructure
use_cases:
- description: Structural engineers use the ASCE Hazard Tool API to obtain site-specific hazard parameters for building and infrastructure design in compliance with ASCE 7 and building codes.
  name: Structural Design
- description: Civil engineers perform preliminary site assessments for new construction projects by querying multiple locations for hazard comparisons.
  name: Site Assessment
- description: Structural engineering software vendors integrate the ASCE Hazard Tool API to automatically populate design parameters based on project location.
  name: Software Integration
website: https://amplify.asce.org/
---
