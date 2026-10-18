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
  href: https://raw.githubusercontent.com/api-evangelist/shibboleth-consortium/refs/heads/main/hosts/shibboleth-consortium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shibboleth-consortium-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.shibboleth.net/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shibboleth
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shibboleth-consortium/refs/heads/main/security/shibboleth-consortium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shibboleth-consortium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shibboleth.net/
created: '2026-10-13'
description: Shibboleth Consortium is a non-profit organization that supports the development, maintenance, and promotion of the Shibboleth open‑source software suite for federated identity and single sign‑on. It provides governance, community coordination, and resources for the Shibboleth Identity Provider, Service Provider, and related tools, ensuring long‑term sustainability and interoperability across academic, research, and enterprise environments.
image: https://www.shibboleth.net/wp-content/uploads/2020/11/shibboleth-share.jpg
layout: provider
modified: '2026-10-13'
name: Shibboleth Consortium
nav: Providers
network: true
overview: 'Shibboleth Consortium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Organization, Identity, Federation, and Open Source.


  Shibboleth Consortium''s developer surface includes support and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Shibboleth Consortium Domain Security
  slug: shibboleth-consortium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shibboleth-consortium
tags:
- Company
- Organization
- Identity
- Federation
- Open Source
- NonProfit
website: https://www.shibboleth.net/
---
