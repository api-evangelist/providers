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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Core REST API for managing QRadar SIEM functionality including offenses, assets, rules, and searches.
  name: QRadar REST API
  slug: qradar-rest-api
- description: API for developing and managing QRadar apps and extensions.
  name: QRadar GUI App Framework API
  slug: qradar-gui-app-framework-api
artifact_total: 7
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qradar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qradar-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/qradar-common
- group: auth
  title: ''
  type: Authentication
  url: https://www.ibm.com/docs/en/qradar-common?topic=api-authentication-methods
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ibm.com/cloud/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibm.com/privacy
- group: operate
  title: ''
  type: Community
  url: https://community.ibm.com/community/user/security/communities/community-home?CommunityKey=d0b01247-b4d8-4466-8605-dc5c7d30c58f
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/security/qradar
created: '2024-01-01'
description: IBM QRadar is a security information and event management (SIEM) platform that provides real-time monitoring, threat detection, and security analytics capabilities through comprehensive REST APIs.
finops:
- name: Qradar Finops
  service_category: API
  slug: qradar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qradar.png
layout: provider
modified: '2026-08-21'
name: IBM QRadar Security Intelligence Platform
nav: Providers
network: true
overview: 'IBM QRadar Security Intelligence Platform publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Log Management, Security, SIEM, and Threat Detection.


  IBM QRadar Security Intelligence Platform''s developer surface includes documentation, authentication, support, and 8 more developer resources.'
plans:
- name: Qradar Plans Pricing
  plan_count: 3
  slug: qradar-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Qradar Rate Limits
  slug: qradar-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 20.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qradar/refs/heads/main/screenshots/qradar-2026-06-20T192355.png
security:
- kind: domain-security
  name: Qradar Domain Security
  slug: qradar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qradar Vulnerability Disclosure
  slug: qradar-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: qradar
tags:
- Analytics
- Log Management
- Security
- SIEM
- Threat Detection
website: https://www.ibm.com/security/qradar
---
