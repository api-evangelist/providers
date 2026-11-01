---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/george-mason-university/llms/george-mason-university-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/george-mason-university-llms.txt
- group: agent
  href: https://artifacts.apis.io/george-mason-university/well-known/george-mason-university-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/george-mason-university-well-known.yml
- group: other
  href: https://artifacts.apis.io/george-mason-university/hosts/george-mason-university-hosts.yml
  title: ''
  type: Hosts
  url: hosts/george-mason-university-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gmu.edu/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.gmu.edu/news
- group: start
  title: ''
  type: GettingStarted
  url: https://its.gmu.edu/help-support/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://help.gmu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CSISS
- group: auth
  href: https://artifacts.apis.io/george-mason-university/security/george-mason-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/george-mason-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://csiss.gmu.edu
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://csiss.gmu.edu
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: 'George Mason University is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-23'
name: George Mason University
nav: Providers
network: true
overview: 'George Mason University is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Research, Spatial Information, Academic, and Software.


  George Mason University''s developer surface includes getting-started guide, documentation, and 8 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 28.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: George Mason University Domain Security
  slug: george-mason-university-domain-security
  summary_line: DMARC
slug: george-mason-university
tags:
- Research
- Spatial Information
- Academic
- Software
website: http://csiss.gmu.edu
---
