---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Documenso Agentic Access
  operation_count: 18
  slug: documenso-agentic-access
  summary_line: 18 operations · 13 acting
api_count: 5
apis:
- description: 'Outbound webhook events covering the full document lifecycle - created, sent, opened, signed, completed, rejected, cancelled - plus template events. Payloads are verified with a shared secret sent in '
  name: Documenso Webhooks
  slug: webhooks
- description: Create, upload, send, retrieve, download, and delete documents.
  name: Documenso Documents API
  slug: documenso-documents-api
- description: Add and configure signature and form fields on a document.
  name: Documenso Fields API
  slug: documenso-fields-api
- description: Manage the recipients (signers, approvers, viewers) of a document.
  name: Documenso Recipients API
  slug: documenso-recipients-api
- description: Manage reusable templates and generate documents from them.
  name: Documenso Templates API
  slug: documenso-templates-api
artifact_total: 13
collections:
- collection_type: open
  name: Documenso Public API
  slug: open-documenso
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/documenso-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/documenso-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/documenso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/documenso-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/documenso
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/documenso
- group: company
  title: ''
  type: Website
  url: https://documenso.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.documenso.com
- group: commercial
  title: ''
  type: Plans
  url: plans/documenso-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/documenso-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/documenso-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://documenso.com/blog
created: '2026-06-20'
description: Documenso is the open-source DocuSign alternative, a developer-friendly e-signature platform for sending, signing, and managing documents. Its public REST API lets you create and upload documents, add recipients and signature fields, send documents for signing, work with reusable templates, and receive webhook events across the document lifecycle. Self-hostable under AGPL.
finops:
- name: Documenso Finops
  service_category: Productivity and Business Applications
  slug: documenso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/documenso.png
layout: provider
modified: '2026-06-20'
name: Documenso
nav: Providers
network: true
overview: 'Documenso publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Fields API, Recipients API, and 1 more. Tagged areas include E-Signature, Documents, Signing, Open Source, and DocuSign Alternative.


  Documenso''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Documenso Plans Pricing
  plan_count: 6
  slug: documenso-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Documenso Rate Limits
  slug: documenso-rate-limits
score:
  band: thin
  composite: 37.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/documenso/refs/heads/main/screenshots/documenso-2026-06-20T180120.png
security:
- kind: authentication
  name: Documenso Authentication
  slug: documenso-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Documenso Domain Security
  slug: documenso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Documenso Vulnerability Disclosure
  slug: documenso-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: documenso
tags:
- E-Signature
- Documents
- Signing
- Open Source
- DocuSign Alternative
website: https://documenso.com
---
