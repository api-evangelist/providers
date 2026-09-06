---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://clausematch.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.corlytics.com:443/ — a different registrable domain (clausematch.com -> corlytics.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clausematch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clausematch.com
created: '2026-07-17'
description: Clausematch is a London-founded regulatory technology (RegTech) company providing a cloud platform for policy and procedure management, regulatory change management, and structured document authoring and collaboration for banks, insurers, and other regulated financial institutions. Its tooling helps compliance teams draft, review, version, and attest to policies while mapping regulatory obligations to internal controls. Clausematch was acquired by Corlytics in 2024; the clausematch.com domain now 301-redirects to corlytics.com. This profile was surfaced as a portfolio company of Speedinvest and added to the API Evangelist network for enrichment. No public developer portal, API reference, or machine-readable API specification was found during enrichment (the web surface is WAF-protected and returns HTTP 403 to automated probes).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clausematch.png
layout: provider
modified: '2026-07-18'
name: Clausematch
nav: Providers
network: true
overview: Clausematch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RegTech, Compliance, Regulatory Change Management, and Policy Management.
random_paper: 7
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clausematch/refs/heads/main/screenshots/clausematch-2026-07-25T205528.png
security:
- kind: domain-security
  name: Clausematch Domain Security
  slug: clausematch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clausematch
tags:
- Company
- RegTech
- Compliance
- Regulatory Change Management
- Policy Management
- Financial-Services
- GovTech
website: https://clausematch.com
---
