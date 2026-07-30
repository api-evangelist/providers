---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Formstack Agentic Access
  operation_count: 39
  slug: formstack-agentic-access
  summary_line: 39 operations · 23 acting
api_count: 17
apis:
- description: REST API for creating, reading, updating, and deleting forms in a Formstack account, including form configuration, styling, and access rules.
  name: Formstack Forms API
  slug: forms
- description: Read, create, update, and delete form submissions; supports filtering by date, search, and field values. Returns submitted field data and metadata.
  name: Formstack Submissions API
  slug: submissions
- description: Programmatically manage form fields - text, select, file upload, signature, payment, calculation, and others - including ordering, validation, and conditional logic.
  name: Formstack Fields API
  slug: fields
- description: Configure webhook subscriptions to receive submission events at a customer-provided URL, with retry semantics for failed deliveries.
  name: Formstack Webhooks API
  slug: webhooks
- description: Manage folder organization for forms within a Formstack account.
  name: Formstack Folders API
  slug: folders
- description: Programmatic interface to Formstack Documents (formerly WebMerge) for generating PDFs, Word docs, and other templated documents from data payloads.
  name: Formstack Documents API
  slug: documents
- description: Electronic signature API for sending documents for signature, tracking status, and retrieving signed copies. Part of the Formstack Suite.
  name: Formstack Sign API
  slug: sign
- description: Workflow automation surface for routing submissions, documents, and approvals across multi-step business processes.
  name: Formstack Workflows API
  slug: workflows
- description: OAuth 2.0 authorization server used to authenticate API clients and issue access tokens for the Formstack REST API.
  name: Formstack OAuth 2.0
  slug: oauth2
- description: The Confirmations API from Formstack — 2 operation(s) for confirmations.
  name: Formstack Confirmations API
  slug: formstack-confirmations-api
- description: The Fields API from Formstack — 2 operation(s) for fields.
  name: Formstack Fields API
  slug: formstack-fields-api
- description: The Folders API from Formstack — 2 operation(s) for folders.
  name: Formstack Folders API
  slug: formstack-folders-api
- description: The Forms API from Formstack — 5 operation(s) for forms.
  name: Formstack Forms API
  slug: formstack-forms-api
- description: The Notifications API from Formstack — 2 operation(s) for notifications.
  name: Formstack Notifications API
  slug: formstack-notifications-api
- description: The Subaccounts API from Formstack — 1 operation(s) for subaccounts.
  name: Formstack Subaccounts API
  slug: formstack-subaccounts-api
- description: The Submissions API from Formstack — 2 operation(s) for submissions.
  name: Formstack Submissions API
  slug: formstack-submissions-api
- description: The Webhooks API from Formstack — 2 operation(s) for webhooks.
  name: Formstack Webhooks API
  slug: formstack-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: Formstack Webhooks
  slug: open-formstack-asyncapi
- collection_type: open
  name: Formstack API
  slug: open-formstack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formstack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/formstack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/formstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formstack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/formstack-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.formstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.formstack.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.formstack.com/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.formstack.com/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formstack
- group: build
  title: ''
  type: GitHub
  url: https://github.com/formstack
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Formstack
- group: company
  title: ''
  type: Blog
  url: https://www.formstack.com/blog/rss.xml
created: '2026-05-23'
description: Formstack is a no-code workplace productivity platform spanning online forms, document generation, electronic signature, and workflow automation. The developer portal at developers.formstack.com exposes a REST API (v2025.0) for forms, submissions, fields, webhooks, folders, and partial submissions, plus product-specific surfaces for Formstack Documents, Formstack Sign, and Formstack Workflows. Authentication uses OAuth 2.0. Machine-readable indexes and OpenAPI artifacts are surfaced at developers.formstack.com/llms.txt.
finops:
- name: Formstack Finops
  service_category: API
  slug: formstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formstack.png
layout: provider
modified: '2026-05-30'
name: Formstack
nav: Providers
network: true
overview: 'Formstack publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Confirmations API, Fields API, and 6 more. Tagged areas include Forms, Documents, eSignature, Workflow Automation, and No-Code.


  Formstack''s developer surface includes authentication, documentation, changelog, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Formstack Plans Pricing
  plan_count: 1
  slug: formstack-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 2
  name: Formstack Rate Limits
  slug: formstack-rate-limits
scopes:
- name: Formstack Scopes
  scope_count: 4
  slug: formstack-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 40.4
  delta: -2.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 63.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 88.9
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formstack/refs/heads/main/screenshots/formstack-2026-06-20T181438.png
security:
- kind: authentication
  name: Formstack Authentication
  slug: formstack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Formstack Domain Security
  slug: formstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Formstack Vulnerability Disclosure
  slug: formstack-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Formstack Trust Center
  slug: formstack-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: formstack
tags:
- Forms
- Documents
- eSignature
- Workflow Automation
- No-Code
- OAuth2
website: https://www.formstack.com/
---
