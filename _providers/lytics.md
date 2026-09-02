---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 941
  human_in_the_loop: 3
  name: Lytics Agentic Access
  operation_count: 1467
  slug: lytics-agentic-access
  summary_line: 1467 operations · 941 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: 'Account related resources of the *Lytics API*. The Account resource describes an account. An account can be a *Master* account, which means that it is a billing account. Master accounts have children '
  name: Lytics Account API
  slug: lytics-account-api
- description: Account Settings describe features/settings for a Lytics account.
  name: Lytics Account Settings API
  slug: lytics-account-settings-api
- description: API for creation or storage of auth tokens. Most of these tokens are created from the Integrations/Imports setup for Lytics integrations. Additionally, api tokens can be created/managed from this endp
  name: Lytics Auth API
  slug: lytics-auth-api
- description: Create and manage credentials and access to external systems.
  name: Lytics Auths API
  slug: lytics-auths-api
- description: Catalog exposes info about the schema of the data in Lytics. * **Entities** are Object Types, the primary one being a *User* although most accounts also have *Content* and *Campaign* as well. Custom o
  name: Lytics Catalog API
  slug: lytics-catalog-api
- description: Create and manage connections to external data sources.
  name: Lytics Connections API
  slug: lytics-connections-api
- description: Content APIs for Lytics Content Affinity Engine, allow for adding content into lytics, getting lists of content, and understanding the content and content-topics. **Content Classification** Content cl
  name: Lytics Content API
  slug: lytics-content-api
- description: Create and manage data models and their record stores.
  name: Lytics Data Models API
  slug: lytics-datamodels-api
- description: APIs for collecting or uploading data. There are two main APIs, one for uploading Large files (bulk, millions of records) and another for sending real-time, or slightly batched events (Less than 10MB)
  name: Lytics Data Upload API
  slug: lytics-dataupload-api
- description: API for creating and managing Experiences as well as all related and/or dependent models such as but not limited to Groups, Templates, Candidates, etc.
  name: Lytics Experience API
  slug: lytics-experience-api
- description: Create and manage flows that orchestrate multi-step audience journeys.
  name: Lytics Flows API
  slug: lytics-flows-api
- description: Create and manage data import and export jobs.
  name: Lytics Jobs API
  slug: lytics-jobs-api
- description: 'The Metric API provides access to a variety of metrics that are recorded in the Lytics platform. With this API, you can access segment-size metrics, events received per-hour, as well as many workflow '
  name: Lytics Metric API
  slug: lytics-metric-api
- description: Query time series metrics for segments, streams, experiences, and other Lytics resources.
  name: Lytics Metrics API
  slug: lytics-metrics-api
- description: The ML Models API from Lytics — 3 operation(s) for ml models.
  name: Lytics ML Models API
  slug: lytics-ml-models-api
- description: 'Entity API, ie Personalization or Profile API. Retrieve attributes and segments an entity (most likely a user) is a member of. The *Entity* is a *User* most likely, but since Lytics is organized as a '
  name: Lytics Personalization API
  slug: lytics-personalization-api
- description: Get and delete user profiles.
  name: Lytics Profiles API
  slug: lytics-profiles-api
- description: Provider is a 3rd party Lytics Integrates with (Mailchimp, Optimizely, Mixpanel, Facebook etc)
  name: Lytics Provider API
  slug: lytics-provider-api
- description: Schema management api to add/edit queries and user-fields. Lytics Query Language ============================= The Lytics Query Language is used to define the transformation of uploaded records, and e
  name: Lytics Query API
  slug: lytics-query-api
- description: Create and manage reports.
  name: Lytics Reports API
  slug: lytics-reports-api
- description: Manage how data sources populate profile fields.
  name: Lytics Schema API
  slug: lytics-schema-api
- description: Segments are named, logical expressions of users. These segments may logically be built using other segments as well. The segment api provides a list of segments built by both the admin, pre-defined s
  name: Lytics Segment API
  slug: lytics-segment-api
- description: Segment Collections are grouped/named lists of segments. Segments that participate in a collection such as **Goals** are related. The Lytics App ui has one predefined collection called **Goals** which
  name: Lytics Segment Collection API
  slug: lytics-segmentcollection-api
- description: SegmentML provides a framework for building custom machine learning models directly in Lytics. Lytics SegmentML models are self-training, continuously-updating and real-time. SegmentML models are buil
  name: Lytics Segment ML API
  slug: lytics-segmentml-api
- description: Create and manage audience segments.
  name: Lytics Segments API
  slug: lytics-segments-api
- description: 'API for creating stream models. A stream is the same as a [data stream](https://learn.lytics.com/product-docs/data-management/using-data-streams#what-are-data-streams? ) and is consumed for ingestion '
  name: Lytics Stream API
  slug: lytics-stream-api
- description: Get metrics and events for data streams in your Lytics account.
  name: Lytics Streams API
  slug: lytics-streams-api
- description: '**BETA API** Subscriptions are queries into real-time events in Lytics, most commonly listening to a list of users entering/leaving segments ie _triggers_. **Common Use Cases** * Upon Entering/Leaving'
  name: Lytics Subscription API
  slug: lytics-subscription-api
