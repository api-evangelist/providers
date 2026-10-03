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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioventrix/refs/heads/main/hosts/bioventrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioventrix-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bioventrix.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioventrix/refs/heads/main/security/bioventrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioventrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bioventrix.com
coverage:
  checked: '2026-09-28'
  detail: The main website returns HTML with no API documentation or machine‑readable spec.
  evidence:
  - status: 200
    url: https://bioventrix.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bioventrix, Inc. is an innovative medical device company focused on cardiothoracic surgery solutions for heart failure patients. Their Revivent System offers a less invasive cardiac remodeling therapy to improve cardiac function and quality of life. The company provides clinical trial data, publications, and resources for physicians and patients, aiming to extend lifespan and enhance health outcomes for those with heart failure.
image: https://bioventrix.com/wp-content/uploads/2023/08/BioVentrix_logo_50-reg-2.png
layout: provider
modified: '2026-09-28'
name: Bioventrix
nav: Providers
network: true
overview: Bioventrix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Heart Failure, Cardiac Therapy, Clinical Trials, and Reimbursement.
random_paper: 20
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bioventrix Domain Security
  slug: bioventrix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bioventrix
tags:
- Heart Failure
- Cardiac Therapy
- Clinical Trials
- Reimbursement
website: https://bioventrix.com
---
