---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Openmercantil Agentic Access
  operation_count: 36
  slug: openmercantil-agentic-access
  summary_line: 36 operations · 2 acting
api_count: 3
apis:
- description: 'Account API credential management: list, create, rotate and revoke opaque omk_* API keys. Secrets are returned once and recoverable only via an identical Idempotency-Key replay inside 24 hours.'
  name: OpenMercantil API Credentials API
  slug: openmercantil-api-credentials-api
- description: Session-bound Stripe checkout, invoices and portal contracts. External actions are bounded, idempotent and never exposed through the public MCP.
  name: OpenMercantil Billing API
  slug: openmercantil-billing-api
- description: Daily BORME publications, multi-source timeline and registry events
  name: OpenMercantil BORME API
  slug: openmercantil-borme-api
- description: Company reports and registry events
  name: OpenMercantil Companies API
  slug: openmercantil-companies-api
- description: Bulk exports (CSV / JSON / aggregated stats)
  name: OpenMercantil Datasets API
  slug: openmercantil-datasets-api
- description: Corporate and person-to-company relationship graphs. Every emitted record retains the source-specific terms authorized by the active public source catalog; no blanket relicensing applies.
  name: OpenMercantil Graph API
  slug: openmercantil-graph-api
- description: Public read-only connector catalog. Never exposes credentials, OAuth tokens, webhook secrets or operator actions.
  name: OpenMercantil Integrations API
  slug: openmercantil-integrations-api
- description: 'Spanish mercantile-law layer (derecho mercantil): legislation corpus + article texts + act→norm bridge. Distributes the consolidated BOE legal corpus structured by OpenMercantil so LLMs and agents can'
  name: OpenMercantil Legal API
  slug: openmercantil-legal-api
- description: Documentary mentions of natural persons in BORME (officer roles). Persons treated as documentary mentions only — no DNI, no contact data, no scoring.
  name: OpenMercantil Persons API
  slug: openmercantil-persons-api
- description: Public procurement awards (PLACSP) and grants (BDNS)
  name: OpenMercantil Public Procurement API
  slug: openmercantil-public-procurement-api
- description: Company and person search endpoints
  name: OpenMercantil Search API
  slug: openmercantil-search-api
- description: CNAE sector aggregates, ratios and company listings
  name: OpenMercantil Sectors API
  slug: openmercantil-sectors-api
- description: Source catalog metadata, freshness and integration status
  name: OpenMercantil Sources API
  slug: openmercantil-sources-api
- description: Customer-support writes. Anonymous creation requires explicit privacy consent; replies require an authenticated owner session and CSRF. Ticket data is never exposed through the public MCP.
  name: OpenMercantil Support API
  slug: openmercantil-support-api
- description: Service health and metadata
  name: OpenMercantil System API
  slug: openmercantil-system-api
- description: Authenticated Panel Pro endpoints — segments, lists, notes, tags, exports, audit. Requires session cookie (browser) and X-CSRF-Token header for mutations.
  name: OpenMercantil User API
  slug: openmercantil-user-api
- description: 'Account outbound webhooks: register, update, rotate the HMAC signing secret and delete event subscriptions. Three subscribable event types; deliveries are signed and fail closed on unknown events.'
  name: OpenMercantil Webhooks API
  slug: openmercantil-webhooks-api
- description: Public procurement (PLACSP) rankings
  name: OpenMercantil Contracts API
  slug: openmercantil-contracts-api
- description: Daily BORME summary feeds
  name: OpenMercantil Daily API
  slug: openmercantil-daily-api
- description: Bulk and per-resource export endpoints
  name: OpenMercantil Export API
  slug: openmercantil-export-api
- description: Geolocation enrichment
  name: OpenMercantil Geocode API
  slug: openmercantil-geocode-api
- description: Company relationship network and embargoes
  name: OpenMercantil Network API
  slug: openmercantil-network-api
- description: Documentary risk signals from public sources (AEPD, CNMC, concursos, AEAT moroso, CENDOJ)
  name: OpenMercantil Risk Signals API
  slug: openmercantil-risk-signals-api
