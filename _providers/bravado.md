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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bravado-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bravado.co/
coverage:
  checked: '2026-08-14'
  detail: bravado.co refuses HTTPS outright and serves a Gandi "this domain name is parked by the owner" page over plain HTTP for every path, so the War Room product, its GraphQL backend and any developer surface are simply gone from the public internet.
  evidence:
  - status: 0
    url: https://bravado.co/
  - status: 200
    url: http://bravado.co/
  - status: 200
    url: http://bravado.co/.well-known/agent-card.json
  - status: 200
    url: http://bravado.co/openapi.json
  - status: 0
    url: https://bravado.me/war-room
  reason: defunct
  state: none
created: '2026-07-17'
description: Bravado is a community platform for sales professionals, best known as the War Room, which it describes as the world's largest online sales community with more than 400,000 members. Founded in 2016 and headquartered in San Francisco, Bravado offers career networking, anonymous peer Q&A, a jobs and hiring marketplace that matches sales talent with companies, an AI recruiter called Hunter, and a virtual "commission points" rewards currency, delivered through the web and a mobile app. The company is backed by Redpoint Ventures. Bravado does not publish a public developer API; its product is built on an internal GraphQL backend. As of this profile's enrichment date the primary domain bravado.co resolves to a Gandi parking page ("this domain name is unavailable") and is not serving the live product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bravado.png
layout: provider
modified: '2026-08-14'
name: Bravado
nav: Providers
network: true
overview: Bravado is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Community, Sales Enablement, and Careers.
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Bravado Domain Security
  slug: bravado-domain-security
  summary_line: no transport/DNS hardening detected
slug: bravado
tags:
- Company
- Sales
- Community
- Sales Enablement
- Careers
- Recruiting
- Jobs Marketplace
- Professional Network
website: https://bravado.co/
---
