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
  href: https://raw.githubusercontent.com/api-evangelist/crispr-qc/refs/heads/main/hosts/crispr-qc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crispr-qc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crispr-qc/refs/heads/main/vendors/crispr-qc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crispr-qc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crisprqc.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crisprqc.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://crisprqc.com/category/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crispr-qc/refs/heads/main/security/crispr-qc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crispr-qc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crisprqc.com/
coverage:
  checked: '2026-10-11'
  detail: The company website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://crisprqc.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: CRISPR QC provides a CRISPR Analytics Platform delivering real‑time kinetic insights into gene‑editing workflows. Their services enable researchers to quantify RNP formation, DNA target binding, and cleavage efficiency, helping optimize guide design, enzyme selection, and process parameters across discovery to manufacturing. By offering detailed kinetic data, CRISPR QC accelerates decision‑making, reduces costly trial‑and‑error, and improves reproducibility for biotech and synthetic biology applications.
layout: provider
modified: '2026-10-11'
name: CRISPR QC
nav: Providers
network: true
overview: CRISPR QC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Editing, Analytics, and Platform.
random_paper: 14
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crispr Qc Domain Security
  slug: crispr-qc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crispr-qc
tags:
- Company
- Biotechnology
- Gene Editing
- Analytics
- Platform
website: https://crisprqc.com/
---
