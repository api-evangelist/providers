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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'The Kittl SDK is the bridge between a sandboxed app and the Kittl editor host. It exposes async namespaces — kittl.design for design operations, kittl.state for editor and app state, kittl.upload for '
  name: Kittl SDK & App Platform
  slug: sdk
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.kittl.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sdk-docs.kittl.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://sdk-docs.kittl.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://sdk-docs.kittl.dev/References/design
- group: start
  title: ''
  type: GettingStarted
  url: https://sdk-docs.kittl.dev/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.kittl.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kittl.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kittl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kittl.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.kittl.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kittl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kittl.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/kittl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kittl-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kittl-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kittl-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kittl-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kittl-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kittl-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kittl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kittl-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kittl-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kittl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kittl-conformance.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kittl-extension-manifest-schema.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kittl-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kittl-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.kittl.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kittl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kittl-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kittl-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Kittl is a Berlin-based, browser-based graphic design platform positioned for commerce-driven creative workflows — "Canva is for content, Kittl is for commerce." It serves small business owners, Shopify and Etsy sellers, print-on-demand businesses, DTC brands, freelancers, agencies and small creative teams, covering branding, packaging, product imagery, marketing campaigns, merchandise, labels, mockups and digital assets with AI-assisted creative workflows. For developers, Kittl runs an app/extension platform: sandboxed web apps run in an isolated iframe inside the Kittl editor and integrate with editor APIs over postMessage through the official @kittl/sdk JavaScript SDK, governed by a declared scope set in manifest.json and shipped through the @kittl/cli toolchain. The platform is in beta and account approval is required to create apps.'
image: https://www.kittl.com/images/og-image.jpg
json_schemas:
- name: Kittl Extension Manifest
  property_count: 7
  slug: kittl-extension-manifest
layout: provider
modified: '2026-07-19'
name: Kittl
nav: Providers
network: true
overview: 'Kittl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Design, Graphic Design, Creative Tools, and SDK.


  Kittl''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 8
scopes:
- name: Kittl Scopes
  scope_count: 12
  slug: kittl-scopes
  summary_line: 12 scopes
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 11.3
    developer_ergonomics: 78.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 38.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kittl/refs/heads/main/screenshots/kittl-2026-07-25T223913.png
security:
- kind: authentication
  name: Kittl Authentication
  slug: kittl-authentication
  summary_line: jwt/oauth2-client/interactive-device-login · 3 schemes
- kind: domain-security
  name: Kittl Domain Security
  slug: kittl-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kittl Vulnerability Disclosure
  slug: kittl-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: kittl
tags:
- Company
- Design
- Graphic Design
- Creative Tools
- SDK
- Developer Platform
- Extensions
- Print On Demand
- E-Commerce
- AI
- Mockups
- Typography
website: https://www.kittl.com
---
