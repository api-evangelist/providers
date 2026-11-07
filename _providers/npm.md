---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Npm Agentic Access
  operation_count: 17
  slug: npm-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 3
apis:
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The npm Registry API provides programmatic access to the npm package registry, the largest software registry in the world hosting over two million JavaScript packages. Developers can query package met
  name: npm Registry API
  slug: registry
- baseURL: https://registry.npmjs.org
  baseurl_source: spec
  description: The npm Hooks API allows developers to subscribe to notifications about changes in the npm registry. Hooks send HTTP POST payloads to a configured URI whenever a package is changed, enabling developer
  name: npm Hooks API
  slug: hooks
- description: 'The npm CLI is the official command-line interface for the npm package manager, providing developers with tools to install, publish, and manage JavaScript packages and their dependencies. It supports '
  name: npm CLI
  slug: cli
- description: npm Provenance provides supply chain security for JavaScript packages by establishing a verifiable link between a published package and its source code repository and build environment. When a package
  name: npm Provenance
  slug: provenance
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: Package tarball downloads.
  name: npm Downloads API
  slug: npm-downloads-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: OpenID Connect token exchange for trusted publishing. Exchange OIDC identity tokens from supported CI/CD providers for short-lived npm registry access tokens.
  name: npm OIDC API
  slug: npm-oidc-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: Package metadata retrieval, including full packuments and version-specific documents.
  name: npm Packages API
  slug: npm-packages-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: Full-text search across the npm registry with weighted scoring.
  name: npm Search API
  slug: npm-search-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: Manage npm access tokens for authentication. Create, list, and delete tokens with customizable permissions and restrictions.
  name: npm Tokens API
  slug: npm-tokens-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: Configure trusted publisher settings for packages to enable OIDC token exchange from CI/CD providers without long-lived npm tokens.
  name: npm Trusted Publishers API
  slug: npm-trusted-publishers-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The Access API from npm — 5 operation(s) for access.
  name: npm Access API
  slug: npm-access-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The Audit API from npm — 1 operation(s) for audit.
  name: npm Audit API
  slug: npm-audit-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The Org API from npm — 2 operation(s) for org.
  name: npm Org API
  slug: npm-org-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The Publish API from npm — 1 operation(s) for publish.
  name: npm Publish API
  slug: npm-publish-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The Stage API from npm — 5 operation(s) for stage.
  name: npm Stage API
  slug: npm-stage-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: The Team API from npm — 3 operation(s) for team.
  name: npm Team API
  slug: npm-team-api
- baseURL: https://registry.npmjs.org
  baseurl_source: declared
  description: Trust-related endpoints for managing package trust and security settings.
  name: npm Trust API
  slug: npm-trust-api
artifact_total: 82
asyncapis:
- description: The npm Hooks event system delivers HTTP POST payloads to subscriber endpoints whenever changes occur in the npm registry. Hooks can be configured to watch for changes to individual packages, all pack
  name: npm Hooks Events
  slug: npm-hooks-asyncapi
collections:
- collection_type: postman
  name: npm Hooks Downloads API
  slug: postman-npm-downloads-api
- collection_type: postman
  name: npm Downloads Hooks API
  slug: postman-npm-hooks-api
- collection_type: postman
  name: npm Hooks Downloads OIDC API
  slug: postman-npm-oidc-api
- collection_type: postman
  name: npm Hooks Downloads Packages API
  slug: postman-npm-packages-api
- collection_type: postman
  name: npm Hooks Downloads Registry API
  slug: postman-npm-registry-api
- collection_type: postman
  name: npm Hooks Downloads Search API
  slug: postman-npm-search-api
- collection_type: postman
  name: npm Hooks Downloads Tokens API
  slug: postman-npm-tokens-api
- collection_type: postman
  name: npm Hooks Downloads Trusted Publishers API
  slug: postman-npm-trusted-publishers-api
- collection_type: open
  name: npm Hooks Downloads API
  slug: open-npm-downloads-api
- collection_type: open
  name: npm Downloads Hooks API
  slug: open-npm-hooks-api
- collection_type: open
  name: npm Hooks Downloads OIDC API
  slug: open-npm-oidc-api
- collection_type: open
  name: npm Hooks Downloads Packages API
  slug: open-npm-packages-api
- collection_type: open
  name: npm Public API
  slug: open-npm-public-api
- collection_type: open
  name: npm Hooks Downloads Registry API
  slug: open-npm-registry-api
- collection_type: open
  name: npm Hooks Downloads Search API
  slug: open-npm-search-api
- collection_type: open
  name: npm Hooks Downloads Tokens API
  slug: open-npm-tokens-api
- collection_type: open
  name: npm Hooks Downloads Trusted Publishers API
  slug: open-npm-trusted-publishers-api
common:
- group: agent
  href: https://artifacts.apis.io/npm/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/npm/overlays/npm-registry-reference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/npm-registry-reference-overlay.yaml
- group: design
  href: https://artifacts.apis.io/npm/rules/npm-rules.yml
  title: ''
  type: Spectral
  url: rules/npm-rules.yml
- group: design
  href: https://artifacts.apis.io/npm/rules/npm-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/npm-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/npm/rules/npm-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/npm-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/npm/json-ld/npm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/npm-context.jsonld
- group: design
  href: https://artifacts.apis.io/npm/vocabulary/npm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/npm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/npm/data-model/npm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/npm-data-model.yml
