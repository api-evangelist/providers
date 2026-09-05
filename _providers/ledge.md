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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 36.9
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.goledge.io
  baseurl_source: declared
  description: Data sources connected to Ledge (banks, payment service providers, ERPs, databases) and the datasets fetched from them.
  name: Ledge Sources API
  slug: ledge-sources-api
- baseURL: https://api.goledge.io
  baseurl_source: declared
  description: Transactions, their matches, and their reconciliation status.
  name: Ledge Transactions API
  slug: ledge-transactions-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ledge Sources API
  slug: open-ledge-sources-api
- collection_type: open
  name: Ledge Sources Transactions API
  slug: open-ledge-transactions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ledge-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ledge.co
- group: start
  title: ''
  type: Portal
  url: https://app.goledge.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ledge.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ledge.co/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ledge.co/api-reference/getting-started
- group: start
  title: ''
  type: Login
  url: https://app.goledge.io
- group: company
  title: ''
  type: Blog
  url: https://www.ledge.co/resources/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ledge.co/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.ledge.co/support-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ledge.co
- group: auth
  title: ''
  type: Security
  url: https://www.ledge.co/security
- group: auth
  title: ''
  type: Compliance
  url: security/ledge-trust-center.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ledge.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ledge.co/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goledge
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ledge-finance
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ledge.co/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ledge-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ledge-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ledge-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ledge-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ledge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ledge-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ledge-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ledge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ledge-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ledge-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ledge-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ledge-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ledge-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Ledge is an AI-powered close management, reconciliation and payment-operations platform for finance teams. It centralizes transaction and payment data from a company''s entire stack — banks, payment service providers, ERPs, billing systems, data warehouses and file feeds — and automates the work on top of it: multiway transaction matching, account and payment reconciliation, automated cash application, flux analysis, working papers, and journal entries posted back to the ERP with review and approval built in. Its Agent Studio lets teams build AI agents that execute close-checklist tasks, with human-in-the-loop review, rationale, and a queryable audit trail. Ledge exposes a REST API over its Sources and Transactions data, authorized with OAuth 2.0 client credentials. Founded in 2022, the company raised a $9M seed round led by NEA with participation from Vertex Ventures, FJ Labs and Picus Capital.'
image: https://cdn.prod.website-files.com/63aadf1c20f6a6eb95024394/68df18eebbbc304be738307c_Ledge%20%7C%20put%20your%20close%20on%20ait-pilot%20with%20a%20team%20of%20AI%20agents.png
layout: provider
modified: '2026-07-19'
name: Ledge
nav: Providers
network: true
overview: 'Ledge publishes 2 APIs on the [APIs.io](https://apis.io/) network: Sources API and Transactions API. Tagged areas include Company, Fintech, Accounting, Reconciliation, and Financial Close.


  Ledge''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, pricing, support, and 25 more developer resources.'
random_paper: 9
scopes:
- name: Ledge Scopes
  scope_count: 0
  slug: ledge-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 17.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 44.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
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
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ledge/refs/heads/main/screenshots/ledge-2026-07-25T224813.png
security:
- kind: authentication
  name: Ledge Authentication
  slug: ledge-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ledge Domain Security
  slug: ledge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ledge Trust Center
  slug: ledge-trust-center
  summary_line: SOC 1, SOC 2, ISO 42001, GDPR
slug: ledge
tags:
- Company
- Fintech
- Accounting
- Reconciliation
- Financial Close
- Payment Operations
- Transaction Matching
- Cash Application
- Journal Entries
- AI Agents
- ERP Integration
- Finance Automation
website: https://www.ledge.co
---
