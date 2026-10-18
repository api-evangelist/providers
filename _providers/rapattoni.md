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
- description: RETS and RESO Web API access to Rapattoni-hosted MLS listing data for licensed third parties. The developer pages are geo-restricted and were not readable from this pass; no base URL is recorded.
  name: Rapattoni MLS Data Services (RETS / RESO Web API)
  slug: mls-data-services
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rapattoni/refs/heads/main/hosts/rapattoni-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rapattoni-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rapattoni
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rapattoni/refs/heads/main/security/rapattoni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rapattoni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rapattoni.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rapattoni.com/dev/665-dev_change_log_rets
created: '2026-10-13'
description: Rapattoni Corporation is a California-based provider of multiple listing service (MLS), association management, accounting and REALTOR association software for boards and MLSs in the United States. It maintains a developer section on rapattoni.com (/dev/) covering its RETS data service and change log and a RESO Web API section for licensed third-party data access to MLS listing data. The rapattoni.com site geo-blocks non-US traffic and returned 403 to every probe in this pass, so no endpoint, base URL or machine-readable contract could be verified; the record holds only what was observable.
layout: provider
modified: '2026-10-13'
name: Rapattoni
nav: Providers
network: true
overview: 'Rapattoni is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, MLS, RESO Web API, and RETS.


  Rapattoni''s developer surface includes documentation and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 21.1
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
  name: Rapattoni Domain Security
  slug: rapattoni-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rapattoni
tags:
- Company
- Real Estate
- MLS
- RESO Web API
- RETS
- Association Management
website: https://rapattoni.com/
---
