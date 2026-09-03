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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thermondo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thermondo.de/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thermondo-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thermondo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/thermondo/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thermondo-well-known.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thermondo
created: '2026-07-17'
description: Thermondo is Germany's largest residential heating installer, focused on heat pumps, photovoltaic (solar) systems, home energy management (thermondo smart), dynamic electricity tariffs, financing and subsidy assistance, and maintenance and repair services for homeowners. Founded in 2013 and headquartered in Berlin, the company employs over 1,200 staff and has completed installations for more than 55,000 customers. Thermondo is a consumer-facing climate-energy provider and a portfolio company of HV Capital. It publishes no public developer API or documentation surface; it does operate a security.txt vulnerability-disclosure program and a GitHub organization. This profile was added to the API Evangelist network from HV Capital's portfolio and enriched with the public security surface that could be verified.
image: https://www.thermondo.de/favicon.ico
layout: provider
modified: '2026-07-21'
name: Thermondo
nav: Providers
network: true
overview: Thermondo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer; Climate Energy, Heat Pumps, Solar, and Home Energy.
random_paper: 10
score:
  band: minimal
  composite: 6.2
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
    operational_transparency: 13.2
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thermondo/refs/heads/main/screenshots/thermondo-2026-09-02T163509.png
security:
- kind: domain-security
  name: Thermondo Domain Security
  slug: thermondo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thermondo Vulnerability Disclosure
  slug: thermondo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thermondo
tags:
- Company
- Consumer; Climate Energy
- Heat Pumps
- Solar
- Home Energy
- Energy Management
- Climate Tech
website: https://www.thermondo.de/
---
