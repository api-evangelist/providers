---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Useanything API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Useanything API
  slug: useanything-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/useanything/vendors/useanything-vendors.yml
  title: ''
  type: Vendors
  url: vendors/useanything-vendors.yml
- group: design
  href: https://artifacts.apis.io/useanything/rules/useanything-rules.yml
  title: ''
  type: Spectral
  url: rules/useanything-rules.yml
- group: design
  href: https://artifacts.apis.io/useanything/vocabulary/useanything-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/useanything-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/useanything/changelog/useanything-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/useanything-changelog.yml
- group: design
  href: https://artifacts.apis.io/useanything/conformance/useanything-conformance.yml
  title: ''
  type: Conformance
  url: conformance/useanything-conformance.yml
- group: other
  href: https://artifacts.apis.io/useanything/hosts/useanything-hosts.yml
  title: ''
  type: Hosts
  url: hosts/useanything-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.useanything.com/mobile/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.useanything.com/mobile/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mintplex-Labs
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.anythingllm.com/changelog/overview
- group: company
  title: ''
  type: Blog
  url: https://anythingllm.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anythingllm.com/setup/embedder-configuration/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useanything.com/
- group: company
  title: ''
  type: Website
  url: https://useanything.com/
- group: auth
  href: https://artifacts.apis.io/useanything/security/useanything-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/useanything-domain-security.yml
created: '2026-10-21'
description: Useanything is a placeholder company currently lacking publicly available documentation or a dedicated website. It appears in the API Evangelist harvest backlog without verifiable online presence, and no concrete API specifications or developer resources have been identified.
image: https://anythingllm.com/share-card.png
layout: provider
modified: '2026-10-21'
name: Useanything
nav: Providers
network: true
overview: 'Useanything is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Placeholder, API-Evangelist, Stub, and Unknown.


  The Useanything catalog on APIs.io includes 1 Spectral governance ruleset.


  Useanything''s developer surface includes changelog, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Useanything API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: useanything-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Useanything Domain Security
  slug: useanything-domain-security
  summary_line: TLSv1.3
slug: useanything
tags:
- Company
- Placeholder
- API-Evangelist
- Stub
- Unknown
website: https://useanything.com/
---
