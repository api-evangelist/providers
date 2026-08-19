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
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Hellosign Agentic Access
  operation_count: 73
  slug: hellosign-agentic-access
  summary_line: 73 operations · 46 acting
api_count: 12
apis:
- description: '{''$ref'': ''./markdown/en/tags/account-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Account API
  slug: hellosign-account-api
- description: '{''$ref'': ''./markdown/en/tags/api-app-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Api App API
  slug: hellosign-api-app-api
- description: '{''$ref'': ''./markdown/en/tags/bulk-send-job-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Bulk Send Job API
  slug: hellosign-bulk-send-job-api
- description: '{''$ref'': ''./markdown/en/tags/embedded-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Embedded API
  slug: hellosign-embedded-api
- description: The Fax API from Dropbox Sign (HelloSign) — 4 operation(s) for fax.
  name: Dropbox Sign (HelloSign) Fax API
  slug: hellosign-fax-api
- description: '{''$ref'': ''./markdown/en/tags/fax-lines-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Fax Line API
  slug: hellosign-fax-line-api
- description: '{''$ref'': ''./markdown/en/tags/oauth-tag-description.md''}'
  name: Dropbox Sign (HelloSign) OAuth API
  slug: hellosign-oauth-api
- description: '{''$ref'': ''./markdown/en/tags/report-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Report API
  slug: hellosign-report-api
- description: '{''$ref'': ''./markdown/en/tags/signature-request-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Signature Request API
  slug: hellosign-signature-request-api
- description: '{''$ref'': ''./markdown/en/tags/team-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Team API
  slug: hellosign-team-api
- description: '{''$ref'': ''./markdown/en/tags/template-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Template API
  slug: hellosign-template-api
- description: '{''$ref'': ''./markdown/en/tags/unclaimed-draft-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Unclaimed Draft API
  slug: hellosign-unclaimed-draft-api
artifact_total: 45
asyncapis:
- description: ''
  name: Hellosign Events Webhooks
  slug: hellosign-events-webhooks
collections:
- collection_type: postman
  name: Dropbox Sign Account API
  slug: postman-hellosign-account-api
- collection_type: postman
  name: Dropbox Sign Account Api App API
  slug: postman-hellosign-api-app-api
- collection_type: postman
  name: Dropbox Sign Account Bulk Send Job API
  slug: postman-hellosign-bulk-send-job-api
- collection_type: postman
  name: Dropbox Sign Account Embedded API
  slug: postman-hellosign-embedded-api
- collection_type: postman
  name: Dropbox Sign Account Fax API
  slug: postman-hellosign-fax-api
- collection_type: postman
  name: Dropbox Sign Account Fax Line API
  slug: postman-hellosign-fax-line-api
- collection_type: postman
  name: Dropbox Sign Account OAuth API
  slug: postman-hellosign-oauth-api
- collection_type: postman
  name: Dropbox Sign Account Report API
  slug: postman-hellosign-report-api
- collection_type: postman
  name: Dropbox Sign Account Signature Request API
  slug: postman-hellosign-signature-request-api
- collection_type: postman
  name: Dropbox Sign Account Team API
  slug: postman-hellosign-team-api
- collection_type: postman
  name: Dropbox Sign Account Template API
  slug: postman-hellosign-template-api
- collection_type: postman
  name: Dropbox Sign Account Unclaimed Draft API
  slug: postman-hellosign-unclaimed-draft-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dropbox Sign Account API
  slug: open-hellosign-account-api
- collection_type: open
  name: Dropbox Sign Account Api App API
  slug: open-hellosign-api-app-api
- collection_type: open
  name: Dropbox Sign Account Bulk Send Job API
  slug: open-hellosign-bulk-send-job-api
- collection_type: open
  name: Dropbox Sign Account Embedded API
  slug: open-hellosign-embedded-api
- collection_type: open
  name: Dropbox Sign Account Fax API
  slug: open-hellosign-fax-api
