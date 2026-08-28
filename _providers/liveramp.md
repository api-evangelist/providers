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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 81
  human_in_the_loop: 0
  name: Liveramp Agentic Access
  operation_count: 179
  slug: liveramp-agentic-access
  summary_line: 179 operations · 81 acting
api_count: 11
apis:
- description: Programmatic activation of first-party and marketplace data across destination partners and connected platforms in the LiveRamp network. Manages destinations, destination integrations, integration con
  name: LiveRamp Activation API
  slug: activation-api
- description: API for setting up and managing clean rooms, partners, data connections, datasets, questions, question runs, flows, exports and destinations for privacy-safe collaborative analytics. This is the forme
  name: LiveRamp Clean Room API
  slug: clean-room-api
- description: Automates data subject requests including opt-outs, deletions and consent updates across the LiveRamp ecosystem. Two operations, and the only endpoint in the LiveRamp portfolio with a documented idemp
  name: LiveRamp Privacy API
  slug: privacy-api
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
artifact_total: 35
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
overview: 'LiveRamp publishes 3 APIs on the [APIs.io](https://apis.io/) network: Activation API, Clean Room API, and Privacy API. Tagged areas include Data Connectivity, Data Collaboration, Identity Resolution, Activation, and Clean Room.


  LiveRamp''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 42 more developer resources.'
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
  composite: 59.1
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 30.3
    contract_quality: 58.8
    developer_ergonomics: 49.4
    discoverability: 83.3
    governance: 30.3
    operational_transparency: 68.4
  previous_composite: 59.1
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
