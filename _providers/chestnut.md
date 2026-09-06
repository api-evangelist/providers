---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.chestnutfi.com'', ''status'': 308, ''note'': ''declared website redirects to https://www.chestnutai.com/ — a different registrable domain (chestnutfi.com -> chestnutai.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/chestnut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chestnutfi.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chestnutfi.com/
- group: operate
  title: ''
  type: Support
  url: https://www.chestnutfi.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chestnutfi.notion.site/Terms-Conditions-aa5de417731340489981af1327ef3c90
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chestnutfi.notion.site/Privacy-Policy-674d7c621c8f43e9a01e59a8651831bc
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/Chestnut
created: '2026-07-17'
description: Chestnut is an AI-native operating system for insurance distribution, built for insurance carriers to manage the entire producer lifecycle. The Seattle-based, Andreessen Horowitz-backed company combines a purpose-built insurance data model with an API-first architecture and an agentic AI layer, providing producer onboarding automation (including NIPR integration), hierarchy configuration, incentive compensation management, debt management, performance tracking, and compensation intelligence. Chestnut positions its platform as a system of record that bridges carriers' operational needs to an agentic AI future, with an API-first, MCP-ready backend. Its public API and developer documentation are gated for carrier customers, so no public specification is available for the catalog at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chestnut.png
layout: provider
modified: '2026-07-18'
name: Chestnut
nav: Providers
network: true
overview: 'Chestnut is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Insurance Distribution, and Producer Management.


  Chestnut''s developer surface includes support and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chestnut/refs/heads/main/screenshots/chestnut-2026-07-25T205202.png
security:
- kind: domain-security
  name: Chestnut Domain Security
  slug: chestnut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chestnut
tags:
- Company
- Insurance
- Insurtech
- Insurance Distribution
- Producer Management
- Incentive Compensation
- Agentic AI
- MCP
- API-First
website: https://www.chestnutfi.com
---
