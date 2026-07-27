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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 16
apis:
- description: 'SCIM 2.0 surface for provisioning Venminder platform users — list, get, search, create and patch Users using urn:ietf:params:scim:schemas:core:2.0:User plus the urn:ietf:params:scim:schemas:extension:'
  name: Venminder SCIM 2.0 User Provisioning API
  slug: venminder-scim-api
- description: The BusinessUnit API from Venminder (Digital Comply) — 1 operation(s) for businessunit.
  name: Venminder (Digital Comply) BusinessUnit API
  slug: venminder-digital-comply-businessunit-api
- description: The ClientInformation API from Venminder (Digital Comply) — 1 operation(s) for clientinformation.
  name: Venminder (Digital Comply) ClientInformation API
  slug: venminder-digital-comply-clientinformation-api
- description: The Contact API from Venminder (Digital Comply) — 1 operation(s) for contact.
  name: Venminder (Digital Comply) Contact API
  slug: venminder-digital-comply-contact-api
- description: The Contracts API from Venminder (Digital Comply) — 9 operation(s) for contracts.
  name: Venminder (Digital Comply) Contracts API
  slug: venminder-digital-comply-contracts-api
- description: The Data API from Venminder (Digital Comply) — 1 operation(s) for data.
  name: Venminder (Digital Comply) Data API
  slug: venminder-digital-comply-data-api
- description: The Documents API from Venminder (Digital Comply) — 2 operation(s) for documents.
  name: Venminder (Digital Comply) Documents API
  slug: venminder-digital-comply-documents-api
- description: The Issues API from Venminder (Digital Comply) — 2 operation(s) for issues.
  name: Venminder (Digital Comply) Issues API
  slug: venminder-digital-comply-issues-api
- description: The OversightRequirement API from Venminder (Digital Comply) — 2 operation(s) for oversightrequirement.
  name: Venminder (Digital Comply) OversightRequirement API
  slug: venminder-digital-comply-oversightrequirement-api
- description: The OversightTask API from Venminder (Digital Comply) — 4 operation(s) for oversighttask.
  name: Venminder (Digital Comply) OversightTask API
  slug: venminder-digital-comply-oversighttask-api
- description: The Questionnaire API from Venminder (Digital Comply) — 4 operation(s) for questionnaire.
  name: Venminder (Digital Comply) Questionnaire API
  slug: venminder-digital-comply-questionnaire-api
- description: The Services API from Venminder (Digital Comply) — 2 operation(s) for services.
  name: Venminder (Digital Comply) Services API
  slug: venminder-digital-comply-services-api
- description: The VendorOnboarding API from Venminder (Digital Comply) — 8 operation(s) for vendoronboarding.
  name: Venminder (Digital Comply) VendorOnboarding API
  slug: venminder-digital-comply-vendoronboarding-api
- description: The Vendors API from Venminder (Digital Comply) — 10 operation(s) for vendors.
  name: Venminder (Digital Comply) Vendors API
  slug: venminder-digital-comply-vendors-api
- description: The VendorSpend API from Venminder (Digital Comply) — 8 operation(s) for vendorspend.
  name: Venminder (Digital Comply) VendorSpend API
  slug: venminder-digital-comply-vendorspend-api
- description: The Venmonitor API from Venminder (Digital Comply) — 1 operation(s) for venmonitor.
  name: Venminder (Digital Comply) Venmonitor API
  slug: venminder-digital-comply-venmonitor-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.venminder.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.venminder.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.venminder.com/318218fb2/p/325101-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.venminder.com/318218fb2/p/9845ac-the-venminder-apis/b/30923a
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.venminder.com/318218fb2/p/325101-getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.venminder.com/contact/customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.venminder.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/venminder
- group: start
  title: ''
  type: Login
  url: https://app.venminder.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.venminder.com/about/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.venminder.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.venminder.com/
- group: build
  title: ''
  type: Postman
  url: postman/venminder-digital-comply-postman-collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/venminder-digital-comply-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/venminder-digital-comply-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/venminder-digital-comply-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/venminder-digital-comply-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/venminder-digital-comply-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/venminder-digital-comply-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/venminder-digital-comply-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/venminder-digital-comply-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.venminder.com/about/legal
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/venminder-digital-comply-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/venminder-digital-comply-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/venminder-digital-comply-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/venminder-digital-comply-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/venminder-digital-comply-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Venminder is a third-party risk management (TPRM) platform for financial institutions — vendor onboarding, due diligence, contract tracking, questionnaires, oversight tasks, issue tracking, spend analysis and Venmonitor continuous monitoring. Founded in Elizabethtown, Kentucky as Digital Comply and backed by Bain Capital Ventures, the company merged with Ncontracts in 2024. The Venminder API (OAuth 2.0 client-credentials, scope venminderApi, tokens from login.venminder.com) exposes a customer's vendors, products, contracts, documents, questionnaires, onboarding requests, oversight and spend data at rsd.venminder.com, alongside a SCIM 2.0 user-provisioning surface at /scim/v2.
image: https://avatars.githubusercontent.com/u/116671086
layout: provider
mcp_servers:
- description: ''
  name: venminder-digital-comply-mcp.yml
  slug: venminder-digital-comply-mcpyml
modified: '2026-07-21'
name: Venminder (Digital Comply)
nav: Providers
network: true
overview: 'Venminder (Digital Comply) publishes 15 APIs on the [APIs.io](https://apis.io/) network, including BusinessUnit API, ClientInformation API, Contact API, and 12 more. Tagged areas include Company, Third-Party Risk Management, Vendor Management, Risk, and Compliance.


  Venminder (Digital Comply)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 4
scopes:
- name: Venminder Digital Comply Scopes
  scope_count: 1
  slug: venminder-digital-comply-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 46.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 45.1
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 46.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Venminder Digital Comply Authentication
  slug: venminder-digital-comply-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Venminder Digital Comply Domain Security
  slug: venminder-digital-comply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: venminder-digital-comply
tags:
- Company
- Third-Party Risk Management
- Vendor Management
- Risk
- Compliance
- Contracts
- Financial Services
- Due Diligence
- SCIM
website: https://www.venminder.com/
---
