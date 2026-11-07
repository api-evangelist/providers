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
    error_semantics: derived
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MinIO Browser UI hosted at pymedusa.com.
  name: MinIO Browser
  slug: minio-browser
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/pymedusa/rules/pymedusa-rules.yml
  title: ''
  type: Spectral
  url: rules/pymedusa-rules.yml
- group: design
  href: https://artifacts.apis.io/pymedusa/data-model/pymedusa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pymedusa-data-model.yml
- group: design
  href: https://artifacts.apis.io/pymedusa/conventions/pymedusa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pymedusa-conventions.yml
- group: design
  href: https://artifacts.apis.io/pymedusa/errors/pymedusa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pymedusa-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pymedusa/conformance/pymedusa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pymedusa-conformance.yml
- group: other
  href: https://artifacts.apis.io/pymedusa/hosts/pymedusa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pymedusa-hosts.yml
- group: other
  href: https://artifacts.apis.io/pymedusa/vendors/pymedusa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pymedusa-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://pymedusa.com/
- group: auth
  href: https://artifacts.apis.io/pymedusa/security/pymedusa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pymedusa-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pymedusa
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pymedusa/Medusa#readme
- group: operate
  title: ''
  type: Support
  url: https://github.com/pymedusa/Medusa/issues
coverage:
  checked: '2026-10-28'
  detail: The provider's site hosts a MinIO Browser UI but does not publish any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://pymedusa.com/minio/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Medusa (TV) is an open-source automated video library manager designed for TV show enthusiasts. It continuously monitors your favorite series for new episodes, automatically downloading, organizing, and renaming them according to your preferences. Built with Python, it integrates with popular indexers, download clients, and media servers, providing a seamless experience for keeping your collection up to date without manual effort.
image: https://avatars.githubusercontent.com/u/16712498?v=4
layout: provider
modified: '2026-10-28'
name: Medusa (TV)
nav: Providers
network: true
overview: 'Medusa (TV) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, TV, Media, Automation, and Open Source.


  The Medusa (TV) catalog on APIs.io includes 1 Spectral governance ruleset.


  Medusa (TV)''s developer surface includes documentation, support, and 10 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 0
  name: Pymedusa Rate Limits
  slug: pymedusa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Medusa (TV) API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: pymedusa-rules
scopes:
- name: Pymedusa Scopes
  scope_count: 0
  slug: pymedusa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pymedusa/pymedusa-2026-11-03T141846.png
security:
- kind: authentication
  name: Pymedusa Authentication
  slug: pymedusa-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pymedusa Domain Security
  slug: pymedusa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pymedusa
tags:
- Company
- TV
- Media
- Automation
- Open Source
- Python
website: https://pymedusa.com/
---
