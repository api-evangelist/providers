---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://sensage.com'', ''status'': 302, ''note'': ''declared website redirects to https://ignitetech.ai:443/ — a different registrable domain (sensage.com -> ignitetech.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sensage.com
created: '2026-07-17'
description: SenSage was a security information and event management (SIEM) and log/event analytics company backed by Battery Ventures and Canaan Partners. Its platform focused on collecting, warehousing, and analyzing very large volumes of security event and log data for threat detection, forensics, and regulatory compliance reporting. SenSage was later acquired by KEYW Holding Corporation and the brand was retired; its former domain, sensage.com, now redirects to IgniteTech (an ESW Capital software-acquisition operator). This profile was surfaced as a venture portfolio company and added to the API Evangelist network as a lead. No active developer portal, public API, or documentation surface was found during enrichment; the company is treated as defunct with no live API footprint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensage.png
layout: provider
modified: '2026-07-21'
name: SenSage
nav: Providers
network: true
overview: SenSage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, SIEM, Log Management, and Security Analytics.
random_paper: 7
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
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensage/refs/heads/main/screenshots/sensage-2026-09-02T154848.png
security:
- kind: domain-security
  name: Sensage Domain Security
  slug: sensage-domain-security
  summary_line: TLSv1.2
slug: sensage
tags:
- Company
- Security
- SIEM
- Log Management
- Security Analytics
- Event Data
- Compliance
- Defunct
website: https://sensage.com
---
