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
  href: https://raw.githubusercontent.com/api-evangelist/anchordx/refs/heads/main/hosts/anchordx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anchordx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anchordx/refs/heads/main/vendors/anchordx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anchordx-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anchordx/refs/heads/main/security/anchordx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anchordx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/anchordx_stock/
created: '2026-09-24'
description: AnchorDx, also known as 基准医疗, is a precision medicine company founded in 2015 in Guangzhou, China, with R&D centers in China and the USA. It focuses on methylation high‑throughput sequencing for early cancer detection, offering blood‑based and urine‑based tests covering over 70% of high‑incidence cancers. The company has filed 82 patents (32 granted) and serves more than 100,000 patients, integrating AI and big‑data platforms for diagnostics and monitoring.
layout: provider
modified: '2026-09-24'
name: AnchorDx
nav: Providers
network: true
overview: AnchorDx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Precision Medicine, Cancer Detection, Genomics, and Artificial Intelligence.
random_paper: 19
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anchordx Domain Security
  slug: anchordx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anchordx
tags:
- Company
- Precision Medicine
- Cancer Detection
- Genomics
- Artificial Intelligence
website: https://forgeglobal.com/anchordx_stock/
---
