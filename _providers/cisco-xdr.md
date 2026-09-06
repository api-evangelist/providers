---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-09-05'
api_count: 12
apis:
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Actor operations
  name: Cisco XDR Actor API
  slug: cisco-xdr-actor-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Asset operations
  name: Cisco XDR Asset API
  slug: cisco-xdr-asset-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Asset Mapping operations
  name: Cisco XDR Asset Mapping API
  slug: cisco-xdr-asset-mapping-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Asset Properties operations
  name: Cisco XDR Asset Properties API
  slug: cisco-xdr-asset-properties-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Attack Pattern operations
  name: Cisco XDR Attack Pattern API
  slug: cisco-xdr-attack-pattern-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Bulk API from Cisco XDR — 1 operation(s) for bulk.
  name: Cisco XDR Bulk API
  slug: cisco-xdr-bulk-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Bundle API from Cisco XDR — 2 operation(s) for bundle.
  name: Cisco XDR Bundle API
  slug: cisco-xdr-bundle-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Campaign operations
  name: Cisco XDR Campaign API
  slug: cisco-xdr-campaign-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Casebook operations
  name: Cisco XDR Casebook API
  slug: cisco-xdr-casebook-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: COA operations
  name: Cisco XDR COA API
  slug: cisco-xdr-coa-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: This set of routes allow to quickly get answers from your integrations You might use them at the start of any investigation to quickly get answers from your modules if something is bad.
  name: Cisco XDR Deliberate API
  slug: cisco-xdr-deliberate-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Events operations
  name: Cisco XDR Event API
  slug: cisco-xdr-event-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Feed operations
  name: Cisco XDR Feed API
  slug: cisco-xdr-feed-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: Feedback Routes
  name: Cisco XDR Feedback API
  slug: cisco-xdr-feedback-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The GraphQL API from Cisco XDR — 1 operation(s) for graphql.
  name: Cisco XDR Graph QL API
  slug: cisco-xdr-graphql-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: This set of routes allow to check the health of your integrations setup Verify if your modules are setup correctly and if your credentials are correct.
  name: Cisco XDR Health API
  slug: cisco-xdr-health-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Incident operations
  name: Cisco XDR Incident API
  slug: cisco-xdr-incident-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Indicator operations
  name: Cisco XDR Indicator API
  slug: cisco-xdr-indicator-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: Inspect related routes
  name: Cisco XDR Inspect API
  slug: cisco-xdr-inspect-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Investigation API from Cisco XDR — 8 operation(s) for investigation.
  name: Cisco XDR Investigation API
  slug: cisco-xdr-investigation-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: The INVITE API from Cisco XDR — 2 operation(s) for invite.
  name: Cisco XDR INVITE API
  slug: cisco-xdr-invite-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: The Iroh API from Cisco XDR — 3 operation(s) for iroh.
  name: Cisco XDR Iroh API
  slug: cisco-xdr-iroh-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Judgement operations
  name: Cisco XDR Judgement API
  slug: cisco-xdr-judgement-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: The LOGIN API from Cisco XDR — 4 operation(s) for login.
  name: Cisco XDR LOGIN API
  slug: cisco-xdr-login-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Malware operations
  name: Cisco XDR Malware API
  slug: cisco-xdr-malware-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Metrics API from Cisco XDR — 1 operation(s) for metrics.
  name: Cisco XDR Metrics API
  slug: cisco-xdr-metrics-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: ModuleInstance Routes
  name: Cisco XDR Module Instance API
  slug: cisco-xdr-moduleinstance-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: ModuleType Routes
  name: Cisco XDR Module Type API
  slug: cisco-xdr-moduletype-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: ModuleTypePatch Routes
  name: Cisco XDR Module Type Patch API
  slug: cisco-xdr-moduletypepatch-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Note API from Cisco XDR — 8 operation(s) for note.
  name: Cisco XDR Note API
  slug: cisco-xdr-note-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: This set of routes allow to get in depth investigation data about a threat You might use them at the start of any investigation to get the full picture and get to know if something has been seen in yo
  name: Cisco XDR Observe API
  slug: cisco-xdr-observe-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: One-click Routes
  name: Cisco XDR One Click API
  slug: cisco-xdr-one-click-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: Access private-intel
  name: Cisco XDR Private Intel API
  slug: cisco-xdr-private-intel-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Properties API from Cisco XDR — 1 operation(s) for properties.
  name: Cisco XDR Properties API
  slug: cisco-xdr-properties-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: This set of routes allow to query for records related to observable events.Results are returned in OCSF format.
  name: Cisco XDR Query API
  slug: cisco-xdr-query-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: This set of routes allow to get relevant Reference links and quickly pivot pursuing your investigation on a specific product interface.
  name: Cisco XDR Refer API
  slug: cisco-xdr-refer-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Relationship operations
  name: Cisco XDR Relationship API
  slug: cisco-xdr-relationship-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: The Reputation API from Cisco XDR — 1 operation(s) for reputation.
  name: Cisco XDR Reputation API
  slug: cisco-xdr-reputation-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: IROH Response
  name: Cisco XDR Response API
  slug: cisco-xdr-response-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: Cookie-based session validation
  name: Cisco XDR Session Cookie API
  slug: cisco-xdr-session-cookie-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Sighting operations
  name: Cisco XDR Sighting API
  slug: cisco-xdr-sighting-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Status API from Cisco XDR — 1 operation(s) for status.
  name: Cisco XDR Status API
  slug: cisco-xdr-status-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Target Record operations
  name: Cisco XDR Target Record API
  slug: cisco-xdr-target-record-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: Tool operations
  name: Cisco XDR Tool API
  slug: cisco-xdr-tool-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Verdict API from Cisco XDR — 1 operation(s) for verdict.
  name: Cisco XDR Verdict API
  slug: cisco-xdr-verdict-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Version API from Cisco XDR — 1 operation(s) for version.
  name: Cisco XDR Version API
  slug: cisco-xdr-version-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Vulnerability API from Cisco XDR — 9 operation(s) for vulnerability.
  name: Cisco XDR Vulnerability API
  slug: cisco-xdr-vulnerability-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: Webhook Routes
  name: Cisco XDR Webhook API
  slug: cisco-xdr-webhook-api
