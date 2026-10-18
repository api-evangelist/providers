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
- description: API documentation for Barostim healthcare professional resources
  name: Barostim API
  slug: barostim-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cvrx/refs/heads/main/hosts/cvrx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cvrx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cvrx/refs/heads/main/vendors/cvrx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cvrx-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.barostim.com/healthcare-professionals/sign-up/
- group: company
  title: ''
  type: Newsroom
  url: https://www.barostim.com/healthcare-professionals/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvrx/refs/heads/main/security/cvrx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.barostim.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.barostim.com/healthcare-professionals/
- group: operate
  title: ''
  type: Support
  url: https://www.barostim.com/contact-cvrx/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.barostim.com/healthcare-professionals/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.barostim.com/healthcare-professionals/privacy-policy/
coverage:
  checked: '2026-10-12'
  detail: Healthcare professional pages render via JavaScript, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://www.barostim.com/healthcare-professionals/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: CVRx (Cardiac Vagus Nerve Stimulation) develops the Barostim™ therapy, an implantable device that delivers targeted vagus nerve stimulation to treat heart failure. The company provides a patient‑focused platform with clinical data, device information, and resources for healthcare professionals. Their website offers detailed product pages, clinical trial results, regulatory information, and investor relations, reflecting a comprehensive approach to cardiac care and device innovation.
image: https://www.barostim.com/wp-content/uploads/2022/11/android-chrome-512x512-1.png
layout: provider
modified: '2026-10-12'
name: CVRx
nav: Providers
network: true
overview: 'CVRx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Cardiology, Implantable Therapy, and Healthcare.


  CVRx''s developer surface includes signup flow, documentation, support, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cvrx Domain Security
  slug: cvrx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cvrx
tags:
- Company
- Medical Devices
- Cardiology
- Implantable Therapy
- Healthcare
website: https://www.barostim.com/
---
