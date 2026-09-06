---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://awakesecurity.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.arista.com/en/solutions/security — a different registrable domain (awakesecurity.com -> arista.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/awake-security-arista-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awakesecurity.com/
created: '2026-07-17'
description: 'Awake Security was a network detection and response (NDR) company founded in 2014 that used AI and machine learning to analyze network traffic and detect threats, compromised devices, and malicious insiders without relying on agents or signatures. Arista Networks acquired Awake Security in 2020 and the technology now ships as Arista NDR within Arista''s security portfolio. The former awakesecurity.com domain redirects to Arista''s security solutions site; the product has no distinct public developer API, OpenAPI specification, developer portal, or SDK program of its own. Originally surfaced as a portfolio company of Bain Capital Ventures. Sector: security.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/awake-security-arista-networks.png
layout: provider
modified: '2026-07-18'
name: Awake Security (Arista Networks)
nav: Providers
network: true
overview: Awake Security (Arista Networks) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Network Detection and Response, NDR, and Cybersecurity.
random_paper: 15
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
screenshot: https://raw.githubusercontent.com/api-evangelist/awake-security-arista-networks/refs/heads/main/screenshots/awake-security-arista-networks-2026-07-25T202012.png
security:
- kind: domain-security
  name: Awake Security Arista Networks Domain Security
  slug: awake-security-arista-networks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: awake-security-arista-networks
tags:
- Company
- Security
- Network Detection and Response
- NDR
- Cybersecurity
- Threat Detection
- Network Security
website: https://awakesecurity.com/
---
