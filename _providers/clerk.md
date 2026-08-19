---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 3
  name: Clerk Agentic Access
  operation_count: 29
  slug: clerk-agentic-access
  summary_line: 29 operations · 19 acting · 3 human-in-the-loop
api_count: 24
apis:
- description: 'Browser-facing API consumed by Clerk''s frontend SDKs and ClerkJS for sign-up, sign-in, session refresh, and user profile mutations. Endpoint is instance-specific (subdomain on clerk.accounts.dev or a '
  name: Clerk Frontend API
  slug: frontend-api
- description: Webhook events delivered via Svix for user, session, organization, email, SMS, and role lifecycle changes. Customers configure endpoints in the dashboard and verify signatures with the Svix libraries.
  name: Clerk Webhooks (Svix)
  slug: webhooks
- description: Official ClerkJS browser library and monorepo of framework adapters (Next.js, React, Expo, React Router, Astro, Chrome Extension, TanStack). Powers Clerk's prebuilt UI components and headless hooks.
  name: Clerk JavaScript SDK
  slug: javascript
- description: Next.js integration covering App Router and Pages Router, middleware, route handlers, server components, and server actions. Distributed from the @clerk/nextjs package inside the JavaScript monorepo.
  name: Clerk Next.js SDK
  slug: sdk-nextjs
- description: React components, hooks, and providers from the @clerk/clerk-react package for plain React SPAs.
  name: Clerk React SDK
  slug: sdk-react
- description: Expo / React Native bindings for Clerk supporting OAuth via deep links, secure session storage, and biometrics.
  name: Clerk Expo SDK
  slug: sdk-expo
- description: Adapter for React Router v7 (Remix successor) covering loaders, actions, and server-rendered authentication.
  name: Clerk React Router SDK
  slug: sdk-react-router
- description: Adapter for the Astro framework with components and middleware.
  name: Clerk Astro SDK
  slug: sdk-astro
- description: Adapter for TanStack Start (React full-stack framework) with route-level authentication helpers.
  name: Clerk TanStack Start SDK
  slug: sdk-tanstack-start
- description: Backend SDK for Node.js (@clerk/backend / @clerk/express / @clerk/fastify) that wraps the Backend API and verifies session JWTs.
  name: Clerk Node.js SDK
  slug: sdk-node
- description: Official Go SDK for the Clerk Backend API.
  name: Clerk Go SDK
  slug: sdk-go
- description: Official Python SDK for the Clerk Backend API.
  name: Clerk Python SDK
  slug: sdk-python
- description: Official Ruby SDK for the Clerk Backend API, with a Rails integration.
  name: Clerk Ruby SDK
  slug: sdk-ruby
- description: Official Java SDK for the Clerk Backend API.
  name: Clerk Java SDK
  slug: sdk-java
- description: Official PHP SDK for the Clerk Backend API.
  name: Clerk PHP SDK
  slug: sdk-php
- description: Official C# / .NET SDK for the Clerk Backend API.
  name: Clerk C# / .NET SDK
  slug: sdk-csharp
- description: Public repository of OpenAPI specifications for Clerk's APIs, used as the source for generated SDKs and documentation.
  name: Clerk OpenAPI Specifications
  slug: openapi-specs
- description: The Invitations API from Clerk — 2 operation(s) for invitations.
  name: Clerk Invitations API
  slug: clerk-invitations-api
- description: The JwtTemplates API from Clerk — 1 operation(s) for jwttemplates.
  name: Clerk JwtTemplates API
  slug: clerk-jwttemplates-api
- description: The Organizations API from Clerk — 4 operation(s) for organizations.
  name: Clerk Organizations API
  slug: clerk-organizations-api
- description: The Sessions API from Clerk — 4 operation(s) for sessions.
  name: Clerk Sessions API
  slug: clerk-sessions-api
- description: The SignInTokens API from Clerk — 2 operation(s) for signintokens.
  name: Clerk SignInTokens API
  slug: clerk-signintokens-api
- description: The Users API from Clerk — 4 operation(s) for users.
  name: Clerk Users API
  slug: clerk-users-api
