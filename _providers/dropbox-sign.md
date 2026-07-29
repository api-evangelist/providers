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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Dropbox Sign Agentic Access
  operation_count: 15
  slug: dropbox-sign-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 6
apis:
- description: Outbound event / callback surface for Dropbox Sign. The platform POSTs JSON event payloads (wrapped in a `multipart/form-data` `json` field) to a subscriber-configured URL whenever signature requests,
  name: Dropbox Sign Events and Callbacks API
  slug: events-api
- description: The Account API from Dropbox Sign — 3 operation(s) for account.
  name: Dropbox Sign Account API
  slug: dropbox-sign-account-api
- description: The API App API from Dropbox Sign — 3 operation(s) for api app.
  name: Dropbox Sign API App API
  slug: dropbox-sign-api-app-api
- description: The Bulk Send Job API from Dropbox Sign — 2 operation(s) for bulk send job.
  name: Dropbox Sign Bulk Send Job API
  slug: dropbox-sign-bulk-send-job-api
- description: The Embedded API from Dropbox Sign — 2 operation(s) for embedded.
  name: Dropbox Sign Embedded API
  slug: dropbox-sign-embedded-api
- description: The Fax API from Dropbox Sign — 2 operation(s) for fax.
  name: Dropbox Sign Fax API
  slug: dropbox-sign-fax-api
artifact_total: 15
asyncapis:
- description: 'AsyncAPI description of the Dropbox Sign (formerly HelloSign) outbound event / callback surface. Dropbox Sign delivers event notifications by issuing HTTP POST requests to a subscriber-configured URL '
  name: Dropbox Sign Events and Callbacks
  slug: dropbox-sign-events-asyncapi
collections:
- collection_type: open
  name: Dropbox Sign API
  slug: open-dropbox-sign
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dropbox-sign-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dropbox-sign-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dropbox-sign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dropbox-sign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dropbox-sign-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dropboxsign
- group: company
  title: ''
  type: Website
  url: https://sign.dropbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hellosign.com
- group: docs
  title: ''
  type: API Documentation
  url: https://developers.hellosign.com/api/api-reference-welcome
- group: commercial
  title: ''
  type: Pricing
  url: https://sign.dropbox.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://sign.dropbox.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hellosign
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.hellosign.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://sign.dropbox.com/blog
created: '2026-05-11'
description: Dropbox Sign (formerly HelloSign) is an eSignature platform that lets developers and businesses embed legally binding electronic signature workflows into their applications and websites. The product supports embedded signing and requesting, reusable templates, custom signer fields, branded signing flows, audit trails, and tamper-proof document delivery. The Dropbox Sign API is documented with an official OpenAPI specification and authenticated via HTTP Basic Auth with an API key or OAuth 2.0 Bearer tokens.
graphqls:
- description: This conceptual GraphQL schema represents the Dropbox Sign (formerly HelloSign) eSignature REST API v3. Dropbox Sign provides legally binding electronic signature workflows including embedded signing,
  name: Dropbox Sign (HelloSign) GraphQL Schema
  slug: dropbox-sign-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dropbox-sign.png
layout: provider
modified: '2026-05-30'
name: Dropbox Sign
nav: Providers
network: true
overview: 'Dropbox Sign publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Events and Callbacks API, Account API, API App API, and 3 more. Tagged areas include eSignature, Electronic Signature, Document Signing, Workflow Automation, and Documents.


  The Dropbox Sign catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Dropbox Sign''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 44
rules:
- name: Dropbox Sign API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: dropbox-sign-asyncapi-spectral-rules
scopes:
- name: Dropbox Sign Scopes
  scope_count: 5
  slug: dropbox-sign-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 35.4
  delta: -2.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 65.7
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dropbox-sign/refs/heads/main/screenshots/dropbox-sign-2026-06-20T180245.png
security:
- kind: authentication
  name: Dropbox Sign Authentication
  slug: dropbox-sign-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Dropbox Sign Domain Security
  slug: dropbox-sign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dropbox Sign Trust Center
  slug: dropbox-sign-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CSA STAR
slug: dropbox-sign
tags:
- eSignature
- Electronic Signature
- Document Signing
- Workflow Automation
- Documents
website: https://sign.dropbox.com
---
