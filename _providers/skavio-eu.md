---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 84
  human_in_the_loop: 18
  name: Skavio Eu Agentic Access
  operation_count: 165
  slug: skavio-eu-agentic-access
  summary_line: 165 operations · 84 acting · 18 human-in-the-loop
api_count: 3
apis:
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Batch processing API from skavio-eu — 5 operation(s) for batch processing.
  name: skavio-eu Batch processing API
  slug: skavio-eu-batch-processing-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Billing API from skavio-eu — 11 operation(s) for billing.
  name: skavio-eu Billing API
  slug: skavio-eu-billing-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Bulk manifests API from skavio-eu — 10 operation(s) for bulk manifests.
  name: skavio-eu Bulk manifests API
  slug: skavio-eu-bulk-manifests-api
- baseURL: https://www.skavio.eu/proof
  baseurl_source: declared
  description: The Contacts API from skavio-eu — 1 operation(s) for contacts.
  name: skavio-eu Contacts API
  slug: skavio-eu-contacts-api
- baseURL: https://www.skavio.eu/proof
  baseurl_source: declared
  description: The Events API from skavio-eu — 1 operation(s) for events.
  name: skavio-eu Events API
  slug: skavio-eu-events-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Flow API from skavio-eu — 1 operation(s) for flow.
  name: skavio-eu Flow API
  slug: skavio-eu-flow-api
- baseURL: https://www.skavio.eu/proof
  baseurl_source: declared
  description: The Invoices API from skavio-eu — 3 operation(s) for invoices.
  name: skavio-eu Invoices API
  slug: skavio-eu-invoices-api
- baseURL: https://www.skavio.eu/proof
  baseurl_source: declared
  description: The Me API from skavio-eu — 1 operation(s) for me.
  name: skavio-eu Me API
  slug: skavio-eu-me-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Operational notifications API from skavio-eu — 2 operation(s) for operational notifications.
  name: skavio-eu Operational notifications API
  slug: skavio-eu-operational-notifications-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The paid web data API from skavio-eu — 4 operation(s) for paid web data.
  name: skavio-eu paid web data API
  slug: skavio-eu-paid-web-data-api
- baseURL: https://www.skavio.eu/proof
  baseurl_source: declared
  description: The Requests API from skavio-eu — 2 operation(s) for requests.
  name: skavio-eu Requests API
  slug: skavio-eu-requests-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Skavio Accounting API from skavio-eu — 16 operation(s) for skavio accounting.
  name: skavio-eu Skavio Accounting API
  slug: skavio-eu-skavio-accounting-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Skavio processing API API from skavio-eu — 55 operation(s) for skavio processing api.
  name: skavio-eu Skavio processing API
  slug: skavio-eu-skavio-processing-api-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The USDC payment verification API from skavio-eu — 3 operation(s) for usdc payment verification.
  name: skavio-eu USDC payment verification API
  slug: skavio-eu-usdc-payment-verification-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Webhooks API from skavio-eu — 4 operation(s) for webhooks.
  name: skavio-eu Webhooks API
  slug: skavio-eu-webhooks-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The Workflow pipelines API from skavio-eu — 8 operation(s) for workflow pipelines.
  name: skavio-eu Workflow pipelines API
  slug: skavio-eu-workflow-pipelines-api
- baseURL: https://getskavio.com
  baseurl_source: declared
  description: The X402 API from skavio-eu — 7 operation(s) for x402.
  name: skavio-eu X402 API
  slug: skavio-eu-x402-api
artifact_total: 38
asyncapis:
- description: ''
  name: Skavio Eu Webhooks
  slug: skavio-eu-webhooks
