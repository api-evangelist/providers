---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The gRPC contract that is Sift's primary API — 51 services and 330 RPCs defined across 66 proto3 files published under MIT in the sift-stack/sift monorepo, including the bidirectional streaming ingest
  name: Sift gRPC API
  slug: sift-grpc-api
- description: Two Model Context Protocol servers. A public, anonymous remote server at https://docs.siftstack.com/mcp exposing search and a virtualized read-only docs filesystem, advertised at /.well-known/mcp.json
  name: Sift MCP Server
  slug: sift-mcp-server
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with [annotation logs](/glossary#annotation).
  name: Sift Stack Annotation Log Service API
  slug: sift-stack-annotationlogservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with annotations.
  name: Sift Stack Annotation Service API
  slug: sift-stack-annotationservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The ApiKeyService API from Sift Stack — 3 operation(s) for apikeyservice.
  name: Sift Stack API Key Service API
  slug: sift-stack-apikeyservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with [assets](/glossary#asset).
  name: Sift Stack Asset Service API
  slug: sift-stack-assetservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The AutomationService API from Sift Stack — 3 operation(s) for automationservice.
  name: Sift Stack Automation Service API
  slug: sift-stack-automationservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The CalculatedChannelService API from Sift Stack — 10 operation(s) for calculatedchannelservice.
  name: Sift Stack Calculated Channel Service API
  slug: sift-stack-calculatedchannelservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with calculated channels.
  name: Sift Stack Calculated Channels Service API
  slug: sift-stack-calculatedchannelsservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The CampaignService API from Sift Stack — 5 operation(s) for campaignservice.
  name: Sift Stack Campaign Service API
  slug: sift-stack-campaignservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with channel schemas
  name: Sift Stack Channel Schema Service API
  slug: sift-stack-channelschemaservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with [channels](/glossary#channel).
  name: Sift Stack Channel Service API
  slug: sift-stack-channelservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with comments attached to resources in the platform.
  name: Sift Stack Comment Service API
  slug: sift-stack-commentservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The DataImportService API from Sift Stack — 6 operation(s) for dataimportservice.
  name: Sift Stack Data Import Service API
  slug: sift-stack-dataimportservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to query data
  name: Sift Stack Data Service API
  slug: sift-stack-dataservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The DlqErrorsService API from Sift Stack — 1 operation(s) for dlqerrorsservice.
  name: Sift Stack Dlq Errors Service API
  slug: sift-stack-dlqerrorsservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The DocsService API from Sift Stack — 2 operation(s) for docsservice.
  name: Sift Stack Docs Service API
  slug: sift-stack-docsservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The ExportService API from Sift Stack — 2 operation(s) for exportservice.
  name: Sift Stack Export Service API
  slug: sift-stack-exportservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The ExternalSyncService API from Sift Stack — 6 operation(s) for externalsyncservice.
  name: Sift Stack External Sync Service API
  slug: sift-stack-externalsyncservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with family configurations.
  name: Sift Stack Family Service API
  slug: sift-stack-familyservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with [ingestion configs](/glossary#ingestion-config).
  name: Sift Stack Ingestion Config Service API
  slug: sift-stack-ingestionconfigservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The JobService API from Sift Stack — 3 operation(s) for jobservice.
  name: Sift Stack Job Service API
  slug: sift-stack-jobservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The MeService API from Sift Stack — 1 operation(s) for meservice.
  name: Sift Stack Me Service API
  slug: sift-stack-meservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The MetadataService API from Sift Stack — 9 operation(s) for metadataservice.
  name: Sift Stack Metadata Service API
  slug: sift-stack-metadataservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with in-app notifications.
  name: Sift Stack Notification Service API
  slug: sift-stack-notificationservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with panel configurations.
  name: Sift Stack Panel Configuration Service API
  slug: sift-stack-panelconfigurationservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The PingService API from Sift Stack — 1 operation(s) for pingservice.
  name: Sift Stack Ping Service API
  slug: sift-stack-pingservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to manage ABAC policies.
  name: Sift Stack Policy Service API
  slug: sift-stack-policyservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to manage ABAC principal attributes.
  name: Sift Stack Principal Attribute Service API
  slug: sift-stack-principalattributeservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with protobuf descriptors used for protobuf ingestion.
  name: Sift Stack Protobuf Descriptor Service API
  slug: sift-stack-protobufdescriptorservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The RemoteFileService API from Sift Stack — 4 operation(s) for remotefileservice.
  name: Sift Stack Remote File Service API
  slug: sift-stack-remotefileservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The ReportService API from Sift Stack — 7 operation(s) for reportservice.
  name: Sift Stack Report Service API
  slug: sift-stack-reportservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The ReportTemplateService API from Sift Stack — 3 operation(s) for reporttemplateservice.
  name: Sift Stack Report Template Service API
  slug: sift-stack-reporttemplateservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to manage ABAC resource attributes (entity attributes).
  name: Sift Stack Resource Attribute Service API
  slug: sift-stack-resourceattributeservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The RoleService API from Sift Stack — 1 operation(s) for roleservice.
  name: Sift Stack Role Service API
  slug: sift-stack-roleservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to evaluate rules.
  name: Sift Stack Rule Evaluation Service API
  slug: sift-stack-ruleevaluationservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with rules.
  name: Sift Stack Rule Service API
  slug: sift-stack-ruleservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with [runs](/glossary#run).
  name: Sift Stack Run Service API
  slug: sift-stack-runservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The SavedSearchService API from Sift Stack — 3 operation(s) for savedsearchservice.
  name: Sift Stack Saved Search Service API
  slug: sift-stack-savedsearchservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with [tags](/glossary#tag).
  name: Sift Stack Tag Service API
  slug: sift-stack-tagservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to manage test reports
  name: Sift Stack Test Report Service API
  slug: sift-stack-testreportservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The UnitService API from Sift Stack — 1 operation(s) for unitservice.
  name: Sift Stack Unit Service API
  slug: sift-stack-unitservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The UserDefinedFunctionService API from Sift Stack — 8 operation(s) for userdefinedfunctionservice.
  name: Sift Stack User Defined Function Service API
  slug: sift-stack-userdefinedfunctionservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The UserGroupService API from Sift Stack — 7 operation(s) for usergroupservice.
  name: Sift Stack User Group Service API
  slug: sift-stack-usergroupservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with user objects.
  name: Sift Stack User Service API
  slug: sift-stack-userservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: Service to programmatically interact with views.
  name: Sift Stack View Service API
  slug: sift-stack-viewservice-api
- baseURL: https://api.siftstack.com
  baseurl_source: declared
  description: The WebhookService API from Sift Stack — 6 operation(s) for webhookservice.
  name: Sift Stack Webhook Service API
  slug: sift-stack-webhookservice-api
artifact_total: 55
asyncapis:
- description: ''
  name: Sift Stack Webhooks
  slug: sift-stack-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/sift-stack/sift/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sift-stack-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sift-stack-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.siftstack.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.siftstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.siftstack.com/documentation/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.siftstack.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.siftstack.com/documentation/get-started
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.siftstack.com/learning-path/overview
- group: company
  title: ''
  type: Blog
  url: https://www.siftstack.com/mission-critical
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sift-stack
- group: start
  title: ''
  type: SignUp
  url: https://www.siftstack.com/weekly-demo
- group: start
  title: ''
  type: Login
  url: https://app.siftstack.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siftstack.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siftstack.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.siftstack.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.siftstack.com/changelog
- group: other
  title: ''
  type: Glossary
  url: https://www.siftstack.com/glossary
- group: operate
  title: ''
  type: FAQ
  url: https://www.siftstack.com/about/faq
- group: build
  title: ''
  type: Packages
  url: packages/sift-stack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sift-stack-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sift-stack-cli.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/sift-stack-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sift-stack-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sift-stack-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sift-stack-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sift-stack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sift-stack-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sift-stack-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/sift-stack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sift-stack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sift-stack-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sift-stack-plans-pricing.yml
created: '2026-08-27'
description: 'Sift (siftstack.com) is a unified observability platform for mission-critical hardware — the telemetry layer for rockets, aircraft, robots, energy systems and autonomous vehicles. Founded by former SpaceX engineers Austin Spiegel and Karthik Gollapudi and headquartered in Marina del Rey, California, Sift ingests, stores and analyzes high-rate, high-cardinality sensor data, then layers automated rule-based anomaly detection, run-to-run comparison and certification-ready reporting on top of it. The product surface is unusually complete for a company this size: a 343-operation REST API transcoded from 330 gRPC RPCs across 66 MIT-licensed .proto files, first-party Python, Rust, Go, C++ and LabVIEW clients, a sift-cli binary, outbound HMAC-signed webhooks, and a Grafana datasource. It is also one of the more agent-ready providers in the catalog — it publishes an A2A agent card, an Agent Skill, llms.txt on two hosts, an anonymous remote MCP documentation server, and a second MCP
  server that ships inside the CLI and talks to a customer''s own Sift environment. Deployment spans SaaS, private cloud, on-premises, airgapped and AWS GovCloud, backed by SOC 2 Type II, NIST SP 800-171 and ITAR compliance.'
image: https://www.siftstack.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Sift MCP servers
  slug: sift-mcp-servers
modified: '2026-08-27'
name: Sift Stack
nav: Providers
network: true
overview: 'Sift Stack publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Annotation Log Service API, Annotation Service API, API Key Service API, and 42 more. Tagged areas include Observability, Telemetry, Aerospace, Defense, and Robotics.


  The Sift Stack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sift Stack''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, FAQ, and 27 more developer resources.'
plans:
- name: Sift Stack Plans Pricing
  plan_count: 0
  slug: sift-stack-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sift Stack Rate Limits
  slug: sift-stack-rate-limits
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 60.3
    developer_ergonomics: 73.8
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 59.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 55.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sift-stack/refs/heads/main/screenshots/sift-stack-2026-09-02T155415.png
security:
- kind: authentication
  name: Sift Stack Authentication
  slug: sift-stack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sift Stack Domain Security
  slug: sift-stack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sift Stack Vulnerability Disclosure
  slug: sift-stack-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sift Stack Trust Center
  slug: sift-stack-trust-center
  summary_line: SOC 2 Type II, NIST SP 800-171, ITAR, FedRAMP, CMMC Level 2
slug: sift-stack
tags:
- Observability
- Telemetry
- Aerospace
- Defense
- Robotics
- Time Series
- Sensor Data
- gRPC
- Data Ingestion
- Anomaly Detection
- Manufacturing
- Energy
- Autonomous Vehicles
- Machine Data
- Agent Ready
website: https://www.siftstack.com/
---
