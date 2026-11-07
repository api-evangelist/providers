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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blink Ledger Systems Agentic Access
  operation_count: 4
  slug: blink-ledger-systems-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: Browser SDK exposing window.blinkSDK. Provides Login with Blink (getAuthorizationCode), subscription entitlement checks (isSubscribed, getSubscription, onSubscriptionChange), single-article charging (
  name: Blink SDK for JavaScript
  slug: blink-ledger-systems-sdk
- description: 'Outbound webhook stream delivering signed JSON notifications for subscription, payment and donation lifecycle events. Every payload is signed with ed25519 over the canonicalized event object, with an '
  name: Blink Notifications (Webhooks)
  slug: blink-ledger-systems-notifications
- baseURL: https://api.blink.net
  baseurl_source: declared
  description: Client account login and bearer token issuance.
  name: Blink Ledger Systems Authentication API
  slug: blink-ledger-systems-authentication-api
- baseURL: https://api.blink.net
  baseurl_source: declared
  description: Registration and retrieval of OAuth application credentials.
  name: Blink Ledger Systems OAuth Applications API
  slug: blink-ledger-systems-oauth-applications-api
- baseURL: https://api.blink.net
  baseurl_source: declared
  description: Blink user profile exchange.
  name: Blink Ledger Systems Users API
  slug: blink-ledger-systems-users-api
artifact_total: 22
asyncapis:
- description: ''
  name: Blink Ledger Systems Notifications Webhooks
  slug: blink-ledger-systems-notifications-webhooks
collections:
- collection_type: open
  name: Blink Server-Side Authentication API
  slug: open-blink-ledger-systems-authentication-api
- collection_type: open
  name: Blink Server-Side Authentication OAuth Applications API
  slug: open-blink-ledger-systems-oauth-applications-api
- collection_type: open
  name: Blink Server-Side Authentication Users API
  slug: open-blink-ledger-systems-users-api
common:
- group: operate
  href: https://artifacts.apis.io/blink-ledger-systems/lifecycle/blink-ledger-systems-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/blink-ledger-systems-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/blink-ledger-systems/agentic-access/blink-ledger-systems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blink-ledger-systems-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/rules/blink-ledger-systems-rules.yml
  title: ''
  type: Spectral
  url: rules/blink-ledger-systems-rules.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/json-ld/blink-ledger-systems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blink-ledger-systems-context.jsonld
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/vocabulary/blink-ledger-systems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blink-ledger-systems-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/blink-ledger-systems/hosts/blink-ledger-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blink-ledger-systems-hosts.yml
- group: other
  href: https://artifacts.apis.io/blink-ledger-systems/vendors/blink-ledger-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blink-ledger-systems-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blink.net/blog/
- group: agent
  href: https://artifacts.apis.io/blink-ledger-systems/mcp/blink-ledger-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/blink-ledger-systems-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://blink.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blink.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blink.net/docs/getting-started/overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blink.net/docs/api-reference/functions.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blink.net/docs/getting-started/quick-start.html
- group: operate
  title: ''
  type: Support
  url: https://docs.blink.net/docs/getting-started/support.html
- group: start
  title: ''
  type: SignUp
  url: https://blink.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blink.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blink.net/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blink.net
- group: docs
  href: https://artifacts.apis.io/blink-ledger-systems/openapi/_ae-authored/blink-ledger-systems-server-side-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/blink-ledger-systems-server-side-api-openapi.yml
- group: other
  href: https://artifacts.apis.io/blink-ledger-systems/overlays/blink-ledger-systems-server-side-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/blink-ledger-systems-server-side-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/blink-ledger-systems/packages/blink-ledger-systems-packages.yml
  title: ''
  type: Packages
  url: packages/blink-ledger-systems-packages.yml
- group: build
  href: https://artifacts.apis.io/blink-ledger-systems/packages/blink-ledger-systems-packages.yml
  title: ''
  type: SDKs
  url: packages/blink-ledger-systems-packages.yml
- group: auth
  href: https://artifacts.apis.io/blink-ledger-systems/authentication/blink-ledger-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blink-ledger-systems-authentication.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/errors/blink-ledger-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blink-ledger-systems-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/conventions/blink-ledger-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blink-ledger-systems-conventions.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/lifecycle/blink-ledger-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blink-ledger-systems-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/blink-ledger-systems/sandbox/blink-ledger-systems-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/blink-ledger-systems-sandbox.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/components/blink-ledger-systems-components.yml
  title: ''
  type: Components
  url: components/blink-ledger-systems-components.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/data-model/blink-ledger-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blink-ledger-systems-data-model.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/asyncapi/blink-ledger-systems-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blink-ledger-systems-notifications-webhooks.yml
- group: design
  href: https://artifacts.apis.io/blink-ledger-systems/conformance/blink-ledger-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blink-ledger-systems-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blink-ledger-systems/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/blink-ledger-systems/security/blink-ledger-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blink-ledger-systems-domain-security.yml
created: '2026-07-17'
description: Blink (Blink Ledger Systems Inc.) builds online identity and payment technologies for digital publishers. A single Blink account works across publishers, giving readers one universal login and frictionless payment so they can subscribe, donate, or buy an individual article or podcast with one click, or enable autopay for small frequent purchases. Publishers integrate three products — Blink Identity, Blink Pay and Blink Donate — through one hosted JavaScript SDK that places Blink-managed panels into the page, a dashboard-configured User Journeys rules engine, four server-side JSON endpoints for OAuth2 login, and a signed webhook notification stream covering subscription, payment and donation events. Founded 2017; incorporated in the US in 2018 and surfaced in the API Evangelist network as a Polychain portfolio company.
image: https://blink.net/resources/favicon.png
json_schemas:
- name: AccessTokenRequest
  property_count: 5
  slug: blink-ledger-systems-access-token-request
- name: LoginRequest
  property_count: 2
  slug: blink-ledger-systems-login-request
- name: LoginToken
  property_count: 1
  slug: blink-ledger-systems-login-token
- name: OAuthApplicationConfig
  property_count: 3
  slug: blink-ledger-systems-oauth-application-config
- name: RegisterApplicationRequest
  property_count: 2
  slug: blink-ledger-systems-register-application-request
- name: UserProfileResponse
  property_count: 1
  slug: blink-ledger-systems-user-profile-response
jsonld:
- class_count: 7
  name: Blink Ledger Systems Context
  property_count: 14
  slug: blink-ledger-systems-context
layout: provider
modified: '2026-10-06'
name: Blink Ledger Systems
nav: Providers
network: true
overview: 'Blink Ledger Systems publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, OAuth Applications API, Users API, and 2 more. Tagged areas include Company, Infrastructure, Payments, Identity, and Authentication.


  The Blink Ledger Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Blink Ledger Systems'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, authentication, and 27 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Blink Ledger Systems API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: blink-ledger-systems-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 34.4
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/blink-ledger-systems/blink-ledger-systems-2026-07-25T203322.png
security:
- kind: authentication
  name: Blink Ledger Systems Authentication
  slug: blink-ledger-systems-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Blink Ledger Systems Domain Security
  slug: blink-ledger-systems-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: blink-login-with-blink
  slug: blink-ledger-systems-login-with-blink
- name: blink-paywall-and-payments
  slug: blink-ledger-systems-paywall-and-payments
slug: blink-ledger-systems
tags:
- Company
- Infrastructure
- Payments
- Identity
- Authentication
- Publishing
- Media
- Subscription
- Donations
- Micropayments
- Paywall
- Webhook
website: https://blink.net
---
