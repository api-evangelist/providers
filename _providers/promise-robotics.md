---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/promise-robotics/hosts/promise-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promise-robotics-hosts.yml
- group: auth
  href: https://artifacts.apis.io/promise-robotics/security/promise-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promise-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.promiserobotics.com
- group: docs
  title: ''
  type: Documentation
  url: https://promiserobotics.com/about
- group: operate
  title: ''
  type: Support
  url: https://promiserobotics.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promiserobotics.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://news.promiserobotics.com
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.promiserobotics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Promise Robotics delivers advanced production capability as a service, integrating AI, robotics, and production intelligence for homebuilding. Their platform unites building intent, production planning, factory operations, and robotic execution, enabling faster, scalable home construction with significant cost and time savings.
image: https://promiserobotics.com/assets/social.jpg
layout: provider
modified: '2026-10-29'
name: Promise Robotics
nav: Providers
network: true
overview: 'Promise Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, AI, Homebuilding, and ConstructionTech.


  Promise Robotics'' developer surface includes documentation, support, engineering blog, and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Promise Robotics Domain Security
  slug: promise-robotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: promise-robotics
tags:
- Company
- Robotics
- AI
- Homebuilding
- ConstructionTech
website: https://www.promiserobotics.com
---
