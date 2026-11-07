---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/pcloud/plans/pcloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pcloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/pcloud/changelog/pcloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pcloud-changelog.yml
- group: auth
  href: https://artifacts.apis.io/pcloud/authentication/pcloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pcloud-authentication.yml
- group: other
  href: https://artifacts.apis.io/pcloud/hosts/pcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pcloud-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.pcloud.com/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pCloud
- group: auth
  href: https://artifacts.apis.io/pcloud/security/pcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pcloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pcloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pcloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pcloud.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pcloud.com/methods/intro/
- group: operate
  title: ''
  type: Support
  url: https://help.pcloud.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.pcloud.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pcloud.com/cloud-storage-pricing-plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pcloud.com/terms_and_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pcloud.com/privacy_policy
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found after probing typical spec URLs.
  evidence:
  - status: 404
    url: https://api.pcloud.com/openapi.json
  - status: 200
    url: https://docs.pcloud.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: pCloud is a secure cloud storage and file sharing service that lets individuals and businesses store, sync, backup, and access their files from any device. It offers encrypted storage, collaborative sharing, automatic backup, and a suite of tools such as pCloud Transfer, pCloud Save, and pCloud Pass for enhanced security and productivity.
image: https://pcdn-www.pcloud.com/ZW7xd/images/logo/pcloud.svg
layout: provider
modified: '2026-10-28'
name: pCloud
nav: Providers
network: true
overview: 'pCloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, File Sync, Backup, Security, and Collaboration.


  pCloud''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 10 more developer resources.'
plans:
- name: Pcloud Plans Pricing
  plan_count: 6
  slug: pcloud-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Pcloud Rate Limits
  slug: pcloud-rate-limits
scopes:
- name: Pcloud Scopes
  scope_count: 0
  slug: pcloud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 33.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pcloud/pcloud-2026-11-03T141030.png
security:
- kind: authentication
  name: Pcloud Authentication
  slug: pcloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pcloud Domain Security
  slug: pcloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pcloud
tags:
- Cloud Storage
- File Sync
- Backup
- Security
- Collaboration
website: https://pcloud.com/
---
