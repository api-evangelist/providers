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
  score: 31.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Palla Agentic Access
  operation_count: 13
  slug: palla-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 7
apis:
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: An Account belongs to a User authorized to use Palla.
  name: Palla Accounts API
  slug: palla-accounts-api
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: Authentication endpoints return tokens for user access.
  name: Palla Auth API
  slug: palla-auth-api
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: Service health.
  name: Palla Health API
  slug: palla-health-api
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: A Link is a unique URL belonging to an Account, used to create Relationships.
  name: Palla Links API
  slug: palla-links-api
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: Payment Methods are used to send and/or receive Transfers.
  name: Palla Payment Methods API
  slug: palla-payment-methods-api
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: A Relationship is the connection between two Accounts.
  name: Palla Relationships API
  slug: palla-relationships-api
- baseURL: https://api.platform.palla.app
  baseurl_source: declared
  description: A Transfer is a record of funds sent to a Relationship.
  name: Palla Transfers API
  slug: palla-transfers-api
artifact_total: 20
asyncapis:
- description: ''
  name: Palla Webhooks
  slug: palla-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Palla Platform Partner Accounts API
  slug: open-palla-accounts-api
- collection_type: open
  name: Palla Platform Partner Accounts Auth API
  slug: open-palla-auth-api
- collection_type: open
  name: Palla Platform Partner Accounts Health API
  slug: open-palla-health-api
- collection_type: open
  name: Palla Platform Partner Accounts Links API
  slug: open-palla-links-api
- collection_type: open
  name: Palla Platform Partner Accounts Payment Methods API
  slug: open-palla-payment-methods-api
- collection_type: open
  name: Palla Platform Partner Accounts Relationships API
  slug: open-palla-relationships-api
- collection_type: open
  name: Palla Platform Partner Accounts Transfers API
  slug: open-palla-transfers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/palla-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.palla.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.platform.palla.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.platform.palla.app
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/306637/TzkyP11Z
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/306637/TzkyP11Z
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PallaFinancial
- group: operate
  title: ''
  type: StatusPage
  url: https://status.palla.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://palla.app/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://palla.app/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/palla-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.palla.com/
- group: build
  title: ''
  type: SDKs
  url: packages/palla-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/palla-packages.yml
- group: design
  title: ''
  type: Components
  url: components/palla-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/palla-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/palla-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/palla-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/palla-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/palla-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/palla-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/palla-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/palla-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/palla-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/palla-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/palla-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/palla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palla-domain-security.yml
created: '2026-07-17'
description: 'Palla Financial is a fintech infrastructure company that powers instant cross-border peer-to-peer (P2P) money transfers to 180+ countries. The Palla Platform Partner API lets trusted partners embed transfers into their own apps: exchange partner client credentials for a user-scoped Bearer token, then create and manage a user''s Account, encrypted Payment Methods, relationship Links, Relationships, and Transfers, with server-to-server transfer callbacks. Palla also ships embeddable UI (Embed, Checkout, Redirect) and a JavaScript Web SDK, with PCI-scoped card storage plus KYC, OFAC, card verification, fraud prevention, and transaction monitoring built in. Backed by Cowboy Ventures.'
image: https://www.palla.com/page-preview.png
layout: provider
modified: '2026-07-20'
name: Palla
nav: Providers
network: true
overview: 'Palla publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auth API, Health API, and 4 more. Tagged areas include Company, Fintech, Payments, Cross-Border Payments, and Remittances.


  The Palla catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Palla''s developer surface includes documentation, API reference, authentication, and 26 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 10.6
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 12.5
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/palla/refs/heads/main/screenshots/palla-2026-08-07T191320.png
security:
- kind: authentication
  name: Palla Authentication
  slug: palla-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Palla Domain Security
  slug: palla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Palla Trust Center
  slug: palla-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: palla
tags:
- Company
- Fintech
- Payments
- Cross-Border Payments
- Remittances
- P2P Payments
- Money Transfer
- Embedded Finance
website: https://www.palla.com
---
