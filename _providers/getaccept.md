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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Getaccept Agentic Access
  operation_count: 86
  slug: getaccept-agentic-access
  summary_line: 86 operations · 40 acting
api_count: 12
apis:
- description: You can upload already signed documents to the document archive to make them searchable and use in your contract management process.
  name: GetAccept Archive API
  slug: getaccept-archive-api
- description: You can upload an attachment and reuse it in many documents.
  name: GetAccept Attachments API
  slug: getaccept-attachments-api
- description: Authentication with the GetAccept API can be made using JWT tokens (JSON Web Tokens) or OAuth 2.0 Authorization Framework http://oauth.net/2/ All requests must be made via HTTPS. All configuration URL
  name: GetAccept Authentication API
  slug: getaccept-authentication-api
- description: Communication templates allow you to customize email and SMS messages sent to recipients.
  name: GetAccept Communication Templates API
  slug: getaccept-communication-templates-api
- description: Everything related to contacts
  name: GetAccept Contacts API
  slug: getaccept-contacts-api
- description: Custom Data enables you to define and use your own document properties as a complement to the default properties.
  name: GetAccept Custom Data API
  slug: getaccept-custom-data-api
- description: Everything related to documents
  name: GetAccept Documents API
  slug: getaccept-documents-api
- description: Additional endpoints used in various integrations.
  name: GetAccept Others API
  slug: getaccept-others-api
- description: 'To simplify the process of checking a documents status and make it more efficient in an integrated application, you can enable API Webhooks. Enable webhooks as a user with administrator privileges in '
  name: GetAccept Subscriptions API
  slug: getaccept-subscriptions-api
- description: GetAccept has extensive support for creating templates in different formats. You can use form fields to receive input data from a recipient or word files to merge custom data into a document.
  name: GetAccept Templates API
  slug: getaccept-templates-api
- description: General user methods for creating, listing of users, single user details and statistics and managing existing users.
  name: GetAccept Users API
  slug: getaccept-users-api
- description: You can upload videos and reuse it in many documents.
  name: GetAccept Videos API
  slug: getaccept-videos-api
artifact_total: 19
asyncapis:
- description: ''
  name: Getaccept Webhooks
  slug: getaccept-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getaccept.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getaccept.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getaccept.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getaccept.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetAccept
- group: company
  title: ''
  type: Blog
  url: https://www.getaccept.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getaccept.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getaccept.com/signup
- group: start
  title: ''
  type: Login
  url: https://login.getaccept.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getaccept.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getaccept.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@getaccept.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getaccept.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.getaccept.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/getaccept-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/getaccept-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getaccept-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/getaccept-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getaccept-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getaccept-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getaccept-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/getaccept-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/getaccept-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getaccept-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getaccept-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/getaccept-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getaccept-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getaccept.com/
created: '2026-07-17'
description: GetAccept is a digital sales room and sales enablement platform that helps revenue teams design, send, promote, track, and e-sign sales documents in one place — combining sales collateral, proposals, contract management, document tracking, and legally binding electronic signatures. The GetAccept REST API (v1, base https://api.getaccept.com/v1) exposes 86 operations across documents, e-signature, recipients, contacts, templates, users, videos, custom data, communication templates, and webhook subscriptions, secured with OAuth2 (authorization code) or bearer tokens. GetAccept is backed by Bessemer Venture Partners and Y Combinator.
image: https://www.getaccept.com/hubfs/logotype.svg
layout: provider
mcp_servers:
- description: ''
  name: getaccept-mcp.yml
  slug: getaccept-mcpyml
modified: '2026-07-19'
name: GetAccept
nav: Providers
network: true
overview: 'GetAccept publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Archive API, Attachments API, Authentication API, and 9 more. Tagged areas include Company, Cloud, Sales Enablement, Electronic Signature, and E-Signature.


  The GetAccept catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GetAccept''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 20
scopes:
- name: Getaccept Scopes
  scope_count: 1
  slug: getaccept-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 54.1
  delta: -2.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.2
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getaccept/refs/heads/main/screenshots/getaccept-2026-07-25T215711.png
security:
- kind: authentication
  name: Getaccept Authentication
  slug: getaccept-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Getaccept Domain Security
  slug: getaccept-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getaccept Trust Center
  slug: getaccept-trust-center
  summary_line: SOC 2, GDPR
slug: getaccept
tags:
- Company
- Cloud
- Sales Enablement
- Electronic Signature
- E-Signature
- Digital Sales Room
- Document Management
- Contract Management
- Proposals
- SaaS
website: https://www.getaccept.com/
---
