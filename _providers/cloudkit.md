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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Cloudkit Agentic Access
  operation_count: 23
  slug: cloudkit-agentic-access
  summary_line: 23 operations · 23 acting
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudkit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudkit-domain-security.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/cloudkit-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudkit-rules.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloudkit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudkit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudkit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cloudkit-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cloudkit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudkit-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudkit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cloudkit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudkit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudkit-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/cloudkit-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudkit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cloudkit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudkit-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cloudkit-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudkit-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloudkit-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/cloudkit-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudkit-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudkit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudkit-rate-limits.yml
- group: agent
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
overview: 'Apple CloudKit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Changes API, Records API, and 4 more. Tagged areas include Apple, Cloud Storage, CloudKit, Database, and iCloud.


  The Apple CloudKit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apple CloudKit''s developer surface includes authentication, documentation, developer console, sandbox, changelog, CLI, API reference, and 33 more developer resources.'
plans:
- name: Cloudkit Plans Pricing
  plan_count: 0
  slug: cloudkit-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Cloudkit Rate Limits
  slug: cloudkit-rate-limits
rules:
- effective_rule_count: 53
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
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 67.0
    catalog_earned_first_party: 12.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 72.7
    contract_quality: 51.7
    developer_ergonomics: 80.4
    discoverability: 59.3
    governance: 72.7
    operational_transparency: 76.3
  previous_composite: 33.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudkit/refs/heads/main/screenshots/cloudkit-2026-06-20T174606.png
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
