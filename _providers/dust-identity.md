---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 106
  human_in_the_loop: 1
  name: Dust Identity Agentic Access
  operation_count: 177
  slug: dust-identity-agentic-access
  summary_line: 177 operations · 106 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The core DUST Platform API (apid). REST over HTTPS with a bearer-JWT Service Account model, organization/team context headers, cursor pagination and a single stable error envelope. Covers Threads, Ide
  name: DUST API
  slug: dust-api
- description: The DUST account service — organizations, users, sessions, Service Accounts and OpenID Connect. Issues the short-lived JWTs the DUST API consumes, via an API-key exchange (GET /api/auth/token with x-a
  name: DUST AuthD
  slug: dust-authd
artifact_total: 10
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
overview: 'Dust Identity publishes 1 API on the [APIs.io](https://apis.io/) network: DUST API. Tagged areas include Authentication, Identity, Supply Chain, Traceability, and Provenance.


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
  composite: 45.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 60.6
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
