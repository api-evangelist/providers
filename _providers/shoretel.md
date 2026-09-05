---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://shoretel.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.mitel.com:443/ — a different registrable domain (shoretel.com -> mitel.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/shoretel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shoretel.com
created: '2026-07-17'
description: 'ShoreTel was a Sunnyvale, California business communications company founded in 1996 that built IP-based unified communications (UC), VoIP phone systems, and contact-center products for the enterprise, spanning on-premises ShoreTel systems and the cloud-hosted ShoreTel Sky platform. Mitel Networks acquired ShoreTel in September 2017 for roughly USD 530 million and folded its products into the Mitel Connect line. ShoreTel no longer operates as an independent company: the shoretel.com domain now 301-redirects to mitel.com, and there is no independent ShoreTel developer portal, API reference, or OpenAPI surface. Legacy integration surfaces (for example the ShoreTel Sky Hosted API and Exchange Web Services integrations) are now documented and hosted under Mitel. This record was surfaced as a Norwest Venture Partners portfolio company and enriched to reflect its acquired, defunct-as-independent status.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shoretel.png
layout: provider
modified: '2026-07-21'
name: Shoretel
nav: Providers
network: true
overview: Shoretel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Unified Communications, VoIP, Telecommunications, and Contact Center.
random_paper: 9
score:
  band: minimal
  composite: 1.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/shoretel/refs/heads/main/screenshots/shoretel-2026-09-02T155311.png
security:
- kind: domain-security
  name: Shoretel Domain Security
  slug: shoretel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shoretel
tags:
- Company
- Unified Communications
- VoIP
- Telecommunications
- Contact Center
- Enterprise Communications
- Acquired
website: https://shoretel.com
---
