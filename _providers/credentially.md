---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Credentially Agentic Access
  operation_count: 81
  slug: credentially-agentic-access
  summary_line: 81 operations · 44 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Profile's compliance packages management proxy endpoints
  name: Credentially Compliance-packages API
  slug: credentially-compliance-packages-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: DBS check lookup and refresh endpoints
  name: Credentially DBS API
  slug: credentially-dbs-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Dictionary lookup endpoints for custom profile field values
  name: Credentially Dictionary API
  slug: credentially-dictionary-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Automated document data extraction and validation endpoints
  name: Credentially Document Auto-fill API
  slug: credentially-document-auto-fill-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Document management proxy endpoints
  name: Credentially Documents API
  slug: credentially-documents-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Placement data scoped to a specific employee.
  name: Credentially Employee Placements API
  slug: credentially-employee-placements-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Org-scoped jurisdictions a placement can reference (read-only).
  name: Credentially Jurisdictions API
  slug: credentially-jurisdictions-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Org-scoped classifications for placement locations (read-only).
  name: Credentially Location Types API
  slug: credentially-location-types-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Facilities / sites where placements occur. Each belongs to one jurisdiction.
  name: Credentially Locations API
  slug: credentially-locations-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: API for fetching metadata
  name: Credentially Meta API
  slug: credentially-meta-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Organisation group member management endpoints
  name: Credentially Organisation Groups API
  slug: credentially-organisation-groups-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Notes attached to a placement — free-text annotations.
  name: Credentially Placement Notes API
  slug: credentially-placement-notes-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Org-scoped roles a placement can reference (e.g. Band 6 RN).
  name: Credentially Placement Roles API
  slug: credentially-placement-roles-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Placement lifecycle proxy endpoints — assignment of an employee to a location + role within the organisation.
  name: Credentially Placements API
  slug: credentially-placements-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Organisation groups proxy endpoints
  name: Credentially Profile Groups API
  slug: credentially-profile-groups-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Profile management proxy endpoints
  name: Credentially Profiles API
  slug: credentially-profiles-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Profile reference status lookup endpoints
  name: Credentially References API
  slug: credentially-references-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Right to work status lookup endpoints
  name: Credentially Right to Work API
  slug: credentially-right-to-work-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Placements scoped to a Kanban stage — board column reads + bulk-move.
  name: Credentially Stage Placements API
  slug: credentially-stage-placements-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: Kanban placement stages — per-org column definitions for the placements board.
  name: Credentially Stages API
  slug: credentially-stages-api
- baseURL: https://app.credentially.io/gateway
  baseurl_source: declared
  description: API for managing webhook callback subscriptions
  name: Credentially Subscriptions API
  slug: credentially-subscriptions-api
artifact_total: 48
asyncapis:
- description: ''
  name: Credentially Webhooks
  slug: credentially-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Credentially Public Compliance-packages API
  slug: open-credentially-compliance-packages-api
- collection_type: open
  name: Credentially Public Compliance-packages DBS API
  slug: open-credentially-dbs-api
- collection_type: open
  name: Credentially Public Compliance-packages Dictionary API
  slug: open-credentially-dictionary-api
- collection_type: open
  name: Credentially Public Compliance-packages Document Auto-fill API
  slug: open-credentially-document-auto-fill-api
- collection_type: open
  name: Credentially Public Compliance-packages Documents API
  slug: open-credentially-documents-api
- collection_type: open
  name: Credentially Public Compliance-packages Employee Placements API
  slug: open-credentially-employee-placements-api
- collection_type: open
  name: Credentially Public Compliance-packages Jurisdictions API
  slug: open-credentially-jurisdictions-api
- collection_type: open
  name: Credentially Public Compliance-packages Location Types API
  slug: open-credentially-location-types-api
- collection_type: open
  name: Credentially Public Compliance-packages Locations API
  slug: open-credentially-locations-api
- collection_type: open
  name: Credentially Public Compliance-packages Meta API
  slug: open-credentially-meta-api
- collection_type: open
  name: Credentially Public Compliance-packages Organisation Groups API
  slug: open-credentially-organisation-groups-api
- collection_type: open
  name: Credentially Public Compliance-packages Placement Notes API
  slug: open-credentially-placement-notes-api
- collection_type: open
  name: Credentially Public Compliance-packages Placement Roles API
  slug: open-credentially-placement-roles-api
- collection_type: open
  name: Credentially Public Compliance-packages Placements API
  slug: open-credentially-placements-api
- collection_type: open
  name: Credentially Public Compliance-packages Profile Groups API
  slug: open-credentially-profile-groups-api
- collection_type: open
  name: Credentially Public Compliance-packages Profiles API
  slug: open-credentially-profiles-api
- collection_type: open
  name: Credentially Public Compliance-packages References API
  slug: open-credentially-references-api
- collection_type: open
  name: Credentially Public Compliance-packages Right to Work API
  slug: open-credentially-right-to-work-api
- collection_type: open
  name: Credentially Public Compliance-packages Stage Placements API
  slug: open-credentially-stage-placements-api
- collection_type: open
  name: Credentially Public Compliance-packages Stages API
  slug: open-credentially-stages-api
- collection_type: open
  name: Credentially Public Compliance-packages Subscriptions API
  slug: open-credentially-subscriptions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/credentially-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/credentially-gateway-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: Credentially
nav: Providers
network: true
overview: 'Credentially publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Compliance-packages API, DBS API, Dictionary API, and 18 more. Tagged areas include Healthcare, Credentialing, Compliance, Onboarding, and Workforce.


  The Credentially catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Credentially''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 20
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 67.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 55.4
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
