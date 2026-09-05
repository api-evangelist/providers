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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Certifaction Agentic Access
  operation_count: 21
  slug: certifaction-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 2
apis:
- baseURL: https://api.certifaction.io
  baseurl_source: declared
  description: Access your user account data
  name: Certifaction Account API
  slug: certifaction-account-api
- baseURL: https://api.certifaction.io
  baseurl_source: declared
  description: Download your documents or remove {{ .ProductName }}'s access to them
  name: Certifaction Documents API
  slug: certifaction-documents-api
- baseURL: https://api.certifaction.io
  baseurl_source: declared
  description: Manage your organization, users, and roles.
  name: Certifaction Organization API
  slug: certifaction-organization-api
- baseURL: https://api.certifaction.io
  baseurl_source: declared
  description: Check the server's status
  name: Certifaction Server API
  slug: certifaction-server-api
- baseURL: https://api.certifaction.io
  baseurl_source: declared
  description: Sign files and request signatures
  name: Certifaction Signing API
  slug: certifaction-signing-api
- baseURL: https://api.certifaction.io
  baseurl_source: declared
  description: Manage teamspaces and their members.
  name: Certifaction Teamspace API
  slug: certifaction-teamspace-api
artifact_total: 18
asyncapis:
- description: ''
  name: Certifaction Webhooks
  slug: certifaction-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: '{{ .ProductName }} Admin Account API'
  slug: open-certifaction-account-api
- collection_type: open
  name: '{{ .ProductName }} Admin Account Documents API'
  slug: open-certifaction-documents-api
- collection_type: open
  name: '{{ .ProductName }} Admin Account Organization API'
  slug: open-certifaction-organization-api
- collection_type: open
  name: '{{ .ProductName }} Admin Account Server API'
  slug: open-certifaction-server-api
- collection_type: open
  name: '{{ .ProductName }} Admin Account Signing API'
  slug: open-certifaction-signing-api
- collection_type: open
  name: '{{ .ProductName }} Admin Account Teamspace API'
  slug: open-certifaction-teamspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/certifaction-admin-api-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: Certifaction
nav: Providers
network: true
overview: 'Certifaction publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Documents API, Organization API, and 3 more. Tagged areas include Company, Ai Enterprise Software, Electronic Signature, Digital Signature, and Document Signing.


  The Certifaction catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Certifaction''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 26 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 53.7
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 51.1
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
