---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Invoicecraftly Agentic Access
  operation_count: 3
  slug: invoicecraftly-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- baseURL: https://invoicecraftly.com
  baseurl_source: declared
  description: Invoice document generation.
  name: InvoiceCraftly Developer Document API Documents API
  slug: invoicecraftly-documents-api
- baseURL: https://invoicecraftly.com
  baseurl_source: declared
  description: EN16931-core readiness and structured XML.
  name: InvoiceCraftly Developer Document API Structured invoicing API
  slug: invoicecraftly-structured-invoicing-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/invoicecraftly/well-known/invoicecraftly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/invoicecraftly-well-known.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://invoicecraftly.com/developers/recipes/
- group: company
  title: ''
  type: BlogRSS
  url: https://invoicecraftly.com/feed.xml
- group: other
  href: https://artifacts.apis.io/invoicecraftly/capabilities/invoicecraftly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/invoicecraftly-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/invoicecraftly/overlays/invoicecraftly-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/invoicecraftly-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/invoicecraftly/agentic-access/invoicecraftly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/invoicecraftly-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/invoicecraftly/plans/invoicecraftly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/invoicecraftly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/invoicecraftly/rules/invoicecraftly-rules.yml
  title: ''
  type: Spectral
  url: rules/invoicecraftly-rules.yml
- group: design
  href: https://artifacts.apis.io/invoicecraftly/json-ld/invoicecraftly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/invoicecraftly-context.jsonld
- group: design
  href: https://artifacts.apis.io/invoicecraftly/vocabulary/invoicecraftly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/invoicecraftly-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/invoicecraftly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/invoicecraftly/data-model/invoicecraftly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/invoicecraftly-data-model.yml
- group: operate
  href: https://artifacts.apis.io/invoicecraftly/changelog/invoicecraftly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/invoicecraftly-changelog.yml
- group: design
  href: https://artifacts.apis.io/invoicecraftly/errors/invoicecraftly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/invoicecraftly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/invoicecraftly/conformance/invoicecraftly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/invoicecraftly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/invoicecraftly/llms/invoicecraftly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/invoicecraftly-llms.txt
- group: other
  href: https://artifacts.apis.io/invoicecraftly/hosts/invoicecraftly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/invoicecraftly-hosts.yml
- group: other
  href: https://artifacts.apis.io/invoicecraftly/vendors/invoicecraftly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/invoicecraftly-vendors.yml
- group: build
  href: https://artifacts.apis.io/invoicecraftly/packages/invoicecraftly-packages.yml
  title: ''
  type: SDKs
  url: packages/invoicecraftly-packages.yml
- group: build
  href: https://artifacts.apis.io/invoicecraftly/packages/invoicecraftly-packages.yml
  title: ''
  type: Packages
  url: packages/invoicecraftly-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://invoicecraftly.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://invoicecraftly.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://invoicecraftly.com/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://invoicecraftly.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://invoicecraftly.com/developers/
- group: auth
  href: https://artifacts.apis.io/invoicecraftly/authentication/invoicecraftly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/invoicecraftly-authentication.yml
- group: auth
  href: https://artifacts.apis.io/invoicecraftly/security/invoicecraftly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invoicecraftly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://invoicecraftly.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://invoicecraftly.com/guides/
- group: operate
  title: ''
  type: Support
  url: https://invoicecraftly.com/contact
created: '2026-09-25'
description: InvoiceCraftly provides a free, no‑signup invoice generator and related tools. Users can create, edit, and export professional invoices, quotes, estimates, receipts, and credit notes in PDF, PNG, SVG, and CSV formats. The platform offers templates, company lookup, QR‑code payment integration, and multilingual support, targeting freelancers, small businesses, and enterprises seeking a simple invoicing solution without account requirements.
finops:
- has_sources: true
  method: derived
  name: Invoicecraftly Finops
  primary_unit: ''
  service_category: ''
  slug: invoicecraftly-finops
  template: true
image: https://invoicecraftly.com/assets/social/homepage-invoice-generator-1200x630.png
json_schemas:
- name: PublicDocumentV1
  property_count: 13
  slug: invoicecraftly-public-document-v1
- name: PublicStructuredArtifactRequestV1
  property_count: 2
  slug: invoicecraftly-public-structured-artifact-request-v1
- name: ReadinessResponse
  property_count: 5
  slug: invoicecraftly-readiness-response
- name: StructuredArtifactResponse
  property_count: 6
  slug: invoicecraftly-structured-artifact-response
jsonld:
- class_count: 15
  name: Invoicecraftly Context
  property_count: 64
  slug: invoicecraftly-context
layout: provider
modified: '2026-10-06'
name: InvoiceCraftly Developer Document API
nav: Providers
network: true
overview: 'InvoiceCraftly Developer Document API publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Documents API and Structured invoicing API. Tagged areas include Invoicing, Invoice Generator, Free Tools, DocumentExport, and Payment QR.


  The InvoiceCraftly Developer Document API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  InvoiceCraftly Developer Document API''s developer surface includes pricing, changelog, documentation, API reference, authentication, getting-started guide, support, and 23 more developer resources.'
plans:
- name: Invoicecraftly Plans Pricing
  plan_count: 1
  slug: invoicecraftly-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: InvoiceCraftly Developer Document API API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: invoicecraftly-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 70.1
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/invoicecraftly/invoicecraftly-2026-10-11T105827.png
security:
- kind: authentication
  name: Invoicecraftly Authentication
  slug: invoicecraftly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Invoicecraftly Domain Security
  slug: invoicecraftly-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: invoicecraftly-check-and-generate-structured-invoice
  slug: invoicecraftly-check-and-generate-structured-invoice
slug: invoicecraftly
tags:
- Invoicing
- Invoice Generator
- Free Tools
- DocumentExport
- Payment QR
- CSV Import
- Company Lookup
website: https://invoicecraftly.com/
---