- baseURL: https://visibility.amp.cisco.com
  baseurl_source: declared
  description: The WebhookResult API from Cisco XDR — 2 operation(s) for webhookresult.
  name: Cisco XDR Webhook Result API
  slug: cisco-xdr-webhookresult-api
- description: Model Context Protocol server published by CiscoDevNet exposing 27 Cisco XDR tools across Inspect, Investigate, Incidents, Response Actions, Casebooks, Threat Intel, Workflows and Admin, plus 5 resour
  name: Cisco XDR MCP Server
  slug: cisco-xdr-mcp-server
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Calendars API from Cisco XDR — 3 operation(s) for calendars.
  name: Cisco XDR Calendars API
  slug: cisco-xdr-calendars-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Categories API from Cisco XDR — 2 operation(s) for categories.
  name: Cisco XDR Categories API
  slug: cisco-xdr-categories-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The ChangeOwner API from Cisco XDR — 1 operation(s) for changeowner.
  name: Cisco XDR Change Owner API
  slug: cisco-xdr-changeowner-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Comments API from Cisco XDR — 2 operation(s) for comments.
  name: Cisco XDR Comments API
  slug: cisco-xdr-comments-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Events API from Cisco XDR — 2 operation(s) for events.
  name: Cisco XDR Events API
  slug: cisco-xdr-events-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The EventsRateLimit API from Cisco XDR — 1 operation(s) for eventsratelimit.
  name: Cisco XDR Events Rate Limit API
  slug: cisco-xdr-eventsratelimit-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Metadata API from Cisco XDR — 1 operation(s) for metadata.
  name: Cisco XDR Metadata API
  slug: cisco-xdr-metadata-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Ratings API from Cisco XDR — 3 operation(s) for ratings.
  name: Cisco XDR Ratings API
  slug: cisco-xdr-ratings-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The References API from Cisco XDR — 1 operation(s) for references.
  name: Cisco XDR References API
  slug: cisco-xdr-references-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The RemoteMeta API from Cisco XDR — 3 operation(s) for remotemeta.
  name: Cisco XDR Remote Meta API
  slug: cisco-xdr-remotemeta-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Rules API from Cisco XDR — 4 operation(s) for rules.
  name: Cisco XDR Rules API
  slug: cisco-xdr-rules-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The RuntimeUsers API from Cisco XDR — 2 operation(s) for runtimeusers.
  name: Cisco XDR Runtime Users API
  slug: cisco-xdr-runtimeusers-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Schedules API from Cisco XDR — 2 operation(s) for schedules.
  name: Cisco XDR Schedules API
  slug: cisco-xdr-schedules-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Schemas API from Cisco XDR — 2 operation(s) for schemas.
  name: Cisco XDR Schemas API
  slug: cisco-xdr-schemas-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The ShareObjectPermissions API from Cisco XDR — 1 operation(s) for shareobjectpermissions.
  name: Cisco XDR Share Object Permissions API
  slug: cisco-xdr-shareobjectpermissions-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The SXIROHIncident API from Cisco XDR — 1 operation(s) for sxirohincident.
  name: Cisco XDR SXIROH Incident API
  slug: cisco-xdr-sxirohincident-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Tables API from Cisco XDR — 2 operation(s) for tables.
  name: Cisco XDR Tables API
  slug: cisco-xdr-tables-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The TableTypes API from Cisco XDR — 2 operation(s) for tabletypes.
  name: Cisco XDR Table Types API
  slug: cisco-xdr-tabletypes-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The TargetGroups API from Cisco XDR — 2 operation(s) for targetgroups.
  name: Cisco XDR Target Groups API
  slug: cisco-xdr-targetgroups-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Targets API from Cisco XDR — 3 operation(s) for targets.
  name: Cisco XDR Targets API
  slug: cisco-xdr-targets-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Tasks API from Cisco XDR — 5 operation(s) for tasks.
  name: Cisco XDR Tasks API
  slug: cisco-xdr-tasks-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Tenants API from Cisco XDR — 3 operation(s) for tenants.
  name: Cisco XDR Tenants API
  slug: cisco-xdr-tenants-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Triggers API from Cisco XDR — 2 operation(s) for triggers.
  name: Cisco XDR Triggers API
  slug: cisco-xdr-triggers-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The v1 API from Cisco XDR — 4 operation(s) for v1.
  name: Cisco XDR V1 API
  slug: cisco-xdr-v1-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The v2 API from Cisco XDR — 75 operation(s) for v2.
  name: Cisco XDR V2 API
  slug: cisco-xdr-v2-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The v3 API from Cisco XDR — 10 operation(s) for v3.
  name: Cisco XDR V3 API
  slug: cisco-xdr-v3-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Variables API from Cisco XDR — 3 operation(s) for variables.
  name: Cisco XDR Variables API
  slug: cisco-xdr-variables-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The VariableTypes API from Cisco XDR — 3 operation(s) for variabletypes.
  name: Cisco XDR Variable Types API
  slug: cisco-xdr-variabletypes-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Webhooks API from Cisco XDR — 3 operation(s) for webhooks.
  name: Cisco XDR Webhooks API
  slug: cisco-xdr-webhooks-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The WorkflowInstances API from Cisco XDR — 7 operation(s) for workflowinstances.
  name: Cisco XDR Workflow Instances API
  slug: cisco-xdr-workflowinstances-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Workflows API from Cisco XDR — 20 operation(s) for workflows.
  name: Cisco XDR Workflows API
  slug: cisco-xdr-workflows-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The WorkflowVariableReferences API from Cisco XDR — 1 operation(s) for workflowvariablereferences.
  name: Cisco XDR Workflow Variable References API
  slug: cisco-xdr-workflowvariablereferences-api