- collection_type: open
  name: Dropbox Sign Account Fax Line API
  slug: open-hellosign-fax-line-api
- collection_type: open
  name: Dropbox Sign Account OAuth API
  slug: open-hellosign-oauth-api
- collection_type: open
  name: Dropbox Sign Account Report API
  slug: open-hellosign-report-api
- collection_type: open
  name: Dropbox Sign Account Signature Request API
  slug: open-hellosign-signature-request-api
- collection_type: open
  name: Dropbox Sign Account Team API
  slug: open-hellosign-team-api
- collection_type: open
  name: Dropbox Sign Account Template API
  slug: open-hellosign-template-api
- collection_type: open
  name: Dropbox Sign Account Unclaimed Draft API
  slug: open-hellosign-unclaimed-draft-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hellosign-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dropbox-sign-hellosign/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hellosign-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hellosign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hellosign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hellosign-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hellosign-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hellosign-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hellosign-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hellosign-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hellosign-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hellosign-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hellosign-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hellosign.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hellosign-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hellosign-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sign.dropbox.com/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/hellosign-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hellosign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/dropbox/dropbox-vdp
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hellosign-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hellosign-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/hellosign-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hellosign-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hellosign-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hellosign.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hellosign.com/docs/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hellosign.com/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hellosign.com/api/api-quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.dropbox.com/sign
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hellosign
- group: commercial
  title: ''
  type: Pricing
  url: https://sign.dropbox.com/products/api
- group: start
  title: ''
  type: SignUp
  url: https://app.hellosign.com/account/signUp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellosign.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellosign.com/privacy
created: '2026-07-17'
description: Dropbox Sign (formerly HelloSign) is an eSignature platform whose v3 REST API lets developers send documents for legally binding electronic signature, build reusable templates, embed signing directly in their own apps, run bulk send jobs, and manage accounts, teams, and API apps. The API exposes 73 operations across 12 product areas (Signature Request, Template, Bulk Send, Embedded, Account, Team, Report, Fax, Fax Line, Unclaimed Draft, API App, OAuth), with API-key and OAuth 2.0 authentication, 23 webhook event types, official SDKs in six languages, and a published hosted documentation MCP server. HelloSign was a Y Combinator company (S11), acquired by Dropbox in 2019 and rebranded to Dropbox Sign in 2022; the API base host remains api.hellosign.com.
image: https://github.com/hellosign.png
layout: provider
mcp_servers:
- description: ''
  name: hellosign-mcp.yml
  slug: hellosign-mcpyml
modified: '2026-07-19'
name: Dropbox Sign (HelloSign)
nav: Providers
network: true
overview: 'Dropbox Sign (HelloSign) publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Api App API, Bulk Send Job API, and 9 more. Tagged areas include Company, eSignature, Electronic Signatures, Documents, and Digital Agreements.


  The Dropbox Sign (HelloSign) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dropbox Sign (HelloSign)''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
random_paper: 71
scopes:
- name: Hellosign Scopes
  scope_count: 7
  slug: hellosign-scopes
  summary_line: 7 scopes
score:
  band: strong
  composite: 61.2
  delta: -2.8
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 68.3
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hellosign/refs/heads/main/screenshots/hellosign-2026-07-25T220935.png
security:
- kind: authentication
  name: Hellosign Authentication
  slug: hellosign-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Hellosign Domain Security
  slug: hellosign-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hellosign Vulnerability Disclosure
  slug: hellosign-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Hellosign Trust Center
  slug: hellosign-trust-center
  summary_line: HIPAA, ISO 9001, SOC (CPA/AICPA attestation), Skyhigh Enterprise-Ready
slug: hellosign
tags:
- Company
- eSignature
- Electronic Signatures
- Documents
- Digital Agreements
- Signature Workflow
- Embedded Signing
- Compliance
website: https://developers.hellosign.com/
---
