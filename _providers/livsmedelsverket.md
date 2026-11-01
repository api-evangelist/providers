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
  href: https://artifacts.apis.io/livsmedelsverket/hosts/livsmedelsverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livsmedelsverket-hosts.yml
- group: other
  href: https://artifacts.apis.io/livsmedelsverket/vendors/livsmedelsverket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/livsmedelsverket-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.livsmedelsverket.se/om-oss/press/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.livsmedelsverket.se/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Livsmedelsverket
- group: auth
  href: https://artifacts.apis.io/livsmedelsverket/security/livsmedelsverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livsmedelsverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livsmedelsverket.se/
coverage:
  checked: '2026-10-26'
  detail: The provider's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.livsmedelsverket.se
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Livsmedelsverket, the Swedish Food Agency, is a government authority responsible for food safety, nutrition, and consumer information in Sweden. It develops regulations, conducts research, and provides guidance to ensure safe and healthy food for the public, covering areas such as food labeling, contaminants, and dietary advice.
layout: provider
modified: '2026-10-26'
name: Livsmedelsverket (Swedish Food Agency)
nav: Providers
network: true
overview: 'Livsmedelsverket (Swedish Food Agency) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Food Safety, Nutrition, and Sweden.


  Livsmedelsverket (Swedish Food Agency)''s developer surface includes documentation and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Livsmedelsverket Domain Security
  slug: livsmedelsverket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livsmedelsverket
tags:
- Company
- Government
- Food Safety
- Nutrition
- Sweden
website: https://www.livsmedelsverket.se/
---
