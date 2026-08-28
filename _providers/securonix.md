---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-08-26'
api_count: 6
apis:
- description: Create, update, enable/disable, delete and fetch Securonix Unified Defense SIEM detection policies, plus MITRE ATT&CK threat-coverage metrics and technique details. OpenAPI 3.1.0, 10 operations, JWT b
  name: Securonix Policy Management API
  slug: securonix-policy-management-api
- description: Configure API-based and Syslog-based data sources, syslog sources and filters, resource groups, parser (CRP) content and activity-import job summaries for Securonix Unified Defense SIEM. OpenAPI 3.0.3
  name: Securonix Datasource Onboarding API
  slug: securonix-datasource-onboarding-api
- description: List monitored devices and their metadata from Securonix Unified Defense SIEM. OpenAPI 3.0.3, one operation, token header authentication against the tenant SNYPR web-services host.
  name: Securonix Device Monitoring API
  slug: securonix-device-monitoring-api
- description: The ThreatQ threat intelligence platform API — adversaries, indicators, events, assets, attributes, signatures, TLP, scoring, exports and integrations. OpenAPI 3.0.0, 209 operations, OAuth2 password g
  name: Securonix ThreatQ API
  slug: securonix-threatq-api
- description: The documented SNYPR / Unified Defense SIEM web-service surface reached at /ws on the tenant host — token generation and validation, incident management and actions, activity, asset, geolocation, list
  name: Securonix Web Services (SNYPR REST API)
  slug: securonix-web-services-snypr-rest-api
- description: Asynchronous search microservice over the Securonix data lake — trigger a Spotter or SQL query, poll its execution status, page results, and cancel a running query. Bearer JWT via the snypr-service-ga
  name: Securonix Spotter API
  slug: securonix-spotter-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.securonix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.securonix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.securonix.com/r/content/rest-api-categories.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.securonix.com/r/content/developer-guide.htm
- group: company
  title: ''
  type: Blog
  url: https://www.securonix.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Securonix
- group: operate
  title: ''
  type: Support
  url: https://www.securonix.com/services/support-services/
- group: start
  title: ''
  type: SignUp
  url: https://connect.securonix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.securonix.com/securonix-end-user-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.securonix.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.securonix.com/gdpr-compliance/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/securonix-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/securonix-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/securonix-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/securonix-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/securonix-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/securonix-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/securonix-problem-types.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/securonix-connectorinfo.schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/securonix-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/securonix-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/securonix-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/securonix-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/securonix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/securonix-rate-limits.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/securonix-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/securonix-well-known.yml
created: '2026-08-26'
description: Securonix is a cybersecurity company whose Unified Defense SIEM platform combines security information and event management, user and entity behavior analytics (UEBA), security orchestration automation and response (SOAR), and — following the June 2025 acquisition of ThreatQuotient — the ThreatQ threat intelligence platform. The platform ingests activity data from hundreds of connectors, applies behavior analytics and MITRE ATT&CK-aligned detection policies, and drives incident workflows for security operations teams. Securonix publishes a Developer Guide covering token-based web services, a Spotter search API, and four OpenAPI 3.x definitions on SwaggerHub for Policy Management, Datasource Onboarding, Device Monitoring and ThreatQ.
image: https://www.securonix.com/wp-content/uploads/2025/09/securonix_logo_color_rgb.png
json_schemas:
- name: ConnectorInfo
  property_count: 13
  slug: securonix-connectorinfo.schema
layout: provider
mcp_servers:
- description: ''
  name: Securonix MCP (www.securonix.com)
  slug: securonix-mcp-wwwsecuronixcom
modified: '2026-08-26'
name: Securonix
nav: Providers
network: true
overview: 'Securonix publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Policy Management API, Datasource Onboarding API, Device Monitoring API, and 1 more. Tagged areas include Security, SIEM, UEBA, SOAR, and Threat Intelligence.


  Securonix''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Securonix Plans Pricing
  plan_count: 0
  slug: securonix-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Securonix Rate Limits
  slug: securonix-rate-limits
score:
  band: developing
  composite: 44.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 16.7
    contract_quality: 50.5
    developer_ergonomics: 49.4
    discoverability: 85.2
    governance: 16.7
    operational_transparency: 21.1
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Securonix Authentication
  slug: securonix-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Securonix Domain Security
  slug: securonix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: securonix
tags:
- Security
- SIEM
- UEBA
- SOAR
- Threat Intelligence
- Security Analytics
- Cybersecurity
- Log Management
- Detection and Response
- MITRE ATT&CK
website: https://www.securonix.com/
---
