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
    agentic_access: false
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
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
api_count: 21
apis:
- description: The Auth API from TrustLayer — 1 operation(s) for auth.
  name: TrustLayer Auth API
  slug: trustlayer-auth-api
- description: The branding API from TrustLayer — 2 operation(s) for branding.
  name: TrustLayer branding API
  slug: trustlayer-branding-api
- description: The compliance-profiles API from TrustLayer — 8 operation(s) for compliance-profiles.
  name: TrustLayer compliance-profiles API
  slug: trustlayer-compliance-profiles-api
- description: The contacts API from TrustLayer — 4 operation(s) for contacts.
  name: TrustLayer contacts API
  slug: trustlayer-contacts-api
- description: The Context Objects API from TrustLayer — 2 operation(s) for context objects.
  name: TrustLayer Context Objects API
  slug: trustlayer-context-objects-api
- description: The Context Records API from TrustLayer — 7 operation(s) for context records.
  name: TrustLayer Context Records API
  slug: trustlayer-context-records-api
- description: The custom-fields API from TrustLayer — 4 operation(s) for custom-fields.
  name: TrustLayer custom-fields API
  slug: trustlayer-custom-fields-api
- description: The Document Types API from TrustLayer — 2 operation(s) for document types.
  name: TrustLayer Document Types API
  slug: trustlayer-document-types-api
- description: The documents API from TrustLayer — 15 operation(s) for documents.
  name: TrustLayer documents API
  slug: trustlayer-documents-api
- description: The Parties API from TrustLayer — 20 operation(s) for parties.
  name: TrustLayer Parties API
  slug: trustlayer-parties-api
- description: The party-types API from TrustLayer — 1 operation(s) for party-types.
  name: TrustLayer party-types API
  slug: trustlayer-party-types-api
- description: The Policies API from TrustLayer — 11 operation(s) for policies.
  name: TrustLayer Policies API
  slug: trustlayer-policies-api
- description: The Primary Objects API from TrustLayer — 2 operation(s) for primary objects.
  name: TrustLayer Primary Objects API
  slug: trustlayer-primary-objects-api
- description: The Primary Records API from TrustLayer — 12 operation(s) for primary records.
  name: TrustLayer Primary Records API
  slug: trustlayer-primary-records-api
- description: The Projects API from TrustLayer — 9 operation(s) for projects.
  name: TrustLayer Projects API
  slug: trustlayer-projects-api
- description: The reports API from TrustLayer — 2 operation(s) for reports.
  name: TrustLayer reports API
  slug: trustlayer-reports-api
- description: The Request Records API from TrustLayer — 7 operation(s) for request records.
  name: TrustLayer Request Records API
  slug: trustlayer-request-records-api
- description: The Requirements API from TrustLayer — 2 operation(s) for requirements.
  name: TrustLayer Requirements API
  slug: trustlayer-requirements-api
- description: The tags API from TrustLayer — 4 operation(s) for tags.
  name: TrustLayer tags API
  slug: trustlayer-tags-api
- description: The Views API from TrustLayer — 2 operation(s) for views.
  name: TrustLayer Views API
  slug: trustlayer-views-api
- description: The Workspaces API from TrustLayer — 1 operation(s) for workspaces.
  name: TrustLayer Workspaces API
  slug: trustlayer-workspaces-api
artifact_total: 26
asyncapis:
- description: ''
  name: Trustlayer Webhooks
  slug: trustlayer-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.trustlayer.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trustlayer.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.trustlayer.io/pages/developers
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustlayer-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trustlayer-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trustlayer-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trustlayer-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trustlayer-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trustlayer-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trustlayer-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trustlayer-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trustlayer-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trustlayer-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trustlayer-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trustlayer.io
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.trustlayer.io/v1/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustlayer-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.trustlayer.io/
- group: company
  title: ''
  type: Blog
  url: https://trustlayer.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://trustlayer.io/pages/starter
- group: start
  title: ''
  type: Login
  url: https://app.trustlayer.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trustlayer.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trustlayer.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://trustlayer.io
created: '2026-07-17'
description: 'TrustLayer is a vendor risk management and certificate of insurance (COI) tracking platform that automates the collection, verification, and ongoing monitoring of compliance documents. It uses AI-powered OCR field extraction, real-time carrier connections, and NIPR license verification to process COIs, W9s, and business licenses across a network of 500,000+ companies. The TrustLayer Platform API lets teams programmatically manage parties (vendors), contacts, projects, documents, and compliance profiles, request documents, and receive real-time webhook notifications as compliance status changes. Backed by Craft Ventures. Sector: insurtech / fintech.'
image: https://developers.trustlayer.io/landing/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: trustlayer-mcp.yml
  slug: trustlayer-mcpyml
modified: '2026-07-21'
name: TrustLayer
nav: Providers
network: true
overview: 'TrustLayer publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Auth API, branding API, compliance-profiles API, and 18 more. Tagged areas include Company, Fintech, Insurtech, Insurance, and Risk Management.


  The TrustLayer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TrustLayer''s developer surface includes documentation, API reference, authentication, sandbox, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 46.8
  delta: -4.4
  facets:
    commercial_clarity: 42.1
    contract_quality: 57.8
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 51.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Trustlayer Authentication
  slug: trustlayer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Trustlayer Domain Security
  slug: trustlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trustlayer Trust Center
  slug: trustlayer-trust-center
  summary_line: trust center published
slug: trustlayer
tags:
- Company
- Fintech
- Insurtech
- Insurance
- Risk Management
- Compliance
- Certificate of Insurance
- Vendor Management
website: https://trustlayer.io
---
