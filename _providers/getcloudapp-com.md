---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/getcloudapp-com/hosts/getcloudapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getcloudapp-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/getcloudapp-com/security/getcloudapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getcloudapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcloudapp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://getcloudapp.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Zight is a technology company offering cloud-based solutions for managing and sharing digital assets. The platform enables users to upload, organize, and distribute files securely, with access controls, analytics, and integration capabilities. Zight simplifies digital asset management for businesses and individuals, supporting collaboration and secure sharing across devices and teams.
layout: provider
modified: '2026-10-21'
name: Zight
nav: Providers
network: true
overview: Zight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Asset Management, File Sharing, and Collaboration.
random_paper: 4
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getcloudapp Com Domain Security
  slug: getcloudapp-com-domain-security
  summary_line: DMARC
slug: getcloudapp-com
tags:
- Company
- Cloud
- Asset Management
- File Sharing
- Collaboration
website: https://getcloudapp.com
---
