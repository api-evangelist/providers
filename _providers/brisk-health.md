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
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brisk-health-mcp-tools-list.json
- group: company
  title: ''
  type: Website
  url: https://www.briskhealthurgentcare.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brisk-health-domain-security.yml
coverage:
  checked: '2026-08-08'
  detail: Brisk Health delivers urgent care from a physical clinic and a fleet of mobile treatment vehicles, so there is no API to publish; the only machine-readable documents on its host are the llms.txt and /_api/mcp endpoint that Wix provisions automatically for every site it hosts, and the patient app that fronted the service is now delisted from both app stores.
  evidence:
  - status: 200
    url: https://www.briskhealthurgentcare.com/
  - status: 404
    url: https://briskhealth.com/
  - status: 404
    url: https://apps.apple.com/us/app/brisk-health/id6450514414
  - status: 400
    url: https://www.briskhealthurgentcare.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: 'Brisk Health is a Colorado urgent care and primary care provider operating a cash-pay clinic in the Denver metro area plus a fleet of mobile vehicles staffed by acute care clinicians for in-home visits, with same-day visits advertised from $49 and no insurance required. In October 2025 it announced a move from its Lakewood location to a purpose-built facility in Littleton, Colorado. Brisk Health is a healthcare services business rather than a software vendor: it publishes no developer program, no public API documentation, no SDKs, and no machine-readable specification of any kind. Its patient-facing mobile app has been delisted from both the Apple App Store and Google Play, and both of its brand domains now serve parked-domain error pages.'
layout: provider
mcp_servers:
- description: ''
  name: Brisk Health MCP Server
  slug: brisk-health-mcp-server
modified: '2026-08-08'
name: Brisk Health
nav: Providers
network: true
overview: Brisk Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Urgent Care, Primary Care, and Home Health.
random_paper: 17
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brisk-health/refs/heads/main/screenshots/brisk-health-2026-09-02T144950.png
security:
- kind: domain-security
  name: Brisk Health Domain Security
  slug: brisk-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brisk-health
tags:
- Company
- Healthcare
- Urgent Care
- Primary Care
- Home Health
- Clinics
- Colorado
website: https://www.briskhealthurgentcare.com/
---
