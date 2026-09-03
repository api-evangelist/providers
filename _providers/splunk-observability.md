---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 48
apis:
- description: Hosted Model Context Protocol server for Splunk Observability Cloud, using the streamable HTTP transport. Twelve tools across metrics/SignalFlow, APM and alerting. Authenticated with X-SF-REALM and X-
  name: Splunk Observability Cloud MCP Server
  slug: splunk-observability-mcp
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The APM service topology API from Splunk Observability Cloud — 2 operation(s) for apm service topology.
  name: Splunk Observability Cloud APM service topology API
  slug: splunk-observability-apm-service-topology-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The APM visibility filters API from Splunk Observability Cloud — 3 operation(s) for apm visibility filters.
  name: Splunk Observability Cloud APM visibility filters API
  slug: splunk-observability-apm-visibility-filters-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Automated archival API from Splunk Observability Cloud — 3 operation(s) for automated archival.
  name: Splunk Observability Cloud Automated archival API
  slug: splunk-observability-automated-archival-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Backfill API from Splunk Observability Cloud — 1 operation(s) for backfill.
  name: Splunk Observability Cloud Backfill API
  slug: splunk-observability-backfill-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Charts API from Splunk Observability Cloud — 2 operation(s) for charts.
  name: Splunk Observability Cloud Charts API
  slug: splunk-observability-charts-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Client Inventory API from Splunk Observability Cloud — 5 operation(s) for client inventory.
  name: Splunk Observability Cloud Client Inventory API
  slug: splunk-observability-client-inventory-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Dashboard groups API from Splunk Observability Cloud — 3 operation(s) for dashboard groups.
  name: Splunk Observability Cloud Dashboard groups API
  slug: splunk-observability-dashboard-groups-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Dashboards API from Splunk Observability Cloud — 3 operation(s) for dashboards.
  name: Splunk Observability Cloud Dashboards API
  slug: splunk-observability-dashboards-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Data links API from Splunk Observability Cloud — 2 operation(s) for data links.
  name: Splunk Observability Cloud Data links API
  slug: splunk-observability-data-links-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Detectors API from Splunk Observability Cloud — 7 operation(s) for detectors.
  name: Splunk Observability Cloud Detectors API
  slug: splunk-observability-detectors-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Download APM traces API from Splunk Observability Cloud — 3 operation(s) for download apm traces.
  name: Splunk Observability Cloud Download APM traces API
  slug: splunk-observability-download-apm-traces-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Incidents and alerts API from Splunk Observability Cloud — 7 operation(s) for incidents and alerts.
  name: Splunk Observability Cloud Incidents and alerts API
  slug: splunk-observability-incidents-and-alerts-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Integrations API from Splunk Observability Cloud — 3 operation(s) for integrations.
  name: Splunk Observability Cloud Integrations API
  slug: splunk-observability-integrations-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Metric ruleset API from Splunk Observability Cloud — 4 operation(s) for metric ruleset.
  name: Splunk Observability Cloud Metric ruleset API
  slug: splunk-observability-metric-ruleset-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Metrics metadata API from Splunk Observability Cloud — 8 operation(s) for metrics metadata.
  name: Splunk Observability Cloud Metrics metadata API
  slug: splunk-observability-metrics-metadata-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Navigators API from Splunk Observability Cloud — 5 operation(s) for navigators.
  name: Splunk Observability Cloud Navigators API
  slug: splunk-observability-navigators-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Org tokens API from Splunk Observability Cloud — 3 operation(s) for org tokens.
  name: Splunk Observability Cloud Org tokens API
  slug: splunk-observability-org-tokens-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Organizations API from Splunk Observability Cloud — 6 operation(s) for organizations.
  name: Splunk Observability Cloud Organizations API
  slug: splunk-observability-organizations-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Passwords API from Splunk Observability Cloud — 1 operation(s) for passwords.
  name: Splunk Observability Cloud Passwords API
  slug: splunk-observability-passwords-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Retrieve events V1 API from Splunk Observability Cloud — 1 operation(s) for retrieve events v1.
  name: Splunk Observability Cloud Retrieve events V1 API
  slug: splunk-observability-retrieve-events-v1-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Retrieve events V2 API from Splunk Observability Cloud — 1 operation(s) for retrieve events v2.
  name: Splunk Observability Cloud Retrieve events V2 API
  slug: splunk-observability-retrieve-events-v2-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Retrieve metric time series (MTS) API from Splunk Observability Cloud — 1 operation(s) for retrieve metric time series (mts).
  name: Splunk Observability Cloud Retrieve metric time series (MTS) API
  slug: splunk-observability-retrieve-metric-time-series-mts-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Role API from Splunk Observability Cloud — 4 operation(s) for role.
  name: Splunk Observability Cloud Role API
  slug: splunk-observability-role-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Send traces, metrics and events API from Splunk Observability Cloud — 5 operation(s) for send traces, metrics and events.
  name: Splunk Observability Cloud Send traces, metrics and events API
  slug: splunk-observability-send-traces-metrics-and-events-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Session tokens API from Splunk Observability Cloud — 1 operation(s) for session tokens.
  name: Splunk Observability Cloud Session tokens API
  slug: splunk-observability-session-tokens-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The SignalFlow API from Splunk Observability Cloud — 6 operation(s) for signalflow.
  name: Splunk Observability Cloud Signal Flow API
  slug: splunk-observability-signalflow-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The SLOs API from Splunk Observability Cloud — 4 operation(s) for slos.
  name: Splunk Observability Cloud SL Os API
  slug: splunk-observability-slos-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Splunk Observability Cloud Audit Events API from Splunk Observability Cloud — 1 operation(s) for splunk observability cloud audit events.
  name: Splunk Observability Cloud Splunk Observability Cloud Audit Events API
  slug: splunk-observability-splunk-observability-cloud-audit-events-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics API tests (V1) API from Splunk Observability Cloud — 5 operation(s) for synthetics api tests (v1).
  name: Splunk Observability Cloud Synthetics API tests (V1) API
  slug: splunk-observability-synthetics-api-tests-v1-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics API tests V2 API from Splunk Observability Cloud — 5 operation(s) for synthetics api tests v2.
  name: Splunk Observability Cloud Synthetics API tests V2 API
  slug: splunk-observability-synthetics-api-tests-v2-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics artifacts API from Splunk Observability Cloud — 3 operation(s) for synthetics artifacts.
  name: Splunk Observability Cloud Synthetics artifacts API
  slug: splunk-observability-synthetics-artifacts-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics audit API from Splunk Observability Cloud — 1 operation(s) for synthetics audit.
  name: Splunk Observability Cloud Synthetics audit API
  slug: splunk-observability-synthetics-audit-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics Browser tests (V1) API from Splunk Observability Cloud — 5 operation(s) for synthetics browser tests (v1).
  name: Splunk Observability Cloud Synthetics Browser tests (V1) API
  slug: splunk-observability-synthetics-browser-tests-v1-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics Browser tests V2 API from Splunk Observability Cloud — 5 operation(s) for synthetics browser tests v2.
  name: Splunk Observability Cloud Synthetics Browser tests V2 API
  slug: splunk-observability-synthetics-browser-tests-v2-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics CA certificates API from Splunk Observability Cloud — 2 operation(s) for synthetics ca certificates.
  name: Splunk Observability Cloud Synthetics CA certificates API
  slug: splunk-observability-synthetics-ca-certificates-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics certificates API from Splunk Observability Cloud — 2 operation(s) for synthetics certificates.
  name: Splunk Observability Cloud Synthetics certificates API
  slug: splunk-observability-synthetics-certificates-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics Chrome flags API from Splunk Observability Cloud — 1 operation(s) for synthetics chrome flags.
  name: Splunk Observability Cloud Synthetics Chrome flags API
  slug: splunk-observability-synthetics-chrome-flags-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics devices API from Splunk Observability Cloud — 1 operation(s) for synthetics devices.
  name: Splunk Observability Cloud Synthetics devices API
  slug: splunk-observability-synthetics-devices-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics downtime configurations API from Splunk Observability Cloud — 3 operation(s) for synthetics downtime configurations.
  name: Splunk Observability Cloud Synthetics downtime configurations API
  slug: splunk-observability-synthetics-downtime-configurations-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics excluded files API from Splunk Observability Cloud — 1 operation(s) for synthetics excluded files.
  name: Splunk Observability Cloud Synthetics excluded files API
  slug: splunk-observability-synthetics-excluded-files-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics global variables API from Splunk Observability Cloud — 2 operation(s) for synthetics global variables.
  name: Splunk Observability Cloud Synthetics global variables API
  slug: splunk-observability-synthetics-global-variables-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics HTTP tests API from Splunk Observability Cloud — 5 operation(s) for synthetics http tests.
  name: Splunk Observability Cloud Synthetics HTTP tests API
  slug: splunk-observability-synthetics-http-tests-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics locations API from Splunk Observability Cloud — 4 operation(s) for synthetics locations.
  name: Splunk Observability Cloud Synthetics locations API
  slug: splunk-observability-synthetics-locations-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics Port tests API from Splunk Observability Cloud — 5 operation(s) for synthetics port tests.
  name: Splunk Observability Cloud Synthetics Port tests API
  slug: splunk-observability-synthetics-port-tests-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics runs API from Splunk Observability Cloud — 1 operation(s) for synthetics runs.
  name: Splunk Observability Cloud Synthetics runs API
  slug: splunk-observability-synthetics-runs-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics SSL Certificate Tests API from Splunk Observability Cloud — 2 operation(s) for synthetics ssl certificate tests.
  name: Splunk Observability Cloud Synthetics SSL Certificate Tests API
  slug: splunk-observability-synthetics-ssl-certificate-tests-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Synthetics tests API from Splunk Observability Cloud — 7 operation(s) for synthetics tests.
  name: Splunk Observability Cloud Synthetics tests API
  slug: splunk-observability-synthetics-tests-api
