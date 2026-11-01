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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/devrel-directory/changelog/devrel-directory-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/devrel-directory-changelog.yml
- group: agent
  href: https://artifacts.apis.io/devrel-directory/llms/devrel-directory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devrel-directory-llms.txt
- group: other
  href: https://artifacts.apis.io/devrel-directory/hosts/devrel-directory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devrel-directory-hosts.yml
- group: other
  href: https://artifacts.apis.io/devrel-directory/vendors/devrel-directory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devrel-directory-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devrel.directory/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://devrel.directory/changelog
- group: auth
  href: https://artifacts.apis.io/devrel-directory/security/devrel-directory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devrel-directory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devrel.directory/
- group: docs
  title: ''
  type: Documentation
  url: https://devrel.directory/docs
- group: company
  title: ''
  type: Blog
  url: https://devrel.directory/blog
coverage:
  detail: DevRel Directory is a knowledge base and does not expose a public API.
  evidence:
  - status: 200
    url: https://devrel.directory/docs
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: DevRel Directory is the central hub for developer relations professionals, offering a curated collection of guides, tools, community resources, job listings, and events. It serves as a comprehensive reference for building, scaling, and sustaining DevRel programs, providing practical advice, best practices, and up-to-date information on the evolving landscape of developer advocacy and community management.
image: https://devrel.directory/og?title=DevRel%20Directory
layout: provider
modified: '2026-10-30'
name: devrel-directory
nav: Providers
network: true
overview: 'devrel-directory is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Relations, Directory, Guides, and Jobs.


  devrel-directory''s developer surface includes changelog, documentation, engineering blog, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devrel Directory Domain Security
  slug: devrel-directory-domain-security
  summary_line: TLSv1.3 · HSTS
slug: devrel-directory
tags:
- Company
- Developer Relations
- Directory
- Guides
- Jobs
website: https://devrel.directory/
---
