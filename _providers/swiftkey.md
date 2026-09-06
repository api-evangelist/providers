---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.swiftkey.com'', ''status'': 308, ''note'': ''declared website redirects to https://www.microsoft.com/en-us/swiftkey — a different registrable domain (swiftkey.com -> microsoft.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: https://apis.io/providers/microsoft/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swiftkey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swiftkey.com
created: '2026-07-17'
description: SwiftKey is a predictive on-screen keyboard for Android and iOS that uses machine learning to improve autocorrect, next-word prediction, and swipe-to-type (SwiftKey Flow). Founded in London as TouchType, it was acquired by Microsoft in 2016 and is now shipped as Microsoft SwiftKey. The former SwiftKey SDK for embedding its prediction engine has been discontinued, and www.swiftkey.com now permanently redirects to microsoft.com/swiftkey. As of this enrichment pass the product exposes no public developer API, SDK registry package, or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swiftkey.png
layout: provider
modified: '2026-07-21'
name: Swiftkey
nav: Providers
network: true
overview: Swiftkey is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Keyboard, Predictive Text, and Machine-Learning.
random_paper: 4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/swiftkey/refs/heads/main/screenshots/swiftkey-2026-09-02T161353.png
security:
- kind: domain-security
  name: Swiftkey Domain Security
  slug: swiftkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swiftkey
tags:
- Company
- Artificial Intelligence
- Keyboard
- Predictive Text
- Machine-Learning
- Mobile
- Microsoft
website: https://www.swiftkey.com
---
