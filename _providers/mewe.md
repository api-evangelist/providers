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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/mewe/hosts/mewe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mewe-hosts.yml
- group: other
  href: https://artifacts.apis.io/mewe/vendors/mewe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mewe-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.mewe.com/hc/en-us
- group: company
  title: ''
  type: Newsroom
  url: https://about.mewe.com/category/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sgrouples/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mewe.com/quickstart
- group: auth
  href: https://artifacts.apis.io/mewe/security/mewe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mewe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mewe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mewe.com/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://mewe.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://mewe.com/api-docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mewe.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mewe.com/privacy
created: '2026-10-26'
description: MeWe is a social networking platform focused on privacy and user control, offering ad‑free communication, groups, and content sharing. It emphasizes no targeted ads, no spyware, and robust privacy settings, positioning itself as a next‑gen alternative to mainstream social media.
image: https://cdn.mewe.com/assets/images/logos/mewe-512.jpg
layout: provider
modified: '2026-10-26'
name: MeWe
nav: Providers
network: true
overview: 'MeWe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Privacy, Networking, and Communication.


  MeWe''s developer surface includes support, getting-started guide, documentation, API reference, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mewe Domain Security
  slug: mewe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mewe
tags:
- Company
- Social
- Privacy
- Networking
- Communication
website: https://mewe.com/
---
