---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.flexgen.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flexgen.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.flexgen.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexgen-power
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flexgen.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/flexgen-power-systems-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/flexgen-power-systems-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flexgen-power-systems-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexgen-power-systems-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/flexgen-power-systems-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flexgen-power-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flexgen-power-systems-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flexgen-power-systems-llms.txt
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/flexgen-power-systems_stock/
coverage:
  checked: '2026-08-16'
  detail: FlexGen markets "automated APIs" and "historian data API access" as HybridOS features but publishes no developer portal or reference anywhere on flexgen.com — api./docs./developer. subdomains do not resolve in DNS, and the only route to HybridOS documentation is the login-gated Noloco customer portal at portal.flexgen.com, which requires an active tenant.
  evidence:
  - status: 200
    url: https://www.flexgen.com/software/hybridos-energy-management-system
  - status: 200
    url: https://portal.flexgen.com/
  - status: 404
    url: https://www.flexgen.com/openapi.json
  - status: 404
    url: https://www.flexgen.com/llms.txt
  - status: 404
    url: https://www.flexgen.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2026-08-16'
description: FlexGen Power Systems is a Durham, North Carolina energy storage technology company founded in 2009 that designs, integrates and operates grid-scale battery energy storage systems (BESS) and the software that runs them. Its flagship product is HybridOS, a hardware-agnostic energy management system (EMS) for multi-source, multi-site battery and solar portfolios, alongside HybridOS Control BMS (a US-built battery management system), a solar power plant controller (PPC), EMS retrofit, activation and lifecycle services, and data-center power solutions. FlexGen has been named a BloombergNEF Tier 1 energy storage company, acquired Clean Energy Services (CES) and the assets of Powin, and states that HybridOS exposes automated APIs and historian data API access to customers. No public developer portal, API reference or machine-readable specification is published; the HybridOS API surface is reached only through customer deployments and the login-gated FlexGen customer portal.
image: https://www.flexgen.com/themes/custom/flexgen/logo.svg
layout: provider
modified: '2026-08-16'
name: FlexGen Power Systems
nav: Providers
network: true
overview: 'FlexGen Power Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Storage, Battery Energy Storage, and Energy Management.


  FlexGen Power Systems'' developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Flexgen Power Systems Plans Pricing
  plan_count: 0
  slug: flexgen-power-systems-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Flexgen Power Systems Rate Limits
  slug: flexgen-power-systems-rate-limits
score:
  band: emerging
  composite: 15.3
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 15.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Flexgen Power Systems Domain Security
  slug: flexgen-power-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flexgen Power Systems Trust Center
  slug: flexgen-power-systems-trust-center
  summary_line: ISO 9001:2015
slug: flexgen-power-systems
tags:
- Company
- Energy
- Energy Storage
- Battery Energy Storage
- Energy Management
- Grid
- Utilities
- Renewable Energy
- Industrial IoT
- SCADA
website: https://www.flexgen.com/
---
