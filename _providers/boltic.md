---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Boltic Agentic Access
  operation_count: 64
  slug: boltic-agentic-access
  summary_line: 64 operations · 36 acting
api_count: 3
apis:
- baseURL: https://gateway.boltic.io/v1
  baseurl_source: spec
  description: Manage SSL/TLS certificates
  name: Boltic Certificates API
  slug: boltic-certificates-api
- baseURL: https://gateway.boltic.io/v1
  baseurl_source: spec
  description: Manage API consumers and access credentials
  name: Boltic Consumers API
  slug: boltic-consumers-api
- baseURL: https://api.boltic.io/v1
  baseurl_source: spec
  description: Manage data destinations
  name: Boltic Destinations API
  slug: boltic-destinations-api
- baseURL: https://api.boltic.io/v1
  baseurl_source: spec
  description: Send and query events
  name: Boltic Events API
  slug: boltic-events-api
- baseURL: https://api.boltic.io/v1
  baseurl_source: spec
  description: Track and manage workflow executions
  name: Boltic Executions API
  slug: boltic-executions-api
- baseURL: https://gateway.boltic.io/v1
  baseurl_source: spec
  description: Manage gateway plugins for transformation and security
  name: Boltic Plugins API
  slug: boltic-plugins-api
- baseURL: https://gateway.boltic.io/v1
  baseurl_source: spec
  description: Manage API routes and request routing rules
  name: Boltic Routes API
  slug: boltic-routes-api
- baseURL: https://gateway.boltic.io/v1
  baseurl_source: spec
  description: The Services API from Boltic — 2 operation(s) for services.
  name: Boltic Services API
  slug: boltic-services-api
- baseURL: https://api.boltic.io/v1
  baseurl_source: spec
  description: Manage stream sources for event ingestion
  name: Boltic Stream Sources API
  slug: boltic-stream-sources-api
- baseURL: https://api.boltic.io/v1
  baseurl_source: spec
  description: Manage workflow triggers
  name: Boltic Triggers API
  slug: boltic-triggers-api
- baseURL: https://api.boltic.io/v1
  baseurl_source: spec
  description: Create and manage automation workflows
  name: Boltic Workflows API
  slug: boltic-workflows-api
artifact_total: 85
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Boltic Gateway Certificates API
  slug: open-boltic-certificates-api
- collection_type: open
  name: Boltic Gateway Certificates Consumers API
  slug: open-boltic-consumers-api
- collection_type: open
  name: Boltic Gateway Certificates Destinations API
  slug: open-boltic-destinations-api
- collection_type: open
  name: Boltic Gateway Certificates Events API
  slug: open-boltic-events-api
- collection_type: open
  name: Boltic Gateway Certificates Executions API
  slug: open-boltic-executions-api
- collection_type: open
  name: Boltic Gateway API
  slug: open-boltic-gateway-api
- collection_type: open
  name: Boltic Gateway Certificates Pipes API
  slug: open-boltic-pipes-api
- collection_type: open
  name: Boltic Gateway Certificates Plugins API
  slug: open-boltic-plugins-api
- collection_type: open
  name: Boltic Gateway Certificates Queries API
  slug: open-boltic-queries-api
- collection_type: open
  name: Boltic Gateway Certificates Routes API
  slug: open-boltic-routes-api
- collection_type: open
  name: Boltic Gateway Certificates Rows API
  slug: open-boltic-rows-api
- collection_type: open
  name: Boltic Gateway Certificates Services API
  slug: open-boltic-services-api
- collection_type: open
  name: Boltic Gateway Certificates Sources API
  slug: open-boltic-sources-api
- collection_type: open
  name: Boltic Gateway Certificates Stream Sources API
  slug: open-boltic-stream-sources-api
- collection_type: open
  name: Boltic Streams API
  slug: open-boltic-streams-api
- collection_type: open
  name: Boltic Gateway Certificates Sync Runs API
  slug: open-boltic-sync-runs-api
- collection_type: open
  name: Boltic Gateway Certificates Tables API
  slug: open-boltic-tables-api
- collection_type: open
  name: Boltic Gateway Certificates Triggers API
  slug: open-boltic-triggers-api
- collection_type: open
  name: Boltic Workflow API
  slug: open-boltic-workflow-api
- collection_type: open
  name: Boltic Gateway Certificates Workflows API
  slug: open-boltic-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boltic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boltic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boltic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bolticio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/officialboltic
- group: company
  title: ''
  type: Website
  url: https://www.boltic.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boltic.io/
- group: other
  title: ''
  type: Templates
  url: https://www.boltic.io/templates
- group: commercial
  title: ''
  type: Pricing
  url: https://www.boltic.io/pricing
- group: company
  title: ''
  type: About
  url: https://www.boltic.io/about-us
- group: company
  title: ''
  type: Partners
  url: https://www.boltic.io/partners
