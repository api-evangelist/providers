---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Tuya Agentic Access
  operation_count: 15
  slug: tuya-agentic-access
  summary_line: 15 operations · 7 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: The Tuya Device Management API provides endpoints to query, control, and manage IoT devices registered to a Tuya cloud project. Capabilities include device information retrieval, factory reset, device
  name: Tuya Device Management API
  slug: device-management
- description: The Tuya Smart Home API provides management capabilities for smart home deployments, including home and room management, device grouping, scene automation (tap-to-run and automation rules), member man
  name: Tuya Smart Home API
  slug: smart-home
- description: The Tuya Authorization API handles authentication for cloud-to-cloud integrations. Supports HMAC-SHA256 request signing using Access ID and Access Secret credentials. Provides token management endpoin
  name: Tuya Authorization API
  slug: authorization
- description: The Tuya Industry API provides enterprise IoT capabilities for non-consumer deployments including industrial device registration, device management, status queries, device control, user management, an
  name: Tuya Industry API
  slug: industry
- description: Control and command IoT devices
  name: Tuya Device Control API
  slug: tuya-device-control-api
- description: Query device operation and event logs
  name: Tuya Device Logs API
  slug: tuya-device-logs-api
- description: Manage user associations with devices
  name: Tuya Device Users API
  slug: tuya-device-users-api
- description: Query and manage IoT device information
  name: Tuya Devices API
  slug: tuya-devices-api
- description: Manage gateway sub-devices
  name: Tuya Sub Devices API
  slug: tuya-sub-devices-api
artifact_total: 26
collections:
- collection_type: open
  name: Tuya Device Management API
  slug: open-tuya-device-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tuya-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tuya-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tuya-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tuya-smart
- group: company
  title: ''
  type: Website
  url: https://developer.tuya.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tuya.com/en/docs/cloud/
- group: start
  title: ''
  type: Signup
  url: https://auth.tuya.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tuya.com/en/docs/iot/quick-start1?id=K95ztz9u9t89n
- group: other
  title: ''
  type: API Explorer
  url: https://developer.tuya.com/en/docs/cloud
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuya
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tuya.com/en/docs/iot/guide-explanation?id=Ke0wpiw0dwxun
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.tuya.com/en/docs/iot/compliance?id=Ka9t0qa3qihn3
- group: start
  title: ''
  type: Portal
  url: https://iot.tuya.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tuya-device-management-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tuya-device-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tuya-command-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tuya-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/tuya-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tuya-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/tuya/tuya-mcp-sdk
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/tuya/tuya-openclaw-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.tuya.com/llms.txt
created: '2025-03-01'
description: 'Tuya Smart is a global leading AI cloud platform service provider (NYSE: TUYA; HKEX: 2391) that enables IoT device manufacturers, solution providers, and app developers to build smart home and industrial IoT applications. The platform provides APIs for device management, smart home management, scene automation, data analytics, and industry-specific integrations across smart home, energy, security, and industrial verticals. Tuya operates six global data centers and handles over 100 million concurrent requests.'
examples:
- key_count: 4
  name: Tuya Get Device Example
  slug: tuya-get-device-example
- key_count: 4
  name: Tuya Send Device Commands Example
  slug: tuya-send-device-commands-example
finops:
- name: Tuya Finops
  service_category: IoT Cloud Platform
  slug: tuya-finops
image: https://images.tuya.com/smart/tuya-logo.png
json_schemas:
- name: Tuya Device Command
  property_count: 1
  slug: tuya-command
- name: Tuya Device
  property_count: 17
  slug: tuya-device
json_structures:
- name: Tuya Device Structure
  property_count: 0
  slug: tuya-device-structure
jsonld:
- class_count: 0
  name: Tuya Context
  property_count: 6
  slug: tuya-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Tuya
nav: Providers
network: true
overview: 'Tuya publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Device Control API, Device Logs API, Device Users API, and 2 more. Tagged areas include IoT, Smart Home, Devices, Cloud Platform, and Automation.


  The Tuya catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tuya''s developer surface includes authentication, documentation, signup flow, getting-started guide, developer portal, and 17 more developer resources.'
plans:
- name: Tuya Plans Pricing
  plan_count: 1
  slug: tuya-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 1
  name: Tuya Rate Limits
  slug: tuya-rate-limits
rules:
- name: Tuya API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tuya-jsonschema-spectral-rules
- name: Tuya API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 7
  slug: tuya-rules
score:
  band: developing
  composite: 52.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 66.4
    developer_ergonomics: 54.3
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tuya/refs/heads/main/screenshots/tuya-2026-06-20T195841.png
security:
- kind: authentication
  name: Tuya Authentication
  slug: tuya-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tuya Domain Security
  slug: tuya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: tuya-smart-control
  slug: tuya-smart-control
slug: tuya
tags:
- IoT
- Smart Home
- Devices
- Cloud Platform
- Automation
- Industrial IoT
- Device Management
website: https://developer.tuya.com/en/
---
