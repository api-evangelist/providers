---
access_model:
  confidence: high
  label: Enterprise · Consumption-based, quoted · Service Account provisioned by a representative
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 81
  human_in_the_loop: 0
  name: Liveramp Agentic Access
  operation_count: 179
  slug: liveramp-agentic-access
  summary_line: 179 operations · 81 acting
api_count: 5
apis:
- description: Privacy-first, PII-based authentication API enabling programmatic addressability without third-party cookies via RampID envelopes. Publishes no OpenAPI. LiveRamp has deprecated the ATS Mobile SDK with
  name: LiveRamp Authenticated Traffic Solution (ATS) API
  slug: ats-api
- description: Identity resolution API that resolves offline PII data into stable AbiliTec links for enterprise customer-database unification, via a Match endpoint (plaintext PII) and a Lookup endpoint (hashed input
  name: LiveRamp AbiliTec API
  slug: abilitec-api
- description: API for matching data to the LiveRamp Identity Graph, including identity envelope creation and decryption, RampID transcoding between pseudonymous identifiers, and batch match/lookup calls returning d
  name: LiveRamp RampID API
  slug: rampid-api
- description: API enabling platforms to host third-party segments from the LiveRamp Data Marketplace and access detailed segment metadata. Currently on v3, from which a segment-details route has been removed and de
  name: LiveRamp Data Marketplace Buyer API
  slug: datamarketplace-buyer-api
- description: General-availability API for data sellers in the LiveRamp Data Marketplace — create and search segments using an Activation API first-party segmentID, update segment metadata, enable segments for comb
  name: LiveRamp Data Seller API
  slug: data-seller-api
- description: Automates Python, PySpark and BigQuery jobs running in LiveRamp's Safe Haven Analytics Environment, so analytics workloads can be scheduled and monitored programmatically instead of through the Job Ma
  name: LiveRamp Safe Haven Job Management API
  slug: job-management-api
- description: Beta API giving customers visibility into the state of their LiveRamp data pipelines. In beta as of this profile; publishes no OpenAPI.
  name: LiveRamp Data Pipeline Visibility API (Beta)
  slug: data-pipeline-visibility-api
- description: Service enabling SSPs to decrypt RampID identity envelopes into DSP-specific identifiers for programmatic activation. Documented on its own ReadMe site rather than the main developer portal.
  name: LiveRamp Sidecar
  slug: sidecar
- description: The Billable Configs API from LiveRamp — 2 operation(s) for billable configs.
  name: LiveRamp Billable Configs API
  slug: liveramp-billable-configs-api
- description: The Cleanroom API from LiveRamp — 2 operation(s) for cleanroom.
  name: LiveRamp Cleanroom API
  slug: liveramp-cleanroom-api
- description: The Cleanroom Datasets API from LiveRamp — 5 operation(s) for cleanroom datasets.
  name: LiveRamp Cleanroom Datasets API
  slug: liveramp-cleanroom-datasets-api
- description: The Cleanroom Destinations API from LiveRamp — 3 operation(s) for cleanroom destinations.
  name: LiveRamp Cleanroom Destinations API
  slug: liveramp-cleanroom-destinations-api
- description: The Cleanroom Exports API from LiveRamp — 4 operation(s) for cleanroom exports.
  name: LiveRamp Cleanroom Exports API
  slug: liveramp-cleanroom-exports-api
- description: The Cleanroom Flow Runs API from LiveRamp — 10 operation(s) for cleanroom flow runs.
  name: LiveRamp Cleanroom Flow Runs API
  slug: liveramp-cleanroom-flow-runs-api
- description: The Cleanroom Flows API from LiveRamp — 10 operation(s) for cleanroom flows.
  name: LiveRamp Cleanroom Flows API
  slug: liveramp-cleanroom-flows-api
- description: The Cleanroom Partners API from LiveRamp — 8 operation(s) for cleanroom partners.
  name: LiveRamp Cleanroom Partners API
  slug: liveramp-cleanroom-partners-api
- description: The Cleanroom Question Datasets API from LiveRamp — 4 operation(s) for cleanroom question datasets.
  name: LiveRamp Cleanroom Question Datasets API
  slug: liveramp-cleanroom-question-datasets-api
- description: The Cleanroom Question Permissions API from LiveRamp — 1 operation(s) for cleanroom question permissions.
  name: LiveRamp Cleanroom Question Permissions API
  slug: liveramp-cleanroom-question-permissions-api
- description: The Cleanroom Question Result Shares API from LiveRamp — 1 operation(s) for cleanroom question result shares.
  name: LiveRamp Cleanroom Question Result Shares API
  slug: liveramp-cleanroom-question-result-shares-api
- description: The Cleanroom Question Run Schedule API from LiveRamp — 2 operation(s) for cleanroom question run schedule.
  name: LiveRamp Cleanroom Question Run Schedule API
  slug: liveramp-cleanroom-question-run-schedule-api
- description: The Cleanroom Question Runs API from LiveRamp — 10 operation(s) for cleanroom question runs.
  name: LiveRamp Cleanroom Question Runs API
  slug: liveramp-cleanroom-question-runs-api
- description: The Cleanroom Question Tags API from LiveRamp — 2 operation(s) for cleanroom question tags.
  name: LiveRamp Cleanroom Question Tags API
  slug: liveramp-cleanroom-question-tags-api
- description: The Cleanroom Questions API from LiveRamp — 5 operation(s) for cleanroom questions.
  name: LiveRamp Cleanroom Questions API
  slug: liveramp-cleanroom-questions-api
- description: The Cleanroom Roles API from LiveRamp — 2 operation(s) for cleanroom roles.
  name: LiveRamp Cleanroom Roles API
  slug: liveramp-cleanroom-roles-api
- description: The Cleanroom Users API from LiveRamp — 3 operation(s) for cleanroom users.
  name: LiveRamp Cleanroom Users API
  slug: liveramp-cleanroom-users-api
- description: The Cleanrooms API from LiveRamp — 4 operation(s) for cleanrooms.
  name: LiveRamp Cleanrooms API
  slug: liveramp-cleanrooms-api
- description: The Configure Distributions API from LiveRamp — 4 operation(s) for configure distributions.
  name: LiveRamp Configure Distributions API
  slug: liveramp-configure-distributions-api
- description: The Credential Sources API from LiveRamp — 3 operation(s) for credential sources.
  name: LiveRamp Credential Sources API
  slug: liveramp-credential-sources-api
- description: The Data Connections API from LiveRamp — 5 operation(s) for data connections.
  name: LiveRamp Data Connections API
  slug: liveramp-data-connections-api
- description: The Data Source Parameters API from LiveRamp — 1 operation(s) for data source parameters.
  name: LiveRamp Data Source Parameters API
  slug: liveramp-data-source-parameters-api
- description: The Data Sources API from LiveRamp — 2 operation(s) for data sources.
  name: LiveRamp Data Sources API
  slug: liveramp-data-sources-api
- description: The Data Types API from LiveRamp — 2 operation(s) for data types.
  name: LiveRamp Data Types API
  slug: liveramp-data-types-api
- description: The DataConnectionViews API from LiveRamp — 2 operation(s) for dataconnectionviews.
  name: LiveRamp Data Connection Views API
  slug: liveramp-dataconnectionviews-api
- description: The Destinations API from LiveRamp — 3 operation(s) for destinations.
  name: LiveRamp Destinations API
  slug: liveramp-destinations-api
- description: The Distribute Data API from LiveRamp — 2 operation(s) for distribute data.
  name: LiveRamp Distribute Data API
  slug: liveramp-distribute-data-api
- description: View Destinations and Integrations where you can distribute data
  name: LiveRamp Explore Destinations API
  slug: liveramp-explore-destinations-api
- description: The Flow Decision Configurations API from LiveRamp — 1 operation(s) for flow decision configurations.
  name: LiveRamp Flow Decision Configurations API
  slug: liveramp-flow-decision-configurations-api
- description: The Health API from LiveRamp — 1 operation(s) for health.
  name: LiveRamp Health API
  slug: liveramp-health-api
- description: The Import Data Types API from LiveRamp — 1 operation(s) for import data types.
  name: LiveRamp Import Data Types API
  slug: liveramp-import-data-types-api
- description: The Intelligence API from LiveRamp — 4 operation(s) for intelligence.
  name: LiveRamp Intelligence API
  slug: liveramp-intelligence-api
- description: For internal LiveRamp consumption. These operations are not part of the supported external customer contract and may change without notice.
  name: LiveRamp Internal API
  slug: liveramp-internal-api
- description: The Invitations API from LiveRamp — 3 operation(s) for invitations.
  name: LiveRamp Invitations API
  slug: liveramp-invitations-api
- description: The OAuth Configuration API from LiveRamp — 4 operation(s) for oauth configuration.
  name: LiveRamp OAuth Configuration API
  slug: liveramp-oauth-configuration-api
- description: The Organization Credentials API from LiveRamp — 2 operation(s) for organization credentials.
  name: LiveRamp Organization Credentials API
  slug: liveramp-organization-credentials-api
- description: The Organization Users API from LiveRamp — 1 operation(s) for organization users.
  name: LiveRamp Organization Users API
  slug: liveramp-organization-users-api
- description: (resource) Manage privacy requests.
  name: LiveRamp Privacy Requests API
  slug: liveramp-privacyrequests-api
- description: The Questions API from LiveRamp — 3 operation(s) for questions.
  name: LiveRamp Questions API
  slug: liveramp-questions-api
- description: (resource) Represents a segment's status
  name: LiveRamp V2/Segment Status API
  slug: liveramp-v2-segmentstatus-api
- description: The View Deliveries API from LiveRamp — 1 operation(s) for view deliveries.
  name: LiveRamp View Deliveries API
  slug: liveramp-view-deliveries-api
- description: The View Segments API from LiveRamp — 2 operation(s) for view segments.
  name: LiveRamp View Segments API
  slug: liveramp-view-segments-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Activation API
  slug: open-liveramp-activation-api
- collection_type: open
  name: External APIs for Customer Integration
  slug: open-liveramp-clean-room-api
- collection_type: open
  name: LiveRamp Activation Deliveries API
  slug: open-liveramp-deliveries-api
- collection_type: open
  name: LiveRamp Activation Deliveries Destination Integrations API
  slug: open-liveramp-destination-integrations-api
- collection_type: open
  name: LiveRamp Activation Deliveries Destinations API
  slug: open-liveramp-destinations-api
- collection_type: open
  name: LiveRamp Activation Deliveries Distribution Managers API
  slug: open-liveramp-distribution-managers-api
- collection_type: open
  name: LiveRamp Activation Deliveries Integration Connections API
  slug: open-liveramp-integration-connections-api
- collection_type: open
  name: LiveRamp Activation Deliveries OAuth Connections API
  slug: open-liveramp-oauth-connections-api
- collection_type: open
  name: Privacy API
  slug: open-liveramp-privacy-api
- collection_type: open
  name: LiveRamp Activation Deliveries Segment Configurations API
  slug: open-liveramp-segment-configurations-api
- collection_type: open
  name: LiveRamp Activation Deliveries Segments API
  slug: open-liveramp-segments-api
- collection_type: open
  name: LiveRamp Activation API
  slug: open-liveramp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/liveramp-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/liveramp-activation-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/liveramp-clean-room-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/liveramp-privacy-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://liveramp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.liveramp.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.liveramp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liveramp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.liveramp.com/activation-api/reference/distribution-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.liveramp.com/activation-api/reference/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://support.liveramp.com/
- group: start
  title: ''
  type: SupportPortal
  url: https://support.liveramp.com/
- group: company
  title: ''
  type: Blog
  url: https://liveramp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LiveRamp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liveramp
- group: commercial
  title: ''
  type: Pricing
  url: https://liveramp.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://liveramp.com/contact/
- group: start
  title: ''
  type: Login
  url: https://app.liveramp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liveramp.com/liveramp-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liveramp.com/privacy/service-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveramp.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/liveramp-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liveramp-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/liveramp-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://liveramp.com/security/bug-bounty
- group: auth
  title: ''
  type: TrustCenter
  url: security/liveramp-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.liveramp.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liveramp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liveramp-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liveramp-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liveramp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liveramp-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liveramp-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liveramp-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/liveramp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liveramp-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liveramp-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/liveramp-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/liveramp-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/liveramp-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/liveramp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/liveramp-packages.yml
- group: design
  title: ''
  type: Components
  url: components/liveramp-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liveramp-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liveramp-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developers.liveramp.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liveramp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/liveramp-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developers.liveramp.com/llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: llms/liveramp-llms.txt
- group: build
  title: ''
  type: PostmanCollection
  url: collections/liveramp.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/liveramp.opencollection.json
created: '2026-03-16'
description: LiveRamp is a data collaboration platform that lets enterprises connect, control, and activate first-party customer data across the digital ecosystem without moving raw PII between parties. Its developer surface spans identity resolution (AbiliTec links and RampID), programmatic activation to more than 500 destination platforms, privacy-safe clean-room collaboration on the former Habu platform, data marketplace buying and selling, Safe Haven analytics job automation, cookieless authenticated addressability through ATS, and a Privacy API for data-subject requests. LiveRamp publishes downloadable OpenAPI specifications for the Activation, Clean Room and Privacy APIs, an RFC 9727 API catalog, and an llms.txt index across ten developer sub-sites; API credentials are issued as Service Accounts by a LiveRamp representative rather than through self-serve signup.
finops:
- name: Liveramp Finops
  service_category: API
  slug: liveramp-finops
graphqls:
- description: '> **Provenance correction, 2026-08-13.** LiveRamp publishes **no GraphQL endpoint** for any of its'
  name: LiveRamp GraphQL — NOT A REAL SURFACE
  slug: liveramp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liveramp.png
layout: provider
mcp_servers:
- description: ''
  name: LiveRamp MCP Server
  slug: liveramp-mcp-server
modified: '2026-08-13'
name: LiveRamp
nav: Providers
network: true
overview: 'LiveRamp publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Billable Configs API, Cleanroom API, Cleanroom Datasets API, and 39 more. Tagged areas include Data Connectivity, Data Collaboration, Identity Resolution, Activation, and Clean Room.


  LiveRamp''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 46 more developer resources.'
plans:
- name: Liveramp Plans Pricing
  plan_count: 0
  slug: liveramp-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Liveramp Rate Limits
  slug: liveramp-rate-limits
scopes:
- name: Liveramp Scopes
  scope_count: 1
  slug: liveramp-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 27
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 59.1
    developer_ergonomics: 49.4
    discoverability: 77.8
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liveramp/refs/heads/main/screenshots/liveramp-2026-06-20T184618.png
security:
- kind: authentication
  name: Liveramp Authentication
  slug: liveramp-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Liveramp Domain Security
  slug: liveramp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Liveramp Vulnerability Disclosure
  slug: liveramp-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Liveramp Trust Center
  slug: liveramp-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: liveramp
tags:
- Data Connectivity
- Data Collaboration
- Identity Resolution
- Activation
- Clean Room
- Privacy
- AdTech
- Marketing
- Consent
- Audience Segments
website: https://liveramp.com
---
