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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circuit-clinical/refs/heads/main/hosts/circuit-clinical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circuit-clinical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circuit-clinical/refs/heads/main/vendors/circuit-clinical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circuit-clinical-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circuitclinical.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://circuitclinical.com/team/
- group: company
  title: ''
  type: Blog
  url: https://circuitclinical.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/circuit-clinical/refs/heads/main/security/circuit-clinical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circuit-clinical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circuitclinical.com
coverage:
  checked: '2026-10-08'
  detail: No public developer documentation or API specification was found on the company's website.
  evidence:
  - status: 200
    url: https://circuitclinical.com
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Circuit Clinical is an Integrated Research Organization (IRO) that connects physicians, patients, and industry to accelerate clinical research. It offers a physician‑focused, patient‑centric platform to improve trial enrollment, retention, and completion, aiming to make clinical trials more accessible and inclusive across diverse communities.
image: https://www.circuitclinical.com/static/cc-social-495270ae837e5a6a7faabb61896a82a5.png
layout: provider
modified: '2026-10-08'
name: Circuit Clinical
nav: Providers
network: true
overview: 'Circuit Clinical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Clinical Trials, Research, and Technology.


  Circuit Clinical''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circuit Clinical Domain Security
  slug: circuit-clinical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circuit-clinical
tags:
- Company
- Healthcare
- Clinical Trials
- Research
- Technology
website: https://circuitclinical.com
---
