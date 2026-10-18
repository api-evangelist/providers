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
- description: API documentation is not publicly available; the company provides health technology solutions but no developer program.
  name: Complement 1 API
  slug: complement-1-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/complement-1/refs/heads/main/hosts/complement-1-hosts.yml
  title: ''
  type: Hosts
  url: hosts/complement-1-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/complement-1/refs/heads/main/vendors/complement-1-vendors.yml
  title: ''
  type: Vendors
  url: vendors/complement-1-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/complement-1/refs/heads/main/security/complement-1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/complement-1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.complement1.com/
- group: company
  title: ''
  type: About
  url: https://www.complement1.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://www.complement1.com/solutions/employers
- group: docs
  title: ''
  type: Documentation
  url: https://www.complement1.com/solutions/healthplans
- group: docs
  title: ''
  type: Documentation
  url: https://www.complement1.com/solutions/healthsystems
- group: operate
  title: ''
  type: Contact
  url: https://www.complement1.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.complement1.com/tnc.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.complement1.com/privacy.html
coverage:
  checked: '2026-10-10'
  detail: No public developer program or API documentation was found on the website.
  evidence:
  - status: 200
    url: https://www.complement1.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Complement 1 is a health technology company founded in 2024 that delivers a tech‑enabled, clinically validated lifestyle modification platform for cancer patients, survivors, and high‑risk individuals. It provides personalized coaching, integrates with clinical workflows, and partners with health plans, providers, and employers to improve cancer‑related health outcomes through evidence‑based lifestyle interventions.
image: https://complement1.com/opengraph-image.png
layout: provider
modified: '2026-10-09'
name: Complement 1
nav: Providers
network: true
overview: 'Complement 1 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Oncology, Lifestyle, and Digital Health.


  Complement 1''s developer surface includes documentation and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
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
  name: Complement 1 Domain Security
  slug: complement-1-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: complement-1
tags:
- Company
- Health Tech
- Oncology
- Lifestyle
- Digital Health
website: https://www.complement1.com/
---
