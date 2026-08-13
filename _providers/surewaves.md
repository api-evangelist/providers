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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surewaves-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.surewaves.com/resources
- group: company
  title: ''
  type: Website
  url: https://www.surewaves.com
- group: design
  title: ''
  type: Conformance
  url: conformance/surewaves-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/surewaves-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/surewaves-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/surewaves-llms.txt
coverage:
  checked: '2026-08-12'
  detail: SureWaves runs a 13-page Framer marketing site whose only call to action is "Request Meeting" — there is no developer program, no API host (api./app./developer./docs./portal./console.surewaves.com all resolve NXDOMAIN), and every contract, docs and /.well-known/ path on www.surewaves.com returns a clean 404, so the ANNA broadcaster platform and the Spot TV network are sold entirely as enterprise engagements with no public integration surface.
  evidence:
  - status: 200
    url: https://www.surewaves.com/sitemap.xml
  - status: 404
    url: https://www.surewaves.com/openapi.json
  - status: 404
    url: https://www.surewaves.com/.well-known/agent-card.json
  - status: 404
    url: https://www.surewaves.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: SureWaves is a broadcast-television advertising technology company that integrates linear TV with digital advertising infrastructure. It provides AI-powered spot and yield management for broadcasters and real-time, pay-for-performance campaign tooling for advertisers, and operates India's largest spot TV network — more than 20 million spots monthly across 550+ local channels reaching 490+ million households. Holder of 50+ patents, backed by Accel, with offices in Bangalore, New York, McLean, Mumbai and New Delhi. Added to the API Evangelist network as a portfolio-lead stub; two enrichment passes (2026-07 and 2026-08) found no public API, developer portal, SDK, package, or machine-readable contract of any kind — the platform is sold as an enterprise engagement behind a "Request Meeting" form. The company does display a SOC 2 Type II badge on its homepage, attested by Prescient Assurance against AICPA SSAE 18.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surewaves.png
layout: provider
modified: '2026-08-12'
name: SureWaves
nav: Providers
network: true
overview: 'SureWaves is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Advertising, Broadcast, and Television.


  SureWaves'' developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Surewaves Plans Pricing
  plan_count: 0
  slug: surewaves-plans-pricing
random_paper: 37
score:
  band: minimal
  composite: 9.3
  delta: 3.9
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 5.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Surewaves Domain Security
  slug: surewaves-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: surewaves
tags:
- Company
- Media
- Advertising
- Broadcast
- Television
- AdTech
- Video
- Marketing
website: https://www.surewaves.com
---
