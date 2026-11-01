---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'squiredocs-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: squiredocs-com API
  slug: squiredocs-com-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/squiredocs-com/rules/squiredocs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/squiredocs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/squiredocs-com/vocabulary/squiredocs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/squiredocs-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/squiredocs-com/security/squiredocs-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/squiredocs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/squiredocs-com/authentication/squiredocs-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/squiredocs-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/squiredocs-com/conformance/squiredocs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/squiredocs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/squiredocs-com/well-known/squiredocs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/squiredocs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/squiredocs-com/hosts/squiredocs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/squiredocs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/squiredocs-com/vendors/squiredocs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/squiredocs-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/squiredocs-com/security/squiredocs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/squiredocs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/squiredocs-com/security/squiredocs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/squiredocs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://squiredocs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://squiredocs.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://squiredocs.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://squiredocs.com/documentation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://squiredocs.com/about
- group: company
  title: ''
  type: Blog
  url: https://squiredocs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squiredocs
- group: operate
  title: ''
  type: Roadmap
  url: https://squiredocs.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://squiredocs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://squiredocs.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://squiredocs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://squiredocs.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://squiredocs.com/mcp
  - status: 200
    url: https://squiredocs.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Squire Docs is an open‑source collaborative document editor designed for people and AI agents to edit the same documents in real time. Every edit is attributed, and the platform provides two‑way markdown synchronization with your repository. Built by 21st Harmonic and released under the MIT license, Squire Docs can be used for free at squiredocs.com or self‑hosted on your own infrastructure. It supports real‑time collaboration, version history, and an API that lets coding agents or CI pipelines keep documents in sync with code repositories.
image: https://squiredocs.com/hero-screenshot.png
layout: provider
modified: '2026-10-31'
name: squiredocs-com
nav: Providers
network: true
overview: 'squiredocs-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, Collaboration, AI Agents, Real-time, and Documentation.


  The squiredocs-com catalog on APIs.io includes 1 Spectral governance ruleset.


  squiredocs-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: squiredocs-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: squiredocs-com-rules
scopes:
- name: Squiredocs Com Scopes
  scope_count: 0
  slug: squiredocs-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.7
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 38.0
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Squiredocs Com Authentication
  slug: squiredocs-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Squiredocs Com Domain Security
  slug: squiredocs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Squiredocs Com Vulnerability Disclosure
  slug: squiredocs-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: squiredocs-com
tags:
- Open Source
- Collaboration
- AI Agents
- Real-time
- Documentation
website: https://squiredocs.com/
---
