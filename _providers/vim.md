---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Vim Agentic Access
  operation_count: 10
  slug: vim-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 2
apis:
- description: The Vim Canvas developer platform and VimOS.js JavaScript SDK for embedding applications at the point of care. Reads EHR state (Patient, Encounter, Orders, Referral, Claim, plus problem/medication/all
  name: Vim Canvas SDK (VimOS.js)
  slug: vim-canvas-sdk
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: Obtaining a Bearer service token to make API requests
  name: Vim Access Token Retrieval API
  slug: vim-access-token-retrieval-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: The Applications API from Vim — 2 operation(s) for applications.
  name: Vim Applications API
  slug: vim-applications-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: The Appointments API from Vim — 1 operation(s) for appointments.
  name: Vim Appointments API
  slug: vim-appointments-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: The Authentication API from Vim — 1 operation(s) for authentication.
  name: Vim Authentication API
  slug: vim-authentication-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: The Chart Retrieval API from Vim — 1 operation(s) for chart retrieval.
  name: Vim Chart Retrieval API
  slug: vim-chart-retrieval-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: Retrieving patient care insights such as diagnosis gaps and care insights
  name: Vim Get Patient Care Insights API
  slug: vim-get-patient-care-insights-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: The Invitations API from Vim — 1 operation(s) for invitations.
  name: Vim Invitations API
  slug: vim-invitations-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: Sending feedback about the care insights
  name: Vim Patient Care Insights Feedback API
  slug: vim-patient-care-insights-feedback-api
- baseURL: https://api.getvim.com/v1
  baseurl_source: declared
  description: Identify the patient based on personal information
  name: Vim Patient Identification API
  slug: vim-patient-identification-api
artifact_total: 19
asyncapis:
- description: ''
  name: Vim Webhooks
  slug: vim-webhooks
collections:
- collection_type: open
  name: Vim Data Source API Integration
  slug: open-vim-data-source-openapi-original
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/capabilities/vim-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vim-capability-edges.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/openapi/_original/vim-data-source-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/vim-data-source-openapi-original.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/openapi/_original/vim-rest-api-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/vim-rest-api-openapi-original.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/mcp/vim-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vim-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/mcp/vim-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vim-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/packages/vim-packages.yml
  title: ''
  type: Packages
  url: packages/vim-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/packages/vim-packages.yml
  title: ''
  type: SDKs
  url: packages/vim-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/errors/vim-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vim-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/conventions/vim-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vim-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/data-model/vim-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vim-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/lifecycle/vim-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vim-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/conformance/vim-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vim-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://getvim.com/technology-security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance-self-service.getvim.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/well-known/vim-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vim-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/llms/vim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vim-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/overlays/vim-data-source-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vim-data-source-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/overlays/vim-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vim-rest-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/errors/vim-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/vim-error-codes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/rate-limits/vim-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vim-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/changelog/vim-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vim-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/sandbox/vim-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vim-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/asyncapi/vim-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vim-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/plans/vim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vim-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/components/vim-components.yml
  title: ''
  type: Components
  url: components/vim-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/security/vim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vim-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/agentic-access/vim-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vim-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/scopes/vim-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vim-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/authentication/vim-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vim-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://getvim.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getvim.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getvim.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getvim.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getvim.com/vim-os-js/setting-up
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/well-known/vim-openid-configuration.json
  title: ''
  type: OpenIDConfiguration
  url: well-known/vim-openid-configuration.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/well-known/vim-oauth-authorization-server.json
  title: ''
  type: OAuthMetadata
  url: well-known/vim-oauth-authorization-server.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getvim
- group: build
  title: ''
  type: Postman
  url: https://docs.getvim.com/invitations-postman-collection.json
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.getvim.com/change-log/
- group: operate
  title: ''
  type: Support
  url: https://getvim.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://console.getvim.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getvim.com
- group: company
  title: ''
  type: Blog
  url: https://getvim.com/blog
- group: auth
  title: ''
  type: Security
  url: https://getvim.com/technology-security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getvim.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getvim.com/legal/privacy/
created: '2026-07-24'
description: Vim is a United States healthcare technology company (getvim.com) that operates a clinical workflow and point-of-care integration platform connecting health plans, provider organizations, and digital-health applications to physicians inside their existing electronic health records. Through the Vim Canvas developer platform and the VimOS.js JavaScript SDK, applications embed actionable clinical insights - diagnosis gaps, risk, quality, and social determinants of health - directly into supported ambulatory EHR workflows and can read and write EHR resources (Patient, Encounter, Orders, Referral, Claim) at the point of care. Vim also exposes a REST API at api.getvim.com/v1 for provisioning applications, organizations, invitations, appointment lookups, and chart retrieval, authenticated with OAuth 2.0 client credentials via an Auth0-backed authorization server (auth.getvim.com). Vim is HIPAA, SOC 2, and HITRUST certified. The platform is proprietary REST and SDK based; it is not
  an HL7 FHIR API and publishes no FHIR CapabilityStatement. The API is available only to application servers hosted within the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-09-16'
name: Vim
nav: Providers
network: true
overview: 'Vim publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Access Token Retrieval API, Applications API, Appointments API, and 6 more. Tagged areas include Healthcare, United States, Clinical AI, EHR Integration, and Point of Care.


  The Vim catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vim''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 40 more developer resources.'
plans:
- name: Vim Plans Pricing
  plan_count: 0
  slug: vim-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Vim Rate Limits
  slug: vim-rate-limits
scopes:
- name: Vim Scopes
  scope_count: 4
  slug: vim-scopes
  summary_line: 4 scopes · implicit/clientCredentials
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 60.0
    developer_ergonomics: 78.0
    discoverability: 66.7
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/vim/refs/heads/main/screenshots/vim-2026-08-17T082750.png
security:
- kind: authentication
  name: Vim Authentication
  slug: vim-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vim Domain Security
  slug: vim-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vim Trust Center
  slug: vim-trust-center
  summary_line: HITRUST CSF, SOC 2 Type II, HIPAA
slug: vim
tags:
- Healthcare
- United States
- Clinical AI
- EHR Integration
- Point of Care
- Interoperability
- Value-Based Care
- Care Gaps
- Authentication
website: https://getvim.com/
---
