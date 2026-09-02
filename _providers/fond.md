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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fond-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fond.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fond.co/resources/our-public-api/
- group: company
  title: ''
  type: Blog
  url: https://www.fond.co/blog/
created: '2026-07-17'
description: Fond (formerly AnyPerk) is a U.S. employee rewards and recognition platform that lets companies run customizable recognition programs combining monetary and non-monetary rewards, perks, and a global rewards catalog. Fond offers a gated public/provider API that allows authenticated partners to programmatically manage a Fond account — provisioning, employee roster management, giving recognition to one or more employees, and rewards redemption — alongside integrations for Workday, ADP, Namely, Salesforce, Slack, and other HR systems. There is no open developer portal or published OpenAPI; API access is arranged directly via integration@fond.co. Fond was acquired by Reward Gateway in March 2023 and fond.co now redirects to rewardgateway.com. Originally added to the API Evangelist network as a portfolio lead of DCM Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fond.png
layout: provider
modified: '2026-07-19'
name: Fond
nav: Providers
network: true
overview: 'Fond is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Employee Recognition, Rewards, and Human Resources.


  Fond''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fond/refs/heads/main/screenshots/fond-2026-07-25T214919.png
security:
- kind: domain-security
  name: Fond Domain Security
  slug: fond-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fond
tags:
- Company
- Enterprise
- Employee Recognition
- Rewards
- Human Resources
- Employee Engagement
- Perks
website: https://fond.co/
---
