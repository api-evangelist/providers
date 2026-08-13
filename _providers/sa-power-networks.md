---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sa-power-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sapowernetworks.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sa-power-networks
- group: company
  title: ''
  type: About
  url: https://www.sapowernetworks.com.au/about-us/our-role/
- group: start
  title: ''
  type: Industry
  url: https://www.sapowernetworks.com.au/industry/
- group: company
  title: ''
  type: Blog
  url: https://www.sapowernetworks.com.au/industry/industry-news/
- group: build
  title: ''
  type: ResourceLibrary
  url: https://www.sapowernetworks.com.au/resource-library/
- group: start
  title: ''
  type: Portal
  url: https://dapr.sapowernetworks.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sapowernetworks.com.au/industry/access-your-clients-meter-data/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sapowernetworks.com.au/industry/flexible-exports/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sapowernetworks.com.au/industry/relevant-agent/
- group: other
  title: ''
  type: Data
  url: https://www.sapowernetworks.com.au/industry/annual-network-plans/
- group: other
  title: ''
  type: Data
  url: https://www.sapowernetworks.com.au/data/324688/2024-2025-zone-substation-data/
- group: start
  title: ''
  type: Portal
  url: https://www.sapowernetworks.com.au/industry/portal/
- group: operate
  title: ''
  type: Support
  url: https://www.sapowernetworks.com.au/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sapowernetworks.com.au/policies/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sapowernetworks.com.au/policies/disclaimer/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sa-power-networks-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sa-power-networks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sa-power-networks-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sa-power-networks-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sa-power-networks-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sa-power-networks-llms.txt
created: '2026-07-27'
description: 'SA Power Networks is South Australia''s sole electricity distributor — the poles-and-wires DNSP that builds, maintains and upgrades the network delivering power to around 900,000 homes and businesses, and the operator of the state''s Flexible Exports dynamic solar export scheme. It sits between the transmission network and the retailers, holding meter data, network capacity data and DER connection data but selling nothing to consumers directly. Its API posture is empty by design: Australia''s Consumer Data Right was extended to energy and is live, but the designation names electricity retailers as primary data holders and AEMO as the secondary data holder — distributors are not designated, and SA Power Networks does not appear among the 84 brands on the live CDR energy register. There is no developer portal, no documented API, and no machine-readable contract of any kind. Third parties reach a customer''s meter data only by registering as an Authorised Representative and logging
  into a web portal; network capacity is a registration-gated map viewer; the genuinely open surface is bulk file downloads (zone substation data, the Distribution Annual Planning Report, the embedded generation register) that anyone can pull anonymously but that carry a redistribution restriction rather than an open licence.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: SA Power Networks
nav: Providers
network: true
overview: 'SA Power Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  SA Power Networks'' developer surface includes engineering blog, developer portal, documentation, support, authentication, and 18 more developer resources.'
random_paper: 72
scopes:
- name: Sa Power Networks Scopes
  scope_count: 36
  slug: sa-power-networks-scopes
  summary_line: 36 scopes · authorizationCode
score:
  band: emerging
  composite: 25.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Sa Power Networks Authentication
  slug: sa-power-networks-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Sa Power Networks Domain Security
  slug: sa-power-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sa-power-networks
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Distribution Network
- Smart Metering
- Solar
- DER
- Open Data
website: https://www.sapowernetworks.com.au/
---
