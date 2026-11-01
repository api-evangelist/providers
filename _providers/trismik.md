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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Trismik provides data comparison tools as described in the QuickCompare SDK documentation.
  name: Trismik API
  slug: trismik-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/trismik/hosts/trismik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trismik-hosts.yml
- group: other
  href: https://artifacts.apis.io/trismik/vendors/trismik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trismik-vendors.yml
- group: build
  href: https://artifacts.apis.io/trismik/packages/trismik-packages.yml
  title: ''
  type: SDKs
  url: packages/trismik-packages.yml
- group: build
  href: https://artifacts.apis.io/trismik/packages/trismik-packages.yml
  title: ''
  type: Packages
  url: packages/trismik-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.trismik.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trismik.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trismik.com/privacy_policy.html
- group: company
  title: ''
  type: Blog
  url: https://blog.trismik.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trismik.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trismik
- group: auth
  href: https://artifacts.apis.io/trismik/security/trismik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trismik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trismik.com/
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.trismik.com/quickcompare/sdk/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: 'Trismik is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://trismik.com/social-card.png
layout: provider
modified: '2026-10-19'
name: Trismik
nav: Providers
network: true
overview: 'Trismik is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Trismik''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Trismik Domain Security
  slug: trismik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trismik
tags:
- Company
website: https://trismik.com/
---
