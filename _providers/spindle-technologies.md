---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://spindle.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.salesforce.com/agentforce/?bc=DB — a different registrable domain (spindle.ai -> salesforce.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spindle-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spindle.ai/
created: '2026-07-17'
description: Spindle Technologies (spindle.ai) was an Accel-backed AI startup that was acquired by Salesforce; as of this enrichment pass its entire domain — including the docs, developer, api, and app subdomains — issues a 301 redirect to salesforce.com/agentforce, so it no longer operates an independent developer portal, API, documentation, or SDK surface. This profile is retained as a network record of the company and its acquisition. No standalone API artifacts could be harvested. Domain-level security posture (TLS/DNSSEC/SPF/DMARC on spindle.ai) was probed and captured.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spindle-technologies.png
layout: provider
modified: '2026-08-21'
name: Spindle Technologies
nav: Providers
network: true
overview: Spindle Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Salesforce, and Acquired.
random_paper: 1
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spindle-technologies/refs/heads/main/screenshots/spindle-technologies-2026-09-02T160440.png
security:
- kind: domain-security
  name: Spindle Technologies Domain Security
  slug: spindle-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spindle-technologies
tags:
- Company
- Artificial Intelligence
- Agents
- Salesforce
- Acquired
website: https://spindle.ai/
---
