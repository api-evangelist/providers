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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Certifaction Agentic Access
  operation_count: 21
  slug: certifaction-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 6
apis:
- description: Access your user account data
  name: Certifaction Account API
  slug: certifaction-account-api
- description: Download your documents or remove {{ .ProductName }}'s access to them
  name: Certifaction Documents API
  slug: certifaction-documents-api
- description: Manage your organization, users, and roles.
  name: Certifaction Organization API
  slug: certifaction-organization-api
- description: Check the server's status
  name: Certifaction Server API
  slug: certifaction-server-api
- description: Sign files and request signatures
  name: Certifaction Signing API
  slug: certifaction-signing-api
- description: Manage teamspaces and their members.
  name: Certifaction Teamspace API
  slug: certifaction-teamspace-api
artifact_total: 12
asyncapis:
- description: ''
  name: Certifaction Webhooks
  slug: certifaction-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://certifaction.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.certifaction.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.certifaction.com/en/guides/about
- group: docs
  title: ''
  type: APIReference
  url: https://developers.certifaction.com/en/references/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.certifaction.com/en/guides/getting-started-api
- group: company
  title: ''
  type: Blog
  url: https://certifaction.com/content-hub/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/certifaction
- group: commercial
  title: ''
  type: Pricing
  url: https://certifaction.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.certifaction.io/signup/
- group: start
  title: ''
  type: Login
  url: https://app.certifaction.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://certifaction.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certifaction.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/certifaction-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/certifaction-local-api-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/certifaction-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/certifaction-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/certifaction-cli.yml
- group: design
  title: ''
  type: Components
  url: components/certifaction-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/certifaction-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/certifaction-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/certifaction-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/certifaction-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/certifaction-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/certifaction-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/certifaction-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/certifaction-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/certifaction-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://certifaction.com/security-esigning-and-data/
- group: auth
  title: ''
  type: TrustCenter
  url: security/certifaction-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certifaction-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/certifaction-agentic-access.yml
created: '2026-07-17'
description: 'Certifaction is a privacy-first digital signature platform built around a Zero Document Knowledge model: documents are hashed and end-to-end encrypted on the client so they can be signed and verified without Certifaction ever seeing their content. It offers Simple, Advanced, and Qualified Electronic Signatures (SES/AES/QES) compliant with eIDAS, ZertES, UETA and ESIGN, delivered through a client-hosted CLI and Local API plus an Admin API for organization, user, role and team-space management, with EU / Switzerland / on-premises data residency and ISO/IEC 27001:2022 certification.'
image: https://developers.certifaction.com/themes/certifaction/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: certifaction-mcp.yml
  slug: certifaction-mcpyml
modified: '2026-07-18'
name: Certifaction
nav: Providers
network: true
overview: 'Certifaction publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Documents API, Organization API, and 3 more. Tagged areas include Company, Ai Enterprise Software, Electronic Signature, Digital Signature, and Document Signing.


  The Certifaction catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Certifaction''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 25 more developer resources.'
random_paper: 115
score:
  band: developing
  composite: 55.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.5
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certifaction/refs/heads/main/screenshots/certifaction-2026-07-25T205000.png
security:
- kind: authentication
  name: Certifaction Authentication
  slug: certifaction-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Certifaction Domain Security
  slug: certifaction-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Certifaction Trust Center
  slug: certifaction-trust-center
  summary_line: ISO/IEC 27001:2022, eIDAS, ZertES, GDPR, revFADP, UETA, ESIGN
slug: certifaction
tags:
- Company
- Ai Enterprise Software
- Electronic Signature
- Digital Signature
- Document Signing
- Qualified Electronic Signature
- eIDAS
- Privacy
- Compliance
- Identity Verification
- Switzerland
website: https://certifaction.com
---
