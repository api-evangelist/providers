---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: 'OAuth 2.0 REST API for managing Snapchat advertising: organizations, ad accounts, campaigns, ad squads, ads, creatives, media, audience segments, measurement/reporting, the Conversions API (server-to-'
  name: Snapchat Marketing API
  slug: snapchat-marketing-api
- description: OAuth 2.0 and OpenID Connect identity platform for "Login with Snapchat", plus Creative Kit and Bitmoji Kit. Lets third-party apps authenticate Snapchatters, fetch approved profile fields, and share c
  name: Snap Kit / Login Kit
  slug: snap-kit-login-kit
- description: SDK and API for embedding Snap's augmented-reality Lenses (Lens Studio content) into third-party mobile and web apps, including a push-to-device API for managing Lens groups and experiences.
  name: Camera Kit
  slug: camera-kit
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.snap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.snap.com/api/marketing-api/Ads-API/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.snap.com/api/marketing-api/Ads-API/api-patterns
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.snap.com/api/marketing-api/Ads-API/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/snap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/snap-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/snap-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/snap-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snap-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snap-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/snap-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/snap-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/snap-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snap-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/snap-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snap-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/snap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/snap-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snap-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Snapchat
- group: operate
  title: ''
  type: Support
  url: https://businesshelp.snapchat.com
- group: start
  title: ''
  type: SignUp
  url: https://ads.snapchat.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snap.com/privacy/privacy-policy
created: '2026-07-17'
description: 'Snap Inc. is the technology company behind Snapchat, Bitmoji, Spectacles, and Lens Studio. Its Snap for Developers program exposes several public APIs and SDKs: the Snapchat Marketing API (Ads API, Ads Gallery API, Conversions API, and Public Profile API) for programmatically managing organizations, ad accounts, campaigns, ad squads, ads, creatives, audiences, measurement, and server-to-server conversion events; Snap Kit / Login Kit for OAuth 2.0 and OpenID Connect powered "Login with Snapchat", Creative Kit, and Bitmoji Kit; and Camera Kit for embedding Snap''s augmented-reality Lenses into third-party apps and web experiences. The Marketing API is an OAuth 2.0 REST API served from adsapi.snapchat.com/v1 with cursor pagination and a structured request envelope. First-party SDKs are published for Java, Python, PHP, JavaScript (Camera Kit on npm), Android, and iOS. Snap was surfaced as a portfolio company of General Catalyst and enriched into the API Evangelist network.'
image: https://developers.snap.com/img/snap-developer-logo.png
layout: provider
mcp_servers:
- description: ''
  name: snap-mcp.yml
  slug: snap-mcpyml
modified: '2026-07-21'
name: Snap
nav: Providers
network: true
overview: 'Snap publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Social Media, and Augmented Reality.


  Snap''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, signup flow, and 20 more developer resources.'
random_paper: 86
scopes:
- name: Snap Scopes
  scope_count: 0
  slug: snap-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 39.5
  previous_composite: 33.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Snap Authentication
  slug: snap-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Snap Domain Security
  slug: snap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snap Vulnerability Disclosure
  slug: snap-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: snap
tags:
- Company
- Advertising
- Marketing
- Social Media
- Augmented Reality
- Camera
- Authentication
- Identity
- Conversions
- Attribution
- SDKs
website: https://developers.snap.com
---
