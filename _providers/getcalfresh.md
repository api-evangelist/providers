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
  url: security/getcalfresh-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codeforamerica
- group: company
  title: ''
  type: Website
  url: https://www.getcalfresh.org
created: '2026-07-03'
description: GetCalFresh is a service delivered by Code for America on behalf of the people of California, providing plain-language guidance to help Californians understand and navigate CalFresh (SNAP) food benefits. Since California's statewide move to BenefitsCal.com on the CalSAWS platform, GetCalFresh.org no longer accepts applications directly - it is an informational and guidance site that hands off to BenefitsCal and county agencies for eligibility determination and case processing. No public developer API is documented; historically, before BenefitsCal existed, Code for America's application tooling submitted CalFresh applications to county systems via generated PDF forms, fax, and secure email rather than a documented API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getcalfresh.png
layout: provider
modified: '2026-07-03'
name: GetCalFresh
nav: Providers
network: true
overview: GetCalFresh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Civic Tech, Non-Profit, Government, Public Benefits, and SNAP.
random_paper: 5
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getcalfresh/refs/heads/main/screenshots/getcalfresh-2026-07-25T215723.png
security:
- kind: domain-security
  name: Getcalfresh Domain Security
  slug: getcalfresh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getcalfresh
tags:
- Civic Tech
- Non-Profit
- Government
- Public Benefits
- SNAP
- Food Assistance
- California
website: https://www.getcalfresh.org
---
