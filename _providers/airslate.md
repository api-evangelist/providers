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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Airslate Agentic Access
  operation_count: 45
  slug: airslate-agentic-access
  summary_line: 45 operations · 32 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'No-code document workflow automation platform (recently rebranded as altaFlow). Supports building workflows that combine forms, contracts, bots, and integrations across CRM and ERP systems. Developer '
  name: airSlate WorkFlow (altaFlow)
  slug: workflow
- description: REST API for signNow, airSlate's electronic signature product. Covers documents, signatures, templates, users, groups, fields, and webhooks. Supports OAuth 2.0 with production base api.signnow.com and
  name: signNow API
  slug: signnow
- description: REST API for pdfFiller, covering document upload and conversion, form filling, templates, and e-signature flows. Used to embed PDF editing and form workflows into third-party applications.
  name: pdfFiller API
  slug: pdffiller
- description: Cloud PDF editor that integrates with Google Workspace. Provides editing, signing, and sharing of PDFs from inside Google apps. Programmatic access is primarily via Google Workspace integration surfac
  name: DocHub
  slug: dochub
- description: Online catalog of 85,000+ state-specific legal forms. Consumer and SMB product; no public developer API.
  name: US Legal Forms
  slug: us-legal-forms
- description: Landing page builder and personalization platform. Offers REST endpoints for account integration via the Instapage developer surface.
  name: Instapage
  slug: instapage
- description: AI-powered automation platform for end-to-end marketing operations. Positioned as a vertical AI product rather than a developer API.
  name: airSlate Marketing Intelligence Platform
  slug: marketing-intelligence
- description: The Document Fields API from airSlate — 3 operation(s) for document fields.
  name: airSlate Document Fields API
  slug: airslate-document-fields-api
- description: The Document Groups API from airSlate — 4 operation(s) for document groups.
  name: airSlate Document Groups API
  slug: airslate-document-groups-api
- description: The Documents API from airSlate — 7 operation(s) for documents.
  name: airSlate Documents API
  slug: airslate-documents-api
- description: The Embedded API from airSlate — 3 operation(s) for embedded.
  name: airSlate Embedded API
  slug: airslate-embedded-api
- description: The Folders API from airSlate — 2 operation(s) for folders.
  name: airSlate Folders API
  slug: airslate-folders-api
- description: The Invites API from airSlate — 5 operation(s) for invites.
  name: airSlate Invites API
  slug: airslate-invites-api
- description: The OAuth API from airSlate — 1 operation(s) for oauth.
  name: airSlate OAuth API
  slug: airslate-oauth-api
- description: The Smart Fields API from airSlate — 1 operation(s) for smart fields.
  name: airSlate Smart Fields API
  slug: airslate-smart-fields-api
- description: The Templates API from airSlate — 4 operation(s) for templates.
  name: airSlate Templates API
  slug: airslate-templates-api
- description: The Users API from airSlate — 3 operation(s) for users.
  name: airSlate Users API
  slug: airslate-users-api
- description: The Webhooks API from airSlate — 2 operation(s) for webhooks.
  name: airSlate Webhooks API
  slug: airslate-webhooks-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: airSlate signNow REST Document Fields API
  slug: open-airslate-document-fields-api
- collection_type: open
  name: airSlate signNow REST Document Fields Document Groups API
  slug: open-airslate-document-groups-api
- collection_type: open
  name: airSlate signNow REST Document Fields Documents API
  slug: open-airslate-documents-api
- collection_type: open
  name: airSlate signNow REST Document Fields Embedded API
  slug: open-airslate-embedded-api
- collection_type: open
  name: airSlate signNow REST Document Fields Folders API
  slug: open-airslate-folders-api
- collection_type: open
  name: airSlate signNow REST Document Fields Invites API
  slug: open-airslate-invites-api
- collection_type: open
  name: airSlate signNow REST Document Fields OAuth API
  slug: open-airslate-oauth-api
- collection_type: open
  name: airSlate signNow REST Document Fields Smart Fields API
  slug: open-airslate-smart-fields-api
- collection_type: open
  name: airSlate signNow REST Document Fields Templates API
  slug: open-airslate-templates-api
- collection_type: open
  name: airSlate signNow REST Document Fields Users API
  slug: open-airslate-users-api
- collection_type: open
  name: airSlate signNow REST Document Fields Webhooks API
  slug: open-airslate-webhooks-api
- collection_type: open
  name: airSlate signNow REST API
  slug: open-airslate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airslate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airslate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airslate-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.airslate.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.airslate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signnow.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airslate
- group: build
  title: ''
  type: GitHub
  url: https://github.com/signnow
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/airSlate_
created: '2026-05-23'
description: airSlate is a document workflow automation holding company whose product family covers no-code workflow automation (altaFlow, formerly airSlate WorkFlow), electronic signature (signNow), PDF editing and form filling (pdfFiller and DocHub), legal forms (US Legal Forms), landing pages (Instapage), and an AI-powered marketing intelligence platform. Developer APIs are exposed primarily through the signNow and pdfFiller product lines; WorkFlow / altaFlow surfaces automation bots and integrations rather than a broad public REST API.
finops:
- name: Airslate Finops
  service_category: API
  slug: airslate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airslate.png
layout: provider
modified: '2026-05-23'
name: airSlate
nav: Providers
network: true
overview: 'airSlate publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Document Fields API, Document Groups API, Documents API, and 8 more. Tagged areas include Document Automation, E-Signature, Workflows, PDF, and No-Code.


  airSlate''s developer surface includes authentication, engineering blog, documentation, GitHub presence, and 5 more developer resources.'
plans:
- name: Airslate Plans Pricing
  plan_count: 1
  slug: airslate-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Airslate Rate Limits
  slug: airslate-rate-limits
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airslate/refs/heads/main/screenshots/airslate-2026-06-20T171429.png
security:
- kind: authentication
  name: Airslate Authentication
  slug: airslate-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Airslate Domain Security
  slug: airslate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airslate
tags:
- Document Automation
- E-Signature
- Workflows
- PDF
- No-Code
- Artificial Intelligence
website: https://www.airslate.com/
---
