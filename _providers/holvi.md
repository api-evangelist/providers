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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Holvi Agentic Access
  operation_count: 9
  slug: holvi-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 4
apis:
- description: AISP endpoints - read Holvi customer payment accounts and payments.
  name: Holvi Account Information API
  slug: holvi-account-information-api
- description: PSU authentication and consent token exchange.
  name: Holvi Consent API
  slug: holvi-consent-api
- description: PISP endpoints - initiate and confirm SEPA / SEPA Instant / SWIFT payments.
  name: Holvi Payment Initiation API
  slug: holvi-payment-initiation-api
- description: TPP certificate lifecycle.
  name: Holvi Third Party Provider API
  slug: holvi-third-party-provider-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/holvi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/holvi-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holvi-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/holvi-psd2-openapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/holvi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/holvi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/holvi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/holvi-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/holvi-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/holvi-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/holvi-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/holvi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.holvi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://holvi-developer.zendesk.com/hc/en-gb
- group: docs
  title: ''
  type: Documentation
  url: https://holvi.github.io/psd2-api/
- group: docs
  title: ''
  type: APIReference
  url: https://holvi.github.io/psd2-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://holvi.github.io/psd2-api/initial_steps/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://holvi.github.io/psd2-api/changelog.html
- group: operate
  title: ''
  type: Support
  url: https://support.holvi.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://blog.holvi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/holvi
- group: commercial
  title: ''
  type: Pricing
  url: https://www.holvi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://login.app.holvi.com/register
- group: start
  title: ''
  type: Login
  url: https://login.app.holvi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.holvi.com/hc/en-gb/articles/33569262656402-Terms-of-Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.holvi.com/hc/en-gb/articles/29831985498258-Privacy-Notice
created: '2026-07-17'
description: Holvi is a Finnish digital business-banking service for freelancers, founders and small businesses, founded in Helsinki in 2011 and operating as a regulated Authorised Payment Institution supervised by the Finnish Financial Supervisory Authority. It combines a business account with its own IBAN, a Holvi Business Mastercard, invoicing, expense tracking, VAT calculation and bookkeeping preparation in one dashboard, serving more than 150,000 businesses across Europe with a focus on Finland, Germany and Austria. For developers, Holvi publishes a PSD2 API v2.0 for licensed Third Party Providers, exposing account information (AISP) and payment initiation (PISP, SEPA / SEPA Instant / SWIFT) with Strong Customer Authentication and optional Verification of Payee.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/holvi.png
layout: provider
mcp_servers:
- description: ''
  name: holvi-mcp.yml
  slug: holvi-mcpyml
modified: '2026-07-19'
name: Holvi
nav: Providers
network: true
overview: 'Holvi publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Consent API, Payment Initiation API, and 1 more. Tagged areas include Company, Banking, Fintech, Payments, and Business Banking.


  Holvi''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, engineering blog, and 20 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 46.9
  delta: -3.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.2
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 36.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/holvi/refs/heads/main/screenshots/holvi-2026-07-25T221323.png
security:
- kind: authentication
  name: Holvi Authentication
  slug: holvi-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Holvi Domain Security
  slug: holvi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: holvi
tags:
- Company
- Banking
- Fintech
- Payments
- Business Banking
- PSD2
- Open Banking
- SEPA
- Finland
website: https://www.holvi.com/
---
