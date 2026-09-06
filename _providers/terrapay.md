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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: GSMA Mobile Money API profile for account validation, FX quotations, and multi-rail money movement (wallet/bank/card) across international corridors.
  name: TerraPay API Suite
  slug: terrapay-api-suite
artifact_total: 4
asyncapis:
- description: ''
  name: Terrapay Notifications Webhooks
  slug: terrapay-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.terrapay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.terrapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.terrapay.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.terrapay.com/apiReference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.terrapay.com/getStarted.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/terrapay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/terrapay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/terrapay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terrapay-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/terrapay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terrapay-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/terrapay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terrapay-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/terrapay-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/terrapay-notifications-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terrapay-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terrapay-domain-security.yml
created: '2026-07-17'
description: TerraPay is a global cross-border payments and digital-wallet infrastructure company connecting banks, mobile wallets, money-transfer operators, merchants, and card networks into a single interoperable network for real-time international money movement. Its partner API Suite follows the GSMA Mobile Money API, exposing account validation, FX quotations, and multi-rail transactions (wallet, bank account, and card) across global remittance corridors, with compliance, monitoring, reconciliation, and reporting built into the platform. Partners authenticate with signed request headers over mutual TLS across Sandbox, UAT, and LIVE environments. Added to the API Evangelist network from the Partech portfolio and enriched from TerraPay's public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terrapay.png
layout: provider
modified: '2026-07-21'
name: TerraPay
nav: Providers
network: true
overview: 'TerraPay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Payments, Cross-Border Payments, and Remittances.


  The TerraPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TerraPay''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 12 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 28.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terrapay/refs/heads/main/screenshots/terrapay-2026-09-02T163159.png
security:
- kind: authentication
  name: Terrapay Authentication
  slug: terrapay-authentication
  summary_line: apiKey/custom-signed-headers/mutualTLS · 6 schemes
- kind: domain-security
  name: Terrapay Domain Security
  slug: terrapay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: terrapay
tags:
- Company
- Financial-Services
- Payments
- Cross-Border Payments
- Remittances
- Mobile Money
- Digital Wallet
- Money Transfer
- Fintech
- GSMA Mobile Money API
website: https://www.terrapay.com/
---
