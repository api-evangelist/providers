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
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: REST APIs for the Ivanti Neurons platform covering inventory, patch management, and bots.
  name: Ivanti Neurons for People and Devices
  slug: neurons-people-devices
- description: REST API for Ivanti Neurons for MDM, providing programmatic access to mobile device management capabilities.
  name: Ivanti Neurons for MDM
  slug: neurons-mdm
- description: REST API for Ivanti Neurons for ITSM, exposing IT service management data and operations.
  name: Ivanti Neurons for ITSM
  slug: neurons-itsm
- description: REST API for Ivanti Neurons for Zero-Trust Access, providing programmatic configuration of zero-trust policies.
  name: Ivanti Neurons for Zero-Trust Access
  slug: neurons-zta
- description: Patch and software distribution APIs for Ivanti Endpoint Manager (EPM).
  name: Ivanti Endpoint Manager
  slug: endpoint-manager
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ivanti-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ivanti-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ivanti
- group: company
  title: ''
  type: Website
  url: https://www.ivanti.com
- group: operate
  title: ''
  type: API Support
  url: https://www.ivanti.com/support/api
- group: other
  title: ''
  type: Resources
  url: https://www.ivanti.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.ivanti.com/blog/rss
created: '2026-03-27'
description: Ivanti is an IT asset management and security platform providing unified endpoint management, patch management, and IT service management. The Ivanti Neurons product family exposes REST APIs across People & Devices, MDM, ITSM, and Zero-Trust Access, alongside Endpoint Manager APIs for patch and software distribution.
finops:
- name: Ivanti Finops
  service_category: API
  slug: ivanti-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ivanti.png
layout: provider
modified: '2026-04-28'
name: Ivanti
nav: Providers
network: true
overview: 'Ivanti publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Endpoint Management, IT Asset Management, IT Service Management, Patch Management, and Mobile Device Management.


  Ivanti''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Ivanti Plans Pricing
  plan_count: 3
  slug: ivanti-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Ivanti Rate Limits
  slug: ivanti-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ivanti/refs/heads/main/screenshots/ivanti-2026-06-20T183639.png
security:
- kind: domain-security
  name: Ivanti Domain Security
  slug: ivanti-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ivanti Vulnerability Disclosure
  slug: ivanti-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ivanti
tags:
- Endpoint Management
- IT Asset Management
- IT Service Management
- Patch Management
- Mobile Device Management
- Zero Trust
website: https://www.ivanti.com
---
