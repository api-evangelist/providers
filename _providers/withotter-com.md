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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/withotter-com/hosts/withotter-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withotter-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/withotter-com/vendors/withotter-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withotter-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withotter.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withotter.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withotter
- group: auth
  href: https://artifacts.apis.io/withotter-com/security/withotter-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withotter-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withotter.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered API hosts.
  evidence:
  - status: 404
    url: https://api.withotter.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Otter is a technology company that provides a platform for managing and automating workflows across various business processes. The company focuses on integrating disparate systems, offering a unified interface for data synchronization, task orchestration, and real-time analytics. Backed by Sequoia Capital, Otter aims to simplify complex operational tasks for enterprises, enabling faster decision-making and improved efficiency through its robust API ecosystem and developer-friendly tools.
image: https://cdn.prod.website-files.com/6424ac4b25764708c6aa49f7/642e393ac0355a46d5c3f130_Otter%20OG%20Image.png
layout: provider
modified: '2026-10-29'
name: Otter
nav: Providers
network: true
overview: Otter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Workflows, and Integration.
random_paper: 22
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/withotter-com/withotter-com-2026-11-03T150213.png
security:
- kind: domain-security
  name: Withotter Com Domain Security
  slug: withotter-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withotter-com
tags:
- Company
- Automation
- Workflows
- Integration
website: https://withotter.com/
---
