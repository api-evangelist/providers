---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.eu1.fullview.io
  baseurl_source: declared
  description: The Bug Report API from Fullview — 2 operation(s) for bug report.
  name: Fullview Bug Report API
  slug: fullview-bug-report-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fullview Bug Report API
  slug: open-fullview-bug-report-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fullview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fullview.io
- group: docs
  title: ''
  type: Documentation
  url: https://support.fullview.io/en/collections/3529098-developer-docs
- group: docs
  title: ''
  type: APIReference
  url: https://support.fullview.io/en/articles/11552509-report-a-bug-api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://support.fullview.io/en/articles/6122361-how-to-install-fullview
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.fullview.io/en/
- group: company
  title: ''
  type: Blog
  url: https://www.fullview.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fullview.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auth.eu1.fullview.io/realms/fullview-idp-users-eu1/protocol/openid-connect/registrations
- group: start
  title: ''
  type: Login
  url: https://app.eu1.fullview.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fullview.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fullview.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fullview-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fullview-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fullview-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/fullview-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fullview-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fullview-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fullview-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/fullview-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/fullview-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fullview-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fullview-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fullview-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fullview-bug-report-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fullview-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fullview-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.fullview.io/
created: '2026-07-17'
description: Fullview is a customer-support platform that combines cobrowsing and session replays. Support agents can view and control a customer's browser session in real time directly from a help-desk ticket, and automatically recorded session replays capture user clicks, scrolls, console logs, network errors and JavaScript exceptions so issues can be diagnosed without asking the customer to screen-share. Fullview integrates one-click with Zendesk, Intercom, Salesforce Service Cloud and HubSpot Service Hub, offers customizable privacy controls and PII masking, and exposes a Bug Report integration API plus web and React Native SDKs. Authentication is handled by a Keycloak-based OpenID Connect provider, with optional RS256 JWT "Signed Identities" to secure end-user identity. Backed by Lightspeed Venture Partners and Seedcamp.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fullview.png
layout: provider
modified: '2026-07-19'
name: Fullview
nav: Providers
network: true
overview: 'Fullview publishes 1 API on the [APIs.io](https://apis.io/) network: Bug Report API. Tagged areas include Company, Customer-Support, Co-Browsing, Session Replay, and Customer Experience.


  Fullview''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 22 more developer resources.'
random_paper: 17
scopes:
- name: Fullview Scopes
  scope_count: 12
  slug: fullview-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 42.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fullview/refs/heads/main/screenshots/fullview-2026-07-25T215258.png
security:
- kind: authentication
  name: Fullview Authentication
  slug: fullview-authentication
  summary_line: openIdConnect/jwt · 2 schemes
- kind: domain-security
  name: Fullview Domain Security
  slug: fullview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fullview Vulnerability Disclosure
  slug: fullview-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Fullview Trust Center
  slug: fullview-trust-center
  summary_line: SOC 2, GDPR
slug: fullview
tags:
- Company
- Customer-Support
- Co-Browsing
- Session Replay
- Customer Experience
- Developer Tools
- Help Desk
- Software-as-a-Service
website: https://www.fullview.io
---
