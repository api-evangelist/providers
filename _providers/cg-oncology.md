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
  href: https://raw.githubusercontent.com/api-evangelist/cg-oncology/refs/heads/main/hosts/cg-oncology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cg-oncology-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cg-oncology/refs/heads/main/security/cg-oncology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cg-oncology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cgoncology.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cgoncology.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cgoncology.com/terms-of-service/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cgoncology.com
coverage:
  checked: '2026-10-08'
  detail: The company provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://cgoncology.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CG Oncology is a publicly traded biotechnology company focused on developing bladder‑sparing immunotherapies for non‑muscle invasive bladder cancer. The firm leverages oncolytic viral platforms to create novel treatments, maintains an active pipeline, and provides extensive investor information through its corporate site. It engages clinicians, patients, and investors with detailed scientific, clinical, and financial resources.
image: https://cgoncology.com/wp-content/uploads/2025/12/OG_Homepage.jpg
layout: provider
modified: '2026-10-07'
name: CG Oncology
nav: Providers
network: true
overview: CG Oncology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Oncology, Bladder Cancer, Immunotherapy, and Drug Development.
random_paper: 21
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
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
  name: Cg Oncology Domain Security
  slug: cg-oncology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cg-oncology
tags:
- Oncology
- Bladder Cancer
- Immunotherapy
- Drug Development
website: https://cgoncology.com
---
