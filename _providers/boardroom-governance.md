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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Boardroom Governance API helps developers fetch and display governance data across DAOs and networks. Provides access to governance protocols, proposals, votes, voters, and delegation data for dec
  name: Boardroom Governance API
  slug: boardroom-governance-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boardroom-governance/refs/heads/main/plans/boardroom-governance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boardroom-governance-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/boardroom-governance/refs/heads/main/rate-limits/boardroom-governance-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/boardroom-governance-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boardroom-governance/refs/heads/main/finops/boardroom-governance-finops.yml
  title: ''
  type: FinOps
  url: finops/boardroom-governance-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://boardroom.io/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boardroom-governance/refs/heads/main/security/boardroom-governance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardroom-governance-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boardroom-inc
- group: company
  title: ''
  type: Website
  url: https://boardroom.io
- group: start
  title: ''
  type: Portal
  url: https://boardroom.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boardroom.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.boardroom.io/docs/getting-started
- group: other
  title: ''
  type: Glossary
  url: https://docs.boardroom.io/docs/glossary
- group: agent
  title: ''
  type: LlmsText
  url: https://boardroom.io/llms.txt
created: '2024-03-30'
description: Boardroom is a governance aggregation platform that helps developers fetch and display governance data across DAOs and decentralized networks. The Boardroom Governance API provides access to proposals, votes, protocols, and voter data for Web3 governance applications.
finops:
- has_sources: false
  method: generated
  name: Boardroom Governance Finops
  primary_unit: ''
  service_category: API
  slug: boardroom-governance-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boardroom-governance.png
layout: provider
modified: '2026-10-06'
name: Boardroom Governance
nav: Providers
network: true
overview: 'Boardroom Governance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Governance, DAO, Web3, and Decentralized.


  Boardroom Governance''s developer surface includes engineering blog, developer portal, documentation, getting-started guide, and 8 more developer resources.'
plans:
- name: Boardroom Governance Plans Pricing
  plan_count: 3
  slug: boardroom-governance-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Boardroom Governance Rate Limits
  slug: boardroom-governance-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/boardroom-governance/refs/heads/main/screenshots/boardroom-governance-2026-06-20T173549.png
security:
- kind: domain-security
  name: Boardroom Governance Domain Security
  slug: boardroom-governance-domain-security
  summary_line: TLSv1.3 · HSTS
slug: boardroom-governance
tags:
- Blockchain
- Governance
- DAO
- Web3
- Decentralized
website: https://boardroom.io
---
