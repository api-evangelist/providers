---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autogrid-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autogrid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sunspec.org/contributing-members/autogrid-2/
- group: auth
  title: ''
  type: Certifications
  url: https://products.openadr.org/product/autogrid-systems-inc-opendr-server-2-0-2/
- group: auth
  title: ''
  type: Certifications
  url: https://products.openadr.org/product/autogrid-systems-inc-autogrid-droms/
- group: other
  title: ''
  type: Standards
  url: conformance/autogrid-ieee-2030-5-csip-pics.yml
- group: other
  title: ''
  type: Standards
  url: conformance/autogrid-openadr-pics.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autogrid-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/autogrid-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autogrid-llms.txt
- group: company
  title: ''
  type: Website
  url: https://auto-grid.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://uplight.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auto-grid
- group: company
  title: ''
  type: About
  url: https://uplight.com/resources/derms/
- group: operate
  title: ''
  type: PressRelease
  url: https://uplight.com/press/uplight-to-acquire-autogrid/
created: '2026-07-27'
description: AutoGrid Systems is a United States grid-technology company founded in 2011 by Amit Narayan in Redwood City, California, that built AI and machine-learning software for distributed energy resource management (DERMS), virtual power plants, and automated demand response under the AutoGrid Flex platform, selling to investor-owned utilities, retailers, and aggregators rather than to end consumers. It sits on the grid-tech / DERMS layer of the energy value chain - a buyer and orchestrator of utility and device data, not a data custodian - so no Green Button, Consumer Data Right, or smart-meter data-sharing obligation attaches to it. Schneider Electric took control of AutoGrid and then sold it to Uplight in a deal announced 14 December 2023 and closed in early 2024; auto-grid.com now serves only a 270-byte meta-refresh to uplight.com (on an expired TLS certificate as of 27 July 2026) and every developer, docs, api, and data subdomain fails to resolve. Its API posture is therefore
  honestly none-published - no public developer portal, no OpenAPI, no SDK, no consumer usage API, and no open market data. Its machine-readable contract is instead expressed as protocol conformance, and that is real and still published by the certifying bodies. AutoGrid is a certified OpenADR 2.0a and 2.0b VTN (server) - AutoGrid DROMS and OpenDR Server 2.0, Simple HTTP + XMPP, pull and push - and holds SunSpec Alliance certificate CS-000074 for AutoGrid Flex as an IEEE 2030.5-2018 / CSIP server, tested by Intertek on 12 December 2023 and awarded 22 January 2024. Both surfaces authenticate with mutual TLS x.509 client certificates and were reachable only under commercial contract. The successor surface at docs.uplight.com is real but fully login-gated, redirecting anonymous visitors to a ReadMe dashboard login, and api.uplight.com answers HTTP 401 with "Invalid or no token provided" - partner and customer access only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-27'
name: AutoGrid
nav: Providers
network: true
overview: AutoGrid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Utilities, Electricity, and Grid.
random_paper: 43
score:
  band: minimal
  composite: 12.3
  delta: 3.3
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 9.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Autogrid Domain Security
  slug: autogrid-domain-security
  summary_line: DNSSEC · DMARC
slug: autogrid
tags:
- Energy
- United States
- Utilities
- Electricity
- Grid
- DERMS
- Distributed Energy Resources
- Virtual Power Plant
- Demand Response
- Acquired
- OpenADR
- IEEE 2030.5
- Smart Grid
- Conformance
website: https://auto-grid.com/
---
