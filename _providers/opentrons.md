---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 3
  name: Opentrons Agentic Access
  operation_count: 29
  slug: opentrons-agentic-access
  summary_line: 29 operations · 12 acting · 3 human-in-the-loop
api_count: 10
apis:
- description: The Opentrons Python Protocol API is an open-source Python framework for writing automated biology lab protocols that run on Opentrons Flex and OT-2 robots. It provides programmatic control over pipet
  name: Opentrons Python Protocol API
  slug: opentrons-python-protocol-api
- description: Query attached pipettes and grippers
  name: Opentrons Attached Instruments API
  slug: opentrons-attached-instruments-api
- description: Query attached hardware modules
  name: Opentrons Attached Modules API
  slug: opentrons-attached-modules-api
- description: Configure the Flex robot deck
  name: Opentrons Flex Deck Configuration API
  slug: opentrons-flex-deck-configuration-api
- description: Robot server health and status endpoints
  name: Opentrons Health API
  slug: opentrons-health-api
- description: Upload, manage, and analyze protocols
  name: Opentrons Protocol Management API
  slug: opentrons-protocol-management-api
- description: Robot-level control including estop and door status
  name: Opentrons Robot API
  slug: opentrons-robot-api
- description: Create and control protocol runs
  name: Opentrons Run Management API
  slug: opentrons-run-management-api
- description: Stateless atomic liquid handling commands
  name: Opentrons Simple Commands API
  slug: opentrons-simple-commands-api
- description: System time and robot control
  name: Opentrons System Control API
  slug: opentrons-system-control-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opentrons-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentrons-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opentrons.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opentrons.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://opentrons.com/pythonapi
- group: company
  title: ''
  type: News
  url: https://opentrons.com/about/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opentrons
- group: operate
  title: ''
  type: Support
  url: https://support.opentrons.com/
- group: operate
  title: ''
  type: Contact
  url: https://opentrons.com/contact-support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opentrons-labworks-inc.
- group: other
  title: ''
  type: X
  url: https://twitter.com/opentrons
- group: build
  title: ''
  type: ProtocolLibrary
  url: https://protocols.opentrons.com/
- group: build
  title: ''
  type: LabwareLibrary
  url: https://labware.opentrons.com/
- group: other
  title: ''
  type: ProtocolDesigner
  url: https://designer.opentrons.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/opentrons-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opentrons-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opentrons-finops.yml
created: '2026-06-13'
description: Opentrons is a lab automation platform providing a REST HTTP API and Python Protocol API for controlling liquid handling robots such as the Opentrons Flex and OT-2. Developers can programmatically manage protocols, control pipettes, run liquid handling workflows, manage labware, and integrate biology lab automation into their applications. The HTTP API operates on-robot over a local network and exposes OpenAPI-defined endpoints for protocol upload, run management, atomic liquid handling commands, and hardware control.
examples:
- key_count: 3
  name: Atomic Liquid Handling
  slug: atomic-liquid-handling
- key_count: 4
  name: Create Run From Protocol
  slug: create-run-from-protocol
finops:
- name: Opentrons Finops
  service_category: ''
  slug: opentrons-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentrons.png
json_schemas:
- name: Opentrons Command
  property_count: 12
  slug: opentrons-command
- name: Opentrons Run
  property_count: 13
  slug: opentrons-run
layout: provider
modified: '2026-06-13'
name: Opentrons
nav: Providers
network: true
overview: 'Opentrons publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Attached Instruments API, Attached Modules API, Flex Deck Configuration API, and 6 more. Tagged areas include Lab Automation, Liquid Handling, Robotics, Biology, and Life Sciences.


  The Opentrons catalog on APIs.io includes 1 Spectral governance ruleset.


  Opentrons'' developer surface includes documentation, getting-started guide, product news, support, and 13 more developer resources.'
plans:
- name: Opentrons Plans Pricing
  plan_count: 4
  slug: opentrons-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 0
  name: Opentrons Rate Limits
  slug: opentrons-rate-limits
rules:
- name: Opentrons API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: opentrons-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.0
  delta: -5.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.3
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/opentrons/refs/heads/main/screenshots/opentrons-2026-06-20T191056.png
security:
- kind: domain-security
  name: Opentrons Domain Security
  slug: opentrons-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opentrons
tags:
- Lab Automation
- Liquid Handling
- Robotics
- Biology
- Life Sciences
- Protocol Management
- Hardware Control
- Open Source
website: https://opentrons.com/
---