- baseURL: https://api.{REALM}.observability.splunkcloud.com/v2
  baseurl_source: declared
  description: The Teams API from Splunk Observability Cloud — 4 operation(s) for teams.
  name: Splunk Observability Cloud Teams API
  slug: splunk-observability-teams-api
artifact_total: 58
asyncapis:
- description: The SignalFlow streaming analytics service. A client opens a WebSocket connection, authenticates with a session token within 5 seconds, then starts computations on named channels and receives control,
  name: Splunk Observability Cloud — SignalFlow streaming
  slug: splunk-observability-signalflow-asyncapi
- description: ''
  name: Splunk Observability Webhooks
  slug: splunk-observability-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-apm-service-topology-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-apm-visibility-filters-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-audit-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-automatedarchival-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-backfill-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-charts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-client-inventory-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-dashboard-groups-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-dashboards-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-datalinks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-detectors-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-incidents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-ingest-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-integrations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-metric-ruleset-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-metrics-metadata-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-navigator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-org-tokens-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-organizations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-passwords-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-retrieve-events-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-retrieve-events-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-retrieve-timeserieswindow-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-roles-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-sessiontokens-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-signalflow-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-slo-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-api-tests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-api-tests-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-artifacts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-audits-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-browser-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-browser-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-ca-certs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-certificates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-chrome-flags-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-devices-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-downtime-configurations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-excluded-files-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-global-variables-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-http-tests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-locations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-ports-tests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-runs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-ssl-tests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-synthetics-tests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-teams-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/splunk-observability-trace-id-overlay.yaml
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
overview: 'Splunk Observability Cloud publishes 48 APIs on the [APIs.io](https://apis.io/) network, including APM service topology API, APM visibility filters API, Automated archival API, and 45 more. Tagged areas include Observability, APM, Monitoring, Telemetry, and OpenTelemetry.


  The Splunk Observability Cloud catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Splunk Observability Cloud''s developer surface includes developer portal, documentation, API reference, getting-started guide, pricing, signup flow, support, and 86 more developer resources.'
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
  composite: 57.6
  coverage:
    artifact_dirs: 22
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 24.2
    developer_ergonomics: 73.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 58.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 48
      marker_coverage: 100.0
      total: 48
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splunk-observability/refs/heads/main/screenshots/splunk-observability-2026-09-02T160527.png
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
