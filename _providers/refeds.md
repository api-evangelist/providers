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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/refeds/refs/heads/main/hosts/refeds-hosts.yml
  title: ''
  type: Hosts
  url: hosts/refeds-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/refeds/refs/heads/main/vendors/refeds-vendors.yml
  title: ''
  type: Vendors
  url: vendors/refeds-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://refeds.org/metadata/contacttype/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://refeds.org/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/REFEDS
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/refeds/refs/heads/main/security/refeds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/refeds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://refeds.org/
- group: company
  title: ''
  type: Blog
  url: https://refeds.org/blog
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.refeds.org
- group: docs
  title: ''
  type: Specifications
  url: https://refeds.org/specifications
- group: operate
  title: ''
  type: Support
  url: https://lists.refeds.org/sympa/subscribe/refeds
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://refeds.org/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: REFEDS (Research and Education FEDerations) is a community-driven organization that serves as the collective voice for research and education identity federations worldwide. It facilitates collaboration, policy development, and technical guidance on identity management, inter‑federation, privacy, and assurance. Through working groups, meetings, and extensive documentation, REFEDS supports participants in developing secure, interoperable identity solutions across the global research and education ecosystem.
layout: provider
modified: '2026-10-13'
name: REFEDS
nav: Providers
network: true
overview: 'REFEDS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Federation, Research, and Education.


  REFEDS''s developer surface includes engineering blog, documentation, support, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Refeds Domain Security
  slug: refeds-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: refeds
tags:
- Company
- Identity
- Federation
- Research
- Education
website: https://refeds.org/
---
