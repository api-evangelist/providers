---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/clovis-oncology/hosts/clovis-oncology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clovis-oncology-hosts.yml
- group: auth
  href: https://artifacts.apis.io/clovis-oncology/security/clovis-oncology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clovis-oncology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clovisoncology.com/
coverage:
  checked: '2026-10-26'
  detail: OpenAPI endpoint returned an HTML error page, no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://api.clovisoncology.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Clovis Oncology is a biopharmaceutical company focused on developing innovative small molecule therapies for the treatment of cancer. The company discovers, develops, and commercializes oncology drugs, aiming to address unmet medical needs in oncology through a pipeline of targeted therapies. While the public website currently returns an error page, the company is known from industry reports and regulatory filings as an active participant in cancer drug development, with several candidates in clinical trials.
layout: provider
modified: '2026-10-26'
name: Clovis Oncology
nav: Providers
network: true
overview: Clovis Oncology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oncology, Biopharma, Cancer Therapeutics, and Clinical Trials.
random_paper: 15
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clovis-oncology/clovis-oncology-2026-11-03T124627.png
security:
- kind: domain-security
  name: Clovis Oncology Domain Security
  slug: clovis-oncology-domain-security
  summary_line: no transport/DNS hardening detected
slug: clovis-oncology
tags:
- Company
- Oncology
- Biopharma
- Cancer Therapeutics
- Clinical Trials
website: https://www.clovisoncology.com/
---
