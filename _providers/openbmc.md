---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 3
  name: Openbmc Agentic Access
  operation_count: 13
  slug: openbmc-agentic-access
  summary_line: 13 operations · 6 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: API for interacting with OpenBMC baseboard management controller firmware, providing programmatic access to server hardware management and monitoring capabilities.
  name: OpenBMC API
  slug: openbmc-api
- description: The AccountService API from OpenBMC — 1 operation(s) for accountservice.
  name: OpenBMC AccountService API
  slug: openbmc-accountservice-api
- description: The Chassis API from OpenBMC — 1 operation(s) for chassis.
  name: OpenBMC Chassis API
  slug: openbmc-chassis-api
- description: The EventService API from OpenBMC — 1 operation(s) for eventservice.
  name: OpenBMC EventService API
  slug: openbmc-eventservice-api
- description: The Managers API from OpenBMC — 3 operation(s) for managers.
  name: OpenBMC Managers API
  slug: openbmc-managers-api
- description: The OpenBMC Redfish API API from OpenBMC — 1 operation(s) for openbmc redfish api.
  name: OpenBMC OpenBMC Redfish API API
  slug: openbmc-openbmc-redfish-api-api
- description: The SessionService API from OpenBMC — 1 operation(s) for sessionservice.
  name: OpenBMC SessionService API
  slug: openbmc-sessionservice-api
- description: The Systems API from OpenBMC — 3 operation(s) for systems.
  name: OpenBMC Systems API
  slug: openbmc-systems-api
- description: The UpdateService API from OpenBMC — 1 operation(s) for updateservice.
  name: OpenBMC UpdateService API
  slug: openbmc-updateservice-api
artifact_total: 15
collections:
- collection_type: open
  name: OpenBMC Redfish API
  slug: open-openbmc
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openbmc-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openbmc-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/openbmc/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openbmc
created: '2026-03-16'
description: OpenBMC is a Linux Foundation project producing an open source implementation of baseboard management controller firmware. Founded by Microsoft, Intel, IBM, Google, and Facebook, it provides a Linux-based firmware stack for managing and monitoring server hardware systems.
finops:
- name: Openbmc Finops
  service_category: API
  slug: openbmc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openbmc.png
layout: provider
modified: '2026-04-28'
name: OpenBMC
nav: Providers
network: true
overview: 'OpenBMC publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AccountService API, Chassis API, EventService API, and 5 more. Tagged areas include Firmware, Hardware, Linux Foundation, and Server.


  OpenBMC''s developer surface includes authentication, documentation, and 2 more developer resources.'
plans:
- name: Openbmc Plans Pricing
  plan_count: 3
  slug: openbmc-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Openbmc Rate Limits
  slug: openbmc-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.1
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openbmc/refs/heads/main/screenshots/openbmc-2026-06-20T190919.png
security:
- kind: authentication
  name: Openbmc Authentication
  slug: openbmc-authentication
  summary_line: apiKey · 1 scheme
slug: openbmc
tags:
- Firmware
- Hardware
- Linux Foundation
- Server
---
