---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 210
  human_in_the_loop: 9
  name: Unleash Agentic Access
  operation_count: 352
  slug: unleash-agentic-access
  summary_line: 352 operations · 210 acting · 9 human-in-the-loop
api_count: 36
apis:
- description: API endpoint consumed by backend Unleash SDKs to fetch complete feature flag configurations including all activation strategies. Supports server-side flag evaluation with zero additional latency after
  name: Unleash Client API
  slug: client-api
- description: Create, update, and delete [Unleash addons](https://docs.getunleash.io/addons).
  name: Unleash Addons API
  slug: unleash-addons-api
- description: Configuration for the Unleash Admin UI. These endpoints should not be relied upon and can change at any point without prior notice.
  name: Unleash Admin UI API
  slug: unleash-admin-ui-api
- description: Create, update, and delete [Unleash API tokens](https://docs.getunleash.io/concepts/api-tokens-and-client-keys).
  name: Unleash API tokens API
  slug: unleash-api-tokens-api
- description: Revive or permanently delete [archived feature flags](https://docs.getunleash.io/advanced/archived_toggles).
  name: Unleash Archive API
  slug: unleash-archive-api
- description: Manage logins, passwords, etc.
  name: Unleash Auth API
  slug: unleash-auth-api
- description: Create, update, flag, and delete [banners](https://docs.getunleash.io/concepts/banners).
  name: Unleash Banners API
  slug: unleash-banners-api
- description: API for managing [change requests](https://docs.getunleash.io/concepts/change-requests).
  name: Unleash Change Requests API
  slug: unleash-change-requests-api
- description: Create, update, and delete [context fields](https://docs.getunleash.io/concepts/unleash-context) that Unleash is aware of.
  name: Unleash Context API
  slug: unleash-context-api
- description: Manage feature dependencies.
  name: Unleash Dependencies API
  slug: unleash-dependencies-api
- description: Create, update, delete, enable or disable [environments](https://docs.getunleash.io/concepts/environments) for this Unleash instance.
  name: Unleash Environments API
  slug: unleash-environments-api
- description: Read events from this Unleash instance.
  name: Unleash Events API
  slug: unleash-events-api
- description: Manage [feature flag types](https://docs.getunleash.io/concepts/feature-flags#feature-flag-types).
  name: Unleash Feature Types API
  slug: unleash-feature-types-api
- description: Create, update, and delete [feature flags](https://docs.getunleash.io/concepts/feature-flags).
  name: Unleash Features API
  slug: unleash-features-api
- description: The [Frontend API](https://docs.getunleash.io/concepts/front-end-api) is used for connecting client-side (frontend) applications to Unleash.
  name: Unleash Frontend API API
  slug: unleash-frontend-api-api
- description: '[Import and export](https://docs.getunleash.io/concepts/import-export) the state of your Unleash instance.'
  name: Unleash Import/Export API
  slug: unleash-import-export-api
- description: Instance admin endpoints used to manage the Unleash instance itself.
  name: Unleash Instance Admin API
  slug: unleash-instance-admin-api
- description: Enable/disable the maintenance mode of Unleash.
  name: Unleash Maintenance API
  slug: unleash-maintenance-api
- description: Register, read, or delete metrics recorded by Unleash.
  name: Unleash Metrics API
  slug: unleash-metrics-api
- description: API for managing [notifications](https://docs.getunleash.io/concepts/notifications).
  name: Unleash Notifications API
  slug: unleash-notifications-api
- description: Endpoints related to the operational status of this Unleash instance.
  name: Unleash Operational API
  slug: unleash-operational-api
- description: Create, update, and delete [Personal access tokens](https://docs.getunleash.io/concepts/api-tokens-and-client-keys#personal-access-tokens).
  name: Unleash Personal access tokens API
  slug: unleash-personal-access-tokens-api
- description: Evaluate an Unleash context against your feature flags.
  name: Unleash Playground API
  slug: unleash-playground-api
- description: Create, update, and delete [Unleash projects](https://docs.getunleash.io/concepts/projects).
  name: Unleash Projects API
  slug: unleash-projects-api
- description: Create, update, and delete [Unleash Public Signup tokens](https://docs.getunleash.io/concepts/public-signup-tokens).
  name: Unleash Public signup tokens API
  slug: unleash-public-signup-tokens-api
- description: API for managing [release templates](https://docs.getunleash.io/concepts/release-templates).
  name: Unleash Release Templates API
  slug: unleash-release-templates-api
- description: Search for features.
  name: Unleash Search API
  slug: unleash-search-api
- description: Create, update, delete, and manage [segments](https://docs.getunleash.io/concepts/segments).
  name: Unleash Segments API
  slug: unleash-segments-api
- description: Endpoints for managing [Service Accounts](https://docs.getunleash.io/concepts/service-accounts), which enable programmatic access to the Unleash API.
  name: Unleash Service Accounts API
  slug: unleash-service-accounts-api
- description: Create, update, delete, manage [custom strategies](https://docs.getunleash.io/concepts/activation-strategies#custom-strategies).
  name: Unleash Strategies API
  slug: unleash-strategies-api
- description: Create, update, and delete [tags and tag types](https://docs.getunleash.io/concepts/feature-flags#tags).
  name: Unleash Tags API
  slug: unleash-tags-api
- description: API for information about telemetry collection
  name: Unleash Telemetry API
  slug: unleash-telemetry-api
- description: Endpoints related to unknown flags.
  name: Unleash Unknown Flags API
  slug: unleash-unknown-flags-api
- description: Endpoints related to [Unleash Edge](https://docs.getunleash.io/unleash-edge).
  name: Unleash Unleash Edge API
  slug: unleash-unleash-edge-api
- description: Experimental endpoints that may change or disappear at any time.
  name: Unleash Unstable API
  slug: unleash-unstable-api
- description: Manage users and passwords.
  name: Unleash Users API
  slug: unleash-users-api
artifact_total: 53
collections:
- collection_type: open
  name: Unleash Admin API
  slug: open-unleash-admin-api
- collection_type: open
  name: Unleash Client API
  slug: open-unleash-client-api
- collection_type: open
  name: Unleash Frontend API
  slug: open-unleash-frontend-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unleash-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unleash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unleash-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getunleash
- group: company
  title: ''
  type: Website
  url: https://www.getunleash.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getunleash.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Unleash/unleash
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getunleash.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.getunleash.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Unleash/unleash/releases
- group: build
  title: ''
  type: SDKs
  url: https://docs.getunleash.io/reference/sdks
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/vocabulary/unleash-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/json-ld/unleash-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/json-schema/unleash-feature-flag-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.getunleash.io/llms.txt
created: '2026-03-16'
description: Unleash is the open-source feature management platform enabling progressive delivery, A/B testing, and canary releases through feature flags (feature toggles). Teams use Unleash to decouple code deployments from feature releases, control rollouts by user segment, run experiments with variants, and maintain kill switches for rapid incident response. Available as open-source (self-hosted) and as Unleash Cloud (managed).
examples:
- key_count: 2
  name: Unleash Client Features Example
  slug: unleash-client-features-example
- key_count: 2
  name: Unleash Create Feature Flag Example
  slug: unleash-create-feature-flag-example
- key_count: 2
  name: Unleash Toggle Feature Example
  slug: unleash-toggle-feature-example
finops:
- name: Unleash Finops
  service_category: Developer Tools
  slug: unleash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unleash.png
json_schemas:
- name: Unleash Feature Flag
  property_count: 13
  slug: unleash-feature-flag
json_structures:
- name: Unleash Feature Flag Structure
  property_count: 0
  slug: unleash-feature-flag-structure
jsonld:
- class_count: 11
  name: Unleash Context
  property_count: 27
  slug: unleash-context
layout: provider
modified: '2026-05-19'
name: Unleash
nav: Providers
network: true
overview: 'Unleash publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Client API, Addons API, Admin UI API, and 33 more. Tagged areas include Feature Flags, Feature Management, Progressive Delivery, A/B Testing, and Open Source.


  The Unleash catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Unleash''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, changelog, and 9 more developer resources.'
plans:
- name: Unleash Plans Pricing
  plan_count: 2
  slug: unleash-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Unleash Rate Limits
  slug: unleash-rate-limits
rules:
- name: Unleash API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unleash-jsonschema-spectral-rules
- name: Unleash API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 4
  slug: unleash-rules
score:
  band: developing
  composite: 50.2
  delta: -5.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/screenshots/unleash-2026-06-20T200436.png
security:
- kind: authentication
  name: Unleash Authentication
  slug: unleash-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Unleash Domain Security
  slug: unleash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: unleash
tags:
- Feature Flags
- Feature Management
- Progressive Delivery
- A/B Testing
- Open Source
- Developer Tools
website: https://www.getunleash.io
---
