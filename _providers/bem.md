---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Bem Agentic Access
  operation_count: 86
  slug: bem-agentic-access
  summary_line: 86 operations · 50 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Buckets are named partitions of the knowledge graph within an account+environment. Entities, mentions, and relations are scoped to a bucket so a single account+environment can host multiple isolated g
  name: Bem Buckets API
  slug: bem-buckets-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'The Calls API provides a unified interface for invoking both **Workflows** and **Functions**. Use this API when you want to: - Execute a complete workflow that chains multiple functions together - Cal'
  name: Bem Calls API
  slug: bem-calls-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Collections are named groups of embedded items used by Enrich functions for semantic search. Each collection is referenced by a `collectionName`, which supports dot notation for hierarchical paths (e.
  name: Bem Collections API
  slug: bem-collections-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Connectors are integrations that trigger a Bem workflow from an external system. A connector binds an inbound source — currently Box or a Paragon-managed integration such as Google Drive — to a specif
  name: Bem Connectors API
  slug: bem-connectors-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Seed the knowledge graph with a batch of customer-authored canonical entities in one request — their types, descriptions, synonyms, and per-entity attributes. - **`POST /v3/entities/bulk`** creates or
  name: Bem Entity Bulk Seed API
  slug: bem-entity-bulk-seed-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'Curate the knowledge graph by transitioning entities through their review lifecycle and editing their metadata. - **`PATCH /v3/entities/{id}`** updates a single entity. Every field is optional but at '
  name: Bem Entity Curation API
  slug: bem-entity-curation-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Manage the human-readable surface forms (synonyms) attached to a canonical entity. Synonyms feed the matcher's exact-match path, so adding the right synonyms improves cross-document entity resolution.
  name: Bem Entity Synonyms API
  slug: bem-entity-synonyms-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'Reviewer assignments link users to the entity types they are responsible for reviewing, scoped to an account+environment. These are dashboard-only endpoints: an assignment needs a user identity, which'
  name: Bem Entity Type Reviewers API
  slug: bem-entity-type-reviewers-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Entity Types are the customer-defined taxonomy for the knowledge graph, scoped to an account+environment. Each type has a unique, immutable name and can be organised into hierarchies via `parentTypeID
  name: Bem Entity Types API
  slug: bem-entity-types-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Retrieve terminal error events from workflow calls. Errors are events produced by function steps that failed during processing. A single workflow call may produce multiple error events if several step
  name: Bem Errors API
  slug: bem-errors-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Submit training corrections for `extract`, `classify`, and `join` events. Feedback is event-centric — each correction is attached to an event by its `eventID`, and the server resolves the correct unde
  name: Bem Feedback API
  slug: bem-feedback-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'Monitor, evaluate, and iterate on the quality of every function in your environment. Function Accuracy bundles two complementary loops: ## Evaluations (`/v3/eval`) Trigger and retrieve per-transformat'
  name: Bem Function Accuracy API
  slug: bem-function-accuracy-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'Functions are the core building blocks of data transformation in Bem. Each function type serves a specific purpose: - **Extract**: Extract structured JSON data from unstructured documents (PDFs, email'
  name: Bem Functions API
  slug: bem-functions-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Read the cross-document knowledge graph — the canonical entities and the directed relations between them that the Parse pipeline populates when `linkAcrossDocuments` is enabled. - **`GET /v3/entities/
  name: Bem Knowledge Graph API
  slug: bem-knowledge-graph-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Retrieve terminal non-error output events from workflow calls. Outputs are events produced by successful terminal function steps — steps that completed without errors and did not spawn further downstr
  name: Bem Outputs API
  slug: bem-outputs-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: The reviewer-facing read surface for entity curation, available on the dashboard (JWT) only. - **`GET /v3/review-queue`** returns a cursor-paginated set of entities awaiting curation, scoped to your a
  name: Bem Review Queue API
  slug: bem-review-queue-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Infer JSON Schemas from uploaded documents using AI. Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema that captures the document's structure. The inferred
  name: Bem Schema Inference API
  slug: bem-schema-inference-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Subscriptions wire up notifications for the events your functions and collections produce. Most subscriptions target a single function (by `functionName` or `functionID`) or a single collection (by `c
  name: Bem Subscriptions API
  slug: bem-subscriptions-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'Views are tabular projections over the `transformations` your functions produce — a saved query that turns raw extracted JSON into a filterable, paginatable, aggregatable table. ## Anatomy A view decl'
  name: Bem Views API
  slug: bem-views-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: 'bem POSTs a JSON event to your configured webhook URL each time a subscribed function call, workflow output, or collection-processing job fires. This section is the reference for those deliveries: the'
  name: Bem Webhooks API
  slug: bem-webhooks-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing. Use these endpoints to create, update, list, and manage workflows, and to invoke them with file
  name: Bem Workflows API
  slug: bem-workflows-api
- baseURL: https://api.bem.ai
  baseurl_source: declared
  description: Unix-shell-style nav over parsed documents and the cross-doc memory store.
  name: Bem Filesystem API
  slug: bem-filesystem-api
artifact_total: 55
asyncapis:
- description: ''
  name: Bem Webhooks
  slug: bem-webhooks
collections:
- collection_type: open
  name: Bem Buckets API
  slug: open-bem-buckets-api
- collection_type: open
  name: Bem Buckets Calls API
  slug: open-bem-calls-api
- collection_type: open
  name: Bem Buckets Collections API
  slug: open-bem-collections-api
- collection_type: open
  name: Bem Buckets Connectors API
  slug: open-bem-connectors-api
- collection_type: open
  name: Bem Buckets Entity Bulk Seed API
  slug: open-bem-entity-bulk-seed-api
- collection_type: open
  name: Bem Buckets Entity Curation API
  slug: open-bem-entity-curation-api
- collection_type: open
  name: Bem Buckets Entity Synonyms API
  slug: open-bem-entity-synonyms-api
- collection_type: open
  name: Bem Buckets Entity Types API
  slug: open-bem-entity-types-api
- collection_type: open
  name: Bem Buckets Errors API
  slug: open-bem-errors-api
- collection_type: open
  name: Bem Buckets Feedback API
  slug: open-bem-feedback-api
- collection_type: open
  name: Bem Buckets File System API
  slug: open-bem-file-system-api
- collection_type: open
  name: Bem Buckets Function Accuracy API
  slug: open-bem-function-accuracy-api
- collection_type: open
  name: Bem Buckets Functions API
  slug: open-bem-functions-api
- collection_type: open
  name: Bem Buckets Knowledge Graph API
  slug: open-bem-knowledge-graph-api
- collection_type: open
  name: Bem Buckets Outputs API
  slug: open-bem-outputs-api
- collection_type: open
  name: Bem Buckets Schema Inference API
  slug: open-bem-schema-inference-api
- collection_type: open
  name: Bem Buckets Subscriptions API
  slug: open-bem-subscriptions-api
- collection_type: open
  name: Bem Buckets Views API
  slug: open-bem-views-api
- collection_type: open
  name: Bem Buckets Webhooks API
  slug: open-bem-webhooks-api
- collection_type: open
  name: Bem Buckets Workflows API
  slug: open-bem-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bem/overview
- group: commercial
  href: https://artifacts.apis.io/bem/plans/bem-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bem-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.bem.ai/feed
- group: other
  href: https://artifacts.apis.io/bem/capabilities/bem-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bem-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/bem/overlays/bem-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bem-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bem.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bem.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bem.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bem.ai/api/v3/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bem.ai/guide/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.bem.ai/log
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bem.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.bem.ai/auth/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bem.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bem.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bem.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bem-team
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bem.ai
- group: auth
  title: ''
  type: Compliance
  url: https://www.bem.ai/security
- group: design
  href: https://artifacts.apis.io/bem/lifecycle/bem-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bem-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/bem/lifecycle/bem-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bem-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/bem/authentication/bem-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bem-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bem/security/bem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bem-domain-security.yml
- group: design
  href: https://artifacts.apis.io/bem/conformance/bem-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bem-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bem/agentic-access/bem-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bem-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/bem/packages/bem-packages.yml
  title: ''
  type: Packages
  url: packages/bem-packages.yml
- group: build
  href: https://artifacts.apis.io/bem/packages/bem-packages.yml
  title: ''
  type: SDKs
  url: packages/bem-packages.yml
- group: build
  href: https://artifacts.apis.io/bem/cli/bem-cli.yml
  title: ''
  type: CLI
  url: cli/bem-cli.yml
- group: agent
  href: https://artifacts.apis.io/bem/mcp/bem-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bem-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bem/llms/bem-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bem-llms.txt
- group: design
  href: https://artifacts.apis.io/bem/errors/bem-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bem-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bem/conventions/bem-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bem-conventions.yml
- group: design
  href: https://artifacts.apis.io/bem/conventions/bem-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bem-conventions.yml
- group: design
  href: https://artifacts.apis.io/bem/data-model/bem-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bem-data-model.yml
- group: design
  href: https://artifacts.apis.io/bem/asyncapi/bem-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bem-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/bem/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bem is the production layer for unstructured data. Its API turns inbound documents — PDFs, images, video, audio, and email — into structured JSON against a schema you define, using versioned, LLM-powered functions (extract, classify, parse, split, join, enrich, payload-shaping, and send) composed into reusable workflows. Bem automates document-heavy tasks such as invoice handling, claims adjudication, and data onboarding, with automatic schema inference, strict type enforcement, confidence scoring and drift detection, human-in-the-loop review, webhooks, and a knowledge graph. It offers US and EU regional endpoints, official SDKs, a CLI, a Terraform provider, and an MCP server, and is SOC 2 Type II, HIPAA, and GDPR compliant.
finops:
- has_sources: true
  method: derived
  name: Bem Finops
  primary_unit: function call
  service_category: ''
  slug: bem-finops
  template: false
image: https://avatars.githubusercontent.com/u/151673182?v=4
layout: provider
mcp_servers:
- description: 'The bem MCP server exposes the bem API to Claude, Cursor, and other MCP-compatible agents. It operates in "Code Mode": rather than one tool per endpoint, the agent writes and runs TypeScript against t'
  name: Bem MCP Server
  slug: bem
modified: '2026-10-06'
name: Bem
nav: Providers
network: true
overview: 'Bem publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buckets API, Calls API, Collections API, and 19 more. Tagged areas include Company, Document Processing, Unstructured Data, Data Extraction, and Artificial Intelligence.


  The Bem catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bem''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 29 more developer resources.'
plans:
- name: Bem Plans Pricing
  plan_count: 10
  slug: bem-plans-pricing
- name: Bem Price Estimates
  plan_count: 0
  slug: bem-price-estimates
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Bem API Rules
  rule_count: 59
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 12
  slug: bem-rules
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 57.2
    developer_ergonomics: 69.6
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 77.8
screenshot: https://apis.io/screenshots/bem/bem-2026-07-25T202722.png
security:
- kind: authentication
  name: Bem Authentication
  slug: bem-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bem Domain Security
  slug: bem-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Bem Trust Center
  slug: bem-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR
skill_count: 3
skills:
- name: Extract structured data from a document
  slug: bem-extract-structured-data
- name: Infer a schema and build an extractor
  slug: bem-infer-schema-and-build-extractor
- name: Subscribe to webhook events and verify signatures
  slug: bem-subscribe-to-webhook-events
slug: bem
tags:
- Company
- Document Processing
- Unstructured Data
- Data Extraction
- Artificial Intelligence
- LLM
- ETL
- Schema Inference
- Webhook
website: https://bem.ai
---
