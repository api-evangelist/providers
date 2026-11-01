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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/openmediavault/changelog/openmediavault-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openmediavault-changelog.yml
- group: operate
  href: https://artifacts.apis.io/openmediavault/lifecycle/openmediavault-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/openmediavault-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/openmediavault/lifecycle/openmediavault-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openmediavault-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/openmediavault/hosts/openmediavault-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openmediavault-hosts.yml
- group: other
  href: https://artifacts.apis.io/openmediavault/vendors/openmediavault-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openmediavault-vendors.yml
- group: auth
  href: https://artifacts.apis.io/openmediavault/security/openmediavault-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openmediavault-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openmediavault.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openmediavault.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.openmediavault.org/install.html
- group: operate
  title: ''
  type: Support
  url: https://forum.openmediavault.org
- group: company
  title: ''
  type: Blog
  url: https://www.openmediavault.org/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openmediavault
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openmediavault.org/imprint.html
created: '2026-10-28'
description: OpenMediaVault provides a free, open‑source network attached storage (NAS) solution built on Debian Linux, enabling individuals and small businesses to store, share, and back up data on their own hardware. It offers a web‑based admin interface, extensible plugins, and features such as S.M.A.R.T., snapshots, and remote access, emphasizing data sovereignty and ease of use without requiring deep technical expertise.
image: https://www.openmediavault.org/favicon.ico
layout: provider
modified: '2026-10-28'
name: openmediavault
nav: Providers
network: true
overview: 'openmediavault is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, NAS, Open Source, Data Sovereignty, and Linux.


  openmediavault''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 0
  name: Openmediavault Rate Limits
  slug: openmediavault-rate-limits
scopes:
- name: Openmediavault Scopes
  scope_count: 0
  slug: openmediavault-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 28.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Openmediavault Authentication
  slug: openmediavault-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Openmediavault Domain Security
  slug: openmediavault-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openmediavault
tags:
- Company
- NAS
- Open Source
- Data Sovereignty
- Linux
website: https://www.openmediavault.org/
---