- description: The Webhooks API from Clerk — 1 operation(s) for webhooks.
  name: Clerk Webhooks API
  slug: clerk-webhooks-api
artifact_total: 43
asyncapis:
- description: AsyncAPI 2.6 specification for Clerk's webhook surface. Clerk delivers webhook events via Svix to customer-configured endpoints. Each delivery is an HTTP POST of a JSON envelope signed with three Svix
  name: Clerk Webhooks
  slug: clerk-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clerk Backend Invitations API
  slug: open-clerk-invitations-api
- collection_type: open
  name: Clerk Backend Invitations JwtTemplates API
  slug: open-clerk-jwttemplates-api
- collection_type: open
  name: Clerk Backend Invitations Organizations API
  slug: open-clerk-organizations-api
- collection_type: open
  name: Clerk Backend Invitations Sessions API
  slug: open-clerk-sessions-api
- collection_type: open
  name: Clerk Backend Invitations SignInTokens API
  slug: open-clerk-signintokens-api
- collection_type: open
  name: Clerk Backend Invitations Users API
  slug: open-clerk-users-api
- collection_type: open
  name: Clerk Backend Invitations Webhooks API
  slug: open-clerk-webhooks-api
- collection_type: open
  name: Clerk Backend API
  slug: open-clerk
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/clerk/javascript/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/clerk/javascript/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/clerk/javascript/blob/main/docs/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/clerk/javascript/blob/main/docs/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/clerk/javascript/blob/main/docs/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/clerk/javascript/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clerk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clerk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clerk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://clerk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clerk.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/clerk
- group: commercial
  title: ''
  type: Pricing
  url: https://clerk.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://clerk.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://clerk.com/blog
- group: operate
  title: ''
  type: Status
  url: https://status.clerk.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clerk-dev/
- group: agent
  title: ''
  type: LlmsText
  url: https://clerk.com/llms.txt
created: '2026-05-23'
description: Clerk is a drop-in authentication and user management platform for web and mobile applications. The product spans sign-up / sign-in flows, user profiles, multi-factor authentication, passkeys, social sign-on, magic links, bot and fraud detection, organizations (B2B / multi-tenant) with custom roles and invitations, and a Billing product for subscriptions. The Backend API at api.clerk.com is authenticated with a Bearer secret key and has an OpenAPI specification. Frontend SDKs cover Next.js, React, React Router, Expo, Astro, TanStack React Start, Chrome Extension, and vanilla JavaScript. Backend SDKs cover Node, Go, Python, Ruby, Java, PHP, and C#. Webhooks are delivered via Svix.
finops:
- name: Clerk Finops
  service_category: API
  slug: clerk-finops
graphqls:
- description: Clerk's public API surface is REST-based. The Backend API lives at `https://api.clerk.com/v1` and is documented at [https://clerk.com/docs/reference/backend-api](https://clerk.com/docs/reference/backe
  name: Clerk GraphQL
  slug: clerk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clerk.png
layout: provider
modified: '2026-05-30'
name: Clerk
nav: Providers
network: true
overview: 'Clerk publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Webhooks (Svix), Invitations API, JwtTemplates API, and 5 more. Tagged areas include Authentication, User Management, Identity, Passkeys, and MFA.


  The Clerk catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Clerk''s developer surface includes authentication, documentation, GitHub presence, pricing, changelog, engineering blog, status page, and 12 more developer resources.'
plans:
- name: Clerk Plans Pricing
  plan_count: 1
  slug: clerk-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 2
  name: Clerk Rate Limits
  slug: clerk-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Clerk API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: clerk-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.4
  delta: -3.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 65.7
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 11.4
    operational_transparency: 52.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clerk/refs/heads/main/screenshots/clerk-2026-06-20T174506.png
security:
- kind: authentication
  name: Clerk Authentication
  slug: clerk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clerk Domain Security
  slug: clerk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clerk Vulnerability Disclosure
  slug: clerk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clerk
tags:
- Authentication
- User Management
- Identity
- Passkeys
- MFA
- B2B
- Organizations
- Billing
website: https://clerk.com/
---