- group: company
  title: ''
  type: Blog
  url: https://www.boltic.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.boltic.io/changelog
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/boltic-context.jsonld
created: '2026-01-02'
description: Boltic is an AI workflow automation platform that helps businesses streamline operations across customer support, finance, product, and marketing functions. The platform enables companies to build autonomous AI agents, create no-code workflows with drag-and-drop functionality, and connect with over 500 integrations including major tools like Salesforce, HubSpot, Shopify, and Google BigQuery.
finops:
- name: Boltic Finops
  service_category: Workflow Automation
  slug: boltic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boltic.png
json_schemas:
- name: Certificate
  property_count: 6
  slug: boltic-certificate
- name: CertificateInput
  property_count: 3
  slug: boltic-certificateinput
- name: Column
  property_count: 6
  slug: boltic-column
- name: ColumnInput
  property_count: 5
  slug: boltic-columninput
- name: Consumer
  property_count: 6
  slug: boltic-consumer
- name: ConsumerInput
  property_count: 3
  slug: boltic-consumerinput
- name: DestinationConfig
  property_count: 3
  slug: boltic-destinationconfig
- name: DestinationType
  property_count: 4
  slug: boltic-destinationtype
- name: Error
  property_count: 3
  slug: boltic-error
- name: Event
  property_count: 9
  slug: boltic-event
- name: EventInput
  property_count: 7
  slug: boltic-eventinput
- name: Execution
  property_count: 10
  slug: boltic-execution
- name: Node
  property_count: 7
  slug: boltic-node
- name: NodeInput
  property_count: 6
  slug: boltic-nodeinput
- name: Pagination
  property_count: 4
  slug: boltic-pagination
- name: Pipe
  property_count: 11
  slug: boltic-pipe
- name: Boltic Pipe
  property_count: 11
  slug: boltic-pipe
- name: PipeInput
  property_count: 5
  slug: boltic-pipeinput
- name: Plugin
  property_count: 8
  slug: boltic-plugin
- name: PluginInput
  property_count: 6
  slug: boltic-plugininput
- name: Route
  property_count: 12
  slug: boltic-route
- name: Boltic Gateway Route
  property_count: 12
  slug: boltic-route
- name: RouteInput
  property_count: 9
  slug: boltic-routeinput
- name: Row
  property_count: 4
  slug: boltic-row
- name: RowInput
  property_count: 1
  slug: boltic-rowinput
- name: Schedule
  property_count: 4
  slug: boltic-schedule
- name: Service
  property_count: 11
  slug: boltic-service
- name: ServiceInput
  property_count: 8
  slug: boltic-serviceinput
- name: SourceConfig
  property_count: 5
  slug: boltic-sourceconfig
- name: SourceType
  property_count: 4
  slug: boltic-sourcetype
- name: Boltic Stream Event
  property_count: 9
  slug: boltic-stream-event
- name: StreamDestination
  property_count: 6
  slug: boltic-streamdestination
- name: StreamDestinationInput
  property_count: 3
  slug: boltic-streamdestinationinput
- name: StreamSource
  property_count: 7
  slug: boltic-streamsource
- name: StreamSourceInput
  property_count: 2
  slug: boltic-streamsourceinput
- name: SyncRun
  property_count: 9
  slug: boltic-syncrun
- name: Table
  property_count: 7
  slug: boltic-table
- name: Boltic Table
  property_count: 7
  slug: boltic-table
- name: TableInput
  property_count: 3
  slug: boltic-tableinput
- name: Trigger
  property_count: 4
  slug: boltic-trigger
- name: TriggerInput
  property_count: 3
  slug: boltic-triggerinput
- name: Workflow
  property_count: 11
  slug: boltic-workflow
- name: Boltic Workflow
  property_count: 11
  slug: boltic-workflow
- name: WorkflowInput
  property_count: 5
  slug: boltic-workflowinput
json_structures:
- name: Boltic Structure
  property_count: 0
  slug: boltic-structure
jsonld:
- class_count: 36
  name: Boltic Context
  property_count: 9
  slug: boltic-context
layout: provider
modified: '2026-05-19'
name: Boltic
nav: Providers
network: true
overview: 'Boltic publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Consumers API, Destinations API, and 8 more. Tagged areas include Automation, Data Sync, Gateways, No-Code, and Streaming.


  The Boltic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Boltic''s developer surface includes authentication, documentation, pricing, engineering blog, changelog, and 9 more developer resources.'
plans:
- name: Boltic Plans Pricing
  plan_count: 5
  slug: boltic-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Boltic Rate Limits
  slug: boltic-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Boltic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: boltic-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 66.9
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boltic/refs/heads/main/screenshots/boltic-2026-06-20T173556.png
security:
- kind: authentication
  name: Boltic Authentication
  slug: boltic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Boltic Domain Security
  slug: boltic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boltic
tags:
- Automation
- Data Sync
- Gateways
- No-Code
- Streaming
- Workflows
website: https://www.boltic.io/
---
