---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 12
  name: Bexio Agentic Access
  operation_count: 20
  slug: bexio-agentic-access
  summary_line: 20 operations · 12 acting · 12 human-in-the-loop
api_count: 9
apis:
- description: The Accounting API from bexio — 4 operation(s) for accounting.
  name: bexio Accounting API
  slug: bexio-accounting-api
- description: The Banking API from bexio — 1 operation(s) for banking.
  name: bexio Banking API
  slug: bexio-banking-api
- description: The Contacts API from bexio — 2 operation(s) for contacts.
  name: bexio Contacts API
  slug: bexio-contacts-api
- description: The Files API from bexio — 1 operation(s) for files.
  name: bexio Files API
  slug: bexio-files-api
- description: The Items API from bexio — 1 operation(s) for items.
  name: bexio Items API
  slug: bexio-items-api
- description: The Payroll API from bexio — 2 operation(s) for payroll.
  name: bexio Payroll API
  slug: bexio-payroll-api
- description: The Projects API from bexio — 2 operation(s) for projects.
  name: bexio Projects API
  slug: bexio-projects-api
- description: The Purchase API from bexio — 2 operation(s) for purchase.
  name: bexio Purchase API
  slug: bexio-purchase-api
- description: The Sales Orders API from bexio — 5 operation(s) for sales orders.
  name: bexio Sales Orders API
  slug: bexio-sales-orders-api
artifact_total: 38
collections:
- collection_type: postman
  name: bexio Accounting API
  slug: postman-bexio-accounting-api
- collection_type: postman
  name: bexio Accounting Banking API
  slug: postman-bexio-banking-api
- collection_type: postman
  name: bexio Accounting Contacts API
  slug: postman-bexio-contacts-api
- collection_type: postman
  name: bexio Accounting Files API
  slug: postman-bexio-files-api
- collection_type: postman
  name: bexio Accounting Items API
  slug: postman-bexio-items-api
- collection_type: postman
  name: bexio Accounting Payroll API
  slug: postman-bexio-payroll-api
- collection_type: postman
  name: bexio Accounting Projects API
  slug: postman-bexio-projects-api
- collection_type: postman
  name: bexio Accounting Purchase API
  slug: postman-bexio-purchase-api
- collection_type: postman
  name: bexio Accounting Sales Orders API
  slug: postman-bexio-sales-orders-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: bexio Accounting API
  slug: open-bexio-accounting-api
- collection_type: open
  name: bexio Accounting Banking API
  slug: open-bexio-banking-api
- collection_type: open
  name: bexio Accounting Contacts API
  slug: open-bexio-contacts-api
- collection_type: open
  name: bexio Accounting Files API
  slug: open-bexio-files-api
- collection_type: open
  name: bexio Accounting Items API
  slug: open-bexio-items-api
- collection_type: open
  name: bexio Accounting Payroll API
  slug: open-bexio-payroll-api
- collection_type: open
  name: bexio Accounting Projects API
  slug: open-bexio-projects-api
- collection_type: open
  name: bexio Accounting Purchase API
  slug: open-bexio-purchase-api
- collection_type: open
  name: bexio Accounting Sales Orders API
  slug: open-bexio-sales-orders-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bexio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bexio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bexio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bexio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bexio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bexio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bexiocom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bexio-ag
- group: company
  title: ''
  type: Website
  url: https://www.bexio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bexio.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bexio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bexio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bexio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bexio.com/en-CH/blog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bexio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bexio-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.bexio.com/en-CH/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.bexio.com/en-CH/security
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bexio-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/bexio-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bexio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bexio-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bexio-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/bexio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bexio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bexio-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://bexio.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.bexio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bexio-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bexio-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bexio-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/bexio.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bexio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bexio.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bexio.com/en-CH/quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://help.bexio.com/s/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bexio.com/en-CH/packages-and-prices
- group: start
  title: ''
  type: SignUp
  url: https://www.bexio.com/en-CH/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bexio.com/en-CH/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bexio.com/en-CH/policies/privacy-policy
created: '2026-07-17'
description: bexio is a Swiss cloud business-management platform for SMBs and self-employed, covering accounting, invoicing (incl. Swiss QR-bill), contacts, sales orders, projects and time tracking, banking, purchasing, and payroll. The bexio REST API at api.bexio.com/2.0 exposes these modules over HTTPS with JSON, secured by OAuth 2.0 (OpenID Connect) or Personal Access Tokens.
finops:
- name: Bexio Finops
  service_category: Business Application Software
  slug: bexio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bexio.png
layout: provider
mcp_servers:
- description: ''
  name: bexio-mcp.yml
  slug: bexio-mcpyml
modified: '2026-07-17'
name: bexio
nav: Providers
network: true
overview: 'bexio publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Banking API, Contacts API, and 6 more. Tagged areas include Accounting, ERP, Invoicing, SMB, and Switzerland.


  bexio''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Bexio Plans Pricing
  plan_count: 5
  slug: bexio-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 2
  name: Bexio Rate Limits
  slug: bexio-rate-limits
scopes:
- name: Bexio Scopes
  scope_count: 71
  slug: bexio-scopes
  summary_line: 71 scopes
score:
  band: exemplar
  composite: 67.3
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 53.7
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 76.3
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bexio/refs/heads/main/screenshots/bexio-2026-07-25T202828.png
security:
- kind: authentication
  name: Bexio Authentication
  slug: bexio-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Bexio Domain Security
  slug: bexio-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Bexio Vulnerability Disclosure
  slug: bexio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bexio Trust Center
  slug: bexio-trust-center
  summary_line: ISO 27001, Swiss FADP (revDSG), GDPR
slug: bexio
tags:
- Accounting
- ERP
- Invoicing
- SMB
- Switzerland
website: https://www.bexio.com/
---
