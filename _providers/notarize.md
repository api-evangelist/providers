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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 43.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST API for creating and managing notarization, eSign, Identify, and real-estate transactions, documents, signers, notaries, templates, and Webhooks V2 subscriptions.
  name: Proof API (formerly Notarize)
  slug: proof-api-formerly-notarize
artifact_total: 7
asyncapis:
- description: ''
  name: Notarize Webhooks
  slug: notarize-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/notarize-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notarize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.proof.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.proof.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.proof.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.proof.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.proof.com/docs/business-quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.proof.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.proof.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.proof.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proof.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@proof.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/notarize
- group: operate
  title: ''
  type: StatusPage
  url: https://status.proof.com
- group: auth
  title: ''
  type: Compliance
  url: https://security.proof.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/notarize-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/notarize-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/notarize-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/notarize-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/notarize-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/notarize-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/notarize-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/notarize-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/notarize-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/notarize-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/notarize-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/notarize-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Notarize (rebranded as Proof) provides Remote Online Notarization (RON), eSignature, identity verification, and reusable digital credentials through the Notarize Network. Its REST API (api.proof.com) lets businesses create notarization, eSign, Identify, and real-estate/mortgage closing transactions, attach and template documents, invite signers, manage notaries, and receive V2 webhooks for every transaction and notary state change. Authentication is by API key or OAuth 2.0 client credentials, with a Fairfax test environment for end-to-end sandbox testing. Widely used across proptech, lending, title, and legal workflows.
image: https://github.com/notarize.png
layout: provider
mcp_servers:
- description: ''
  name: notarize-mcp.yml
  slug: notarize-mcpyml
modified: '2026-07-20'
name: Notarize
nav: Providers
network: true
overview: 'Notarize publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Proptech, Notarization, Remote Online Notarization, and Identity Verification.


  The Notarize catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Notarize''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
random_paper: 60
scopes:
- name: Notarize Scopes
  scope_count: 2
  slug: notarize-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 43.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Notarize Authentication
  slug: notarize-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Notarize Domain Security
  slug: notarize-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Notarize Trust Center
  slug: notarize-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: notarize
tags:
- Company
- Proptech
- Notarization
- Remote Online Notarization
- Identity Verification
- eSignature
- Digital Credentials
- Real Estate
- Mortgage
- Legal Tech
website: https://www.proof.com/
---