- baseURL: https://private.intel.amp.cisco.com
  baseurl_source: declared
  description: The Xchange API from Cisco XDR — 4 operation(s) for xchange.
  name: Cisco XDR Xchange API
  slug: cisco-xdr-xchange-api
artifact_total: 93
asyncapis:
- description: ''
  name: Cisco Xdr Webhooks
  slug: cisco-xdr-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cisco-xdr-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-xdr-incidents-investigations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-xdr-automation-overlay.yaml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cisco-xdr-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-xdr-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-xdr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-xdr-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/docs/cisco-xdr/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/cisco-xdr/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/cisco-xdr/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/CiscoDevNet/xdr-mcp-community
- group: company
  title: ''
  type: Website
  url: https://www.cisco.com/site/us/en/products/security/xdr/index.html
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cisco-xdr-incidents-investigations-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cisco-xdr-automation-openapi.json
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-xdr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-xdr-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-xdr-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-xdr-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tdr.cisco.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-xdr-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.cisco.com/docs/cisco-xdr/api-changelog/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-xdr-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-xdr-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/cisco-xdr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cisco-xdr-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cisco-xdr-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-xdr-security.txt
- group: auth
  title: ''
  type: Security
  url: https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/cisco-xdr-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustportal.cisco.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-xdr-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cisco-xdr-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-xdr-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-xdr-inspect-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-xdr-iroh-response-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cisco-xdr-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cisco-xdr-tool-crosswalk.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/cisco-xdr/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/cisco-xdr/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/docs/cisco-xdr/developer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.xdr.security.cisco.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/xdr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: start
  title: ''
  type: Login
  url: https://xdr.us.security.cisco.com/