- group: build
  href: https://artifacts.apis.io/npm/cli/npm-cli.yml
  title: ''
  type: CLI
  url: cli/npm-cli.yml
- group: operate
  href: https://artifacts.apis.io/npm/changelog/npm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/npm-changelog.yml
- group: design
  href: https://artifacts.apis.io/npm/conventions/npm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/npm-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.npmjs.org/deprecating-and-undeprecating-packages-or-package-versions
- group: design
  href: https://artifacts.apis.io/npm/lifecycle/npm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/npm-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/npm/errors/npm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/npm-problem-types.yml
- group: design
  href: https://artifacts.apis.io/npm/conformance/npm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/npm-conformance.yml
- group: auth
  href: https://artifacts.apis.io/npm/well-known/npm-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/npm-status-security.txt
- group: agent
  href: https://artifacts.apis.io/npm/well-known/npm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/npm-well-known.yml
- group: other
  href: https://artifacts.apis.io/npm/hosts/npm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/npm-hosts.yml
- group: other
  href: https://artifacts.apis.io/npm/vendors/npm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/npm-vendors.yml
- group: build
  href: https://artifacts.apis.io/npm/packages/npm-packages.yml
  title: ''
  type: SDKs
  url: packages/npm-packages.yml
- group: build
  href: https://artifacts.apis.io/npm/packages/npm-packages.yml
  title: ''
  type: Packages
  url: packages/npm-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.npmjs.org/getting-started
- group: commercial
  href: https://artifacts.apis.io/npm/plans/npm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/npm-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/npm/rate-limits/npm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/npm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/npm/finops/npm-finops.yml
  title: ''
  type: FinOps
  url: finops/npm-finops.yml
- group: other
  href: https://artifacts.apis.io/npm/capabilities/npm-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/npm-capability-edges.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/npm/cli/blob/latest/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/npm/cli/blob/latest/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/npm/cli/blob/latest/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/npm/overview
- group: agent
  href: https://artifacts.apis.io/npm/agentic-access/npm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/npm-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/npm/security/npm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/npm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/npm/security/npm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/npm-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/npm/authentication/npm-authentication.yml
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
- has_sources: true
  method: generated
  name: Npm Finops
  primary_unit: seat
  service_category: Developer Tools / Package Registry
  slug: npm-finops
  template: false
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
- name: OidcConfigsCreate
  property_count: 0
  slug: npm-oidc-configs-create
- name: OidcConfigs
  property_count: 0
  slug: npm-oidc-configs
- name: PackageDocument
  property_count: 16
  slug: npm-package-document
- name: npm Package Document
  property_count: 17
  slug: npm-package
- name: PackageVersion
  property_count: 19
  slug: npm-package-version
- name: PackageVersionStatus
  property_count: 3
  slug: npm-package-version-status
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
- name: SearchResults
  property_count: 3
  slug: npm-search-results
- name: SearchResultItem
  property_count: 3
  slug: npm-searchresultitem
- name: SearchResults
  property_count: 3
  slug: npm-searchresults
- name: StagePackageList
  property_count: 4
  slug: npm-stage-package-list
- name: StagePackageVersion
  property_count: 10
  slug: npm-stage-package-version
- name: StagedPackumentRequest
  property_count: 18
  slug: npm-staged-packument-request
- name: TokenCreateRequest
  property_count: 4
  slug: npm-token-create-request
- name: Token
  property_count: 7
  slug: npm-token
- name: TokenWithValue
  property_count: 7
  slug: npm-token-with-value
- name: TokenCreateRequest
  property_count: 4
  slug: npm-tokencreaterequest
- name: TokenWithValue
  property_count: 1
  slug: npm-tokenwithvalue
- name: TrustedPublisherRequest
  property_count: 5
  slug: npm-trusted-publisher-request
- name: TrustedPublisher
  property_count: 7
  slug: npm-trusted-publisher
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
overview: 'npm publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Registry API, Hooks API, Downloads API, and 14 more. Tagged areas include Packages, JavaScript, Node.js, Package Management, and Registry.


  The npm catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  npm''s developer surface includes CLI, changelog, getting-started guide, authentication, developer portal, documentation, engineering blog, and 38 more developer resources.'
plans:
- name: Npm Plans Pricing
  plan_count: 4
  slug: npm-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Npm Rate Limits
  slug: npm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: npm — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: npm-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: npm — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: npm-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 114
  extends:
  - spectral:oas
  name: npm API Rules
  rule_count: 73
  severity_counts:
    error: 54
    hint: 0
    info: 8
    warn: 11
  slug: npm-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 39
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.0
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 71.8
    developer_ergonomics: 67.3
    discoverability: 69.6
    operational_transparency: 63.2
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/npm/npm-2026-06-20T190449.png
security:
- kind: authentication
  name: Npm Authentication
  slug: npm-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Npm Domain Security
  slug: npm-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Npm Vulnerability Disclosure
  slug: npm-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: npm-configure-trusted-publishing
  slug: npm-configure-trusted-publishing
- name: npm-manage-access-tokens
  slug: npm-manage-access-tokens
- name: npm-staged-publish
  slug: npm-staged-publish
slug: npm
tags:
- Packages
- JavaScript
- Node.js
- Package Management
- Registry
- Security
- Developer Tools
- npm
website: https://www.npmjs.com/
---
