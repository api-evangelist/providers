---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Certifaction Agentic Access
  operation_count: 22
  slug: certifaction-agentic-access
  summary_line: 22 operations · 14 acting
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
artifact_total: 23
asyncapis:
- description: ''
  name: Certifaction Webhooks
  slug: certifaction-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/certifaction/plans/certifaction-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/certifaction-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/certifaction/capabilities/certifaction-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/certifaction-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/certifaction/overlays/certifaction-admin-api-overlay.yaml
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
  href: https://artifacts.apis.io/certifaction/authentication/certifaction-authentication.yml
  title: ''
  type: Authentication
  url: authentication/certifaction-authentication.yml
- group: docs
  href: https://artifacts.apis.io/certifaction/openapi/_original/certifaction-local-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/certifaction-local-api-openapi.yml
- group: build
  href: https://artifacts.apis.io/certifaction/packages/certifaction-packages.yml
  title: ''
  type: Packages
  url: packages/certifaction-packages.yml
- group: build
  href: https://artifacts.apis.io/certifaction/packages/certifaction-packages.yml
  title: ''
  type: SDKs
  url: packages/certifaction-packages.yml
- group: build
  href: https://artifacts.apis.io/certifaction/cli/certifaction-cli.yml
  title: ''
  type: CLI
  url: cli/certifaction-cli.yml
- group: design
  href: https://artifacts.apis.io/certifaction/components/certifaction-components.yml
  title: ''
  type: Components
  url: components/certifaction-components.yml
- group: agent
  href: https://artifacts.apis.io/certifaction/mcp/certifaction-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/certifaction-mcp.yml
- group: agent
  href: https://artifacts.apis.io/certifaction/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/certifaction/llms/certifaction-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/certifaction-llms.txt
- group: design
  href: https://artifacts.apis.io/certifaction/asyncapi/certifaction-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/certifaction-webhooks.yml
- group: design
  href: https://artifacts.apis.io/certifaction/conventions/certifaction-conventions.yml
  title: ''
  type: Conventions
  url: conventions/certifaction-conventions.yml
- group: design
  href: https://artifacts.apis.io/certifaction/errors/certifaction-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/certifaction-problem-types.yml
- group: design
  href: https://artifacts.apis.io/certifaction/lifecycle/certifaction-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/certifaction-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/certifaction/changelog/certifaction-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/certifaction-changelog.yml
- group: design
  href: https://artifacts.apis.io/certifaction/data-model/certifaction-data-model.yml
  title: ''
  type: DataModel
  url: data-model/certifaction-data-model.yml
- group: design
  href: https://artifacts.apis.io/certifaction/conformance/certifaction-conformance.yml
  title: ''
  type: Conformance
  url: conformance/certifaction-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://certifaction.com/security-esigning-and-data/
- group: auth
  href: https://artifacts.apis.io/certifaction/security/certifaction-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/certifaction-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/certifaction/security/certifaction-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certifaction-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/certifaction/agentic-access/certifaction-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/certifaction-agentic-access.yml
created: '2026-07-17'
description: 'Certifaction is a privacy-first digital signature platform built around a Zero Document Knowledge model: documents are hashed and end-to-end encrypted on the client so they can be signed and verified without Certifaction ever seeing their content. It offers Simple, Advanced, and Qualified Electronic Signatures (SES/AES/QES) compliant with eIDAS, ZertES, UETA and ESIGN, delivered through a client-hosted CLI and Local API plus an Admin API for organization, user, role and team-space management, with EU / Switzerland / on-premises data residency and ISO/IEC 27001:2022 certification.'
finops:
- has_sources: true
  method: derived
  name: Certifaction Finops
  primary_unit: ''
  service_category: ''
  slug: certifaction-finops
  template: true
image: https://developers.certifaction.com/themes/certifaction/logo.svg
layout: provider
modified: '2026-07-18'
name: Certifaction
nav: Providers
network: true
overview: 'Certifaction publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Documents API, Organization API, and 3 more. Tagged areas include Company, Ai Enterprise Software, E-Signature, Digital Signature, and Qualified Electronic Signature.


  The Certifaction catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Certifaction''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 28 more developer resources.'
plans:
- name: Certifaction Plans Pricing
  plan_count: 1
  slug: certifaction-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Certifaction API Rules
  rule_count: 46
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 4
  slug: certifaction-rules
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    contract_governance: 31.8
    contract_quality: 51.1
    developer_ergonomics: 68.5
    discoverability: 73.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 57.5
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
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/certifaction/certifaction-2026-07-25T205000.png
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
skill_count: 3
skills:
- name: Request signatures and track them with Certifaction
  slug: certifaction-request-signature
- name: Sign a document with Certifaction
  slug: certifaction-sign-document
- name: Verify and retrieve a signed document with Certifaction
  slug: certifaction-verify-download
slug: certifaction
tags:
- Company
- Ai Enterprise Software
- E-Signature
- Digital Signature
- Qualified Electronic Signature
- eIDAS
- Privacy
- Compliance
- Identity Verification
- Switzerland
website: https://certifaction.com
---