created: '2026-08-19'
description: 'Cisco XDR is Cisco''s extended detection and response platform, the successor to SecureX. It correlates telemetry from Cisco Secure Endpoint, Secure Firewall, Umbrella, Duo, Secure Email and third-party sources into incidents, and exposes four distinct REST API families behind a single OAuth 2.0 authorization server: the IROH platform (inspect, enrich, response actions, integration modules, events, webhooks) at visibility.amp.cisco.com, the CTIA private-intelligence store at private.intel.amp.cisco.com, the Conure v2 incidents and investigations service at conure.us.security.cisco.com, and the Automation workflow engine at automate.us.security.cisco.com. All four publish anonymously fetchable machine-readable contracts — 52 documents, 581 operations, 1,176 schema definitions — and Cisco additionally ships a 27-tool MCP server through CiscoDevNet, stdio-only. There is no sandbox, no test mode and no idempotency key anywhere, including on the operation that blocks, isolates and
  quarantines.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco.png
layout: provider
mcp_servers:
- description: ''
  name: Cisco XDR MCP Server
  slug: cisco-xdr-mcp-server
- description: ''
  name: Cisco XDR MCP Server
  slug: cisco-xdr-mcp-server-2
modified: '2026-08-19'
name: Cisco XDR
nav: Providers
network: true
overview: 'Cisco XDR publishes 82 APIs on the [APIs.io](https://apis.io/) network, including Actor API, Asset API, Asset Mapping API, and 79 more. Tagged areas include Security, XDR, Threat Detection, Incident Response, and SOC.


  The Cisco XDR catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cisco XDR''s developer surface includes authentication, developer portal, documentation, API reference, changelog, getting-started guide, support, and 42 more developer resources.'
plans:
- name: Cisco Xdr Plans Pricing
  plan_count: 3
  slug: cisco-xdr-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Cisco Xdr Rate Limits
  slug: cisco-xdr-rate-limits
scopes:
- name: Cisco Xdr Scopes
  scope_count: 41
  slug: cisco-xdr-scopes
  summary_line: 41 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 4.5
    contract_quality: 61.3
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 59.8
  provenance:
    conformance: derived
    contracts:
      callable: 62.2
      derived: 0
      marker_coverage: 100.0
      total: 82
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-xdr/refs/heads/main/screenshots/cisco-xdr-2026-09-02T145050.png
security:
- kind: authentication
  name: Cisco Xdr Authentication
  slug: cisco-xdr-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Cisco Xdr Domain Security
  slug: cisco-xdr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Xdr Vulnerability Disclosure
  slug: cisco-xdr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cisco Xdr Trust Center
  slug: cisco-xdr-trust-center
  summary_line: ISO 27001, FedRAMP, GDPR, SOC 2, BSI C5
slug: cisco-xdr
tags:
- Security
- XDR
- Threat Detection
- Incident Response
- SOC
- Threat Intelligence
- Extended Detection and Response
- Authentication
- Webhook
- Automation
- MCP
website: https://www.cisco.com/site/us/en/products/security/xdr/index.html
---
