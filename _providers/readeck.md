---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Readeck provides a web service for saving, organizing, and revisiting articles, images, and videos.
  name: Readeck API
  slug: readeck-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/readeck/hosts/readeck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/readeck-hosts.yml
- group: auth
  href: https://artifacts.apis.io/readeck/security/readeck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/readeck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://readeck.org/
- group: company
  title: ''
  type: Blog
  url: https://readeck.org/en/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://readeck.org/en/docs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://readeck.org/en/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/readeck
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are served as HTML shells that load content via JavaScript, preventing machine‑readable extraction.
  evidence:
  - status: 200
    url: https://readeck.org/en/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Readeck is a web-based service that lets users save, organize, and revisit interesting articles, long‑read pieces, pictures, and videos. It offers features such as dynamic collections, full‑text search, highlighting, exporting content as e‑books, and personalized reading settings. Users can browse their saved content, create themed collections, and access them across devices, making it a powerful tool for content curation and personal knowledge management.
image: https://readeck.org/media/img/card-image.webp
layout: provider
modified: '2026-10-28'
name: Readeck
nav: Providers
network: true
overview: 'Readeck is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reading, Content Curation, Bookmarking, and Productivity.


  Readeck''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
plans:
- name: Readeck Plans Pricing
  plan_count: 0
  slug: readeck-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Readeck Rate Limits
  slug: readeck-rate-limits
scopes:
- name: Readeck Scopes
  scope_count: 0
  slug: readeck-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/readeck/readeck-2026-11-03T142015.png
security:
- kind: authentication
  name: Readeck Authentication
  slug: readeck-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Readeck Domain Security
  slug: readeck-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: readeck
tags:
- Company
- Reading
- Content Curation
- Bookmarking
- Productivity
website: https://readeck.org/
---
