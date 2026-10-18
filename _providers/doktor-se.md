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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doktor-se/refs/heads/main/llms/doktor-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doktor-se-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doktor-se/refs/heads/main/well-known/doktor-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doktor-se-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/doktor-se/refs/heads/main/hosts/doktor-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doktor-se-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/doktor-se/refs/heads/main/vendors/doktor-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doktor-se-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://doktor.se/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/doktor-se/refs/heads/main/security/doktor-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doktor-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doktor.se/
- group: docs
  title: ''
  type: Documentation
  url: https://doktor.se/om-oss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doktor.se/allmanna-villkor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doktor.se/integritetspolicy
- group: company
  title: ''
  type: Blog
  url: https://doktor.se/artiklar
coverage:
  checked: '2026-10-12'
  detail: The site provides no machine‑readable API specification and no documentation host was discovered.
  evidence:
  - status: 200
    url: https://doktor.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Doktor.se is a Swedish digital healthcare platform offering online medical consultations, prescription services, and access to a network of primary care clinics. Users can book appointments, receive medical advice via chat or video within minutes, and manage prescriptions through the app. The service emphasizes rapid access to licensed healthcare professionals and integrates vaccination and testing services across Sweden.
image: https://a.storyblok.com/f/205847/1600x900/c831f343b0/doktorse-og-image.png
layout: provider
modified: '2026-10-12'
name: Doktor.se
nav: Providers
network: true
overview: 'Doktor.se is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Telehealth, Sweden, and Digital Health.


  Doktor.se''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doktor Se Domain Security
  slug: doktor-se-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doktor-se
tags:
- Healthcare
- Telehealth
- Sweden
- Digital Health
website: https://doktor.se/
---
