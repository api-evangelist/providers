---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: Token issuance and session verification for the Origami Risk platform APIs. Two documented token formats — a simple JSON payload (Account, User, Password, ClientName) and an OAuth-style client_credent
  name: Origami Risk Authentication API
  slug: origami-risk-authentication-api
- description: The core Origami Risk platform API — generic domain and entity CRUD (get, upsert, bulk insert, bulk upsert, delete), domain metadata and data dictionary lookups, screen configuration, notes, emails, f
  name: Origami Risk Public API
  slug: origami-risk-public-api
- description: Standalone standard rating service that accepts a rating request referencing a rater and intake payloads and returns rating results, offered in both synchronous and asynchronous modes with request ret
  name: Origami Risk Standard Rating API
  slug: origami-risk-standard-rating-api
- description: Quote-side policy lifecycle — create and patch proposals, add and remove policy lines, coverages, schedules and linked schedules, list insurance programs, carriers, policy lines and states, run or que
  name: Origami Risk Quotes and Proposals API
  slug: origami-risk-quotes-and-proposals-api
- description: Issue-side policy administration — accept, reject, undo-accept, undo-reject and undo-binding a bound proposal to issue a policy, then endorse, cancel, reinstate, change billing frequency and take paym
  name: Origami Risk Policies API
  slug: origami-risk-policies-api
- description: Billing account operations including making and reversing payments, plus an online policy payment surface integrated with the One Inc payment gateway covering payment submission, payment-method acknow
  name: Origami Risk Billing and Payments API
  slug: origami-risk-billing-accounts-api
- description: Real-time and queued platform actions triggered against any domain record — including creating a claim from an incident (the FNOL path), FirstReport, Reserve, Review, RootCause, EDIReport state report
  name: Origami Risk Actions API
  slug: origami-risk-actions-api
- description: Inbound webhook surface for the Origami Risk platform. An Origami "webhook handler" is a bespoke endpoint built inside Origami by the services team that an external system posts data into — list the c
  name: Origami Risk Webhooks API
  slug: origami-risk-webhooks-api
- description: Reporting surface for requesting a report run, retrieving report details and options, validating a report filter, and converting between the platform's view-filter string form and its JSON tree form.
  name: Origami Risk Reports API
  slug: origami-risk-reports-api
artifact_total: 15
asyncapis:
- description: ''
  name: Origami Risk Webhooks
  slug: origami-risk-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/origami-risk-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.origamirisk.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/origami-risk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/origami-risk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/origami-risk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/origami-risk-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/origami-risk-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/origami-risk-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.origamirisk.com/
- group: operate
  title: ''
  type: SLA
  url: https://www.origamirisk.com/serviceterms/sla/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/origami-risk-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.origamirisk.com/platform/product-updates/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/origami-risk-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/origami-risk-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/origami-risk-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/origami-risk-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/origami-risk-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/origami-risk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/origami-risk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.origamirisk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.origamirisk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.origamirisk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.origamirisk.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.origamirisk.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.origamirisk.com/reference/authentication-methods
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.origamirisk.com/reference/limits
- group: other
  title: ''
  type: ProductOverview
  url: https://www.origamirisk.com/platform/api-access/
- group: company
  title: ''
  type: Partners
  url: https://www.origamirisk.com/partners/
- group: start
  title: ''
  type: Login
  url: https://developers.origamirisk.com/login?redirect_uri=/
- group: operate
  title: ''
  type: Support
  url: https://www.origamirisk.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.origamirisk.com/resources/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.origamirisk.com/serviceterms/aipricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.origamirisk.com/origami-risk-website-terms-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.origamirisk.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/origamirisk
created: '2026-07-25'
description: Origami Risk is a Chicago-headquartered risk, safety and insurance SaaS company founded in 2009 that began as a single-version cloud RMIS (risk management information system) and grew into a core-systems platform for the United States property and casualty market. It sells policy administration, digital underwriting, rating, billing, premium audit, claims administration, compliance and EHS/GRC modules to carriers, MGAs, program administrators, third-party administrators, risk pools, brokers, healthcare systems and large self-insureds, across workers' compensation, medical professional liability, personal auto and homeowners lines. Unlike most US insurance organizations, Origami Risk sits in the software layer between carriers and distribution and therefore does publish a genuinely public, self-serve developer portal at developers.origamirisk.com — a ReadMe-hosted reference readable without login, covering quote and proposal creation, rating, bind, policy issue/endorse/cancel,
  billing and payments, claims-from-incident and first-report actions, files, reports, domain metadata and outbound webhooks. Four OpenAPI definitions are downloadable from the portal's spec registry, though three of the four are thin scaffolds and the bulk of the reference is hand-authored per-endpoint documentation rather than a complete machine-readable spec. Access to a live tenant is still commercial — the base URL is a per-customer https://{environment}.origamirisk.com host and authentication is token-based or HMAC against a provisioned account — and no ACORD, AL3, IVANS or NGDS conformance is claimed anywhere in the marketing site or the developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool list (no official server published)
  slug: candidate-mcp-tool-list-no-official-server-published
modified: '2026-07-25'
name: Origami Risk
nav: Providers
network: true
overview: 'Origami Risk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Public API, and Standard Rating API. Tagged areas include Insurance, United States, Property and Casualty, Policy Administration, and Claims.


  The Origami Risk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Origami Risk''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
random_paper: 45
rate_limits:
- limit_count: 0
  name: Origami Risk Rate Limits
  slug: origami-risk-rate-limits
score:
  band: developing
  composite: 51.9
  delta: -5.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 57.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Origami Risk Authentication
  slug: origami-risk-authentication
  summary_line: apiKey/token-endpoint/hmac · 6 schemes
- kind: domain-security
  name: Origami Risk Domain Security
  slug: origami-risk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Origami Risk Trust Center
  slug: origami-risk-trust-center
  summary_line: trust center published
slug: origami-risk
tags:
- Insurance
- United States
- Property and Casualty
- Policy Administration
- Claims
- Underwriting
- Core Systems
- Risk Management
- Workers Compensation
- Insurtech
- Billing
website: https://www.origamirisk.com/
---
