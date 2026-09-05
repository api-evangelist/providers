---
access_model:
  confidence: high
  label: Paid with free developer tier
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://www.salesforce.com/service/pricing/
  - https://developer.salesforce.com/signup
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Core REST API for Service Cloud operations: sObject CRUD over Case, CaseComment, EmailMessage, Knowledge articles and every other standard and custom object, plus SOQL query, SOSL search and composite'
  name: Service Cloud REST API
  slug: service-cloud-rest-api
- description: The Case object and its children — CaseComment, CaseHistory, EmailMessage — worked through the sObjects REST resources. Assignment-rule behaviour on create and update is controlled by the Sforce-Auto-
  name: Service Cloud Case Management API
  slug: service-cloud-case-management-api
- description: Knowledge article management — article versions, categories, publishing states and the knowledgeManagement REST resources used to surface self-service content.
  name: Service Cloud Knowledge API
  slug: service-cloud-knowledge-api
- description: Omni-channel presence, work assignment and routing, exposed through the connect/omnichannel REST resources and the ServiceChannel / PendingServiceRouting objects.
  name: Service Cloud Omni-Channel API
  slug: service-cloud-omni-channel-api
- description: Real-time chat with customers over the Live Agent REST surface. Superseded for new builds by Messaging for In-App and Web, which authenticates with the scrt_api OAuth scope.
  name: Service Cloud Live Agent API
  slug: service-cloud-live-agent-api
- description: The gRPC event API. Publish and subscribe to platform events and Change Data Capture events (including /data/CaseChangeEvent) with Avro-encoded payloads and replay-tracked subscriptions. Six RPCs on t
  name: Service Cloud Pub/Sub API
  slug: service-cloud-pubsub-api
- description: CometD/Bayeux long-polling surface for PushTopic, generic streaming and platform event subscriptions. The legacy transport; new integrations should use the Pub/Sub API.
  name: Service Cloud Streaming API
  slug: service-cloud-streaming-api
- description: Open CTI — the JavaScript API that connects a telephony system's softphone to the Service Cloud console, plus the Voice/contact-centre surfaces built on it.
  name: Service Cloud CTI API
  slug: service-cloud-cti-api
- description: Generally available remote Model Context Protocol servers that expose the Salesforce sObject layer to AI agents over OAuth. Four least-privilege SObject servers (all, reads, mutations, deletes) plus D
  name: Salesforce Hosted MCP Servers
  slug: salesforce-hosted-mcp-servers
- baseURL: https://runtime-api-na-west.prod.chatbots.sfdc.sh
  baseurl_source: spec
  description: The bot API from Salesforce Service Cloud APIs — 3 operation(s) for bot.
  name: Salesforce Service Cloud APIs Bot API
  slug: service-cloud-bot-api
- baseURL: https://runtime-api-na-west.prod.chatbots.sfdc.sh
  baseurl_source: spec
  description: The health API from Salesforce Service Cloud APIs — 1 operation(s) for health.
  name: Salesforce Service Cloud APIs Health API
  slug: service-cloud-health-api
- baseURL: https://runtime-api-na-west.prod.chatbots.sfdc.sh
  baseurl_source: spec
  description: The versions API from Salesforce Service Cloud APIs — 1 operation(s) for versions.
  name: Salesforce Service Cloud APIs Versions API
  slug: service-cloud-versions-api
artifact_total: 22
asyncapis:
- description: ''
  name: Service Cloud Event Surface
  slug: service-cloud-event-surface
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/forcedotcom/pub-sub-api/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/service-cloud-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/service-cloud-einstein-bot-session.md
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/service/
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: company
  title: ''
  type: Blog
  url: https://www.salesforce.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forcedotcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforce-for-service
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/salesforce-developers/salesforce-developers/overview
- group: start
  title: ''
  type: SignUp
  url: https://www.salesforce.com/products/free-trial/developer/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/service/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/service-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/service-cloud-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/service-cloud-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/service-cloud-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/service-cloud-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/service-cloud-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/service-cloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/service-cloud-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/service-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/service-cloud-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/service-cloud-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/service-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/service-cloud-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/service-cloud-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/service-cloud-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/service-cloud-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/service-cloud-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/service-cloud-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/service-cloud-pubsub-api.proto
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/service-cloud-event-surface.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/service-cloud-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/service-cloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.salesforce.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/service-cloud-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.salesforce.com/
- group: auth
  title: ''
  type: Security
  url: https://www.salesforce.com/company/disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/service-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/service-cloud-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/service-cloud-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/service-cloud-einstein-bots-overlay.yaml
created: '2024-01-15'
description: 'Salesforce Service Cloud is the customer-service and contact-centre product on the Salesforce Platform, and its API surface is the Salesforce Platform API applied to service objects — Case, CaseComment, Knowledge articles, LiveChatTranscript, MessagingSession, entitlements and omni-channel routing — reached through the REST, SOAP, Bulk and Composite APIs. Alongside that record layer Salesforce ships purpose-built runtimes with their own contracts: an OpenAPI 3.0 document for the Einstein Bots Runtime API, a gRPC/protobuf contract for the Pub/Sub event API, a CometD Streaming API, and generally available hosted MCP servers that expose the sObject layer to AI agents over OAuth. There is no single global API host — every call is made against the customer''s own org at the instance_url returned with the OAuth token, on API version 67.0 (Summer ''26). Authentication is OAuth 2.0 only; Salesforce issues no API keys.'
finops:
- name: Service Cloud Finops
  service_category: API
  slug: service-cloud-finops
image: https://wp.sfdcdigital.com/en-us/wp-content/uploads/sites/4/2024/11/logo-salesforce.svg
layout: provider
mcp_servers:
- description: ''
  name: Salesforce Hosted MCP Servers + Salesforce DX MCP Server
  slug: salesforce-hosted-mcp-servers-salesforce-dx-mcp-server
modified: '2026-08-27'
name: Salesforce Service Cloud APIs
nav: Providers
network: true
overview: 'Salesforce Service Cloud APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bot API, Health API, and Versions API. Tagged areas include Cloud, CRM, Customer Service, Enterprise, and Salesforce.


  The Salesforce Service Cloud APIs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Salesforce Service Cloud APIs'' developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 43 more developer resources.'
plans:
- name: Service Cloud Plans Pricing
  plan_count: 5
  slug: service-cloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Service Cloud Rate Limits
  slug: service-cloud-rate-limits
scopes:
- name: Service Cloud Scopes
  scope_count: 36
  slug: service-cloud-scopes
  summary_line: 36 scopes · authorizationCode/implicit
score:
  band: exemplar
  composite: 67.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 54.0
    catalog_earned_first_party: 24.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 55.6
    developer_ergonomics: 80.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 67.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/service-cloud/refs/heads/main/screenshots/service-cloud-2026-06-20T193724.png
security:
- kind: authentication
  name: Service Cloud Authentication
  slug: service-cloud-authentication
  summary_line: oauth2/openIdConnect/http-bearer · 4 schemes
- kind: domain-security
  name: Service Cloud Domain Security
  slug: service-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Service Cloud Vulnerability Disclosure
  slug: service-cloud-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Service Cloud Trust Center
  slug: service-cloud-trust-center
  summary_line: note, observed, unverified_in_this_pass, unverified_note
slug: service-cloud
tags:
- Cloud
- CRM
- Customer Service
- Enterprise
- Salesforce
- Support
website: https://www.salesforce.com/service/
---
