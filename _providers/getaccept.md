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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-19'
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
artifact_total: 34
asyncapis:
- description: ''
  name: Getaccept Webhooks
  slug: getaccept-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GetAccept Archive API
  slug: open-getaccept-archive-api
- collection_type: open
  name: GetAccept Archive Attachments API
  slug: open-getaccept-attachments-api
- collection_type: open
  name: GetAccept Archive Authentication API
  slug: open-getaccept-authentication-api
- collection_type: open
  name: GetAccept Archive Communication Templates API
  slug: open-getaccept-communication-templates-api
- collection_type: open
  name: GetAccept Archive Contacts API
  slug: open-getaccept-contacts-api
- collection_type: open
  name: GetAccept Archive Custom Data API
  slug: open-getaccept-custom-data-api
- collection_type: open
  name: GetAccept Archive Documents API
  slug: open-getaccept-documents-api
- collection_type: open
  name: GetAccept Archive Others API
  slug: open-getaccept-others-api
- collection_type: open
  name: GetAccept Archive Subscriptions API
  slug: open-getaccept-subscriptions-api
- collection_type: open
  name: GetAccept Archive Templates API
  slug: open-getaccept-templates-api
- collection_type: open
  name: GetAccept Archive Users API
  slug: open-getaccept-users-api
- collection_type: open
  name: GetAccept Archive Videos API
  slug: open-getaccept-videos-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/getaccept-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getaccept.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.getaccept.com/en/collections/9436688-api
- group: docs
  title: ''
  type: APIReference
  url: https://app.getaccept.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.getaccept.com/en/articles/2393314-how-to-use-the-getaccept-public-api
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
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getaccept.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/GetAccept/openapi
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.getaccept.com/whats-new
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/getaccept-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/getaccept-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getaccept-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/getaccept-packages.yml
created: '2026-07-17'
description: GetAccept is a digital sales room and sales enablement platform that helps revenue teams design, send, promote, track, and e-sign sales documents in one place — combining sales collateral, proposals, contract management, document tracking, and legally binding electronic signatures. The GetAccept REST API (v1, base https://api.getaccept.com/v1) exposes 86 operations across documents, e-signature, recipients, contacts, templates, users, videos, custom data, communication templates, and webhook subscriptions, secured with OAuth2 (authorization code) or bearer tokens. GetAccept is backed by Bessemer Venture Partners and Y Combinator.
image: https://www.getaccept.com/hubfs/logotype.svg
layout: provider
mcp_servers:
- description: ''
  name: getaccept-mcp.yml
  slug: getaccept-mcpyml
modified: '2026-08-14'
name: GetAccept
nav: Providers
network: true
overview: 'GetAccept publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Archive API, Attachments API, Authentication API, and 9 more. Tagged areas include Company, Cloud, Sales Enablement, Electronic Signature, and E-Signature.


  The GetAccept catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GetAccept''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 30 more developer resources.'
plans:
- name: Getaccept Plans Pricing
  plan_count: 3
  slug: getaccept-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 0
  name: Getaccept Rate Limits
  slug: getaccept-rate-limits
scopes:
- name: Getaccept Scopes
  scope_count: 1
  slug: getaccept-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.3
  delta: -0.3
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 67.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
  summary_line: SOC 2 Type II, GDPR, CCPA, eIDAS (EU Regulation No 910/2014), ESIGN Act, UETA, Electronic Communications Act 2000
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