- description: Manage Lytics system users and their access to data and resources.
  name: Lytics System API
  slug: lytics-system-api
- description: Get internal Lytics system events. These events are generally related to internal changes to state of an account. Common changes are CRUD Operations (Create, Update, Delete) of *Account*, *Admin User*
  name: Lytics System Events API
  slug: lytics-system-events-api
- description: Create, manage, and test templates.
  name: Lytics Templates API
  slug: lytics-templates-api
- description: Info about Administrative Lytics account users * Lytics users are unique across accounts * They get *invited* to have access to your account
  name: Lytics User API
  slug: lytics-user-api
- description: 'Work is an *integration* unit, typically for imports and exports. Most run continually, while some run to completion. You generally would only use it through the Webadmin Integrations. * *Workflow* A '
  name: Lytics Work API
  slug: lytics-work-api
- description: Workflow is a specification for a work unit
  name: Lytics Workflow API
  slug: lytics-workflow-api
artifact_total: 54
asyncapis:
- description: ''
  name: Lytics Webhooks
  slug: lytics-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: V1 Lytics API
  slug: open-lytics-api-v1
- collection_type: open
  name: Lytics API
  slug: open-lytics-api-v2
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lytics-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lytics-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lytics-api-v1-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lytics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lytics.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lytics
- group: company
  title: ''
  type: Blog
  url: https://www.lytics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lytics.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://lytics.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/lyticsio
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lytics.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.lytics.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/lytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lytics-finops.yml
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://dash.readme.com/api/v1/api-registry/1y876emrv8pb2i
- group: build
  title: ''
  type: Packages
  url: packages/lytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lytics-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lytics-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lytics-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/lytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lytics-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lytics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lytics-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/lytics-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lytics-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lytics-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lytics-trust-center.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lytics-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/lytics-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lytics-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lytics-user-profile-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lytics-collect-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lytics-segment-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-user-profile-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-collect-event-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-segment-scan-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-segment-scan-response-example.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lytics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lytics.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lytics.com/reference/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.lytics.com/docs/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.lytics.com/register
- group: start
  title: ''
  type: Login
  url: https://app.lytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lytics.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lytics.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lytics-cdp/lytics-s-public-workspace
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lytics
- group: operate
  title: ''
  type: Community
  url: https://docs.lytics.com/discuss
- group: auth
  title: ''
  type: Compliance
  url: https://docs.lytics.com/docs/compliance
created: '2026-06-13'
description: Lytics is a customer data platform (CDP) that provides two concurrent REST APIs for managing unified user profiles, behavioral audiences, content affinity scoring, campaign flows, and real-time personalization. The v2 API (886 paths / 1,331 operations) covers accounts, authorizations, connections, schema and identity configuration, data models, streams, jobs and ML models; the v1 API still owns data collection, personalization, entity lookup and content classification. Lytics ingests data from 100+ sources, builds predictive audiences, and activates them across advertising networks, email providers, data warehouses and on-site personalization. Lytics joined Contentstack in January 2025.
examples:
- key_count: 7
  name: Lytics Collect Event Example
  slug: lytics-collect-event-example
- key_count: 1
  name: Lytics Segment Scan Request Example
  slug: lytics-segment-scan-request-example
- key_count: 5
  name: Lytics Segment Scan Response Example
  slug: lytics-segment-scan-response-example
- key_count: 11
  name: Lytics User Profile Example
  slug: lytics-user-profile-example
finops:
- name: Lytics Finops
  service_category: ''
  slug: lytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lytics.png
json_schemas:
- name: Lytics Collect Event
  property_count: 7
  slug: lytics-collect-event
- name: Lytics Segment
  property_count: 10
  slug: lytics-segment
- name: Lytics User Profile
  property_count: 11
  slug: lytics-user-profile
jsonld:
- class_count: 8
  name: Lytics Context
  property_count: 32
  slug: lytics-context
layout: provider
modified: '2026-08-13'
name: Lytics
nav: Providers
network: true
overview: 'Lytics publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Settings API, Auth API, and 31 more. Tagged areas include Customer Data Platform, CDP, Personalization, Segmentation, and User Profiles.


  The Lytics catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lytics'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, CLI, and 49 more developer resources.'
plans:
- name: Lytics Plans Pricing
  plan_count: 3
  slug: lytics-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Lytics Rate Limits
  slug: lytics-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lytics-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 31
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.6
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 29.5
    contract_quality: 69.5
    developer_ergonomics: 65.5
    discoverability: 51.9
    governance: 29.5
    operational_transparency: 34.2
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lytics/refs/heads/main/screenshots/lytics-2026-06-20T184816.png
security:
- kind: authentication
  name: Lytics Authentication
  slug: lytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lytics Domain Security
  slug: lytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lytics Trust Center
  slug: lytics-trust-center
  summary_line: trust center published
slug: lytics
tags:
- Customer Data Platform
- CDP
- Personalization
- Segmentation
- User Profiles
- Behavioral Analytics
- Content Affinity
- Real-Time Data
- Marketing Automation
- Audience Activation
website: https://www.lytics.com/
---
