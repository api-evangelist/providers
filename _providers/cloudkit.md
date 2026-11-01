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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cloudkit Agentic Access
  operation_count: 23
  slug: cloudkit-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 1
apis:
- description: 'The CloudKit Web Services REST API is structured as /database/1/{container}/{environment}/{database}/{operation}, where database is one of public, private, or shared and environment is development or '
  name: CloudKit Web Services
  slug: web-services
- description: CloudKit JS is Apple's JavaScript SDK that wraps the CloudKit Web Services REST API for browser apps. It provides Sign in with Apple authentication, container/database/zone access, queries, record ope
  name: CloudKit JS
  slug: js
- description: The native CloudKit framework for iOS, iPadOS, macOS, tvOS, watchOS, and visionOS. Provides programmatic access to CloudKit containers, records, zones, subscriptions, and sharing. Out of band of the w
  name: CloudKit Framework
  slug: framework
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Assets API from Apple CloudKit — 2 operation(s) for assets.
  name: Apple CloudKit Assets API
  slug: cloudkit-assets-api
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Changes API from Apple CloudKit — 2 operation(s) for changes.
  name: Apple CloudKit Changes API
  slug: cloudkit-changes-api
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Records API from Apple CloudKit — 6 operation(s) for records.
  name: Apple CloudKit Records API
  slug: cloudkit-records-api
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Subscriptions API from Apple CloudKit — 3 operation(s) for subscriptions.
  name: Apple CloudKit Subscriptions API
  slug: cloudkit-subscriptions-api
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Tokens API from Apple CloudKit — 2 operation(s) for tokens.
  name: Apple CloudKit Tokens API
  slug: cloudkit-tokens-api
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Users API from Apple CloudKit — 4 operation(s) for users.
  name: Apple CloudKit Users API
  slug: cloudkit-users-api
- baseURL: https://api.apple-cloudkit.com/database/1
  baseurl_source: declared
  description: The Zones API from Apple CloudKit — 4 operation(s) for zones.
  name: Apple CloudKit Zones API
  slug: cloudkit-zones-api
artifact_total: 33
collections:
- collection_type: open
  name: Apple CloudKit Web Services Assets API
  slug: open-cloudkit-assets-api
- collection_type: open
  name: Apple CloudKit Web Services Assets Changes API
  slug: open-cloudkit-changes-api
- collection_type: open
  name: Apple CloudKit Web Services Assets Records API
  slug: open-cloudkit-records-api
- collection_type: open
  name: Apple CloudKit Web Services Assets Subscriptions API
  slug: open-cloudkit-subscriptions-api
- collection_type: open
  name: Apple CloudKit Web Services Assets Tokens API
  slug: open-cloudkit-tokens-api
- collection_type: open
  name: Apple CloudKit Web Services Assets Users API
  slug: open-cloudkit-users-api
- collection_type: open
  name: Apple CloudKit Web Services Assets Zones API
  slug: open-cloudkit-zones-api
- collection_type: open
  name: Apple CloudKit Web Services
  slug: open-cloudkit
common:
- group: agent
  href: https://artifacts.apis.io/cloudkit/agentic-access/cloudkit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudkit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/security/cloudkit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudkit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/authentication/cloudkit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudkit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.icloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apple.com/documentation/cloudkit
- group: start
  title: ''
  type: Console
  url: https://icloud.developer.apple.com/dashboard/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apple.com/legal/privacy/
- group: design
  href: https://artifacts.apis.io/cloudkit/json-ld/cloudkit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudkit-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudkit/rules/cloudkit-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudkit-rules.yml
- group: build
  href: https://artifacts.apis.io/cloudkit/packages/cloudkit-packages.yml
  title: ''
  type: Packages
  url: packages/cloudkit-packages.yml
- group: build
  href: https://artifacts.apis.io/cloudkit/packages/cloudkit-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudkit-packages.yml
- group: agent
  href: https://artifacts.apis.io/cloudkit/well-known/cloudkit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudkit-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/well-known/cloudkit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloudkit-security.txt
- group: agent
  href: https://artifacts.apis.io/cloudkit/mcp/cloudkit-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cloudkit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cloudkit/llms/cloudkit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudkit-llms.txt
