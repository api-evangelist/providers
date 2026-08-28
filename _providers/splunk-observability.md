---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-08-26'
api_count: 49
apis:
- description: 'APIs to retrieve the upstream and downstream dependencies for a given service, as well as to retrieve the complete graph-based topology of all services in a given environment and time window. You can '
  name: Splunk Observability Cloud APM service topology
  slug: splunk-observability-apm-service-topology-api
- description: APIs to manage visibility filters on indexed and unindexed span tags in Splunk APM. These filters identify and hide span tag values that might contain sensitive data from everywhere in Splunk APM. Not
  name: Splunk Observability Cloud APM visibility filters
  slug: splunk-observability-apm-visibility-filters-api
- description: The Audit Events API provides programmatic access to your organization's audit trail,
  name: Splunk Observability Cloud Splunk Observability Cloud Audit Events
  slug: splunk-observability-audit-events-api
- description: The Automated archival API from Splunk Observability Cloud — 6 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Automated archival
  slug: splunk-observability-automatedarchival-api
- description: API for sending historical metric time series (MTS) data points to Splunk Observability Cloud, overwriting any existing data points for the same time period.
  name: Splunk Observability Cloud Backfill
  slug: splunk-observability-backfill-api
- description: API for creating, retrieving, updating, and deleting charts.
  name: Splunk Observability Cloud Charts
  slug: splunk-observability-charts-api
- description: The Client Inventory API from Splunk Observability Cloud — 5 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2/fm-service/v1.
  name: Splunk Observability Cloud Client Inventory
  slug: splunk-observability-client-inventory-api
- description: API for creating a new dashboard group, retrieving the properties of one or more dashboard groups, updating the properties of a single dashboard group, making a clone of a dashboard to a group, adding
  name: Splunk Observability Cloud Dashboard groups
  slug: splunk-observability-dashboard-groups-api
- description: API for creating, retrieving, updating, and deleting dashboards.
  name: Splunk Observability Cloud Dashboards
  slug: splunk-observability-dashboards-api
- description: API for creating, retrieving, updating, and deleting data links.
  name: Splunk Observability Cloud Data links
  slug: splunk-observability-datalinks-api
- description: API for creating, retrieving, updating, and deleting detectors.
  name: Splunk Observability Cloud Detectors
  slug: splunk-observability-detectors-api
- description: API for retrieving or clearing incidents and muting "critical-notifications".
  name: Splunk Observability Cloud Incidents and alerts
  slug: splunk-observability-incidents-api
- description: The Send traces, metrics and events API from Splunk Observability Cloud — 5 operation(s) at https://ingest.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Send traces, metrics and events
  slug: splunk-observability-ingest-data-api
- description: API for creating, retrieving, updating, and deleting integrations, which define the connection between an external system and Splunk Observability Cloud.
  name: Splunk Observability Cloud Integrations
  slug: splunk-observability-integrations-api
- description: The Metric ruleset API from Splunk Observability Cloud — 7 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Metric ruleset
  slug: splunk-observability-metric-ruleset-api
- description: API for creating, retrieving, updating, and deleting metric metadata and MTS metadata.
  name: Splunk Observability Cloud Metrics metadata
  slug: splunk-observability-metrics-metadata-api
- description: API for creating, updating, retrieving, and deleting custom navigators.
  name: Splunk Observability Cloud Navigators
  slug: splunk-observability-navigator-api
- description: API for creating, updating, retrieving, deleting, and rotating org tokens.
  name: Splunk Observability Cloud Org tokens
  slug: splunk-observability-org-tokens-api
- description: API for creating, updating, retrieving, and deleting organizations.
  name: Splunk Observability Cloud Organizations
  slug: splunk-observability-organizations-api
- description: The Passwords API from Splunk Observability Cloud — 1 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Passwords
  slug: splunk-observability-passwords-api
- description: The Retrieve events V1 API from Splunk Observability Cloud — 1 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v1.
  name: Splunk Observability Cloud Retrieve events V1
  slug: splunk-observability-retrieve-events-v1-api
- description: The Retrieve events V2 API from Splunk Observability Cloud — 1 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Retrieve events V2
  slug: splunk-observability-retrieve-events-v2-api
- description: API for retrieving data points from a metric times series (MTS) for a given time window
  name: Splunk Observability Cloud Retrieve metric time series (MTS)
  slug: splunk-observability-retrieve-timeserieswindow-api
- description: API for assigning, retrieving, and removing roles associated with an organization, user, or token.
  name: Splunk Observability Cloud Role
  slug: splunk-observability-roles-api
- description: The Session tokens API from Splunk Observability Cloud — 2 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Session tokens
  slug: splunk-observability-sessiontokens-api
- description: API for streaming data to SignalFlow and managing SignalFlow background
  name: Splunk Observability Cloud SignalFlow
  slug: splunk-observability-signalflow-api
