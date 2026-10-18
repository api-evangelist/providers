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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alpheus-medical/refs/heads/main/llms/alpheus-medical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpheus-medical-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alpheus-medical/refs/heads/main/hosts/alpheus-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpheus-medical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alpheus-medical/refs/heads/main/vendors/alpheus-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpheus-medical-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alpheusmedical.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alpheusmedical.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://alpheusmedical.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alpheus-medical/refs/heads/main/security/alpheus-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpheus-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alpheusmedical.com/
coverage:
  checked: '2026-10-05'
  detail: The API host https://api.alpheusmedical.com returns no response, providing no machine‑readable specification.
  evidence:
  - status: 0
    url: https://api.alpheusmedical.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Alpheus Medical is a private, clinical-stage biotechnology company developing Porphyrin Metabolite Activation (PoMA™), a drug-led, tumor-selective oncology approach using low‑intensity ultrasound to activate a tumor‑accumulating drug, currently in Phase 2b trials for glioblastoma. The therapy aims to improve outcomes while reducing treatment burden for patients and families.
image: https://alpheusmedical.com/wp-content/uploads/alpheus-medical-facebook-og-scaled.jpg
layout: provider
modified: '2026-09-24'
name: Alpheus Medical
nav: Providers
network: true
overview: Alpheus Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Oncology, Medical Devices, Clinical Trials, and Company.
random_paper: 0
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.5
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 0.3
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
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alpheus Medical Domain Security
  slug: alpheus-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alpheus-medical
tags:
- Biotechnology
- Oncology
- Medical Devices
- Clinical Trials
- Company
website: https://alpheusmedical.com/
---
