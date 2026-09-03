---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.5
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: The documented SNYPR / Unified Defense SIEM web-service surface reached at /ws on the tenant host — token generation and validation, incident management and actions, activity, asset, geolocation, list
  name: Securonix Web Services (SNYPR REST API)
  slug: securonix-web-services-snypr-rest-api
- description: Asynchronous search microservice over the Securonix data lake — trigger a Spotter or SQL query, poll its execution status, page results, and cancel a running query. Bearer JWT via the snypr-service-ga
  name: Securonix Spotter API
  slug: securonix-spotter-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Adversaries API from Securonix — 3 operation(s) for adversaries.
  name: Securonix Adversaries API
  slug: securonix-adversaries-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Assets API from Securonix — 3 operation(s) for assets.
  name: Securonix Assets API
  slug: securonix-assets-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Attachments (Files) API from Securonix — 2 operation(s) for attachments (files).
  name: Securonix Attachments (Files) API
  slug: securonix-attachments-files-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Attack Pattern API from Securonix — 3 operation(s) for attack pattern.
  name: Securonix Attack Pattern API
  slug: securonix-attack-pattern-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Authentication API from Securonix — 2 operation(s) for authentication.
  name: Securonix Authentication API
  slug: securonix-authentication-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Basic Search API from Securonix — 3 operation(s) for basic search.
  name: Securonix Basic Search API
  slug: securonix-basic-search-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Campaign API from Securonix — 3 operation(s) for campaign.
  name: Securonix Campaign API
  slug: securonix-campaign-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Connectors API from Securonix — 2 operation(s) for connectors.
  name: Securonix Connectors API
  slug: securonix-connectors-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Course of Action API from Securonix — 3 operation(s) for course of action.
  name: Securonix Course of Action API
  slug: securonix-course-of-action-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: Config Datasource Controller
  name: Securonix Datasource Management API
  slug: securonix-datasource-management-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: List of monitored devices and metadata.
  name: Securonix Device Monitoring API
  slug: securonix-device-monitoring-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Events API from Securonix — 3 operation(s) for events.
  name: Securonix Events API
  slug: securonix-events-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Exploit Target API from Securonix — 3 operation(s) for exploit target.
  name: Securonix Exploit Target API
  slug: securonix-exploit-target-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Identity API from Securonix — 3 operation(s) for identity.
  name: Securonix Identity API
  slug: securonix-identity-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Incident API from Securonix — 3 operation(s) for incident.
  name: Securonix Incident API
  slug: securonix-incident-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Indicators API from Securonix — 3 operation(s) for indicators.
  name: Securonix Indicators API
  slug: securonix-indicators-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Infrastructure API from Securonix — 3 operation(s) for infrastructure.
  name: Securonix Infrastructure API
  slug: securonix-infrastructure-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Intrusion Set API from Securonix — 3 operation(s) for intrusion set.
  name: Securonix Intrusion Set API
  slug: securonix-intrusion-set-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Investigations API from Securonix — 2 operation(s) for investigations.
  name: Securonix Investigations API
  slug: securonix-investigations-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: Manage Datasource Jobs Controller
  name: Securonix Job Management API
  slug: securonix-job-management-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Malware API from Securonix — 3 operation(s) for malware.
  name: Securonix Malware API
  slug: securonix-malware-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Notes API from Securonix — 3 operation(s) for notes.
  name: Securonix Notes API
  slug: securonix-notes-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Attribute Sources API from Securonix — 1 operation(s) for object attribute sources.
  name: Securonix Object Attribute Sources API
  slug: securonix-object-attribute-sources-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Attributes API from Securonix — 3 operation(s) for object attributes.
  name: Securonix Object Attributes API
  slug: securonix-object-attributes-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Comments API from Securonix — 3 operation(s) for object comments.
  name: Securonix Object Comments API
  slug: securonix-object-comments-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Relation Counts API from Securonix — 1 operation(s) for object relation counts.
  name: Securonix Object Relation Counts API
  slug: securonix-object-relation-counts-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Relationship Attributes API from Securonix — 2 operation(s) for object relationship attributes.
  name: Securonix Object Relationship Attributes API
  slug: securonix-object-relationship-attributes-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Relationship Comments API from Securonix — 2 operation(s) for object relationship comments.
  name: Securonix Object Relationship Comments API
  slug: securonix-object-relationship-comments-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Relationships API from Securonix — 2 operation(s) for object relationships.
  name: Securonix Object Relationships API
  slug: securonix-object-relationships-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Sources API from Securonix — 2 operation(s) for object sources.
  name: Securonix Object Sources API
  slug: securonix-object-sources-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Summary API from Securonix — 1 operation(s) for object summary.
  name: Securonix Object Summary API
  slug: securonix-object-summary-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Tags API from Securonix — 2 operation(s) for object tags.
  name: Securonix Object Tags API
  slug: securonix-object-tags-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Object Watchlist API from Securonix — 3 operation(s) for object watchlist.
  name: Securonix Object Watchlist API
  slug: securonix-object-watchlist-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: Config Resource Parser Controller
  name: Securonix Parser Management API
  slug: securonix-parser-management-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Policy Management API allows users to configure policies in the Unified Defense SIEM platform (UDS).
  name: Securonix Policy Management API
  slug: securonix-policy-management-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Report API from Securonix — 3 operation(s) for report.
  name: Securonix Report API
  slug: securonix-report-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Search API from Securonix — 2 operation(s) for search.
  name: Securonix Search API
  slug: securonix-search-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Signatures API from Securonix — 3 operation(s) for signatures.
  name: Securonix Signatures API
  slug: securonix-signatures-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Sources API from Securonix — 2 operation(s) for sources.
  name: Securonix Sources API
  slug: securonix-sources-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Spearphish Events API from Securonix — 3 operation(s) for spearphish events.
  name: Securonix Spearphish Events API
  slug: securonix-spearphish-events-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: Health Check Controller
  name: Securonix Supporting API
  slug: securonix-supporting-api-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The System API from Securonix — 2 operation(s) for system.
  name: Securonix System API
  slug: securonix-system-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Tags API from Securonix — 2 operation(s) for tags.
  name: Securonix Tags API
  slug: securonix-tags-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Tasks API from Securonix — 2 operation(s) for tasks.
  name: Securonix Tasks API
  slug: securonix-tasks-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: MITRE ATT&CK threat coverage analysis API for analyzing policy coverage across tactics and techniques.
  name: Securonix Threat Coverage API
  slug: securonix-threat-coverage-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The TLP API from Securonix — 3 operation(s) for tlp.
  name: Securonix TLP API
  slug: securonix-tlp-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Tool API from Securonix — 3 operation(s) for tool.
  name: Securonix Tool API
  slug: securonix-tool-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The TTP API from Securonix — 3 operation(s) for ttp.
  name: Securonix TTP API
  slug: securonix-ttp-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Vulnerability API from Securonix — 3 operation(s) for vulnerability.
  name: Securonix Vulnerability API
  slug: securonix-vulnerability-api
- baseURL: https://policymanagement.api.securonix.net
  baseurl_source: declared
  description: The Whitelist Rules API from Securonix — 5 operation(s) for whitelist rules.
  name: Securonix Whitelist Rules API
  slug: securonix-whitelist-rules-api
artifact_total: 58
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/securonix-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/securonix-policy-management-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/securonix-datasource-onboarding-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/securonix-device-monitoring-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/securonix-threatq-api-overlay.yaml
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
overview: 'Securonix publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Adversaries API, Assets API, Attachments (Files) API, and 47 more. Tagged areas include Security, SIEM, UEBA, SOAR, and Threat Intelligence.


  Securonix''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 26 more developer resources.'
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
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 56.8
    developer_ergonomics: 8.9
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 33.9
  provenance:
    conformance: derived
    contracts:
      callable: 96.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/securonix/refs/heads/main/screenshots/securonix-2026-09-02T154728.png
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
