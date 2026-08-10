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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Vendasta Agentic Access
  operation_count: 28
  slug: vendasta-agentic-access
  summary_line: 28 operations · 15 acting
api_count: 8
apis:
- description: The Account APIs allow you to perform actions against a single account that your application has been added to.
  name: Vendasta account API
  slug: vendasta-account-api
- description: 'The Activity API lets you inform us of new activity from your Marketplace App. It will be displayed in the user''s activity stream and used for notifications. Note: This endpoint has duplicate detectio'
  name: Vendasta activity API
  slug: vendasta-activity-api
- description: The Change Spend APIs allow interact with change spend requests, like resolving them by approving or rejecting
  name: Vendasta change_spend API
  slug: vendasta-change-spend-api
- description: The Customer APIs allow you to perform actions against customers of the account that your application has been added to.
  name: Vendasta customer API
  slug: vendasta-customer-api
- description: The executive report APIs are used to submit data to the executive report for a single app on an account.
  name: Vendasta executive_report API
  slug: vendasta-executive-report-api
- description: The Marketplace App APIs allow you to perform actions against your applications, as well as certain operations against all marketplace apps.
  name: Vendasta marketplace_app API
  slug: vendasta-marketplace-app-api
- description: The OAuth APIs allow applications to retrieve a bearer token that must be supplied with all API calls. See the Authentication documentation for more details.
  name: Vendasta oauth API
  slug: vendasta-oauth-api
- description: The User APIs allow you to perform operations against Vendasta Users. Each user has a unique identifier in the format UID-{}. This ID is guaranteed to stay the same, while the email associated to a us
  name: Vendasta user API
  slug: vendasta-user-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vendasta-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vendasta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendasta-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vendasta-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vendasta-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/vendasta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vendasta-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vendasta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendasta-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vendasta-marketplace-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vendasta-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vendasta-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vendasta-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vendasta-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vendasta-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vendasta-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.vendasta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.vendasta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vendasta.com/vendor
- group: docs
  title: ''
  type: APIReference
  url: https://developers.vendasta.com/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.vendasta.com/vendor
- group: auth
  title: ''
  type: Security
  url: https://www.vendasta.com/security/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vendasta.com/
- group: operate
  title: ''
  type: Support
  url: https://support.vendasta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vendasta.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendasta.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.vendasta.com/resources?name=terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.vendasta.com/resources?name=customer-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vendasta.com/
created: '2026-07-17'
description: Vendasta is an end-to-end commerce and operating platform that lets agencies, media companies, banks, telcos and other channel partners sell digital products and services to small and medium-sized businesses under their own brand. The platform bundles a white-label Marketplace of resellable products, a Business App client dashboard, CRM and sales pipeline, marketing automation, billing and an AI-powered concierge. Vendasta's public Marketplace API V1 is a REST API secured with OAuth2 bearer tokens that lets partners manage accounts, users, customers, activated add-ons, activities, executive reports, file groups and pending activations programmatically, plus a set of Early Access platform APIs and per-service SDKs for deeper integrations. Headquartered in Saskatoon, Canada, Vendasta was founded in 2008.
image: https://www.vendasta.com/wp-content/uploads/2021/03/vendasta-logo.png
layout: provider
mcp_servers:
- description: ''
  name: vendasta-mcp.yml
  slug: vendasta-mcpyml
modified: '2026-07-21'
name: Vendasta
nav: Providers
network: true
overview: 'Vendasta publishes 8 APIs on the [APIs.io](https://apis.io/) network, including account API, activity API, change_spend API, and 5 more. Tagged areas include Company, SaaS, Marketplace, SMB, and White Label.


  Vendasta''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 42
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.8
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 49.9
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Vendasta Authentication
  slug: vendasta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vendasta Domain Security
  slug: vendasta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vendasta Vulnerability Disclosure
  slug: vendasta-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Vendasta Trust Center
  slug: vendasta-trust-center
  summary_line: SOC 2
slug: vendasta
tags:
- Company
- SaaS
- Marketplace
- SMB
- White Label
- Reseller
- Marketing
- CRM
- Digital Agency
- Platform
website: https://www.vendasta.com
---
