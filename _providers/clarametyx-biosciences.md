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
  href: https://raw.githubusercontent.com/api-evangelist/clarametyx-biosciences/refs/heads/main/hosts/clarametyx-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clarametyx-biosciences-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarametyx-biosciences/refs/heads/main/security/clarametyx-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarametyx-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clarametyx.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarametyx.com/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://clarametyx.com
  - status: 200
    url: https://forgeglobal.com/clarametyx-biosciences_stock/
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Clarametyx Biosciences is a biopharmaceutical company focused on developing novel immune‑enabling therapies targeting bacterial biofilms that drive chronic respiratory diseases such as cystic fibrosis. The company advances its pipeline through pre‑clinical and early‑stage clinical programs, aiming to modify disease progression rather than merely alleviate symptoms. Recent announcements include positive topline data from a Phase 2a study of CMTX‑101 and significant Series A financing to accelerate development.
layout: provider
modified: '2026-10-08'
name: Clarametyx Biosciences
nav: Providers
network: true
overview: Clarametyx Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Respiratory Diseases, Clinical Trials, Drug Development, and Biofilms.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
  name: Clarametyx Biosciences Domain Security
  slug: clarametyx-biosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: clarametyx-biosciences
tags:
- Respiratory Diseases
- Clinical Trials
- Drug Development
- Biofilms
website: https://clarametyx.com
---
