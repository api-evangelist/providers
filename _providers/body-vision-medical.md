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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/body-vision-medical/refs/heads/main/llms/body-vision-medical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/body-vision-medical-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/body-vision-medical/refs/heads/main/hosts/body-vision-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/body-vision-medical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/body-vision-medical/refs/heads/main/vendors/body-vision-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/body-vision-medical-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bodyvisionmedical.com/privacy-and-cookies
- group: company
  title: ''
  type: Newsroom
  url: https://www.bodyvisionmedical.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/body-vision-medical/refs/heads/main/security/body-vision-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/body-vision-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bodyvisionmedical.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.bodyvisionmedical.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Body Vision Medical is a medical technology company developing AI‑powered intraoperative imaging solutions. In August 2026 the company announced a new funding round to accelerate global expansion of its platform, aiming to improve surgical outcomes through real‑time visualisation. The firm focuses on integrating advanced computer‑vision algorithms with imaging hardware to provide surgeons with enhanced decision‑making tools during procedures.
layout: provider
modified: '2026-10-02'
name: Body Vision Medical
nav: Providers
network: true
overview: Body Vision Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Technology, Artificial Intelligence, Imaging, Surgery, and Company.
random_paper: 11
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Body Vision Medical Domain Security
  slug: body-vision-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: body-vision-medical
tags:
- Medical Technology
- Artificial Intelligence
- Imaging
- Surgery
- Company
website: https://www.bodyvisionmedical.com
---
