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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terawatt-infrastructure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.terawattinfrastructure.com/
- group: company
  title: ''
  type: Blog
  url: https://www.terawattinfrastructure.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.terawattinfrastructure.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.terawattinfrastructure.com/privacy-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/terawatt-infrastructure-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/terawatt-infrastructure-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terawatt-infrastructure-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Terawatt states in its own engineering blog that it "implemented Open Charge Point Interface (OCPI) with custom extensions" to give customers visibility into its charging facilities, but that surface is reachable only under a charging-as-a-service agreement — there is no developer portal, no OCPI version-discovery endpoint answering anonymously, and no API host in DNS at all (api./developer./docs./portal./ocpi..terawattinfrastructure.com are every one NXDOMAIN).
  evidence:
  - status: 200
    url: https://www.terawattinfrastructure.com/blog/how-terawatts-full-stack-platform-delivers-reliable-ev-av-fleet-charging
  - status: 404
    url: https://www.terawattinfrastructure.com/ocpi/versions
  - status: 404
    url: https://www.terawattinfrastructure.com/developers
  - status: 404
    url: https://www.terawattinfrastructure.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2026-08-30'
description: 'Terawatt Infrastructure is a US infrastructure company that acquires, develops, owns, and operates purpose-built electric-vehicle charging centers for commercial fleets — medium- and heavy-duty trucking, drayage, autonomous vehicle and rideshare operators. The company sells charging-as-a-service rather than software: it holds real estate and grid interconnection, builds high-power charging sites (including the I-10 electrified corridor and sites near the Ports of Los Angeles and Long Beach), and runs them with its own proprietary Charge Management Software, operations and maintenance program, and a customer reservations portal. Terawatt states publicly that it has implemented the Open Charge Point Interface (OCPI) with custom extensions so fleet customers get visibility into its charging facilities, but it publishes no public developer portal, API reference, or machine-readable contract for that surface.'
image: https://cdn.prod.website-files.com/659d87f22f67fd9bbaac94a7/68b990218fbb9220fa26b901_Frame%201.png
layout: provider
modified: '2026-08-30'
name: Terawatt Infrastructure
nav: Providers
network: true
overview: 'Terawatt Infrastructure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electric Vehicles, EV Charging, and Fleet Management.


  Terawatt Infrastructure''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Terawatt Infrastructure Plans Pricing
  plan_count: 0
  slug: terawatt-infrastructure-plans-pricing
random_paper: 1
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terawatt-infrastructure/refs/heads/main/screenshots/terawatt-infrastructure-2026-09-02T163126.png
security:
- kind: domain-security
  name: Terawatt Infrastructure Domain Security
  slug: terawatt-infrastructure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: terawatt-infrastructure
tags:
- Company
- Energy
- Electric Vehicles
- EV Charging
- Fleet Management
- Transportation
- Logistics
- Infrastructure
- Sustainability
- Charging as a Service
website: https://www.terawattinfrastructure.com/
---
