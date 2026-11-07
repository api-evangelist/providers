---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to AIA Contract Documents platform resources and guides. No machine‑readable API contract was found; documentation is HTML only.
  name: AIA Contract Documents API
  slug: aia-contract-documents-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/aia-contract-documents/conformance/aia-contract-documents-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aia-contract-documents-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aia-contract-documents/llms/aia-contract-documents-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aia-contract-documents-llms.txt
- group: agent
  href: https://artifacts.apis.io/aia-contract-documents/well-known/aia-contract-documents-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aia-contract-documents-well-known.yml
- group: other
  href: https://artifacts.apis.io/aia-contract-documents/hosts/aia-contract-documents-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aia-contract-documents-hosts.yml
- group: other
  href: https://artifacts.apis.io/aia-contract-documents/vendors/aia-contract-documents-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aia-contract-documents-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://aiacontracts.com/leadership
- group: auth
  href: https://artifacts.apis.io/aia-contract-documents/security/aia-contract-documents-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aia-contract-documents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiacontracts.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aiacontracts.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://help.aiacontracts.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://aiacontracts.com/subscriptions/unlimited-subscription
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiacontracts.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiacontracts.com/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://learn.aiacontracts.com/guides/architects-contracts-guide/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: AIA Contract Documents provides the industry‑standard suite of construction contract templates and management tools for architects, owners, contractors, and consultants. Through a cloud‑based platform, users can browse, customize, and execute AIA‑approved contracts, ensuring legal compliance and streamlined project delivery across the building lifecycle. The service supports over 1 million contracts written annually, serving thousands of firms and billions of dollars in contract value, and offers resources such as guides, articles, and training to help stakeholders manage risk and improve outcomes.
image: https://aiacontracts.com/images/og-image.png
layout: provider
modified: '2026-10-28'
name: AIA Contract Documents
nav: Providers
network: true
overview: 'AIA Contract Documents is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Contracts, Architecture, and Software.


  AIA Contract Documents'' developer surface includes getting-started guide, support, pricing, and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aia-contract-documents/aia-contract-documents-2026-11-03T120443.png
security:
- kind: domain-security
  name: Aia Contract Documents Domain Security
  slug: aia-contract-documents-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aia-contract-documents
tags:
- Company
- Construction
- Contracts
- Architecture
- Software
website: https://aiacontracts.com/
---