common:
- group: build
  href: https://artifacts.apis.io/skavio-eu/integrations/skavio-eu-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/skavio-eu-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/skavio-eu/agentic-access/skavio-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/skavio-eu-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/rules/skavio-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/skavio-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/json-ld/skavio-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/skavio-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/skavio-eu/vocabulary/skavio-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/skavio-eu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/skavio-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/asyncapi/skavio-eu-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/skavio-eu-webhooks.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/data-model/skavio-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skavio-eu-data-model.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/conventions/skavio-eu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/skavio-eu-conventions.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/conventions/skavio-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/skavio-eu-conventions.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/errors/skavio-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/skavio-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/skavio-eu/conformance/skavio-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skavio-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/skavio-eu/llms/skavio-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skavio-eu-llms.txt
- group: auth
  href: https://artifacts.apis.io/skavio-eu/well-known/skavio-eu-mcprush-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skavio-eu-mcprush-security.txt
- group: agent
  href: https://artifacts.apis.io/skavio-eu/well-known/skavio-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skavio-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/skavio-eu/hosts/skavio-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skavio-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/skavio-eu/vendors/skavio-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skavio-eu-vendors.yml
- group: auth
  href: https://artifacts.apis.io/skavio-eu/authentication/skavio-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skavio-eu-authentication.yml
- group: auth
  href: https://artifacts.apis.io/skavio-eu/security/skavio-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skavio-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skavio.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getskavio.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://getskavio.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://getskavio.com/api/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://getskavio.com/
- group: operate
  title: ''
  type: Support
  url: https://getskavio.com/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://getskavio.com/checkout/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getskavio.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getskavio.com/privacy/
created: '2026-10-30'
description: Skavio LLC offers a suite of simple business tools that automate document handling, invoice conversion, audio transcription, meeting note generation, and payment proof creation. Users can upload PDFs or audio files and receive structured CSVs, transcripts, or verified payment links, with transparent pricing displayed before processing. The platform provides developer integrations, live x402 payment APIs, MCP processing endpoints, and detailed documentation for each tool.
image: https://via.placeholder.com/300?text=Skavio
json_schemas:
- name: Batch
  property_count: 15
  slug: skavio-eu-batch
- name: BatchSpec
  property_count: 10
  slug: skavio-eu-batch-spec
- name: BulkSpec
  property_count: 12
  slug: skavio-eu-bulk-spec
- name: Event
  property_count: 5
  slug: skavio-eu-event
- name: InvoiceCreate
  property_count: 12
  slug: skavio-eu-invoice-create
- name: Invoice
  property_count: 13
  slug: skavio-eu-invoice
- name: Me
  property_count: 4
  slug: skavio-eu-me
- name: PipelineRun
  property_count: 12
  slug: skavio-eu-pipeline-run
- name: RequestCreate
  property_count: 6
  slug: skavio-eu-request-create
- name: Request
  property_count: 15
  slug: skavio-eu-request
- name: Spec
  property_count: 8
  slug: skavio-eu-spec
- name: StorageObject
  property_count: 16
  slug: skavio-eu-storage-object
jsonld:
- class_count: 89
  name: Skavio Eu Context
  property_count: 220
  slug: skavio-eu-context
layout: provider
modified: '2026-10-30'
name: skavio-eu
nav: Providers
network: true
overview: 'skavio-eu publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch processing API, Billing API, Bulk manifests API, and 14 more. Tagged areas include BusinessTools, Document Processing, Invoice Automation, Audio Transcription, and Payments.


  The skavio-eu catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  skavio-eu''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 22 more developer resources.'
plans:
- name: Skavio Eu Plans Pricing
  plan_count: 0
  slug: skavio-eu-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: skavio-eu API Rules
  rule_count: 14
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 5
  slug: skavio-eu-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 67.0
    developer_ergonomics: 61.2
    discoverability: 71.4
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Skavio Eu Authentication
  slug: skavio-eu-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Skavio Eu Domain Security
  slug: skavio-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: skavio-eu-processing
  slug: skavio-eu-processing
- name: skavio-eu-x402
  slug: skavio-eu-x402
slug: skavio-eu
tags:
- BusinessTools
- Document Processing
- Invoice Automation
- Audio Transcription
- Payments
website: https://skavio.eu/
---
