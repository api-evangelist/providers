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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation is available at the provider's docs site.
  name: One Identity API
  slug: one-identity-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oneidentity/refs/heads/main/hosts/oneidentity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oneidentity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oneidentity/refs/heads/main/vendors/oneidentity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oneidentity-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oneidentity/refs/heads/main/packages/oneidentity-packages.yml
  title: ''
  type: SDKs
  url: packages/oneidentity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oneidentity/refs/heads/main/packages/oneidentity-packages.yml
  title: ''
  type: Packages
  url: packages/oneidentity-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.oneidentity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oneidentity.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneIdentity
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oneidentity/refs/heads/main/security/oneidentity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oneidentity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oneidentity.com
coverage:
  checked: '2026-10-04'
  detail: Docs site returns only a JavaScript shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 202
    url: https://docs.oneidentity.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: 'One Identity is a company surfaced via the API Evangelist harvest backlog (source: gartner-mq) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-03'
name: One Identity
nav: Providers
network: true
overview: 'One Identity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  One Identity''s developer surface includes documentation and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 42.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oneidentity Domain Security
  slug: oneidentity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oneidentity
tags:
- Company
website: https://www.oneidentity.com
---
