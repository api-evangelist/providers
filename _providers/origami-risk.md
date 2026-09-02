---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-01'
api_count: 4
apis:
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
- description: The Authentication API from Origami Risk — 4 operation(s) for authentication.
  name: Origami Risk Authentication API
  slug: origami-risk-authentication-api
- description: The HasTokenExpired API from Origami Risk — 1 operation(s) for hastokenexpired.
  name: Origami Risk Has Token Expired API
  slug: origami-risk-hastokenexpired-api
- description: The New Endpoint 1 API from Origami Risk — 1 operation(s) for new endpoint 1.
  name: Origami Risk New Endpoint 1 API
  slug: origami-risk-new-endpoint-1-api
- description: The New Endpoint API from Origami Risk — 1 operation(s) for new endpoint.
  name: Origami Risk New Endpoint API
  slug: origami-risk-new-endpoint-api
- description: The Requests API from Origami Risk — 3 operation(s) for requests.
  name: Origami Risk Requests API
  slug: origami-risk-requests-api
artifact_total: 21
asyncapis:
- description: ''
  name: Origami Risk Webhooks
  slug: origami-risk-webhooks
collections:
- collection_type: open
  name: Origami Risk Authentication
  slug: open-origami-risk-authentication
- collection_type: open
  name: Origami Risk Public API
  slug: open-origami-risk-public-api
- collection_type: open
  name: Rating API
  slug: open-origami-risk-rating-api
- collection_type: open
  name: Rating API
  slug: open-origami-risk-standard-rating-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/origami-risk-authentication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/origami-risk-public-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/origami-risk-domain-data-access.md
- group: other
  title: ''
  type: Overlay
  url: overlays/origami-risk-standard-rating-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/origami-risk-rating-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/origami-risk-standard-rating-service.md
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
overview: 'Origami Risk publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Has Token Expired API, New Endpoint 1 API, and 2 more. Tagged areas include Insurance, United States, Property and Casualty, Policy Administration, and Claims.


  The Origami Risk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Origami Risk''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 35 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 5
  name: Origami Risk Rate Limits
  slug: origami-risk-rate-limits
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.5
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 49.3
    developer_ergonomics: 50.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 53.0
  provenance:
    conformance: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/origami-risk/refs/heads/main/screenshots/origami-risk-2026-08-07T190927.png
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
