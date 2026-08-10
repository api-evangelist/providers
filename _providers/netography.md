---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 101
  human_in_the_loop: 14
  name: Netography Agentic Access
  operation_count: 173
  slug: netography-agentic-access
  summary_line: 173 operations · 101 acting · 14 human-in-the-loop
api_count: 28
apis:
- description: The Analytics API from Netography — 5 operation(s) for analytics.
  name: Netography Analytics API
  slug: netography-analytics-api
- description: The API Keys API from Netography — 3 operation(s) for api keys.
  name: Netography API Keys API
  slug: netography-api-keys-api
- description: The Authentication API from Netography — 3 operation(s) for authentication.
  name: Netography Authentication API
  slug: netography-authentication-api
- description: The Auto Thresholds API from Netography — 3 operation(s) for auto thresholds.
  name: Netography Auto Thresholds API
  slug: netography-auto-thresholds-api
- description: The Block List API from Netography — 1 operation(s) for block list.
  name: Netography Block List API
  slug: netography-block-list-api
- description: The Configuration API from Netography — 1 operation(s) for configuration.
  name: Netography Configuration API
  slug: netography-configuration-api
- description: The Detect and Respond - Context Creation Models API from Netography — 6 operation(s) for detect and respond - context creation models.
  name: Netography Detect and Respond - Context Creation Models API
  slug: netography-detect-and-respond-context-creation-models-api
- description: The Detect and Respond - Detection Categories API from Netography — 2 operation(s) for detect and respond - detection categories.
  name: Netography Detect and Respond - Detection Categories API
  slug: netography-detect-and-respond-detection-categories-api
- description: The Detect and Respond - Response Policies API from Netography — 5 operation(s) for detect and respond - response policies.
  name: Netography Detect and Respond - Response Policies API
  slug: netography-detect-and-respond-response-policies-api
- description: The Detect and Respond - Threshold Overrides API from Netography — 4 operation(s) for detect and respond - threshold overrides.
  name: Netography Detect and Respond - Threshold Overrides API
  slug: netography-detect-and-respond-threshold-overrides-api
- description: The Detect and Respond - Traffic Detection Models API from Netography — 6 operation(s) for detect and respond - traffic detection models.
  name: Netography Detect and Respond - Traffic Detection Models API
  slug: netography-detect-and-respond-traffic-detection-models-api
- description: The Integrations - Context API from Netography — 4 operation(s) for integrations - context.
  name: Netography Integrations - Context API
  slug: netography-integrations-context-api
- description: The Integrations - Response API from Netography — 3 operation(s) for integrations - response.
  name: Netography Integrations - Response API
  slug: netography-integrations-response-api
- description: The Intelligence API from Netography — 3 operation(s) for intelligence.
  name: Netography Intelligence API
  slug: netography-intelligence-api
- description: The Labels - IPs API from Netography — 6 operation(s) for labels - ips.
  name: Netography Labels - IPs API
  slug: netography-labels-ips-api
- description: The Labels - Ports API from Netography — 10 operation(s) for labels - ports.
  name: Netography Labels - Ports API
  slug: netography-labels-ports-api
- description: The MITRE ATT&CK API from Netography — 2 operation(s) for mitre att&ck.
  name: Netography MITRE ATT&CK API
  slug: netography-mitre-att-ck-api
- description: The Raw Records - Fetch API from Netography — 1 operation(s) for raw records - fetch.
  name: Netography Raw Records - Fetch API
  slug: netography-raw-records-fetch-api
- description: The Raw Records - Search API from Netography — 2 operation(s) for raw records - search.
  name: Netography Raw Records - Search API
  slug: netography-raw-records-search-api
- description: The Resellers API from Netography — 4 operation(s) for resellers.
  name: Netography Resellers API
  slug: netography-resellers-api
- description: The Roles API from Netography — 3 operation(s) for roles.
  name: Netography Roles API
  slug: netography-roles-api
- description: The Settings - Security API from Netography — 1 operation(s) for settings - security.
  name: Netography Settings - Security API
  slug: netography-settings-security-api
- description: The Settings - Traffic Classification API from Netography — 4 operation(s) for settings - traffic classification.
  name: Netography Settings - Traffic Classification API
  slug: netography-settings-traffic-classification-api
- description: The Tags API from Netography — 5 operation(s) for tags.
  name: Netography Tags API
  slug: netography-tags-api
- description: The Traffic Sources - Devices API from Netography — 11 operation(s) for traffic sources - devices.
  name: Netography Traffic Sources - Devices API
  slug: netography-traffic-sources-devices-api
- description: The Traffic Sources - DNS Devices API from Netography — 5 operation(s) for traffic sources - dns devices.
  name: Netography Traffic Sources - DNS Devices API
  slug: netography-traffic-sources-dns-devices-api
- description: The Traffic Sources - VPCs API from Netography — 8 operation(s) for traffic sources - vpcs.
  name: Netography Traffic Sources - VPCs API
  slug: netography-traffic-sources-vpcs-api
- description: The Users API from Netography — 3 operation(s) for users.
  name: Netography Users API
  slug: netography-users-api
artifact_total: 34
asyncapis:
- description: ''
  name: Netography Webhooks
  slug: netography-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netography-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netography-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netography-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netography.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fusion.vectra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fusion.vectra.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fusion.vectra.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fusion.vectra.ai/readme.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netography
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/netography-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/netography-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/netography-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/netography-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/netography-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/netography-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/netography-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/netography-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/netography-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/netography-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/netography-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/netography-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Netography Fusion is a SaaS network defense and observability platform (now Vectra Fusion) that ingests cloud VPC flow logs, DNS, and NetFlow/sFlow from AWS, Azure, GCP, IBM, and Oracle to deliver real-time network detection and response without sensors or agents. Its REST API (base https://api.netography.com) exposes analytics and NQL raw-record search, IP/port context labels, threat intelligence lookups, MITRE ATT&CK mapped detection models, response policies and block lists, cloud traffic sources, and context/response integrations. Authentication is a JWT bearer token minted from a NETOSECRET API key. An official MCP server (neto-mcp) exposes the query endpoints to agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netography.png
layout: provider
mcp_servers:
- description: ''
  name: netography-mcp.yml
  slug: netography-mcpyml
modified: '2026-07-20'
name: Netography
nav: Providers
network: true
overview: 'Netography publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, API Keys API, Authentication API, and 25 more. Tagged areas include Network Security, Network Detection and Response, Cloud Security, Network Observability, and Flow Data.


  The Netography catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Netography''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, and 17 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 64.5
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 28
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netography/refs/heads/main/screenshots/netography-2026-08-07T184939.png
security:
- kind: authentication
  name: Netography Authentication
  slug: netography-authentication
  summary_line: http-bearer-jwt/api-key-derived · 3 schemes
- kind: domain-security
  name: Netography Domain Security
  slug: netography-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netography Vulnerability Disclosure
  slug: netography-vulnerability-disclosure
  summary_line: disclosure policy published
slug: netography
tags:
- Network Security
- Network Detection and Response
- Cloud Security
- Network Observability
- Flow Data
- Threat Intelligence
- DDoS
- Cybersecurity
- MITRE ATT&CK
- Company
website: https://netography.com/
---
