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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Figure Agentic Access
  operation_count: 36
  slug: figure-agentic-access
  summary_line: 36 operations · 15 acting
api_count: 8
apis:
- description: The Encryption API from Figure — 1 operation(s) for encryption.
  name: Figure Encryption API
  slug: figure-encryption-api
- description: The HELOC application requests API from Figure — 19 operation(s) for heloc application requests.
  name: Figure HELOC application requests API
  slug: figure-heloc-application-requests-api
- description: The HELOC Offers API from Figure — 2 operation(s) for heloc offers.
  name: Figure HELOC Offers API
  slug: figure-heloc-offers-api
- description: The Loan Originator requests API from Figure — 1 operation(s) for loan originator requests.
  name: Figure Loan Originator requests API
  slug: figure-loan-originator-requests-api
- description: The Loan Tape V1 API from Figure — 6 operation(s) for loan tape v1.
  name: Figure Loan Tape V1 API
  slug: figure-loan-tape-v1-api
- description: The Loan Tape V2 API from Figure — 3 operation(s) for loan tape v2.
  name: Figure Loan Tape V2 API
  slug: figure-loan-tape-v2-api
- description: The Payment History V1 API from Figure — 3 operation(s) for payment history v1.
  name: Figure Payment History V1 API
  slug: figure-payment-history-v1-api
- description: The Payment History V2 API from Figure — 1 operation(s) for payment history v2.
  name: Figure Payment History V2 API
  slug: figure-payment-history-v2-api
artifact_total: 22
asyncapis:
- description: ''
  name: Figure Webhooks
  slug: figure-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HELOC Inquiries Encryption API
  slug: open-figure-encryption-api
- collection_type: open
  name: HELOC Inquiries Encryption HELOC application requests API
  slug: open-figure-heloc-application-requests-api
- collection_type: open
  name: HELOC Inquiries Encryption HELOC Offers API
  slug: open-figure-heloc-offers-api
- collection_type: open
  name: HELOC Inquiries Encryption Loan Originator requests API
  slug: open-figure-loan-originator-requests-api
- collection_type: open
  name: HELOC Inquiries Encryption Loan Tape V1 API
  slug: open-figure-loan-tape-v1-api
- collection_type: open
  name: HELOC Inquiries Encryption Loan Tape V2 API
  slug: open-figure-loan-tape-v2-api
- collection_type: open
  name: HELOC Inquiries Encryption Payment History V1 API
  slug: open-figure-payment-history-v1-api
- collection_type: open
  name: HELOC Inquiries Encryption Payment History V2 API
  slug: open-figure-payment-history-v2-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.figure.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.figure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.figure.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.figure.com/heloc-inquiries/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.figure.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.figure.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.figure.com/partner/success-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FigureTechnologies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figure.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.figure.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://www.figure.com/leadportal/login/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figure.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/figure-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figure-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/figure-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/figure-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/figure-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/figure-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/figure-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/figure-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figure-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/figure-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/figure-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/figure-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-heloc-inquiries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-heloc-pre-qualification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-portfolio-manager-overlay.yaml
created: '2026-07-17'
description: Figure is a fintech lender and blockchain-native capital marketplace, backed by Ribbit Capital, and one of the largest non-bank HELOC (home equity line of credit) originators in the United States. Its Partner APIs let affiliates, brokers, and loan originators run the full HELOC lifecycle — pre-qualification, inquiry creation, borrower/SSN/income and property enrichment, lien verification, matching-property and offer selection, borrower costs, and document retrieval — plus a Portfolio Manager reporting API for asset holders to query and download owned and pledged loan-tape and payment-history data. The REST APIs authenticate with an apikey header behind a Kong gateway, support optional JWE/RSA payload encryption, expose separate test and production environments, and push webhooks as inquiries and applications progress.
image: https://cdn.figure.com/shared-assets/social-logos/figure-logo-social.png
layout: provider
mcp_servers:
- description: ''
  name: figure-mcp.yml
  slug: figure-mcpyml
modified: '2026-07-19'
name: Figure
nav: Providers
network: true
overview: 'Figure publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Encryption API, HELOC application requests API, HELOC Offers API, and 5 more. Tagged areas include Company, Fintech, Lending, HELOC, and Home Equity.


  The Figure catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Figure''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 41.0
  delta: -7.1
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 58.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/figure/refs/heads/main/screenshots/figure-2026-07-25T214439.png
security:
- kind: authentication
  name: Figure Authentication
  slug: figure-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Figure Domain Security
  slug: figure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: figure
tags:
- Company
- Fintech
- Lending
- HELOC
- Home Equity
- Mortgage
- Loan Origination
- Webhooks
- Capital Markets
website: https://www.figure.com
---
