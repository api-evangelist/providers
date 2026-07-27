---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Npm Agentic Access
  operation_count: 17
  slug: npm-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 10
apis:
- description: The npm Registry API provides programmatic access to the npm package registry, the largest software registry in the world hosting over two million JavaScript packages. Developers can query package met
  name: npm Registry API
  slug: registry
- description: The npm Hooks API allows developers to subscribe to notifications about changes in the npm registry. Hooks send HTTP POST payloads to a configured URI whenever a package is changed, enabling developer
  name: npm Hooks API
  slug: hooks
- description: 'The npm CLI is the official command-line interface for the npm package manager, providing developers with tools to install, publish, and manage JavaScript packages and their dependencies. It supports '
  name: npm CLI
  slug: cli
- description: npm Provenance provides supply chain security for JavaScript packages by establishing a verifiable link between a published package and its source code repository and build environment. When a package
  name: npm Provenance
  slug: provenance
- description: Package tarball downloads.
  name: npm Downloads API
  slug: npm-downloads-api
- description: OpenID Connect token exchange for trusted publishing. Exchange OIDC identity tokens from supported CI/CD providers for short-lived npm registry access tokens.
  name: npm OIDC API
  slug: npm-oidc-api
- description: Package metadata retrieval, including full packuments and version-specific documents.
  name: npm Packages API
  slug: npm-packages-api
- description: Full-text search across the npm registry with weighted scoring.
  name: npm Search API
  slug: npm-search-api
- description: Manage npm access tokens for authentication. Create, list, and delete tokens with customizable permissions and restrictions.
  name: npm Tokens API
  slug: npm-tokens-api
- description: Configure trusted publisher settings for packages to enable OIDC token exchange from CI/CD providers without long-lived npm tokens.
  name: npm Trusted Publishers API
  slug: npm-trusted-publishers-api
artifact_total: 44
asyncapis:
- description: The npm Hooks event system delivers HTTP POST payloads to subscriber endpoints whenever changes occur in the npm registry. Hooks can be configured to watch for changes to individual packages, all pack
  name: npm Hooks Events
  slug: npm-hooks-asyncapi
collections:
- collection_type: open
  name: npm Hooks API
  slug: open-npm-hooks-api
- collection_type: open
  name: npm Public API
  slug: open-npm-public-api
- collection_type: open
  name: npm Registry API
  slug: open-npm-registry-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/npm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/npm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/npm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/npm-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/npm-inc-
- group: start
  title: ''
  type: Portal
  url: https://www.npmjs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.npmjs.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.npmjs.org/
- group: start
  title: ''
  type: Login
  url: https://www.npmjs.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.npmjs.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.npmjs.com/policies/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.npmjs.com/policies/terms
- group: company
  title: ''
  type: Website
  url: https://www.npmjs.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/npm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.npmjs.org/
created: '2026-03-20'
description: npm is the world's largest software registry, hosting over two million JavaScript packages for the Node.js ecosystem. Their developer platform provides APIs for searching and retrieving package metadata, managing access tokens, subscribing to registry event webhooks, and publishing packages with supply chain provenance verification.
finops:
- name: Npm Finops
  service_category: Developer Tools / Package Registry
  slug: npm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/npm.png
json_schemas:
- name: Distribution
  property_count: 6
  slug: npm-distribution
- name: Error
  property_count: 2
  slug: npm-error
- name: npm Hook Event Payload
  property_count: 8
  slug: npm-hook-event
- name: Hook
  property_count: 10
  slug: npm-hook
- name: HookCreateRequest
  property_count: 4
  slug: npm-hookcreaterequest
- name: HookUpdateRequest
  property_count: 2
  slug: npm-hookupdaterequest
- name: npm Package Document
  property_count: 17
  slug: npm-package
- name: PackageDocument
  property_count: 16
  slug: npm-packagedocument
- name: PackageVersion
  property_count: 19
  slug: npm-packageversion
- name: Person
  property_count: 3
  slug: npm-person
- name: RegistryMetadata
  property_count: 11
  slug: npm-registrymetadata
- name: Repository
  property_count: 2
  slug: npm-repository
- name: SearchResultItem
  property_count: 3
  slug: npm-searchresultitem
- name: SearchResults
  property_count: 3
  slug: npm-searchresults
- name: Token
  property_count: 7
  slug: npm-token
- name: TokenCreateRequest
  property_count: 4
  slug: npm-tokencreaterequest
- name: TokenWithValue
  property_count: 0
  slug: npm-tokenwithvalue
- name: TrustedPublisher
  property_count: 7
  slug: npm-trustedpublisher
- name: TrustedPublisherRequest
  property_count: 5
  slug: npm-trustedpublisherrequest
json_structures:
- name: Npm Structure
  property_count: 0
  slug: npm-structure
jsonld:
- class_count: 0
  name: Npm Context
  property_count: 8
  slug: npm-context
layout: provider
modified: '2026-05-19'
name: npm
nav: Providers
network: true
overview: 'npm publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Registry API, Hooks API, Downloads API, and 5 more. Tagged areas include Packages, JavaScript, Node.js, Package Management, and Registry.


  The npm catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  npm''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Npm Plans Pricing
  plan_count: 4
  slug: npm-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 4
  name: Npm Rate Limits
  slug: npm-rate-limits
rules:
- name: npm API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: npm-asyncapi-spectral-rules
- name: npm API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: npm-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.4
  delta: 3.3
  facets:
    commercial_clarity: 73.7
    contract_quality: 79.6
    developer_ergonomics: 34.8
    discoverability: 87.5
    governance: 60.5
    operational_transparency: 52.6
  previous_composite: 61.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/npm/refs/heads/main/screenshots/npm-2026-06-20T190449.png
security:
- kind: authentication
  name: Npm Authentication
  slug: npm-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Npm Domain Security
  slug: npm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Npm Vulnerability Disclosure
  slug: npm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: npm
tags:
- Packages
- JavaScript
- Node.js
- Package Management
- Registry
- Security
website: https://www.npmjs.com/
---