- description: API for creating, retrieiving, and managing service level objectives (SLOs).
  name: Splunk Observability Cloud SLOs
  slug: splunk-observability-slo-api
- description: API for creating, updating, retrieving, and deleting Splunk Synthetic Monitoring API tests using the legacy service routes (/tests/api).
  name: Splunk Observability Cloud Synthetics API tests (V1)
  slug: splunk-observability-synthetics-api-tests-api
- description: V2 API for creating, updating, retrieving, and deleting Splunk Synthetic Monitoring API tests.
  name: Splunk Observability Cloud Synthetics API tests V2
  slug: splunk-observability-synthetics-api-tests-v2-api
- description: API for retrieving artifacts used in Splunk Synthetic Monitoring tests.
  name: Splunk Observability Cloud Synthetics artifacts
  slug: splunk-observability-synthetics-artifacts-api
- description: API for retrieving audit log in Splunk Synthetic Monitoring.
  name: Splunk Observability Cloud Synthetics audit
  slug: splunk-observability-synthetics-audits-api
- description: API for creating, updating, retrieving, and deleting Splunk Synthetic Monitoring Browser tests using the legacy service routes (/tests/browser). Requests use the legacy step shape (selectorType and se
  name: Splunk Observability Cloud Synthetics Browser tests (V1)
  slug: splunk-observability-synthetics-browser-api
- description: V2 API for creating, updating, retrieving, and deleting Splunk Synthetic Monitoring Browser tests.
  name: Splunk Observability Cloud Synthetics Browser tests V2
  slug: splunk-observability-synthetics-browser-v2-api
- description: API for creating, updating, and deleting Certificate Authority (CA) certificates.
  name: Splunk Observability Cloud Synthetics CA certificates
  slug: splunk-observability-synthetics-ca-certs-api
- description: API for creating, updating, and deleting client certificates.
  name: Splunk Observability Cloud Synthetics certificates
  slug: splunk-observability-synthetics-certificates-api
- description: API for retrieving a list of Chrome flags supported in Splunk Synthetic Monitoring browser tests.
  name: Splunk Observability Cloud Synthetics Chrome flags
  slug: splunk-observability-synthetics-chrome-flags-api
- description: API for retrieving devices used in Splunk Synthetic Monitoring tests.
  name: Splunk Observability Cloud Synthetics devices
  slug: splunk-observability-synthetics-devices-api
- description: API for creating, updating, ending, and deleting downtime configurations.
  name: Splunk Observability Cloud Synthetics downtime configurations
  slug: splunk-observability-synthetics-downtime-configurations-api
- description: The Synthetics excluded files API from Splunk Observability Cloud — 1 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2/synthetics.
  name: Splunk Observability Cloud Synthetics excluded files
  slug: splunk-observability-synthetics-excluded-files-api
- description: The Synthetics global variables API from Splunk Observability Cloud — 5 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2/synthetics.
  name: Splunk Observability Cloud Synthetics global variables
  slug: splunk-observability-synthetics-global-variables-api
- description: API for creating, updating, retrieving, and deleting Synthetics HTTP tests.
  name: Splunk Observability Cloud Synthetics HTTP tests
  slug: splunk-observability-synthetics-http-tests-api
- description: API for managing locations used in Splunk Synthetic Monitoring tests.
  name: Splunk Observability Cloud Synthetics locations
  slug: splunk-observability-synthetics-locations-api
- description: API for creating, updating, retrieving, and deleting Port tests in Splunk Synthetic Monitoring.
  name: Splunk Observability Cloud Synthetics Port tests
  slug: splunk-observability-synthetics-ports-tests-api
- description: The Synthetics runs API from Splunk Observability Cloud — 1 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2/synthetics.
  name: Splunk Observability Cloud Synthetics runs
  slug: splunk-observability-synthetics-runs-api
- description: API for creating, updating, and deleting SSL Certificate Tests.
  name: Splunk Observability Cloud Synthetics SSL Certificate Tests
  slug: splunk-observability-synthetics-ssl-tests-api
- description: API for retrieving and deleting tests in Splunk Synthetic Monitoring.
  name: Splunk Observability Cloud Synthetics tests
  slug: splunk-observability-synthetics-tests-api
- description: API for creating, updating, deleting, adding members, and removing members from teams.
  name: Splunk Observability Cloud Teams
  slug: splunk-observability-teams-api
- description: The Download APM traces API from Splunk Observability Cloud — 3 operation(s) at https://api.{REALM}.observability.splunkcloud.com/v2.
  name: Splunk Observability Cloud Download APM traces
  slug: splunk-observability-trace-id-api
- description: Hosted Model Context Protocol server for Splunk Observability Cloud, using the streamable HTTP transport. Twelve tools across metrics/SignalFlow, APM and alerting. Authenticated with X-SF-REALM and X-
  name: Splunk Observability Cloud MCP Server
  slug: splunk-observability-mcp
artifact_total: 58
asyncapis:
- description: The SignalFlow streaming analytics service. A client opens a WebSocket connection, authenticates with a session token within 5 seconds, then starts computations on named channels and receives control,
  name: Splunk Observability Cloud — SignalFlow streaming
  slug: splunk-observability-signalflow-asyncapi
- description: ''
  name: Splunk Observability Webhooks
  slug: splunk-observability-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/splunk-observability-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/splunk-observability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splunk-observability-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/splunk/
- group: start
  title: ''
  type: Portal
  url: https://dev.splunk.com/observability/reference/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.splunk.com/observability/reference/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.splunk.com/observability/docs/apibasics/api_list/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/splunk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.splunk.com/observability/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.splunk.com/observability/docs/apibasics/
- group: company
  title: ''
  type: Website
  url: https://www.splunk.com/en_us/products/observability.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.splunk.com/en_us/products/pricing/observability.html
- group: commercial
  title: ''
  type: Plans
  url: plans/splunk-observability-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/splunk-observability-rate-limits.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.splunk.com/en_us/download/o11y-cloud-free-trial.html
- group: start
  title: ''
  type: Login
  url: https://login.signalfx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splunk.com/en_us/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splunk.com/en_us/legal/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.splunk.com/en_us/support-and-services.html
- group: company
  title: ''
  type: Blog
  url: https://www.splunk.com/en_us/blog/observability.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.splunk.com/en/splunk-observability-cloud/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/splunk-observability-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signalfx.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/splunk-observability-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.splunk.com/en/splunk-observability-cloud/administer/org-reference-info/view-your-realm-api-endpoints-and-organization
- group: auth
  title: ''
  type: Authentication
  url: authentication/splunk-observability-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/splunk-observability-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/splunk-observability-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/splunk-observability-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/splunk-observability-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.splunk.com/en_us/about-splunk/splunk-data-security-and-privacy/compliance-at-splunk.html
- group: auth
  title: ''
  type: Security
  url: https://advisory.splunk.com/report
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/splunk-observability-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splunk-observability-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/splunk-observability-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/splunk-observability-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/splunk-observability-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/splunk-observability-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/splunk-observability-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/splunk-observability-signalflow-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/splunk-observability-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splunk-observability-llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.splunk.com/en/splunk-observability-cloud
created: '2026-08-19'
description: 'Splunk Observability Cloud is the observability platform Splunk built on SignalFx and now runs as part of Cisco: infrastructure monitoring, APM, real user monitoring, synthetics, Log Observer and incident response over OpenTelemetry-native ingest. Its control plane is the largest API surface Splunk operates — 48 OpenAPI documents and 242 operations covering charts, dashboards, detectors, incidents and muting rules, metrics and dimension metadata, SignalFlow, SLOs, org and session tokens, teams, integrations and twenty distinct Synthetics services — alongside a SignalFlow WebSocket/SSE streaming interface and a hosted MCP server for agents. Authentication is a single X-SF-TOKEN header, the realm is part of the hostname, and Splunk publishes no downloadable spec file: the contract is embedded in its own reference pages.'
image: https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Splunk MCP server (Splunk AI Assistant in Observability Cloud)
  slug: splunk-mcp-server-splunk-ai-assistant-in-observability-cloud
modified: '2026-08-19'
name: Splunk Observability Cloud
nav: Providers
network: true
overview: 'Splunk Observability Cloud publishes 48 APIs on the [APIs.io](https://apis.io/) network, including APM service topology, APM visibility filters, Splunk Observability Cloud Audit Events, and 45 more. Tagged areas include Observability, APM, Monitoring, Telemetry, and OpenTelemetry.


  The Splunk Observability Cloud catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Splunk Observability Cloud''s developer surface includes developer portal, documentation, API reference, getting-started guide, pricing, signup flow, support, and 38 more developer resources.'
plans:
- name: Splunk Observability Plans Pricing
  plan_count: 10
  slug: splunk-observability-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Splunk Observability Rate Limits
  slug: splunk-observability-rate-limits
score:
  band: strong
  composite: 60.6
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 21.2
    developer_ergonomics: 73.2
    discoverability: 79.6
    governance: 30.3
    operational_transparency: 81.6
  previous_composite: 60.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 48
      marker_coverage: 100.0
      total: 48
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Splunk Observability Authentication
  slug: splunk-observability-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Splunk Observability Domain Security
  slug: splunk-observability-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Splunk Observability Vulnerability Disclosure
  slug: splunk-observability-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Splunk Observability Trust Center
  slug: splunk-observability-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: splunk-observability
tags:
- Observability
- APM
- Monitoring
- Telemetry
- OpenTelemetry
- Synthetics
- Alerting
- Metrics
- Tracing
- Real User Monitoring
- Incident Response
- Dashboards
- Logging
- SignalFlow
- MCP
website: https://www.splunk.com/en_us/products/observability.html
---
