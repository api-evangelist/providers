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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eaglevirtual/refs/heads/main/hosts/eaglevirtual-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eaglevirtual-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eaglevirtual/refs/heads/main/vendors/eaglevirtual-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eaglevirtual-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eaglevirtual.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://eaglevirtual.com/status
- group: auth
  title: ''
  type: Security
  url: https://eaglevirtual.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eaglevirtual.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://eaglevirtual.com/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eaglevirtual/refs/heads/main/security/eaglevirtual-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eaglevirtual-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eaglevirtual/refs/heads/main/security/eaglevirtual-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eaglevirtual-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eaglevirtual.com/
- group: docs
  title: ''
  type: Documentation
  url: https://eaglevirtual.com/api
created: '2026-09-28'
description: 'Eagle Virtual is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://eaglevirtual.com/static/images/og-default.png
layout: provider
modified: '2026-09-28'
name: Eagle Virtual
nav: Providers
network: true
overview: 'Eagle Virtual is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Eagle Virtual''s developer surface includes pricing, documentation, and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 30.4
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eaglevirtual Domain Security
  slug: eaglevirtual-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eaglevirtual Vulnerability Disclosure
  slug: eaglevirtual-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eaglevirtual
tags:
- Company
website: https://eaglevirtual.com/
---
