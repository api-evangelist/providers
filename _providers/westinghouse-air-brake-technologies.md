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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: WabtecONE is Wabtec's digital intelligence platform enabling railroads and industrial operators to connect embedded devices and transmit operational data to the cloud for analysis. The platform provid
  name: WabtecONE Platform
  slug: wabtec-one
- description: RailConnect TMS is the backbone operational and inventory management system for railroads, providing first mile and last mile connectivity, increased visibility, and automation of day-to-day operation
  name: RailConnect Transportation Management System
  slug: railconnect-tms
- description: Wabtec's condition monitoring platform (FleetONE and CMMS - Condition Monitoring Management System) provides advanced data management for asset monitoring devices. The system integrates telematics dat
  name: Condition Monitoring and Fleet Management
  slug: condition-monitoring
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/westinghouse-air-brake-technologies-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wabtec
- group: company
  title: ''
  type: Website
  url: https://www.wabteccorp.com
- group: start
  title: ''
  type: Portal
  url: https://one.wabtec.com
- group: other
  title: ''
  type: DigitalIntelligence
  url: https://www.wabteccorp.com/digital-intelligence
- group: operate
  title: ''
  type: Support
  url: https://www.wabteccorp.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wabtec-corporation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wabteccorp.com/privacy-policy
description: Westinghouse Air Brake Technologies Corporation (Wabtec) is a leading global provider of equipment, systems, digital solutions, and value-added services for the freight rail and passenger transit industries. Wabtec's digital platform, WabtecONE, delivers cloud and on-premise solutions for fleet management, condition monitoring, transportation management (RailConnect TMS), performance analytics, predictive maintenance, and signaling. Wabtec provides B2B API integrations for railroad operators, mines, ports, and transit agencies to connect their operations with the WabtecONE platform.
finops:
- name: Westinghouse Air Brake Technologies Finops
  service_category: API
  slug: westinghouse-air-brake-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/westinghouse-air-brake-technologies.png
json_schemas:
- name: Locomotive
  property_count: 14
  slug: westinghouse-air-brake-technologies-locomotive
- name: Work Order
  property_count: 15
  slug: westinghouse-air-brake-technologies-work-order
json_structures:
- name: Westinghouse Air Brake Technologies Locomotive Structure
  property_count: 0
  slug: westinghouse-air-brake-technologies-locomotive-structure
jsonld:
- class_count: 0
  name: Westinghouse Air Brake Technologies Context
  property_count: 21
  slug: westinghouse-air-brake-technologies-context
layout: provider
modified: '2026-05-03'
name: Westinghouse Air Brake Technologies Corporation
nav: Providers
network: true
overview: 'Westinghouse Air Brake Technologies Corporation publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000.


  The Westinghouse Air Brake Technologies Corporation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Westinghouse Air Brake Technologies Corporation''s developer surface includes developer portal, support, and 6 more developer resources.'
plans:
- name: Westinghouse Air Brake Technologies Plans Pricing
  plan_count: 3
  slug: westinghouse-air-brake-technologies-plans-pricing
press:
- date: '2026-05-25'
  title: Westinghouse Air Brake Technologies Corporation
  url: https://www.fitchratings.com/research/corporate-finance/westinghouse-air-brake-technologies-corporation-10-02-2025
- date: '2026-05-25'
  title: Westinghouse Air Brake Technologies Corp. (WAB)
  url: https://ir.wabteccorp.com/static-files/ab33037d-07b6-463c-ac5b-6ac03458a364
- date: '2026-05-25'
  title: Westinghouse Air Brake Technologies Corporation (WAB)
  url: https://finance.yahoo.com/news/westinghouse-air-brake-technologies-corporation-010847021.html
- date: '2026-05-25'
  title: Annual Report for Fiscal Year Ending December 31, 2024 ...
  url: https://www.publicnow.com/view/51C109988EB19FEAF0C1AF917ABF20F56E184D5E?1739393331
- date: '2026-05-25'
  title: Westinghouse Air Brake Technologies Corp (NYSE:WAB) ...
  url: https://www.proactiveinvestors.com/NYSE:WAB/Westinghouse-Air-Brake-Technologies-Corp
random_paper: 20
rate_limits:
- limit_count: 5
  name: Westinghouse Air Brake Technologies Rate Limits
  slug: westinghouse-air-brake-technologies-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Westinghouse Air Brake Technologies Corporation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: westinghouse-air-brake-technologies-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 19.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/westinghouse-air-brake-technologies/refs/heads/main/screenshots/westinghouse-air-brake-technologies-2026-06-20T201407.png
security:
- kind: domain-security
  name: Westinghouse Air Brake Technologies Domain Security
  slug: westinghouse-air-brake-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: westinghouse-air-brake-technologies
tags:
- Fortune 1000
website: https://www.wabteccorp.com
---
