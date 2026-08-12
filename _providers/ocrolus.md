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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 34
  human_in_the_loop: 1
  name: Ocrolus Agentic Access
  operation_count: 82
  slug: ocrolus-agentic-access
  summary_line: 82 operations · 34 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: The Book Commands API from Ocrolus — 3 operation(s) for book commands.
  name: Ocrolus Book Commands API
  slug: ocrolus-book-commands-api
- description: The Book Queries API from Ocrolus — 5 operation(s) for book queries.
  name: Ocrolus Book Queries API
  slug: ocrolus-book-queries-api
- description: The Business history API from Ocrolus — 4 operation(s) for business history.
  name: Ocrolus Business history API
  slug: ocrolus-business-history-api
- description: The Business Verification (Deprecated) API from Ocrolus — 3 operation(s) for business verification (deprecated).
  name: Ocrolus Business Verification (Deprecated) API
  slug: ocrolus-business-verification-deprecated-api
- description: The Capture API from Ocrolus — 7 operation(s) for capture.
  name: Ocrolus Capture API
  slug: ocrolus-capture-api
- description: The Cash Flow Analytics API from Ocrolus — 10 operation(s) for cash flow analytics.
  name: Ocrolus Cash Flow Analytics API
  slug: ocrolus-cash-flow-analytics-api
- description: The Detect API from Ocrolus — 4 operation(s) for detect.
  name: Ocrolus Detect API
  slug: ocrolus-detect-api
- description: The Encore API from Ocrolus — 5 operation(s) for encore.
  name: Ocrolus Encore API
  slug: ocrolus-encore-api
- description: The File Uploads API from Ocrolus — 7 operation(s) for file uploads.
  name: Ocrolus File Uploads API
  slug: ocrolus-file-uploads-api
- description: The Income API from Ocrolus — 5 operation(s) for income.
  name: Ocrolus Income API
  slug: ocrolus-income-api
- description: The Legacy Cash Flow Analytics (Deprecated) API from Ocrolus — 4 operation(s) for legacy cash flow analytics (deprecated).
  name: Ocrolus Legacy Cash Flow Analytics (Deprecated) API
  slug: ocrolus-legacy-cash-flow-analytics-deprecated-api
- description: The Oauth API from Ocrolus — 1 operation(s) for oauth.
  name: Ocrolus Oauth API
  slug: ocrolus-oauth-api
- description: The Org Level Webhooks API from Ocrolus — 8 operation(s) for org level webhooks.
  name: Ocrolus Org Level Webhooks API
  slug: ocrolus-org-level-webhooks-api
- description: The Tag Management API from Ocrolus — 4 operation(s) for tag management.
  name: Ocrolus Tag Management API
  slug: ocrolus-tag-management-api
- description: The User management API from Ocrolus — 2 operation(s) for user management.
  name: Ocrolus User management API
  slug: ocrolus-user-management-api
- description: The Webhooks API from Ocrolus — 4 operation(s) for webhooks.
  name: Ocrolus Webhooks API
  slug: ocrolus-webhooks-api
artifact_total: 40
asyncapis:
- description: ''
  name: Ocrolus Webhooks
  slug: ocrolus-webhooks
collections:
- collection_type: postman
  name: Account Level Webhooks Book Commands API
  slug: postman-ocrolus-book-commands-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Book Queries API
  slug: postman-ocrolus-book-queries-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Business history API
  slug: postman-ocrolus-business-history-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Business Verification (Deprecated) API
  slug: postman-ocrolus-business-verification-deprecated-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Capture API
  slug: postman-ocrolus-capture-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Cash Flow Analytics API
  slug: postman-ocrolus-cash-flow-analytics-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Detect API
  slug: postman-ocrolus-detect-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Encore API
  slug: postman-ocrolus-encore-api
