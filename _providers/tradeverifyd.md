---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Tradeverifyd Agentic Access
  operation_count: 46
  slug: tradeverifyd-agentic-access
  summary_line: 46 operations · 10 acting
api_count: 2
apis:
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Operations involving documents
  name: Tradeverifyd Documents API
  slug: tradeverifyd-documents-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Operations involving entities. Entities encompass a range of organizations and individuals, primarily focusing on companies. This section provides functionalities to manage and interact with informati
  name: Tradeverifyd Entity API
  slug: tradeverifyd-entity-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Flags impacting an entity
  name: Tradeverifyd Flags API
  slug: tradeverifyd-flags-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: The Organizations API from Tradeverifyd — 1 operation(s) for organizations.
  name: Tradeverifyd Organizations API
  slug: tradeverifyd-organizations-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Relationships between entities
  name: Tradeverifyd Relationships API
  slug: tradeverifyd-relationships-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Access detailed Tradeverifyd reports. These comprehensive reports offer an in-depth analysis of suppliers, complete with compliance scoring to highlight potential trade-related issues. Utilize these r
  name: Tradeverifyd Reports API
  slug: tradeverifyd-reports-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: 'Manage and retrieve events related to entities. This includes real-time updates on critical incidents like supply chain disruptions, compliance issues, or significant changes affecting entities. Stay '
  name: Tradeverifyd Risk Events API
  slug: tradeverifyd-risk-events-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: SCRAPI related http resources
  name: Tradeverifyd SCITT Reference APIs API
  slug: tradeverifyd-scitt-reference-apis-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Operations involving shipments
  name: Tradeverifyd Shipments API
  slug: tradeverifyd-shipments-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: System operations and monitoring
  name: Tradeverifyd System API
  slug: tradeverifyd-system-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Auxillary resources for securing and analyzing supply chain artifacts
  name: Tradeverifyd Transparency Log API
  slug: tradeverifyd-transparency-log-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: The US Customs API from Tradeverifyd — 1 operation(s) for us customs.
  name: Tradeverifyd US Customs API
  slug: tradeverifyd-us-customs-api
- baseURL: https://api.tradeverifyd.com
  baseurl_source: declared
  description: Operations involving verifiable credentials
  name: Tradeverifyd Verifiable Credentials API
  slug: tradeverifyd-verifiable-credentials-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tradeverifyd Documents API
  slug: open-tradeverifyd-documents-api
- collection_type: open
  name: Tradeverifyd Documents Entity API
  slug: open-tradeverifyd-entity-api
- collection_type: open
  name: Tradeverifyd Documents Flags API
  slug: open-tradeverifyd-flags-api
- collection_type: open
  name: Tradeverifyd Documents Organizations API
  slug: open-tradeverifyd-organizations-api
- collection_type: open
  name: Tradeverifyd Documents Relationships API
  slug: open-tradeverifyd-relationships-api
- collection_type: open
  name: Tradeverifyd Documents Reports API
  slug: open-tradeverifyd-reports-api
- collection_type: open
  name: Tradeverifyd Documents Risk Events API
  slug: open-tradeverifyd-risk-events-api
- collection_type: open
  name: Tradeverifyd Documents SCITT Reference APIs API
  slug: open-tradeverifyd-scitt-reference-apis-api
- collection_type: open
  name: Tradeverifyd Documents Shipments API
  slug: open-tradeverifyd-shipments-api
- collection_type: open
  name: Tradeverifyd Documents System API
  slug: open-tradeverifyd-system-api
- collection_type: open
  name: Tradeverifyd Documents Transparency Log API
  slug: open-tradeverifyd-transparency-log-api
- collection_type: open
  name: Tradeverifyd Documents US Customs API
  slug: open-tradeverifyd-us-customs-api
- collection_type: open
  name: Tradeverifyd Documents Verifiable Credentials API
  slug: open-tradeverifyd-verifiable-credentials-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tradeverifyd-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tradeverifyd-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://tradeverifyd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.tradeverifyd.com/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.tradeverifyd.com/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/tradeverifyd/docs_examples
- group: operate
  title: ''
  type: Support
  url: mailto:support@tradeverifyd.com
- group: company
  title: ''
  type: Blog
  url: https://tradeverifyd.com/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradeverifyd
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tradeverifyd.com/
- group: start
  title: ''
  type: Login
  url: https://app.tradeverifyd.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tradeverifyd.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tradeverifyd.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: postman/tradeverifyd-shipments-cbp-postman-collection.json
- group: build
  title: ''
  type: Examples
  url: examples/tradeverifyd-entities-by-flag-type-guide.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradeverifyd-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradeverifyd-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tradeverifyd-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tradeverifyd-agentic-access.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tradeverifyd-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tradeverifyd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tradeverifyd-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tradeverifyd-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tradeverifyd-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tradeverifyd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradeverifyd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tradeverifyd-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tradeverifyd-transparency-service-openapi.yaml
created: '2026-07-17'
description: Tradeverifyd is a supply chain intelligence platform, formed by the combination of Transmute and mesur.io and backed by Techstars, that screens suppliers against 200+ global data sources, maps multi-tier supplier relationship graphs, monitors global risk events, and issues W3C Verifiable Credentials that can be presented to US Customs (CBP). Its coverage spans UFLPA, EU CSDDD, UK Modern Slavery Act, OFAC, EU/UN sanctions, NDAA, and EUDR. The v1 REST API exposes entity search and resolution, relationship graphs, flags, risk events, reports, shipments, supplier information requests, and verifiable-credential issuance, authenticated with an ocp-apim-subscription-key header.
image: https://app.tradeverifyd.com/tradeverifyd_logo.svg
layout: provider
modified: '2026-07-21'
name: Tradeverifyd
nav: Providers
network: true
overview: 'Tradeverifyd publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Entity API, Flags API, and 10 more. Tagged areas include Supply Chain, Trade Compliance, Risk Management, Verifiable Credentials, and Customs.


  Tradeverifyd''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, code examples, authentication, and 22 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 63.5
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 84.6
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tradeverifyd/refs/heads/main/screenshots/tradeverifyd-2026-08-17T082420.png
security:
- kind: authentication
  name: Tradeverifyd Authentication
  slug: tradeverifyd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tradeverifyd Domain Security
  slug: tradeverifyd-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Tradeverifyd Trust Center
  slug: tradeverifyd-trust-center
  summary_line: trust center published
slug: tradeverifyd
tags:
- Supply Chain
- Trade Compliance
- Risk Management
- Verifiable Credentials
- Customs
- Entity Resolution
- Logistics
website: https://tradeverifyd.com/
---
