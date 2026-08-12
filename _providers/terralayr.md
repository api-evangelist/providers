---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.trlyr.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trlyr.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Terralayr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trlyr.com/policies
- group: agent
  title: ''
  type: WellKnown
  url: well-known/terralayr-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terralayr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/terralayr-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terralayr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/terralayr-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terralayr-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terralayr-llms.txt
created: '2026-07-17'
description: terralayr is a German energy-flexibility company that develops, owns and operates utility-scale battery energy storage systems (BESS) and runs LAYR, a cloud platform that aggregates heterogeneous storage assets and makes their flexibility available as bookable capacity to utilities, grid operators, power traders, aggregators and asset owners. The platform lets customers buy and sell dispatchable capacity to balance renewable generation against fluctuating grid demand, with storage bookable via API and no complex hardware onboarding. terralayr is backed by Creandum and Earlybird. Its LAYR product API is B2B/private and publishes no public OpenAPI, SDKs or developer documentation; this profile captures the public well-known discovery, security and operational surface.
image: https://www.trlyr.com/media-kit
layout: provider
modified: '2026-07-21'
name: terralayr
nav: Providers
network: true
overview: 'terralayr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Energy, Battery Energy Storage, and Grid Flexibility.


  terralayr''s developer surface includes authentication and 10 more developer resources.'
random_paper: 54
scopes:
- name: Terralayr Scopes
  scope_count: 2
  slug: terralayr-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 18.9
  delta: -0.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 57.4
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 19.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Terralayr Authentication
  slug: terralayr-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Terralayr Domain Security
  slug: terralayr-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: terralayr
tags:
- Company
- Climate
- Energy
- Battery Energy Storage
- Grid Flexibility
- Renewable Energy
- Cleantech
- Energy Trading
website: https://www.trlyr.com/
---