- group: design
  href: https://artifacts.apis.io/cloudkit/conformance/cloudkit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudkit-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/conformance/cloudkit-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cloudkit-conformance.yml
- group: design
  href: https://artifacts.apis.io/cloudkit/errors/cloudkit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudkit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudkit/lifecycle/cloudkit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudkit-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cloudkit/lifecycle/cloudkit-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/cloudkit-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/security/cloudkit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudkit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/security/cloudkit-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cloudkit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudkit/security/cloudkit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudkit-trust-center.yml
- group: start
  href: https://artifacts.apis.io/cloudkit/sandbox/cloudkit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cloudkit-sandbox.yml
- group: design
  href: https://artifacts.apis.io/cloudkit/conventions/cloudkit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudkit-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cloudkit/changelog/cloudkit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudkit-changelog.yml
- group: build
  href: https://artifacts.apis.io/cloudkit/cli/cloudkit-cli.yml
  title: ''
  type: CLI
  url: cli/cloudkit-cli.yml
- group: design
  href: https://artifacts.apis.io/cloudkit/data-model/cloudkit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudkit-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/cloudkit/plans/cloudkit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudkit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudkit/rate-limits/cloudkit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudkit-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/cloudkit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apple.com/icloud/cloudkit/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html
- group: operate
  title: ''
  type: Support
  url: https://developer.apple.com/support/
- group: company
  title: ''
  type: Blog
  url: https://developer.apple.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apple
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.apple.com/programs/
- group: start
  title: ''
  type: SignUp
  url: https://developer.apple.com/programs/enroll/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apple.com/legal/internet-services/icloud/
created: '2024-01-01'
description: Apple CloudKit is the cloud backend for iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and the web. CloudKit Web Services is the public REST surface that lets non-Apple-platform clients (web apps, servers) read and write data into a CloudKit container's public, private, or shared database. The web service is hosted at api.apple-cloudkit.com and accepts either an API token (for end-user-authenticated access) or a server-to- server ECDSA key for backend access. Operations cover records, zones, subscriptions, assets, users, and database changes.
finops:
- has_sources: true
  method: derived
  name: Cloudkit Finops
  primary_unit: membership
  service_category: ''
  slug: cloudkit-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudkit.png
jsonld:
- class_count: 0
  name: Cloudkit Context
  property_count: 8
  slug: cloudkit-context
layout: provider
modified: '2026-09-05'
name: Apple CloudKit
nav: Providers
network: true
overview: 'Apple CloudKit publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Changes API, Records API, and 7 more. Tagged areas include Apple, Cloud Storage, CloudKit, Database, and iCloud.


  The Apple CloudKit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apple CloudKit''s developer surface includes authentication, documentation, developer console, sandbox, changelog, CLI, API reference, and 33 more developer resources.'
plans:
- name: Cloudkit Plans Pricing
  plan_count: 3
  slug: cloudkit-plans-pricing
- name: Cloudkit Price Estimates
  plan_count: 0
  slug: cloudkit-price-estimates
random_paper: 23
rate_limits:
- limit_count: 6
  name: Cloudkit Rate Limits
  slug: cloudkit-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apple CloudKit API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: cloudkit-rules
score:
  band: exemplar
  composite: 70.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 46.9
    developer_ergonomics: 80.4
    discoverability: 57.1
    operational_transparency: 78.9
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloudkit/cloudkit-2026-06-20T174606.png
security:
- kind: authentication
  name: Cloudkit Authentication
  slug: cloudkit-authentication
  summary_line: apiKey/signature · 4 schemes
- kind: domain-security
  name: Cloudkit Domain Security
  slug: cloudkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudkit Vulnerability Disclosure
  slug: cloudkit-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cloudkit Trust Center
  slug: cloudkit-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27018, SOC 3
skill_count: 4
skills:
- name: cloudkit-modify-records
  slug: cloudkit-modify-records
- name: cloudkit-query-records
  slug: cloudkit-query-records
- name: cloudkit-sync-changes
  slug: cloudkit-sync-changes
- name: cloudkit-upload-assets
  slug: cloudkit-upload-assets
slug: cloudkit
tags:
- Apple
- Cloud Storage
- CloudKit
- Database
- iCloud
- Mobile
- Sync
- Web Services
website: https://www.icloud.com/
---
