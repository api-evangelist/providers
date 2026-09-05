---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.broadsoft.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.cisco.com/site/us/en/products/collaboration/index.html — a different registrable domain (broadsoft.com -> cisco.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/broadsoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.broadsoft.com/
created: '2026-07-17'
description: BroadSoft was a cloud unified-communications (UCaaS) and VoIP software provider whose BroadWorks and BroadCloud platforms powered hosted PBX, calling, messaging, and contact-center services for telecom carriers and service providers worldwide. Its developer surface centered on the Xtended Services Interface (XSI) and OCI (Open Client Interface) provisioning APIs. Cisco acquired BroadSoft in February 2018 and folded the products into its Collaboration portfolio; the platform now ships as Cisco BroadWorks. The independent developer presence has been retired — www.broadsoft.com 301-redirects to cisco.com — so this profile carries no standalone live API surface. Originally surfaced as a bessemer-venture-partners portfolio company and added to the API Evangelist network for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/broadsoft.png
layout: provider
modified: '2026-08-19'
name: Broadsoft
nav: Providers
network: true
overview: Broadsoft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Unified Communications, UCaaS, VoIP, and Telecommunications.
random_paper: 19
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 3
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
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/broadsoft/refs/heads/main/screenshots/broadsoft-2026-07-25T203945.png
security:
- kind: domain-security
  name: Broadsoft Domain Security
  slug: broadsoft-domain-security
  summary_line: TLSv1.3
slug: broadsoft
tags:
- Company
- Unified Communications
- UCaaS
- VoIP
- Telecommunications
- Cloud Communications
- Contact Center
- Acquired
- Cisco
website: https://www.broadsoft.com/
---
