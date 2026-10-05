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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akili/refs/heads/main/hosts/akili-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akili-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akili/refs/heads/main/vendors/akili-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akili-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.akiliinteractive.com/terms-of-use
- group: start
  title: ''
  type: Sandbox
  url: https://www.akiliinteractive.com/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.akiliinteractive.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.akiliinteractive.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akili/refs/heads/main/security/akili-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akili-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akiliinteractive.com/
created: '2026-09-24'
description: Akili creates digital medicines delivered as video game experiences for people with cognitive impairments. It offers EndeavorOTC™, a game‑based treatment for adults with ADHD, and EndeavorRx®, an FDA‑authorized prescription video game for children with ADHD. The products are available through app stores and require a prescription for use.
image: http://static1.squarespace.com/static/5a0457fa18b27dc7e8aef79b/t/5be303a303ce646801a1e90b/1541604261020/og-share.jpg?format=1500w
layout: provider
modified: '2026-09-24'
name: Akili
nav: Providers
network: true
overview: 'Akili is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Medicine, ADHD, cognitive impairment, and Neuroscience.


  Akili''s developer surface includes sandbox and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 41.7
    operational_transparency: 0.0
  previous_composite: 9.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Akili Domain Security
  slug: akili-domain-security
  summary_line: TLSv1.3 · DMARC
slug: akili
tags:
- Digital Medicine
- ADHD
- cognitive impairment
- Neuroscience
website: https://www.akiliinteractive.com/
---
