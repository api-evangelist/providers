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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Alibaba Sentinel Agentic Access
  operation_count: 9
  slug: alibaba-sentinel-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The Authority Rules API from Alibaba Sentinel — 1 operation(s) for authority rules.
  name: Alibaba Sentinel Authority Rules API
  slug: alibaba-sentinel-authority-rules-api
- description: The Degrade Rules API from Alibaba Sentinel — 2 operation(s) for degrade rules.
  name: Alibaba Sentinel Degrade Rules API
  slug: alibaba-sentinel-degrade-rules-api
- description: The Flow Rules API from Alibaba Sentinel — 2 operation(s) for flow rules.
  name: Alibaba Sentinel Flow Rules API
  slug: alibaba-sentinel-flow-rules-api
- description: The System Rules API from Alibaba Sentinel — 1 operation(s) for system rules.
  name: Alibaba Sentinel System Rules API
  slug: alibaba-sentinel-system-rules-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alibaba Sentinel Dashboard Authority Rules API
  slug: open-alibaba-sentinel-authority-rules-api
- collection_type: open
  name: Alibaba Sentinel Dashboard Authority Rules Degrade Rules API
  slug: open-alibaba-sentinel-degrade-rules-api
- collection_type: open
  name: Alibaba Sentinel Dashboard Authority Rules Flow Rules API
  slug: open-alibaba-sentinel-flow-rules-api
- collection_type: open
  name: Alibaba Sentinel Dashboard Authority Rules System Rules API
  slug: open-alibaba-sentinel-system-rules-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alibaba-sentinel-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/alibaba-sentinel-sentinel-dashboard-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alibaba-sentinel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alibaba-sentinel-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/alibaba-sentinel-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alibaba-sentinel-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alibaba-sentinel-llms.txt
- group: company
  title: ''
  type: Website
  url: https://sentinelguard.io/
- group: docs
  title: ''
  type: Documentation
  url: https://sentinelguard.io/en-us/docs/introduction.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/alibaba/Sentinel/wiki/How-to-Use
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alibaba/Sentinel
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alibaba/sentinel-golang
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alibaba
- group: other
  title: ''
  type: Wiki
  url: https://github.com/alibaba/Sentinel/wiki
- group: operate
  title: ''
  type: Issues
  url: https://github.com/alibaba/Sentinel/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/alibaba/Sentinel/releases
created: '2026-03-26'
description: Alibaba Sentinel is a powerful open source flow control component enabling reliability, resilience, and monitoring for microservices. Originally developed by Alibaba and used in production at Alibaba for over 10 years, Sentinel provides flow control, traffic shaping, concurrency limiting, circuit breaking, and system adaptive overload protection. The project is written primarily in Java with a Go implementation (sentinel-golang) also available. Sentinel integrates with major frameworks including Spring Cloud, Dubbo, gRPC, Apache RocketMQ, and Servlet. It provides a real-time monitoring dashboard for visualizing metrics and configuring rules dynamically. The project is hosted on GitHub under the Alibaba organization and is widely adopted in cloud-native microservice architectures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alibaba-sentinel.png
json_schemas:
- name: Alibaba Sentinel Degrade Rule
  property_count: 0
  slug: degrade-rule
- name: Alibaba Sentinel Flow Rule
  property_count: 0
  slug: flow-rule
layout: provider
mcp_servers:
- description: ''
  name: Alibaba Sentinel MCP Server
  slug: alibaba-sentinel-mcp-server
modified: '2026-06-20'
name: Alibaba Sentinel
nav: Providers
network: true
overview: 'Alibaba Sentinel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authority Rules API, Degrade Rules API, Flow Rules API, and 1 more. Tagged areas include Alibaba, Circuit Breaker, Flow Control, Java, and Microservices.


  The Alibaba Sentinel catalog on APIs.io includes 1 Spectral governance ruleset.


  Alibaba Sentinel''s developer surface includes documentation, getting-started guide, GitHub presence, and 13 more developer resources.'
random_paper: 15
rules:
- effective_rule_count: 5
  extends: []
  name: Alibaba Sentinel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: alibaba-sentinel-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 14.4
    contract_quality: 45.6
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 14.4
    operational_transparency: 21.1
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alibaba-sentinel/refs/heads/main/screenshots/alibaba-sentinel-2026-07-25T195610.png
security:
- kind: domain-security
  name: Alibaba Sentinel Domain Security
  slug: alibaba-sentinel-domain-security
  summary_line: TLSv1.2
slug: alibaba-sentinel
tags:
- Alibaba
- Circuit Breaker
- Flow Control
- Java
- Microservices
- Rate Limiting
- Resilience
- Traffic Shaping
- Open-Source
- Cloud-Native
- Spring Cloud
website: https://sentinelguard.io/
---