- description: Company score, trust score and activity timeseries
  name: OpenMercantil Score API
  slug: openmercantil-score-api
- description: Aggregate statistics by region and sector
  name: OpenMercantil Stats API
  slug: openmercantil-stats-api
artifact_total: 61
asyncapis:
- description: ''
  name: Openmercantil Webhooks
  slug: openmercantil-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenMercantil Public Billing API
  slug: open-openmercantil-billing-api
- collection_type: open
  name: OpenMercantil Public Billing Companies API
  slug: open-openmercantil-companies-api
- collection_type: open
  name: OpenMercantil Public Billing Contracts API
  slug: open-openmercantil-contracts-api
- collection_type: open
  name: OpenMercantil Public Billing Daily API
  slug: open-openmercantil-daily-api
- collection_type: open
  name: OpenMercantil Public Billing Export API
  slug: open-openmercantil-export-api
- collection_type: open
  name: OpenMercantil Public Billing Geocode API
  slug: open-openmercantil-geocode-api
- collection_type: open
  name: OpenMercantil Public Billing Network API
  slug: open-openmercantil-network-api
- collection_type: open
  name: OpenMercantil Public Billing Persons API
  slug: open-openmercantil-persons-api
- collection_type: open
  name: OpenMercantil Public Billing Score API
  slug: open-openmercantil-score-api
- collection_type: open
  name: OpenMercantil Public Billing Search API
  slug: open-openmercantil-search-api
- collection_type: open
  name: OpenMercantil Public Billing Sectors API
  slug: open-openmercantil-sectors-api
- collection_type: open
  name: OpenMercantil Public Billing Sources API
  slug: open-openmercantil-sources-api
- collection_type: open
  name: OpenMercantil Public Billing Stats API
  slug: open-openmercantil-stats-api
- collection_type: open
  name: OpenMercantil Public Billing System API
  slug: open-openmercantil-system-api
- collection_type: open
  name: OpenMercantil Public API
  slug: open-openmercantil
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/openmercantil-risk-signals-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openmercantil-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openmercantil-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openmercantil-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openmercantil.es/
- group: docs
  title: ''
  type: Documentation
  url: https://openmercantil.es/api/documentacion
- group: other
  title: ''
  type: APIsJSON
  url: https://openmercantil.es/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://openmercantil.es/precios
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openmercantil.es/terminos-de-uso
- group: operate
  title: ''
  type: Support
  url: https://openmercantil.es/soporte
- group: other
  title: ''
  type: Downloads
  url: https://openmercantil.es/descargas
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PabloCirre
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openmercantil-company-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openmercantil-event-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/openmercantil-company-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/openmercantil-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-search-companies-example.json
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-get-company-example.json
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-get-company-events-example.json
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-health-example.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/openmercantil-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openmercantil-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openmercantil-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openmercantil-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openmercantil-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://openmercantil.es/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/openmercantil-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openmercantil-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/openmercantil-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openmercantil-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openmercantil-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://openmercantil.es/status
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/openmercantil-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openmercantil-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openmercantil-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/openmercantil-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openmercantil-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openmercantil-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/openmercantil-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openmercantil-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openmercantil-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/openmercantil-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openmercantil-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openmercantil.es/api
- group: docs
  title: ''
  type: APIReference
  url: https://openmercantil.es/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://openmercantil.es/api/documentacion
- group: docs
  title: ''
  type: OpenAPI
  url: https://openmercantil.es/openapi.json
- group: start
  title: ''
  type: SignUp
  url: https://openmercantil.es/mi-cuenta/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openmercantil.es/privacidad
- group: operate
  title: ''
  type: HelpCenter
  url: https://openmercantil.es/faq
