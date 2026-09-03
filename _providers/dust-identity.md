---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 106
  human_in_the_loop: 1
  name: Dust Identity Agentic Access
  operation_count: 177
  slug: dust-identity-agentic-access
  summary_line: 177 operations · 106 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The DUST account service — organizations, users, sessions, Service Accounts and OpenID Connect. Issues the short-lived JWTs the DUST API consumes, via an API-key exchange (GET /api/auth/token with x-a
  name: DUST AuthD
  slug: dust-authd
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Authentication and authorization
  name: Dust Identity Auth API
  slug: dust-identity-auth-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Unordered teams of threads
  name: Dust Identity Bundles API
  slug: dust-identity-bundles-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Create and manage certificate form designs
  name: Dust Identity Certificate Forms API
  slug: dust-identity-certificate-forms-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Generate, list, and void certificates
  name: Dust Identity Certificates API
  slug: dust-identity-certificates-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Connections (team links) between Teams; they gate sharing and shipments
  name: Dust Identity Connections API
  slug: dust-identity-connections-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Work with system events
  name: Dust Identity Events API
  slug: dust-identity-events-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: The Fabric API from Dust Identity — 25 operation(s) for fabric.
  name: Dust Identity Fabric API
  slug: dust-identity-fabric-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Upload and manage files
  name: Dust Identity Files API
  slug: dust-identity-files-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Organization and team metrics.
  name: Dust Identity Metrics API
  slug: dust-identity-metrics-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Manage user notifications.
  name: Dust Identity Notifications API
  slug: dust-identity-notifications-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Org-admin management of teams and memberships
  name: Dust Identity Org Admin API
  slug: dust-identity-org-admin-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Manage organizations and their members.
  name: Dust Identity Organizations API
  slug: dust-identity-organizations-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: The Sharing API from Dust Identity — 4 operation(s) for sharing.
  name: Dust Identity Sharing API
  slug: dust-identity-sharing-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: The Slices API from Dust Identity — 3 operation(s) for slices.
  name: Dust Identity Slices API
  slug: dust-identity-slices-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Health and status checks
  name: Dust Identity System API
  slug: dust-identity-system-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Manage identifiers and their metadata
  name: Dust Identity Tags API
  slug: dust-identity-tags-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Manage user teams and permissions
  name: Dust Identity Teams API
  slug: dust-identity-teams-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Manage thread templates
  name: Dust Identity Templates API
  slug: dust-identity-templates-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Link threads with relations
  name: Dust Identity Thread Links API
  slug: dust-identity-thread-links-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: The ways threads can be linked
  name: Dust Identity Thread Relations API
  slug: dust-identity-thread-relations-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Create and manage threads
  name: Dust Identity Threads API
  slug: dust-identity-threads-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Transfer ownership of threads across organizations
  name: Dust Identity Transfers API
  slug: dust-identity-transfers-api
- baseURL: https://apid.dustid.io
  baseurl_source: declared
  description: Manage user accounts and profiles
  name: Dust Identity Users API
  slug: dust-identity-users-api
artifact_total: 32
asyncapis:
- description: ''
  name: Dust Identity Events
  slug: dust-identity-events
collections:
- collection_type: open
  name: DUST API
  slug: open-dust-identity-apid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dust-identity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dust-identity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dust-identity-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dustidentity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dustid.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dustid.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dustid.io/reference/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dustid.io/api/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://www.dustidentity.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.dustidentity.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://dice.dustid.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dustidentity.com/legal-pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dustidentity.com/legal-pages/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dust-identity-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/dust-identity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dust-identity-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dust-identity-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dust-identity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dust-identity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dust-identity-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dustid.io/api/compatibility/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dust-identity-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/dust-identity-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/dust-identity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dust-identity-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/dust-identity-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dust-identity-apid-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/dust-identity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dust-identity-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/dust-identity-dice-api-integration.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/dust-identity-dust-go-connect-integration.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dustid
- group: build
  title: ''
  type: Examples
  url: examples/dust-identity-examples.yml
created: '2026-08-12'
description: 'DUST Identity (Newton, Massachusetts; founded 2018 as an MIT spinout) binds physical objects to trusted digital records using the Diamond Unclonable Security Tag — an applied coating of engineered nano-diamonds in a polymer matrix that forms an unclonable optical fingerprint. The DUST Platform (DICE) tracks each marked item as a "Thread": a digital record carrying typed fields, files, physical identifiers (DUST, QR, barcode, Data Matrix, NFC), an immutable event history, and Fabric lineage across slices, shipments and organization boundaries. It is used for aerospace and defense raw-material traceability, secure electronics, certified-pre-owned authentication, return-fraud detection, security labeling and high-value asset identity. The company publishes a public OpenAPI 3.1 contract for the DUST API (apid) covering 177 operations, a Starlight documentation site, llms.txt, and two provider-authored agent skills.'
image: https://cdn.prod.website-files.com/696a1cb647f26194e423aba4/6980a035011540d3493bf124_Webclip%20Dust%20Identity.png
layout: provider
modified: '2026-08-12'
name: Dust Identity
nav: Providers
network: true
overview: 'Dust Identity publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Bundles API, Certificate Forms API, and 20 more. Tagged areas include Authentication, Identity, Supply Chain, Traceability, and Provenance.


  The Dust Identity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dust Identity''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 27 more developer resources.'
plans:
- name: Dust Identity Plans Pricing
  plan_count: 0
  slug: dust-identity-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Dust Identity Rate Limits
  slug: dust-identity-rate-limits
scopes:
- name: Dust Identity Scopes
  scope_count: 6
  slug: dust-identity-scopes
  summary_line: 6 scopes · authorizationCode/refreshToken/clientCredentials
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dust-identity/refs/heads/main/screenshots/dust-identity-2026-08-17T080906.png
security:
- kind: authentication
  name: Dust Identity Authentication
  slug: dust-identity-authentication
  summary_line: http/oauth2/openIdConnect/apiKey · 4 schemes
- kind: domain-security
  name: Dust Identity Domain Security
  slug: dust-identity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dust-identity
tags:
- Authentication
- Identity
- Supply Chain
- Traceability
- Provenance
- Anti-Counterfeiting
- Asset Tracking
- Aerospace and Defense
- Manufacturing
- Security
website: https://www.dustidentity.com/
---
