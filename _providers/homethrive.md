---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homethrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://homethrive.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/homethrive-inc
- group: company
  title: ''
  type: Blog
  url: https://homethrive.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://homethrive.com/eligible-members/
created: '2026-07-03'
description: Homethrive is a technology-enabled caregiving-support benefit sold to employers, health plans, financial institutions, ancillary insurers, brokers, and platform partners. It pairs a digital assistant (Homethrive Dari) with human Care Guides to help family caregivers navigate backup care, aging, complex health, estate planning, and loss for their loved ones. Homethrive is a B2B2C member platform - it is delivered to covered members through their employer or health plan, not as a self-serve product. There is no public or partner developer API, API reference, or developer portal. Customer integration is handled during enterprise onboarding via an eligibility-file specification (typically SFTP/CSV batch files) and Single Sign-On (SSO), with utilization and engagement data returned to the sponsor - all arranged through implementation, not a documented self-service API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homethrive.png
layout: provider
modified: '2026-07-03'
name: Homethrive
nav: Providers
network: true
overview: 'Homethrive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Caregiving, Family Caregivers, Employee Benefits, Health Plans, and Elder Care.


  Homethrive''s developer surface includes engineering blog, signup flow, and 3 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homethrive/refs/heads/main/screenshots/homethrive-2026-07-25T221345.png
security:
- kind: domain-security
  name: Homethrive Domain Security
  slug: homethrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: homethrive
tags:
- Caregiving
- Family Caregivers
- Employee Benefits
- Health Plans
- Elder Care
- Back-Up Care
- Caregiver Support
- Digital Health
- B2B2C
- No Public API
website: https://homethrive.com
---
