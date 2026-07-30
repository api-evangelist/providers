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
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Steadily Agentic Access
  operation_count: 39
  slug: steadily-agentic-access
  summary_line: 39 operations · 14 acting
api_count: 8
apis:
- description: 'Steadily uses Bearer Tokens to authenticate requests to the quoting endpoints on behalf of some appointed agent. There''s two steps to this process: 1. Use your agency''s Steadily API Key to request a b'
  name: Steadily Account API
  slug: steadily-account-api
- description: A Draft Quote is an editable draft of a policy. Create a new draft quote by passing in basic insured and property information to `POST /v1/agency/draft_quote` with an authenticated bearer token header
  name: Steadily Draft Quote API
  slug: steadily-draft-quote-api
- description: Submit and retrieve lead referrals. Use the refer lead endpoint to submit a lead with full quote details and start the insurance quote process. You'll get back a quote estimate and a start_url for the
  name: Steadily Lead Referrals API
  slug: steadily-lead-referrals-api
- description: Policy information and change requests for third-party lender integrations
  name: Steadily Lender API
  slug: steadily-lender-api
- description: A Policy is an issued insurance policy. The declaration document and policy packet are available.
  name: Steadily Policy API
  slug: steadily-policy-api
- description: The Instant Estimate API is a one-step express API to quickly get a landlord insurance estimate you can display within your platform. To get started, you only need to send the address and a unique pro
  name: Steadily Quote Estimates API
  slug: steadily-quote-estimates-api
- description: An Offer is an immutable offer for coverage extended to a customer. Offers are generated from draft quotes and provides a PDF quote document. Creating an offer requires no outstanding underwriting ale
  name: Steadily Quote Offer API
  slug: steadily-quote-offer-api
- description: Reporting on the referrals you've sent Steadily and the referral fees you've earned. The lead, account, and policy endpoints follow each referral through its lifetime. The summary views provide aggreg
  name: Steadily Reporting API
  slug: steadily-reporting-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/steadily-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steadily-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/steadily-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.steadily.com/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steadily-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/steadily-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/steadily-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/steadily-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/steadily-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/steadily-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/steadily-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/steadily-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.steadily.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.steadily.com/redoc
- group: docs
  title: ''
  type: APIReference
  url: https://api.steadily.com/estimate-api/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://www.steadily.com/api
- group: company
  title: ''
  type: Blog
  url: https://www.steadily.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.steadily.com/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.steadily.com
- group: start
  title: ''
  type: SignUp
  url: https://www.steadily.com/partners
- group: company
  title: ''
  type: Website
  url: https://steadily.com
created: '2026-07-17'
description: Steadily is a US landlord-insurance provider — built by landlords, for landlords — writing rental-property policies in all 50 states with online quotes in minutes and coverage designed around how rental properties actually work. Its Partner API, a FastAPI-based REST service at api.steadily.com, lets property managers, lenders, and marketplaces generate instant insurance estimates, refer leads, and track bound policies. Appointed independent agencies use the companion Rater Quotes API to create, price, underwrite, and offer quotes directly from their rater. Steadily was founded by a landlord who could not find decent insurance for his own rental property.
image: https://app.steadily.com/static/images/steadily-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: steadily-mcp.yml
  slug: steadily-mcpyml
modified: '2026-07-21'
name: Steadily
nav: Providers
network: true
overview: 'Steadily publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Draft Quote API, Lead Referrals API, and 5 more. Tagged areas include Company, Fintech, Insurance, Landlord Insurance, and Insurtech.


  Steadily''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 40.1
  delta: -5.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 48.0
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 40.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Steadily Authentication
  slug: steadily-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Steadily Domain Security
  slug: steadily-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Steadily Vulnerability Disclosure
  slug: steadily-vulnerability-disclosure
  summary_line: disclosure policy published
slug: steadily
tags:
- Company
- Fintech
- Insurance
- Landlord Insurance
- Insurtech
- Real Estate
- Rental Property
- API
website: https://steadily.com
---
