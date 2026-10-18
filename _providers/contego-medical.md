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
- description: API reference (access gated by bot challenge, no open spec discovered)
  name: Contego Medical API
  slug: contego-medical-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contego-medical/refs/heads/main/hosts/contego-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contego-medical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contego-medical/refs/heads/main/vendors/contego-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contego-medical-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contego-medical/refs/heads/main/security/contego-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contego-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contegomedical.com
- group: docs
  title: ''
  type: Documentation
  url: https://contegomedical.com/company/
- group: start
  title: ''
  type: GettingStarted
  url: https://contegomedical.com/company/
- group: operate
  title: ''
  type: Support
  url: https://contegomedical.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://contegomedical.com/company/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contegomedical.com/terms-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contegomedical.com/privacy-policy/
created: '2026-10-10'
description: Contego Medical develops integrated embolic protection and revascularization solutions for carotid and peripheral vascular disease, aiming to improve patient outcomes and procedural efficiency. The company partners with Medtronic for U.S. distribution and offers products such as Neuroguard IEP, Excipio, and Vanguard IEP, with a focus on simplifying complex vascular procedures.
image: https://contegomedical.com/wp-content/uploads/2022/10/contego-logo.svg
layout: provider
modified: '2026-10-10'
name: Contego Medical
nav: Providers
network: true
overview: 'Contego Medical is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Vascular, Revascularization, Embolic Protection, and Healthcare.


  Contego Medical''s developer surface includes documentation, getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
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
  name: Contego Medical Domain Security
  slug: contego-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contego-medical
tags:
- Medical Devices
- Vascular
- Revascularization
- Embolic Protection
- Healthcare
website: https://contegomedical.com
---
