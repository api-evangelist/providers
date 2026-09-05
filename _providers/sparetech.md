---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Sparetech Agentic Access
  operation_count: 28
  slug: sparetech-agentic-access
  summary_line: 28 operations · 20 acting
api_count: 2
apis:
- baseURL: https://sync.sparetech.io/v1
  baseurl_source: declared
  description: The Authentication API from Sparetech — 2 operation(s) for authentication.
  name: Sparetech Authentication API
  slug: sparetech-authentication-api
- baseURL: https://sync.sparetech.io/v1
  baseurl_source: declared
  description: The ChangeIntent API from Sparetech — 4 operation(s) for changeintent.
  name: Sparetech ChangeIntent API
  slug: sparetech-changeintent-api
- baseURL: https://sync.sparetech.io/v1
  baseurl_source: declared
  description: The CreationIntent API from Sparetech — 4 operation(s) for creationintent.
  name: Sparetech CreationIntent API
  slug: sparetech-creationintent-api
- baseURL: https://sync.sparetech.io/v1
  baseurl_source: declared
  description: The ExtensionIntent API from Sparetech — 4 operation(s) for extensionintent.
  name: Sparetech ExtensionIntent API
  slug: sparetech-extensionintent-api
- baseURL: https://sync.sparetech.io/v1
  baseurl_source: declared
  description: The Material Master Sync API from Sparetech — 3 operation(s) for material master sync.
  name: Sparetech Material Master Sync API
  slug: sparetech-material-master-sync-api
- baseURL: https://sync.sparetech.io/v1
  baseurl_source: declared
  description: The Schema API from Sparetech — 2 operation(s) for schema.
  name: Sparetech Schema API
  slug: sparetech-schema-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sync Authentication API
  slug: open-sparetech-authentication-api
- collection_type: open
  name: Sync Authentication ChangeIntent API
  slug: open-sparetech-changeintent-api
- collection_type: open
  name: Sync Authentication CreationIntent API
  slug: open-sparetech-creationintent-api
- collection_type: open
  name: Sync Authentication ExtensionIntent API
  slug: open-sparetech-extensionintent-api
- collection_type: open
  name: Sync Authentication Material Master Sync API
  slug: open-sparetech-material-master-sync-api
- collection_type: open
  name: Sync Authentication Schema API
  slug: open-sparetech-schema-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sparetech-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.sparetech.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sparetech.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sparetech.io/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sparetech.io/product/api
- group: company
  title: ''
  type: Blog
  url: https://www.sparetech.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.sparetech.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.sparetech.io/demo-request
- group: start
  title: ''
  type: Login
  url: https://app.sparetech.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sparetech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sparetech.io/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sparetech.io/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.sparetech.io/security-and-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sparetech.io/
- group: auth
  title: ''
  type: Security
  url: https://www.sparetech.io/security-and-compliance
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sparetech-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sparetech-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparetech-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sparetech-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sparetech-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sparetech-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sparetech-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sparetech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sparetech-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sparetech-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sparetech-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sparetech-sync-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sparetech-sync-v2-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sparetech-llms.txt
created: '2026-07-17'
description: SPARETECH is an enterprise MRO (Maintenance, Repair and Operations) SaaS that helps manufacturing maintenance and procurement teams reduce spend and optimize spare-parts inventory. Founded in 2018 in Stuttgart, Germany, it pairs a global catalog of 40M+ original manufacturer part records with proprietary matching and AI to deliver automated duplicate detection, data enrichment, obsolescence management and BOM processing. It is a 100% cloud SaaS, available in 14 languages, an official SAP partner in the SAP Store, and certified under SOC 2 Type II, ISO 27001 and GDPR. For developers it exposes a REST Sync API (v1 for all ERPs, v2 for SAP S/4HANA) using JWT authentication with a dedicated sandbox for material creation, change and extension synchronization between SPARETECH and ERP/CMMS/MDM systems. Customers include Bosch, Porsche, BMW, Volkswagen, Nestlé and Sanofi.
image: https://app.sparetech.io/img/sparetech-logo.png
layout: provider
modified: '2026-07-21'
name: Sparetech
nav: Providers
network: true
overview: 'Sparetech publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, ChangeIntent API, CreationIntent API, and 3 more. Tagged areas include Company, Manufacturing, Spare Parts, MRO, and Maintenance.


  Sparetech''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 23 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sparetech/refs/heads/main/screenshots/sparetech-2026-08-17T082021.png
security:
- kind: authentication
  name: Sparetech Authentication
  slug: sparetech-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Sparetech Domain Security
  slug: sparetech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sparetech Vulnerability Disclosure
  slug: sparetech-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Sparetech Trust Center
  slug: sparetech-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: sparetech
tags:
- Company
- Manufacturing
- Spare Parts
- MRO
- Maintenance
- Procurement
- Inventory Optimization
- ERP Integration
- SAP
- Master Data Management
website: https://www.sparetech.io/
---
