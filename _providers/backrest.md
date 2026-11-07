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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Backrest provides a secure, web‑accessible backup solution with a Web UI for managing backups.
  name: Backrest API
  slug: backrest-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/backrest/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/backrest/well-known/backrest-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backrest-well-known.yml
- group: other
  href: https://artifacts.apis.io/backrest/hosts/backrest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backrest-hosts.yml
- group: other
  href: https://artifacts.apis.io/backrest/vendors/backrest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backrest-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backrest.org/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backrest.org/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://backrest.org/category/blog/
- group: auth
  href: https://artifacts.apis.io/backrest/security/backrest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backrest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backrest.org/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on the provider's hosts.
  evidence:
  - status: timeout
    url: https://api.backrest.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Backrest provides a secure, web‑accessible backup solution built on top of restic. It offers an intuitive Web UI for managing repositories, snapshots, and restores, with features like scheduling, repository health monitoring, and support for multiple storage backends such as S3, B2, Azure, and GCS. The platform simplifies backup workflows for both technical and non‑technical users, delivering encrypted, reliable backups through a lightweight Go binary.
image: https://backrest.org/wp-content/uploads/2026/03/cropped-Capture-removebg-preview-6.png
layout: provider
modified: '2026-10-28'
name: Backrest
nav: Providers
network: true
overview: 'Backrest is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Backup, Storage, Restic, Open Source, and Go.


  Backrest''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.6
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.4
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/backrest/backrest-2026-11-03T121514.png
security:
- kind: domain-security
  name: Backrest Domain Security
  slug: backrest-domain-security
  summary_line: TLSv1.3
slug: backrest
tags:
- Backup
- Storage
- Restic
- Open Source
- Go
website: https://backrest.org/
---
