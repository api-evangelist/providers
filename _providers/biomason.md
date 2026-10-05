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
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biomason/refs/heads/main/security/biomason-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biomason-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biomason.com/
- group: docs
  title: ''
  type: Documentation
  url: https://biomason.com/
- group: company
  title: ''
  type: About
  url: https://biomason.com/about
- group: operate
  title: ''
  type: Contact
  url: https://biomason.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biomason.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biomason.com/privacy-policy
created: '2026-09-28'
description: Biomason is a biotechnology company that engineers living concrete using microbes to replace traditional Portland cement, aiming to reduce carbon emissions and create sustainable building materials. Founded in Research Triangle Park, NC, Biomason offers biocement products and services for construction, partnering with industry leaders to scale eco‑friendly concrete solutions.
layout: provider
modified: '2026-09-28'
name: Biomason
nav: Providers
network: true
overview: 'Biomason is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Sustainable Construction, Concrete, Bioengineering, and Company.


  Biomason''s developer surface includes documentation and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biomason Domain Security
  slug: biomason-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biomason
tags:
- Biotechnology
- Sustainable Construction
- Concrete
- Bioengineering
- Company
website: https://biomason.com/
---
