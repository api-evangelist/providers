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
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: REST API to programmatically create and manage Firebase projects, apps (Web, Android, Apple), and their configuration.
  name: Firebase Management API
  slug: firebase-management-api
- description: REST API for reading and writing documents, running queries, and managing indexes in Cloud Firestore.
  name: Cloud Firestore REST API
  slug: cloud-firestore-rest-api
- description: REST API to read and write JSON data in the Firebase Realtime Database over HTTPS.
  name: Firebase Realtime Database REST API
  slug: firebase-realtime-database-rest-api
- description: REST API to send notification and data messages to devices via Firebase Cloud Messaging (FCM).
  name: Firebase Cloud Messaging HTTP v1 API
  slug: firebase-cloud-messaging-http-v1-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/firebase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firebase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firebase.google.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://firebase.google.com
- group: docs
  title: ''
  type: Documentation
  url: https://firebase.google.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://firebase.google.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://firebase.google.com/docs/guides
- group: start
  title: ''
  type: Console
  url: https://console.firebase.google.com
- group: start
  title: ''
  type: SignUp
  url: https://console.firebase.google.com
- group: commercial
  title: ''
  type: Pricing
  url: https://firebase.google.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://firebase.blog
- group: operate
  title: ''
  type: Support
  url: https://firebase.google.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firebase
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firebase.google.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://firebase.google.com/support/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firebase.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://cloud.google.com/security/compliance
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- group: operate
  title: ''
  type: Deprecation
  url: https://cloud.google.com/terms/deprecation
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: build
  title: ''
  type: Packages
  url: packages/firebase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/firebase-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/firebase-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/firebase-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/firebase-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/firebase-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/firebase-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/firebase-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/firebase-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/firebase-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/firebase-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/firebase-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/firebase-llms.txt
created: '2026-07-17'
description: Firebase is Google's app development platform — a backend-as-a-service (BaaS) suite for building, running, and growing web and mobile apps. It bundles managed backend products including Authentication, Cloud Firestore, Realtime Database, Cloud Storage, Cloud Functions, Hosting and App Hosting, Cloud Messaging (FCM), Remote Config, Crashlytics, Performance Monitoring, App Distribution, Test Lab, A/B Testing, App Check, Firebase AI Logic, and Extensions. Firebase exposes Google-hosted REST APIs (Management, Firestore, Realtime Database, FCM, Remote Config, Identity Toolkit) plus first-party client and Admin SDKs for Apple, Android, Web, Flutter, Unity, C++, Node.js, Python, Java, Go, and .NET, a cross-platform CLI (firebase-tools), a local Emulator Suite, and an official MCP server for agent-driven workflows.
image: https://firebase.google.com/downloads/brand-guidelines/PNG/logo-logomark.png
layout: provider
mcp_servers:
- description: ''
  name: Firebase MCP Server
  slug: firebase-mcp-server
modified: '2026-07-19'
name: Firebase
nav: Providers
network: true
overview: 'Firebase publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backend-as-a-Service, Application Development, Mobile, and Web.


  Firebase''s developer surface includes documentation, API reference, getting-started guide, developer console, signup flow, pricing, engineering blog, and 27 more developer resources.'
random_paper: 14
scopes:
- name: Firebase Scopes
  scope_count: 8
  slug: firebase-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 42.8
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firebase/refs/heads/main/screenshots/firebase-2026-07-25T214552.png
security:
- kind: authentication
  name: Firebase Authentication
  slug: firebase-authentication
  summary_line: apiKey/oauth2/bearer/serviceAccount/idToken · 5 schemes
- kind: domain-security
  name: Firebase Domain Security
  slug: firebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Firebase Vulnerability Disclosure
  slug: firebase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: firebase
tags:
- Company
- Backend-as-a-Service
- Application Development
- Mobile
- Web
- Authentication
- Database
- Cloud Functions
- Messaging
- Google
website: https://firebase.google.com
---