created: '2026-05-09'
description: OpenMercantil is an independent public-data API for Spanish company intelligence. It indexes the Boletin Oficial del Registro Mercantil (BORME) and cross-references it with 80+ official public sources (BOE, CNMV, CNMC, AEAT, AEPD, PLACSP, TED EU, BDNS, OEPM, EPO, WIPO, CENDOJ, GLEIF, OpenSanctions, ICIJ and more) to expose company and person search, structured company reports, BORME registry event timelines, documentary officer mentions, CNAE sector navigation and ratios, daily BORME summaries, public-procurement notices and rankings, documentary risk signals, a corporate relationship graph, a Spanish mercantile-law corpus that bridges registry acts to the governing BOE norm, account-plane datasets and HMAC-signed outbound webhooks, and CSV/JSON bulk exports. The live OpenAPI 3.1 contract (v1.9.3) declares 118 paths and 139 operations. The public read plane is free and anonymous with no API key, rate-limited at 60 req/min and 200 req/day per IP, with paid Profesional, MAX and
  Enterprise tiers raising the quota. Derived data is CC BY 4.0 and every response carries its own source and attribution metadata. The project is informational and does not replace official Registro Mercantil certificates.
examples:
- key_count: 2
  name: Openmercantil Get Company Events Example
  slug: openmercantil-get-company-events-example
- key_count: 2
  name: Openmercantil Get Company Example
  slug: openmercantil-get-company-example
- key_count: 2
  name: Openmercantil Health Example
  slug: openmercantil-health-example
- key_count: 2
  name: Openmercantil Search Companies Example
  slug: openmercantil-search-companies-example
finops:
- name: Openmercantil Finops
  service_category: Open Data / Public Records
  slug: openmercantil-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openmercantil.png
json_schemas:
- name: OpenMercantil Company
  property_count: 13
  slug: openmercantil-company
- name: OpenMercantil Company Event
  property_count: 5
  slug: openmercantil-event
json_structures:
- name: Openmercantil Company Structure
  property_count: 13
  slug: openmercantil-company-structure
jsonld:
- class_count: 31
  name: Openmercantil Context
  property_count: 2
  slug: openmercantil-context
layout: provider
modified: '2026-08-14'
name: OpenMercantil
nav: Providers
network: true
overview: 'OpenMercantil publishes 25 APIs on the [APIs.io](https://apis.io/) network, including API Credentials API, Billing API, BORME API, and 22 more. Tagged areas include BDNS, BORME, Business Registry, CIF, and CNAE.


  The OpenMercantil catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  OpenMercantil''s developer surface includes authentication, documentation, pricing, support, code examples, changelog, API reference, and 44 more developer resources.'
plans:
- name: Openmercantil Plans Pricing
  plan_count: 4
  slug: openmercantil-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Openmercantil Rate Limits
  slug: openmercantil-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenMercantil API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openmercantil-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: OpenMercantil API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 4
  slug: openmercantil-rules
scopes:
- name: Openmercantil Scopes
  scope_count: 0
  slug: openmercantil-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 86.4
  coverage:
    artifact_dirs: 29
    catalog_gap: 30.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 77.7
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 47.0
    operational_transparency: 94.7
  previous_composite: 86.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 85.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/screenshots/openmercantil-2026-06-20T191016.png
security:
- kind: authentication
  name: Openmercantil Authentication
  slug: openmercantil-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Openmercantil Domain Security
  slug: openmercantil-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Openmercantil Vulnerability Disclosure
  slug: openmercantil-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Openmercantil Trust Center
  slug: openmercantil-trust-center
  summary_line: trust center published
slug: openmercantil
tags:
- BDNS
- BORME
- Business Registry
- CIF
- CNAE
- CNMV
- CSV
- Company Data
- Company Search
- Corporate Registry
- DCAT-AP
- Daily Summary
- Geocoding
- JSON
- Legal Data
- Mercantile Law
- OEPM
- Open Data
- Open Government Data
- OpenAPI
- OpenSanctions
- PLACSP
- Public Procurement
- Public Records
- Public-Interest Data
- REST API
- Registry Timeline
- Risk Signals
- Sanctions
- Spain
- Spanish Companies
- Spanish Open Data
- Tenders
- Trust Score
- Webhook
website: https://openmercantil.es/
---
