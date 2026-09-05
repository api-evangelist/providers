---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://groundspeed.com/'', ''status'': 301, ''note'': ''declared website redirects to https://insurancequantified.com/solutions/ — a different registrable domain (groundspeed.com -> insurancequantified.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/groundspeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://groundspeed.com/
- group: company
  title: ''
  type: Website
  url: https://insurancequantified.com/groundspeed/
- group: operate
  title: ''
  type: Support
  url: https://insurancequantified.com/talk-to-an-expert/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insurancequantified.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insurancequantified.com/legal-disclosure/
created: '2026-07-17'
description: Groundspeed is an insurance data and analytics company that pioneered AI-powered extraction and standardization of unstructured commercial property and casualty (P&C) insurance documents — loss runs, schedules of values, ACORD forms, and broker submissions — turning them into structured, analytics-ready data for underwriters, brokers, and carriers. Founded in Ann Arbor, Michigan and backed by Insight Partners, Groundspeed was acquired by Insurance Quantified, where its technology now powers the Intake, Workflow, and Intelligence products of an AI-driven underwriting platform serving commercial P&C carriers and MGAs. Groundspeed does not currently publish a public developer program, API reference, or self-service onboarding surface; this profile tracks its identity and public web properties in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groundspeed.png
layout: provider
modified: '2026-07-19'
name: Groundspeed
nav: Providers
network: true
overview: 'Groundspeed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Underwriting, and Analytics.


  Groundspeed''s developer surface includes support and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groundspeed/refs/heads/main/screenshots/groundspeed-2026-07-25T220340.png
security:
- kind: domain-security
  name: Groundspeed Domain Security
  slug: groundspeed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: groundspeed
tags:
- Company
- Insurance
- Insurtech
- Underwriting
- Analytics
- Commercial Insurance
- Property and Casualty
- Document Processing
- Data Extraction
- Artificial Intelligence
website: https://groundspeed.com/
---
