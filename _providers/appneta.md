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
  - '{''url'': ''https://www.appneta.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.broadcom.com/products/software/network-management/appneta — a different registrable domain (appneta.com -> broadcom.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-09-17'
api_count: 2
apis:
- description: RESTful API for AppNeta Performance Manager, covering monitoring policies and policy groups, web paths, web applications (locations, targets, user flows), monitoring points, alarm connectors (v4), and
  name: AppNeta Performance Manager API
  slug: appneta-performance-manager-api
- description: Token-authenticated REST API for the AppNeta SaaS platform. v4 (Intelligent Alarms) and v3 (Classic) expose monitoring data, monitoring policies, Monitoring Point provisioning, web-application and net
  name: AppNeta REST API
  slug: appneta-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Appneta Event Integration Webhooks
  slug: appneta-event-integration-webhooks
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/broadcom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA.html
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api/api-v4.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/authentication/appneta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appneta-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.broadcom.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appneta
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/packages/appneta-packages.yml
  title: ''
  type: Packages
  url: packages/appneta-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/security/appneta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appneta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appneta.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.broadcom.com/appneta
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/tracelytics/
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/getting-started.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.broadcom.com/services/appneta
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/lifecycle/appneta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appneta-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/changelog/appneta-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appneta-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta/GA/integrate/api/api-v3.html#title-appneta-api_api-changes
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/errors/appneta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appneta-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/rate-limits/appneta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appneta-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/conventions/appneta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appneta-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/components/appneta-components.yml
  title: ''
  type: Components
  url: components/appneta-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/asyncapi/appneta-event-integration-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/appneta-event-integration-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/plans/appneta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appneta-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/llms/appneta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appneta-llms.txt
created: '2026-07-17'
description: AppNeta is a network performance monitoring (NPM) platform for the distributed, cloud-connected enterprise, now delivered as a Broadcom product under its IT Operations Management / Network Management portfolio. AppNeta Performance Manager continuously measures network paths, delivery quality, usage, and end-user application experience across SaaS, cloud, and internet paths using a combination of active (synthetic) and passive monitoring from distributed monitoring points. It exposes a RESTful API (v3 for AppNeta Classic and v4 for AppNeta with Intelligent Alarms) for programmatic access to monitoring policies, web paths, web applications, alarm connectors, and event/observer integrations, authenticated with API access tokens. As of February 2026 the API interface and documentation were upgraded from Swagger to OpenAPI 3.0. AppNeta was originally an independent, Battery Ventures-backed company before joining Broadcom.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appneta.png
layout: provider
modified: '2026-09-16'
name: AppNeta
nav: Providers
network: true
overview: 'AppNeta publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Network Monitoring, Network Performance Monitoring, Observability, and Application Performance Monitoring.


  The AppNeta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppNeta''s developer surface includes documentation, API reference, authentication, support, getting-started guide, changelog, and 20 more developer resources.'
plans:
- name: Appneta Plans Pricing
  plan_count: 0
  slug: appneta-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 10
  name: Appneta Rate Limits
  slug: appneta-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 42.9
    discoverability: 68.5
    operational_transparency: 73.7
  previous_composite: 39.6
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/appneta/refs/heads/main/screenshots/appneta-2026-07-25T200818.png
security:
- kind: authentication
  name: Appneta Authentication
  slug: appneta-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appneta Domain Security
  slug: appneta-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: appneta
tags:
- Company
- Network Monitoring
- Network Performance Monitoring
- Observability
- Application Performance Monitoring
- Synthetic Monitoring
- Monitoring
- Broadcom
website: https://www.appneta.com/
---
