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
  band: agent-ready
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Sensible Io Agentic Access
  operation_count: 32
  slug: sensible-io-agentic-access
  summary_line: 32 operations · 20 acting
api_count: 1
apis:
- description: REST API for document extraction (sync/async, single-document or portfolio), classification, fill, generation and configuration management. Bearer-token auth.
  name: Sensible REST API
  slug: rest
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Account-related resources
  name: Sensible Account API
  slug: sensible-io-account-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Document type classification
  name: Sensible Classify API
  slug: sensible-io-classify-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Manage document type configs (SenseML)
  name: Sensible Configs API
  slug: sensible-io-configs-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Manage document types
  name: Sensible Document Types API
  slug: sensible-io-document-types-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Retrieve documents and extractions
  name: Sensible Documents API
  slug: sensible-io-documents-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Document data extraction
  name: Sensible Extract API
  slug: sensible-io-extract-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Manage reference documents per type
  name: Sensible Reference Documents API
  slug: sensible-io-reference-documents-api
- baseURL: https://api.sensible.so/v0
  baseurl_source: declared
  description: Generate upload URLs for documents
  name: Sensible Upload API
  slug: sensible-io-upload-api
artifact_total: 28
collections:
- collection_type: open
  name: Sensible REST Account API
  slug: open-sensible-io-account-api
- collection_type: open
  name: Sensible REST Account Classify API
  slug: open-sensible-io-classify-api
- collection_type: open
  name: Sensible REST Account Configs API
  slug: open-sensible-io-configs-api
- collection_type: open
  name: Sensible REST Account Document Types API
  slug: open-sensible-io-document-types-api
- collection_type: open
  name: Sensible REST Account Documents API
  slug: open-sensible-io-documents-api
- collection_type: open
  name: Sensible REST Account Extract API
  slug: open-sensible-io-extract-api
- collection_type: open
  name: Sensible REST Account Reference Documents API
  slug: open-sensible-io-reference-documents-api
- collection_type: open
  name: Sensible REST Account Upload API
  slug: open-sensible-io-upload-api
- collection_type: open
  name: Sensible REST API
  slug: open-sensible-io
common:
- group: other
  href: https://artifacts.apis.io/sensible-io/capabilities/sensible-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sensible-io-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sensible-io/agentic-access/sensible-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sensible-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sensible-io/security/sensible-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sensible-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sensible-io/security/sensible-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sensible-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sensible-io/security/sensible-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sensible-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sensible-io/authentication/sensible-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sensible-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sensible-io
- group: company
  title: ''
  type: Website
  url: https://www.sensible.so/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensible.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sensible.so/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sensible-hq
- group: commercial
  href: https://artifacts.apis.io/sensible-io/plans/sensible-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sensible-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sensible-io/rate-limits/sensible-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sensible-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sensible-io/finops/sensible-io-finops.yml
  title: ''
  type: FinOps
  url: finops/sensible-io-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sensible.so/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.sensible.so/blog
created: '2026-05-08'
description: Sensible is a developer-focused document understanding platform that converts unstructured documents (PDFs, emails, images) into JSON. The core IP is SenseML — a document-specific query language combining LLM techniques with layout-based rules. The REST API exposes extract, classify, fill, generate and document-management endpoints, with SDKs for Node, Python and Go.
finops:
- has_sources: true
  method: generated
  name: Sensible Io Finops
  primary_unit: document
  service_category: Document AI
  slug: sensible-io-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensible-io.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.sensible.so over HTTP.
  name: Sensible MCP Server
  slug: sensible-io
modified: '2026-05-08'
name: Sensible
nav: Providers
network: true
overview: 'Sensible publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Classify API, Configs API, and 6 more. Tagged areas include Artificial Intelligence, Document AI, Intelligent Document Processing, Extraction, and LLM.


  The Sensible catalog on APIs.io includes 1 Spectral governance ruleset.


  Sensible''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Sensible Io Plans Pricing
  plan_count: 3
  slug: sensible-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Sensible Io Rate Limits
  slug: sensible-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Sensible API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: sensible-io-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 48.7
    developer_ergonomics: 34.5
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sensible-io/sensible-io-2026-06-20T193703.png
security:
- kind: authentication
  name: Sensible Io Authentication
  slug: sensible-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sensible Io Domain Security
  slug: sensible-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sensible Io Vulnerability Disclosure
  slug: sensible-io-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Sensible Io Trust Center
  slug: sensible-io-trust-center
  summary_line: SOC 2, HIPAA
slug: sensible-io
tags:
- Artificial Intelligence
- Document AI
- Intelligent Document Processing
- Extraction
- LLM
- SenseML
- PDF
website: https://www.sensible.so/
---
