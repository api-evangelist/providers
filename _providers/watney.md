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
  href: https://artifacts.apis.io/watney/hosts/watney-hosts.yml
  title: ''
  type: Hosts
  url: hosts/watney-hosts.yml
- group: auth
  href: https://artifacts.apis.io/watney/security/watney-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/watney-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://watney.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://watney.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://watney.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://watney.com/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/watneyrobotics
coverage:
  checked: '2026-10-29'
  detail: All attempted OpenAPI spec URLs (e.g., https://watney.com/openapi.json) returned 404 or HTML pages, with no machine‑readable API contract found.
  evidence:
  - status: 404
    url: https://watney.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Watney Robotics is a forward‑looking robotics company that designs and manufactures autonomous hardware solutions for expanding human ambition in the physical world. Founded in 2023, the company focuses on integrating advanced AI, sensor fusion, and modular design to enable robots that can operate in diverse environments, from industrial settings to space exploration. Watney’s flagship platform empowers developers and engineers to build custom applications, leveraging open APIs and robust SDKs. The firm emphasizes safety, reliability, and scalability, aiming to accelerate the adoption of robotics across industries and accelerate humanity’s reach beyond Earth.
image: https://framerusercontent.com/images/OiK6O9nNJfYzho3p6FPqGT8dg.png
layout: provider
modified: '2026-10-29'
name: Watney
nav: Providers
network: true
overview: 'Watney is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Artificial Intelligence, Automation, and Space.


  Watney''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/watney/watney-2026-11-03T150005.png
security:
- kind: domain-security
  name: Watney Domain Security
  slug: watney-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: watney
tags:
- Company
- Robotics
- Artificial Intelligence
- Automation
- Space
website: https://watney.com/
---