- collection_type: postman
  name: Account Level Webhooks Book Commands File Uploads API
  slug: postman-ocrolus-file-uploads-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Income API
  slug: postman-ocrolus-income-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Legacy Cash Flow Analytics (Deprecated) API
  slug: postman-ocrolus-legacy-cash-flow-analytics-deprecated-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Oauth API
  slug: postman-ocrolus-oauth-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Org Level Webhooks API
  slug: postman-ocrolus-org-level-webhooks-api
- collection_type: postman
  name: Account Level Webhooks Book Commands Tag Management API
  slug: postman-ocrolus-tag-management-api
- collection_type: postman
  name: Account Level Webhooks Book Commands User management API
  slug: postman-ocrolus-user-management-api
- collection_type: postman
  name: Account Level Book Commands Webhooks API
  slug: postman-ocrolus-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ocrolus/overview
- group: company
  title: ''
  type: Website
  url: https://ocrolus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ocrolus.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ocrolus.com/docs/guide
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ocrolus.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ocrolus.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocrolus-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.ocrolus.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ocrolus.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ocrolus
- group: start
  title: ''
  type: SignUp
  url: https://app.ocrolus.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.ocrolus.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.ocrolus.com/legal/terms-of-use-88ee7151
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.ocrolus.com/legal/privacy-policy-958a2463
- group: build
  title: ''
  type: Postman
  url: https://docs.ocrolus.com/docs/using-ocrolus-with-postman
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ocrolus.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ocrolus.com/changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ocrolus.com/docs/breaking-change-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ocrolus-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.ocrolus.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ocrolus-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://security.ocrolus.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ocrolus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocrolus-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ocrolus-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ocrolus-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ocrolus-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ocrolus-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ocrolus-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocrolus-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-account-level-webhooks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-analyze-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-authentication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-book-commands-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-book-queries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-business-history-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-capture-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-detect-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-encore-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-file-uploads-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-income-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-org-level-webhooks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-tag-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocrolus-user-management-overlay.yaml
created: '2026-07-17'
description: 'Ocrolus is a fintech document-automation and analytics platform that helps lenders analyze financial documents - bank statements, pay stubs, tax forms and more - with high accuracy. Its API covers Classify, Capture, Detect and Analyze: document classification and data extraction, fraud and authenticity detection, cash-flow analytics, income calculation for mortgage and SMB/consumer lending, business verification, tag management and webhooks. Authentication is OAuth 2.0 client credentials issuing JWT access tokens, over a REST API at api.ocrolus.com.'
image: https://www.ocrolus.com/wp-content/uploads/2025/10/social-home-page.jpg
layout: provider
mcp_servers:
- description: ''
  name: ocrolus-mcp.yml
  slug: ocrolus-mcpyml
modified: '2026-07-20'
name: Ocrolus
nav: Providers
network: true
overview: 'Ocrolus publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Book Commands API, Book Queries API, Business history API, and 13 more. Tagged areas include Company, Fintech, Document Automation, Lending, and Underwriting.


  The Ocrolus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ocrolus'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 38 more developer resources.'
random_paper: 79
rate_limits:
- limit_count: 1
  name: Ocrolus Rate Limits
  slug: ocrolus-rate-limits
score:
  band: strong
  composite: 58.7
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.2
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 76.3
  previous_composite: 60.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocrolus/refs/heads/main/screenshots/ocrolus-2026-08-07T185929.png
security:
- kind: authentication
  name: Ocrolus Authentication
  slug: ocrolus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ocrolus Domain Security
  slug: ocrolus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ocrolus Vulnerability Disclosure
  slug: ocrolus-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Ocrolus Trust Center
  slug: ocrolus-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR
slug: ocrolus
tags:
- Company
- Fintech
- Document Automation
- Lending
- Underwriting
- OCR
- Fraud Detection
- Income Verification
- Bank Statement Analysis
- Mortgage
- Machine Learning
- Cash Flow Analytics
website: https://ocrolus.com
---
