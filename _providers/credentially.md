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
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Credentially Agentic Access
  operation_count: 81
  slug: credentially-agentic-access
  summary_line: 81 operations · 44 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: Profile's compliance packages management proxy endpoints
  name: Credentially Compliance-packages API
  slug: credentially-compliance-packages-api
- description: DBS check lookup and refresh endpoints
  name: Credentially DBS API
  slug: credentially-dbs-api
- description: Dictionary lookup endpoints for custom profile field values
  name: Credentially Dictionary API
  slug: credentially-dictionary-api
- description: Automated document data extraction and validation endpoints
  name: Credentially Document Auto-fill API
  slug: credentially-document-auto-fill-api
- description: Document management proxy endpoints
  name: Credentially Documents API
  slug: credentially-documents-api
- description: Placement data scoped to a specific employee.
  name: Credentially Employee Placements API
  slug: credentially-employee-placements-api
- description: Org-scoped jurisdictions a placement can reference (read-only).
  name: Credentially Jurisdictions API
  slug: credentially-jurisdictions-api
- description: Org-scoped classifications for placement locations (read-only).
  name: Credentially Location Types API
  slug: credentially-location-types-api
- description: Facilities / sites where placements occur. Each belongs to one jurisdiction.
  name: Credentially Locations API
  slug: credentially-locations-api
- description: API for fetching metadata
  name: Credentially Meta API
  slug: credentially-meta-api
- description: Organisation group member management endpoints
  name: Credentially Organisation Groups API
  slug: credentially-organisation-groups-api
- description: Notes attached to a placement — free-text annotations.
  name: Credentially Placement Notes API
  slug: credentially-placement-notes-api
- description: Org-scoped roles a placement can reference (e.g. Band 6 RN).
  name: Credentially Placement Roles API
  slug: credentially-placement-roles-api
- description: Placement lifecycle proxy endpoints — assignment of an employee to a location + role within the organisation.
  name: Credentially Placements API
  slug: credentially-placements-api
- description: Organisation groups proxy endpoints
  name: Credentially Profile Groups API
  slug: credentially-profile-groups-api
- description: Profile management proxy endpoints
  name: Credentially Profiles API
  slug: credentially-profiles-api
- description: Profile reference status lookup endpoints
  name: Credentially References API
  slug: credentially-references-api
- description: Right to work status lookup endpoints
  name: Credentially Right to Work API
  slug: credentially-right-to-work-api
- description: Placements scoped to a Kanban stage — board column reads + bulk-move.
  name: Credentially Stage Placements API
  slug: credentially-stage-placements-api
- description: Kanban placement stages — per-org column definitions for the placements board.
  name: Credentially Stages API
  slug: credentially-stages-api
- description: API for managing webhook callback subscriptions
  name: Credentially Subscriptions API
  slug: credentially-subscriptions-api
artifact_total: 27
asyncapis:
- description: ''
  name: Credentially Webhooks
  slug: credentially-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://credentially.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://credentially.readme.io/reference/getting-started-with-your-api
- group: docs
  title: ''
  type: Documentation
  url: https://credentially.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://credentially.readme.io/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://credentially.readme.io/reference/getting-started-with-your-api
- group: operate
  title: ''
  type: Support
  url: https://credentially.my.site.com/s/KnowledgeHub
- group: company
  title: ''
  type: Blog
  url: https://www.credentially.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Credentially
- group: commercial
  title: ''
  type: Pricing
  url: https://www.credentially.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.credentially.io/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://app.credentially.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credentially.io/terms-policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credentially.io/terms-policies/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.credentially.io/
- group: auth
  title: ''
  type: Compliance
  url: https://www.credentially.io/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/credentially-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credentially-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/credentially-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/credentially-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/credentially-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credentially-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/credentially-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/credentially-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/credentially-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/credentially-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/credentially-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/credentially-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/credentially-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Credentially is a UK-founded, healthcare-only onboarding and compliance automation platform used by NHS trusts, private providers, urgent care and clinical staffing agencies in the UK and US. It brings pre-employment checks, DBS and right-to-work validation, primary source verification, credentialing and continuous compliance monitoring onto one platform, cutting the platform-managed steps of onboarding clinical staff from an industry average of around 60 days to as little as 5. The Credentially Public API (OpenAPI 3.1) exposes profiles, placements, documents with OCR auto-fill, DBS checks, references, right-to-work status and compliance packages, with a companion Webhook API for state-change events.
image: https://cdn.prod.website-files.com/67f6367b305814423f88598b/6839b1c0c6313ba54fe9856d_5e3042f6ca409a0e92b09c9e_1231.png
layout: provider
mcp_servers:
- description: ''
  name: credentially-mcp.yml
  slug: credentially-mcpyml
modified: '2026-07-18'
name: Credentially
nav: Providers
network: true
overview: 'Credentially publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Compliance-packages API, DBS API, Dictionary API, and 18 more. Tagged areas include Healthcare, Credentialing, Compliance, Onboarding, and Workforce.


  The Credentially catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Credentially''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 55.7
  delta: -3.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: first-party
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
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/credentially/refs/heads/main/screenshots/credentially-2026-07-25T210710.png
security:
- kind: authentication
  name: Credentially Authentication
  slug: credentially-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Credentially Domain Security
  slug: credentially-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Credentially Trust Center
  slug: credentially-trust-center
  summary_line: ISO/IEC 27001:2022, Cyber Essentials Plus, NHS Data Security and Protection Toolkit (Standards Exceeded), NHS DTAC, GDPR, ICO registered
slug: credentially
tags:
- Healthcare
- Credentialing
- Compliance
- Onboarding
- Workforce
- Identity Verification
- Background Checks
- NHS
- Company
website: https://credentially.io/
---
