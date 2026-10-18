---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation is presented on the Connect portal but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was discovered.
  name: Alter Learning API
  slug: alter-learning-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alter-learning/refs/heads/main/hosts/alter-learning-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alter-learning-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alter-learning.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alter-learning.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://alter-learning.com/media/
- group: start
  title: ''
  type: Login
  url: https://connect.alter-learning.com/login
- group: company
  title: ''
  type: Blog
  url: https://alter-learning.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alter-learning/refs/heads/main/security/alter-learning-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alter-learning-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alter-learning.com/
coverage:
  checked: '2026-10-05'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec could be found.
  evidence:
  - status: 200
    url: https://connect.alter-learning.com/market/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Alter Learning appears to be a private company with limited public presence. The domain alterlearning.com is currently for sale, and attempts to locate an official website or corporate information returned only marketplace listings on ForgeGlobal and no verifiable corporate site. No API documentation, developer portal, or official contact information could be found. The company may be a placeholder entry without an active online footprint.
image: https://alter-learning.com/wp-content/uploads/2024/05/Alter_Learning_Educational_Platform.webp
layout: provider
modified: '2026-09-24'
name: Alter Learning
nav: Providers
network: true
overview: 'Alter Learning is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include STEAM, Educational Games, Kids, Teachers, and Scientists.


  Alter Learning''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.5
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 5.3
  previous_composite: 1.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alter Learning Domain Security
  slug: alter-learning-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alter-learning
tags:
- STEAM
- Educational Games
- Kids
- Teachers
- Scientists
- Subscription
- Platform
website: https://alter-learning.com/
---
