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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/mersana/llms/mersana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mersana-llms.txt
- group: agent
  href: https://artifacts.apis.io/mersana/well-known/mersana-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mersana-well-known.yml
- group: other
  href: https://artifacts.apis.io/mersana/hosts/mersana-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mersana-hosts.yml
- group: other
  href: https://artifacts.apis.io/mersana/vendors/mersana-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mersana-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mersana/security/mersana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mersana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dayonebio.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.dayonebio.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dayonebio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dayonebio.com/privacy-notice
- group: operate
  title: ''
  type: Support
  url: https://www.dayonebio.com/our-company/contact-us/
created: '2026-10-22'
description: Mersana is a biotechnology company focused on developing innovative therapies for pediatric and adult cancers. It aims to accelerate drug development through advanced platforms and collaborations, targeting unmet medical needs in oncology.
image: https://www.dayonebio.com/wp-content/uploads/2025/01/image-9.png
layout: provider
modified: '2026-10-22'
name: Mersana
nav: Providers
network: true
overview: 'Mersana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Oncology, Therapeutics, ClinicalTrials, and Company.


  Mersana''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.6
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
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mersana Domain Security
  slug: mersana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mersana
tags:
- Biotechnology
- Oncology
- Therapeutics
- ClinicalTrials
- Company
website: https://www.dayonebio.com
---
