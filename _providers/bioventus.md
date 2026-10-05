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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioventus/refs/heads/main/hosts/bioventus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioventus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioventus/refs/heads/main/vendors/bioventus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bioventus-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bioventus.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bioventus.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bioventus.com/news/
- group: start
  title: ''
  type: Login
  url: https://test-portal.bioventus.com/en/accounts/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.bioventus.com/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioventus/refs/heads/main/security/bioventus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioventus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bioventus.com/
coverage:
  checked: '2026-09-28'
  detail: No public API documentation or machine‑readable contract was found for Bioventus.
  evidence:
  - status: no-response
    url: https://api.bioventus.com
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bioventus is a global leader of innovations for active healing and surgical orthobiologics, offering a comprehensive portfolio of clinically efficacious and cost‑effective solutions for patients, physicians, and payers. The company focuses on pain treatments, platelet‑rich plasma, restorative therapies, and surgical solutions, aiming to improve active lifestyles worldwide.
image: http://www.bioventus.com/wp-content/uploads/2020/07/BIOV_FacebookShare_img_2x-min.jpg
layout: provider
modified: '2026-09-28'
name: Bioventus
nav: Providers
network: true
overview: Bioventus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Orthobiologics, Medical Devices, Healthcare, and Innovation.
random_paper: 1
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bioventus Domain Security
  slug: bioventus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bioventus
tags:
- Company
- Orthobiologics
- Medical Devices
- Healthcare
- Innovation
website: https://www.bioventus.com/
---
