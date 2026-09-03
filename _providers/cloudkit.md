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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 17.3
  scored_at: '2026-09-02'
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
artifact_total: 24
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
- group: other
  title: ''
  type: Developer
  url: https://developer.apple.com/icloud/cloudkit/
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
created: '2024-01-01'
description: Apple CloudKit is the cloud backend for iOS, iPadOS, macOS, tvOS, watchOS, visionOS, and the web. CloudKit Web Services is the public REST surface that lets non-Apple-platform clients (web apps, servers) read and write data into a CloudKit container's public, private, or shared database. The web service is hosted at api.apple-cloudkit.com and accepts either an API token (for end-user-authenticated access) or a server-to- server ECDSA key for backend access. Operations cover records, zones, subscriptions, assets, users, and database changes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudkit.png
jsonld:
- class_count: 0
  name: Cloudkit Context
  property_count: 8
  slug: cloudkit-context
layout: provider
modified: '2026-04-25'
name: Apple CloudKit
nav: Providers
network: true
overview: 'Apple CloudKit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Changes API, Records API, and 4 more. Tagged areas include Apple, Cloud Storage, CloudKit, Database, and iCloud.


  The Apple CloudKit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apple CloudKit''s developer surface includes authentication, documentation, developer console, and 7 more developer resources.'
random_paper: 2
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
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 54.5
    contract_quality: 51.7
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 54.5
    operational_transparency: 0.0
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudkit/refs/heads/main/screenshots/cloudkit-2026-06-20T174606.png
security:
- kind: authentication
  name: Cloudkit Authentication
  slug: cloudkit-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cloudkit Domain Security
  slug: cloudkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
