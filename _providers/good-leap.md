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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Good Leap Agentic Access
  operation_count: 53
  slug: good-leap-agentic-access
  summary_line: 53 operations · 21 acting
api_count: 18
apis:
- description: The Authorization & Elevation Management API from Good Leap — 4 operation(s) for authorization & elevation management.
  name: Good Leap Authorization & Elevation Management API
  slug: good-leap-authorization-elevation-management-api
- description: The Calculate Payments API from Good Leap — 2 operation(s) for calculate payments.
  name: Good Leap Calculate Payments API
  slug: good-leap-calculate-payments-api
- description: The Case (loan stipulations) Management API from Good Leap — 5 operation(s) for case (loan stipulations) management.
  name: Good Leap Case (loan stipulations) Management API
  slug: good-leap-case-loan-stipulations-management-api
- description: The Disclosures API from Good Leap — 1 operation(s) for disclosures.
  name: Good Leap Disclosures API
  slug: good-leap-disclosures-api
- description: The Install Categories & Loan Limitations API from Good Leap — 3 operation(s) for install categories & loan limitations.
  name: Good Leap Install Categories & Loan Limitations API
  slug: good-leap-install-categories-loan-limitations-api
- description: The Loan Change Orders API from Good Leap — 3 operation(s) for loan change orders.
  name: Good Leap Loan Change Orders API
  slug: good-leap-loan-change-orders-api
- description: The Loan Documents Management API from Good Leap — 2 operation(s) for loan documents management.
  name: Good Leap Loan Documents Management API
  slug: good-leap-loan-documents-management-api
- description: The Loan Notes Management API from Good Leap — 2 operation(s) for loan notes management.
  name: Good Leap Loan Notes Management API
  slug: good-leap-loan-notes-management-api
- description: The Loan Status API from Good Leap — 6 operation(s) for loan status.
  name: Good Leap Loan Status API
  slug: good-leap-loan-status-api
- description: The Loan Submission API from Good Leap — 2 operation(s) for loan submission.
  name: Good Leap Loan Submission API
  slug: good-leap-loan-submission-api
- description: The Loan Tag Management API from Good Leap — 2 operation(s) for loan tag management.
  name: Good Leap Loan Tag Management API
  slug: good-leap-loan-tag-management-api
- description: The Milestone Management API from Good Leap — 2 operation(s) for milestone management.
  name: Good Leap Milestone Management API
  slug: good-leap-milestone-management-api
- description: The Project Management API from Good Leap — 4 operation(s) for project management.
  name: Good Leap Project Management API
  slug: good-leap-project-management-api
- description: The Promotions API from Good Leap — 1 operation(s) for promotions.
  name: Good Leap Promotions API
  slug: good-leap-promotions-api
- description: The States & Channels API from Good Leap — 2 operation(s) for states & channels.
  name: Good Leap States & Channels API
  slug: good-leap-states-channels-api
- description: The Toolbox API from Good Leap — 1 operation(s) for toolbox.
  name: Good Leap Toolbox API
  slug: good-leap-toolbox-api
- description: The User Management API from Good Leap — 7 operation(s) for user management.
  name: Good Leap User Management API
  slug: good-leap-user-management-api
- description: The Verify Loan Details API from Good Leap — 1 operation(s) for verify loan details.
  name: Good Leap Verify Loan Details API
  slug: good-leap-verify-loan-details-api
arazzos:
- description: Authenticate, submit a loan application, then track its status and next actions.
  name: Originate and track a GoodLeap loan
  slug: good-leap-originate-and-track-loan
artifact_total: 25
collections:
- collection_type: postman
  name: GoodLeap - Developer API
  slug: postman-good-leap-developer-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/good-leap-developer-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.goodleap.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goodleap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goodleap.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.goodleap.com/reference
- group: company
  title: ''
  type: Blog
  url: https://www.goodleap.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.goodleap.com/support/solutions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodleap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodleap.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/loanpalapidocuments/goodleap-developer-api-public-resources/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/good-leap-developer-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/good-leap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/good-leap-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/good-leap-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/good-leap-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/good-leap-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/good-leap-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/good-leap-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/good-leap-originate-and-track-loan.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/good-leap-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/good-leap-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://www.goodleap.com/report-a-security-bug
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/good-leap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/good-leap-domain-security.yml
created: '2026-07-17'
description: 'GoodLeap (formerly Loanpal) is a fintech platform providing point-of-sale financing for sustainable home improvements — solar and battery storage, efficient heating and cooling, roofing and ventilation, water conservation, and energy-efficient windows. Its Developer API (v2, POS financing) lets approved partners originate and manage home-improvement loans through the full lifecycle: authentication and elevation, offers and payment calculation, loan submission, status and timeline tracking, case (stipulation) management, document upload via pre-signed URLs, project and milestone management, change orders, notes, tags, and user management. Authentication is JWT bearer; partner credentials from developer.goodleap.com are required. This profile was surfaced as a portfolio company of Ribbit Capital and enriched from GoodLeap''s public developer surface (developer portal + public Postman collection).'
image: https://www.goodleap.com/opengraph-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: good-leap-mcp.yml
  slug: good-leap-mcpyml
modified: '2026-07-19'
name: Good Leap
nav: Providers
network: true
overview: 'Good Leap publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Authorization & Elevation Management API, Calculate Payments API, Case (loan stipulations) Management API, and 15 more. Tagged areas include Company, Fintech, Financing, Lending, and Solar.


  Good Leap''s developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 19 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 55.0
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/good-leap/refs/heads/main/screenshots/good-leap-2026-07-25T220101.png
security:
- kind: authentication
  name: Good Leap Authentication
  slug: good-leap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Good Leap Domain Security
  slug: good-leap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Good Leap Vulnerability Disclosure
  slug: good-leap-vulnerability-disclosure
  summary_line: contact published
slug: good-leap
tags:
- Company
- Fintech
- Financing
- Lending
- Solar
- Home Improvement
- Sustainability
- Point of Sale
- Loans
- Payments
website: https://www.goodleap.com
---
