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
    agentic_access: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-08-11'
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
modified: '2026-04-28'
name: IBM QRadar Security Intelligence Platform
nav: Providers
network: true
overview: 'IBM QRadar Security Intelligence Platform publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Log Management, Security, SIEM, and Threat Detection.


  IBM QRadar Security Intelligence Platform''s developer surface includes documentation, authentication, support, and 7 more developer resources.'
plans:
- name: Qradar Plans Pricing
  plan_count: 3
  slug: qradar-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Qradar Rate Limits
  slug: qradar-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: -7.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 28.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
