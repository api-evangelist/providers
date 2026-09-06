---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
- group: company
  title: ''
  type: Website
  url: https://www.searchlight.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.searchlight.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/searchlight-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/searchlight-domain-security.yml
created: '2026-07-17'
description: Searchlight (searchlight.ai) is an Accel-backed company in the services sector, added to the API Evangelist network from Accel's portfolio. Its primary web presence is a Webflow-hosted marketing site at www.searchlight.ai, with a product application at app.searchlight.ai and an internal API host at api.searchlight.ai — both of which sit behind Cloudflare and return HTTP 525 (origin unreachable to the public), and the marketing site rejects non-browser TLS clients, so no public developer documentation, OpenAPI, or SDKs could be discovered. A public Instatus status page is live at status.searchlight.ai (monitoring Website and App components). Email runs on Google Workspace with HubSpot, and the domain publishes SPF and DMARC records. This profile captures the verifiable public infrastructure; no public API surface was found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/searchlight.png
layout: provider
modified: '2026-07-21'
name: Searchlight
nav: Providers
network: true
overview: Searchlight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Services, Startup, Software-as-a-Service, and Accel.
random_paper: 11
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Searchlight Domain Security
  slug: searchlight-domain-security
  summary_line: DMARC
slug: searchlight
tags:
- Company
- Services
- Startup
- Software-as-a-Service
- Accel
- Web Application
website: https://www.searchlight.ai
---
