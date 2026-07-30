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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
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
random_paper: 74
score:
  band: minimal
  composite: 8.2
  delta: -0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 8.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
