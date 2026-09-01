---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Netdata Agentic Access
  operation_count: 79
  slug: netdata-agentic-access
  summary_line: 79 operations · 12 acting
api_count: 1
apis:
- description: Everything related to alerts
  name: Netdata alerts API
  slug: netdata-alerts-api
- description: Everything related to chart instances - DO NOT USE IN NEW CODE - use contexts instead
  name: Netdata charts API
  slug: netdata-charts-api
artifact_total: 59
collections:
- collection_type: postman
  name: Netdata agent API
  slug: postman-netdata-agent-api
- collection_type: postman
  name: Netdata agent alerts API
  slug: postman-netdata-alerts-api
- collection_type: postman
  name: Netdata agent authentication API
  slug: postman-netdata-authentication-api
- collection_type: postman
  name: Netdata agent badges API
  slug: postman-netdata-badges-api
- collection_type: postman
  name: Netdata agent charts API
  slug: postman-netdata-charts-api
- collection_type: postman
  name: Netdata agent claiming API
  slug: postman-netdata-claiming-api
- collection_type: postman
  name: Netdata agent config API
  slug: postman-netdata-config-api
- collection_type: postman
  name: Netdata agent contexts API
  slug: postman-netdata-contexts-api
- collection_type: postman
  name: Netdata agent data API
  slug: postman-netdata-data-api
- collection_type: postman
  name: Netdata agent dyncfg API
  slug: postman-netdata-dyncfg-api
- collection_type: postman
  name: Netdata agent functions API
  slug: postman-netdata-functions-api
- collection_type: postman
  name: Netdata agent management API
  slug: postman-netdata-management-api
- collection_type: postman
  name: Netdata agent nodes API
  slug: postman-netdata-nodes-api
- collection_type: postman
  name: Netdata agent registry API
  slug: postman-netdata-registry-api
- collection_type: postman
  name: Netdata agent settings API
  slug: postman-netdata-settings-api
- collection_type: postman
  name: Netdata agent streaming API
  slug: postman-netdata-streaming-api
- collection_type: postman
  name: Netdata agent variables API
  slug: postman-netdata-variables-api
- collection_type: postman
  name: Netdata agent versions API
  slug: postman-netdata-versions-api
- collection_type: postman
  name: Netdata agent webrtc API
  slug: postman-netdata-webrtc-api
- collection_type: postman
  name: Netdata agent weights API
  slug: postman-netdata-weights-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Netdata agent API
  slug: open-netdata-agent-api
- collection_type: open
  name: Netdata agent alerts API
  slug: open-netdata-alerts-api
- collection_type: open
  name: Netdata agent authentication API
  slug: open-netdata-authentication-api
- collection_type: open
  name: Netdata agent badges API
  slug: open-netdata-badges-api
- collection_type: open
  name: Netdata agent charts API
  slug: open-netdata-charts-api
- collection_type: open
  name: Netdata agent claiming API
  slug: open-netdata-claiming-api
- collection_type: open
  name: Netdata agent config API
  slug: open-netdata-config-api
- collection_type: open
  name: Netdata agent contexts API
  slug: open-netdata-contexts-api
- collection_type: open
  name: Netdata agent data API
  slug: open-netdata-data-api
- collection_type: open
  name: Netdata agent dyncfg API
  slug: open-netdata-dyncfg-api
- collection_type: open
  name: Netdata agent functions API
  slug: open-netdata-functions-api
- collection_type: open
  name: Netdata agent management API
  slug: open-netdata-management-api
- collection_type: open
  name: Netdata agent nodes API
  slug: open-netdata-nodes-api
- collection_type: open
  name: Netdata agent registry API
  slug: open-netdata-registry-api
- collection_type: open
  name: Netdata agent settings API
  slug: open-netdata-settings-api
- collection_type: open
  name: Netdata agent streaming API
  slug: open-netdata-streaming-api
- collection_type: open
  name: Netdata agent variables API
  slug: open-netdata-variables-api
- collection_type: open
  name: Netdata agent versions API
  slug: open-netdata-versions-api
- collection_type: open
  name: Netdata agent webrtc API
  slug: open-netdata-webrtc-api
- collection_type: open
  name: Netdata agent weights API
  slug: open-netdata-weights-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/netdata/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netdata-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/netdata-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netdata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netdata-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.netdata.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.netdata.cloud/docs/developer-and-contributor-corner/rest-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netdata-cloud
- group: other
  title: ''
  type: X
  url: https://x.com/netdatahq
- group: company
  title: ''
  type: Blog
  url: https://www.netdata.cloud/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.netdata.cloud/docs/netdata-agent/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netdata.cloud/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.netdata.cloud/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/netdata-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/netdata-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/netdata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/netdata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/netdata-finops.yml
created: '2026-06-12'
description: Netdata is a real-time infrastructure monitoring and observability platform that collects per-second metrics from physical servers, virtual machines, cloud deployments, Kubernetes clusters, and IoT devices. It provides a REST API for querying metrics, alerts, and configuration on individual nodes (Agent API) as well as a Cloud API for programmatic access to Netdata Cloud resources including spaces, rooms, and nodes across distributed infrastructure. Authentication uses Bearer tokens generated from the Netdata Cloud account settings, with scopes controlling access to agent UI, Grafana plugin, MCP, and full API access. The platform includes AI-powered troubleshooting, role-based access control, and supports both cloud-hosted and on-premises deployments.
examples:
- key_count: 5
  name: Netdata Alerts Example
  slug: netdata-alerts-example
- key_count: 9
  name: Netdata Charts List Example
  slug: netdata-charts-list-example
- key_count: 19
  name: Netdata Data Query Example
  slug: netdata-data-query-example
- key_count: 20
  name: Netdata Node Info Example
  slug: netdata-node-info-example
finops:
- name: Netdata Finops
  service_category: Monitoring and Observability
  slug: netdata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netdata.png
json_schemas:
- name: Netdata Alert
  property_count: 13
  slug: netdata-alert
- name: Netdata Chart
  property_count: 13
  slug: netdata-chart
- name: Netdata Node
  property_count: 18
  slug: netdata-node
jsonld:
- class_count: 15
  name: Netdata Context
  property_count: 34
  slug: netdata-context
layout: provider
modified: '2026-06-12'
name: Netdata
nav: Providers
network: true
overview: 'Netdata publishes 2 APIs on the [APIs.io](https://apis.io/) network: alerts API and charts API. Tagged areas include Monitoring, Observability, Infrastructure, Metrics, and Alerts.


  The Netdata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Netdata''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 14 more developer resources.'
plans:
- name: Netdata Plans Pricing
  plan_count: 3
  slug: netdata-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Netdata Rate Limits
  slug: netdata-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Netdata API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: netdata-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 66.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netdata/refs/heads/main/screenshots/netdata-2026-06-20T190147.png
security:
- kind: authentication
  name: Netdata Authentication
  slug: netdata-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Netdata Domain Security
  slug: netdata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Netdata Trust Center
  slug: netdata-trust-center
  summary_line: SOC 2, ISO 27001
slug: netdata
tags:
- Monitoring
- Observability
- Infrastructure
- Metrics
- Alerts
- Real-Time
- APM
- DevOps
website: https://www.netdata.cloud/
---
