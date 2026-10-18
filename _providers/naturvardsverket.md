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
- description: Documentation page for API reference
  name: Documentation API
  slug: documentation-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/naturvardsverket/refs/heads/main/hosts/naturvardsverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/naturvardsverket-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/naturvardsverket/refs/heads/main/vendors/naturvardsverket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/naturvardsverket-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.naturvardsverket.se/om-oss/regeringsuppdrag/slutredovisade-regeringsuppdrag/register-over-uppgifter-om-anvandning-av-slam-i-jordbruket/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.naturvardsverket.se/en/topics/the-right-of-public-access/activities-and-places/privacy-protection-zone/
- group: docs
  title: ''
  type: Documentation
  url: https://www.naturvardsverket.se/en/international/cooperation/bilateral/western-balkans/an-active-network-of-aq-civil-servants-from-national-and-local-level/documentation/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/naturvardsverket/refs/heads/main/security/naturvardsverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/naturvardsverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://naturvardsverket.se/
coverage:
  checked: '2026-10-15'
  detail: The provider's documentation page contains only HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.naturvardsverket.se/en/international/cooperation/bilateral/western-balkans/an-active-network-of-aq-civil-servants-from-national-and-local-level/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Naturvårdsverket is Sweden’s Environmental Protection Agency, working to promote a sustainable environment, climate transition, circular economy and biodiversity. It provides guidance, grants, data and statistics, and supports stakeholders through policies, regulations and tools aimed at improving environmental quality across the nation.
layout: provider
modified: '2026-10-15'
name: Naturvårdsverket
nav: Providers
network: true
overview: 'Naturvårdsverket is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Environment, Sweden, Agency, and Sustainability.


  Naturvårdsverket''s developer surface includes signup flow, documentation, and 5 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Naturvardsverket Domain Security
  slug: naturvardsverket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: naturvardsverket
tags:
- Government
- Environment
- Sweden
- Agency
- Sustainability
website: https://naturvardsverket.se/
---
