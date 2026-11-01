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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/joaoapps-join/hosts/joaoapps-join-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joaoapps-join-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joaoapps.com/autoweb/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joaoapps.com/join/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://joaoapps.com/join/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://joaoapps.com/autoremote/eventghost/
- group: auth
  href: https://artifacts.apis.io/joaoapps-join/security/joaoapps-join-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joaoapps-join-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joaoapps.com/
coverage:
  checked: '2026-10-28'
  detail: Access to API specifications is blocked by a 403 response requiring authentication.
  evidence:
  - status: 403
    url: https://joaoapps.com/graphql
  reason: partner-login
  state: gated
created: '2026-10-28'
description: 'Join and Tasker (joaoapps) is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-28'
name: Join and Tasker (joaoapps)
nav: Providers
network: true
overview: 'Join and Tasker (joaoapps) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Join and Tasker (joaoapps)''s developer surface includes changelog, getting-started guide, and 5 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 26.8
    operational_transparency: 15.8
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
  name: Joaoapps Join Domain Security
  slug: joaoapps-join-domain-security
  summary_line: DMARC
slug: joaoapps-join
tags:
- Company
website: https://joaoapps.com/
---
