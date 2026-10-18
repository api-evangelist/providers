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
api_count: 1
apis:
- description: Readly provides a digital magazine subscription service; the API documentation is referenced on their developers page.
  name: Readly API
  slug: readly-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/readly/refs/heads/main/security/readly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/readly-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/readly/refs/heads/main/hosts/readly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/readly-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/readly/refs/heads/main/security/readly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/readly-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/readly/refs/heads/main/security/readly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/readly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://readly.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://readly.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: 'Readly is a company surfaced via the API Evangelist harvest backlog (source: stockholm-trip) and added to the network as a stub for full-pipeline profiling.'
image: https://s3-eu-west-1.amazonaws.com/public.readly.com/local_images/refer_a_friend_winter_2020/gb.jpg
layout: provider
modified: '2026-10-14'
name: Readly
nav: Providers
network: true
overview: Readly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 3
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Readly Domain Security
  slug: readly-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Readly Vulnerability Disclosure
  slug: readly-vulnerability-disclosure
  summary_line: no policy recorded
slug: readly
tags:
- Company
website: https://readly.com/
---
