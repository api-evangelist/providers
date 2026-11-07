---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://www.leanplum.com'', ''status'': 301, ''note'': ''declared website redirects to https://clevertap.com:443/ — a different registrable domain (leanplum.com -> clevertap.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Leanplum Agentic Access
  operation_count: 27
  slug: leanplum-agentic-access
  summary_line: 27 operations · 15 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The A/B Tests API from Leanplum — 3 operation(s) for a/b tests.
  name: Leanplum A/B Tests API
  slug: leanplum-a-b-tests-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The Campaigns API from Leanplum — 1 operation(s) for campaigns.
  name: Leanplum Campaigns API
  slug: leanplum-campaigns-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The Export Data API from Leanplum — 8 operation(s) for export data.
  name: Leanplum Export Data API
  slug: leanplum-export-data-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The Files and Variables API from Leanplum — 5 operation(s) for files and variables.
  name: Leanplum Files and Variables API
  slug: leanplum-files-and-variables-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The Import Data API from Leanplum — 2 operation(s) for import data.
  name: Leanplum Import Data API
  slug: leanplum-import-data-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The Messages API from Leanplum — 7 operation(s) for messages.
  name: Leanplum Messages API
  slug: leanplum-messages-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The User Behavior API from Leanplum — 9 operation(s) for user behavior.
  name: Leanplum User Behavior API
  slug: leanplum-user-behavior-api
- baseURL: https://api.leanplum.com/api
  baseurl_source: declared
  description: The User Information API from Leanplum — 7 operation(s) for user information.
  name: Leanplum User Information API
  slug: leanplum-user-information-api
artifact_total: 30
asyncapis:
- description: ''
  name: Leanplum Postbacks Webhooks
  slug: leanplum-postbacks-webhooks
collections:
- collection_type: open
  name: Leanplum A/B Tests API
  slug: open-leanplum-a-b-tests-api
- collection_type: open
  name: API
  slug: open-leanplum-api
- collection_type: open
  name: Leanplum A/B Tests Content & Variables API
  slug: open-leanplum-content-variables-api
- collection_type: open
  name: Leanplum A/B Tests Data Export API
  slug: open-leanplum-data-export-api
- collection_type: open
  name: Leanplum A/B Tests Events & Tracking API
  slug: open-leanplum-events-tracking-api
- collection_type: open
  name: Leanplum A/B Tests Messaging API
  slug: open-leanplum-messaging-api
- collection_type: open
  name: Leanplum A/B Tests Postbacks & Batch API
  slug: open-leanplum-postbacks-batch-api
- collection_type: open
  name: Leanplum A/B Tests User & Device Attributes API
  slug: open-leanplum-user-device-attributes-api
- collection_type: open
  name: Leanplum API
  slug: open-leanplum
common:
- group: other
  href: https://artifacts.apis.io/leanplum/capabilities/leanplum-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leanplum-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/clevertap/
- group: auth
  href: https://artifacts.apis.io/leanplum/authentication/leanplum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leanplum-authentication.yml
- group: agent
  href: https://artifacts.apis.io/leanplum/agentic-access/leanplum-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leanplum-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/leanplum/security/leanplum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leanplum-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Leanplum
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leanplum
- group: company
  title: ''
  type: Website
  url: https://www.leanplum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leanplum.com
- group: commercial
  href: https://artifacts.apis.io/leanplum/plans/leanplum-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leanplum-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/leanplum/rate-limits/leanplum-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leanplum-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leanplum/finops/leanplum-finops.yml
  title: ''
  type: FinOps
  url: finops/leanplum-finops.yml
- group: build
  href: https://artifacts.apis.io/leanplum/packages/leanplum-packages.yml
  title: ''
  type: Packages
  url: packages/leanplum-packages.yml
- group: build
  href: https://artifacts.apis.io/leanplum/packages/leanplum-packages.yml
  title: ''
  type: SDKs
  url: packages/leanplum-packages.yml
- group: agent
  href: https://artifacts.apis.io/leanplum/llms/leanplum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leanplum-llms.txt
- group: design
  href: https://artifacts.apis.io/leanplum/conformance/leanplum-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leanplum-conformance.yml
- group: auth
  href: https://artifacts.apis.io/leanplum/security/leanplum-trust-center.yml
  title: ''
  type: Compliance
  url: security/leanplum-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/leanplum/security/leanplum-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/leanplum-trust-center.yml
- group: design
  href: https://artifacts.apis.io/leanplum/errors/leanplum-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leanplum-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leanplum/lifecycle/leanplum-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leanplum-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/leanplum/conventions/leanplum-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leanplum-conventions.yml
- group: operate
  href: https://artifacts.apis.io/leanplum/changelog/leanplum-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leanplum-changelog.yml
- group: start
  href: https://artifacts.apis.io/leanplum/sandbox/leanplum-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/leanplum-sandbox.yml
- group: design
  href: https://artifacts.apis.io/leanplum/data-model/leanplum-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leanplum-data-model.yml
- group: design
  href: https://artifacts.apis.io/leanplum/asyncapi/leanplum-postbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/leanplum-postbacks-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/leanplum/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/leanplum/overlays/leanplum-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leanplum-api-overlay.yaml
- group: build
  title: ''
  type: Postman
  url: https://www.getpostman.com/collections/378a83c1424d632661d0
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leanplum.com/reference/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leanplum.com/reference/api-methods
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leanplum.com/reference/api-introduction
- group: operate
  title: ''
  type: Support
  url: https://docs.leanplum.com/docs/leanplum-help-center
- group: company
  title: ''
  type: Blog
  url: https://clevertap.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://clevertap.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.leanplum.com/dashboard/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevertap.com/terms-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevertap.com/privacy-policy/
created: '2026-07-03'
description: Leanplum is a mobile marketing and multichannel customer engagement platform offering push notifications, in-app and email messaging, behavioral event tracking and analytics, A/B testing, and remotely configurable content variables. Leanplum was acquired by CleverTap in 2022 and now operates as "Leanplum by CleverTap"; the brand and its documented REST API remain active while customers are migrated onto the CleverTap platform (CleverTap has wrapped its own methods behind the Leanplum API surface to smooth that transition). All API requests are made to https://api.leanplum.com/api and authenticated with an appId plus an operation-specific clientKey (production, development, data export, or content read-only).
finops:
- has_sources: true
  method: derived
  name: Leanplum Finops
  primary_unit: mau tier (up to 5,000 mau)
  service_category: ''
  slug: leanplum-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leanplum.png
layout: provider
modified: '2026-08-13'
name: Leanplum
nav: Providers
network: true
overview: 'Leanplum publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including A/B Tests API, Campaigns API, Export Data API, and 5 more. Tagged areas include Mobile Marketing, Customer Engagement, Push Notifications, Messaging, and A/B Testing.


  The Leanplum catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Leanplum''s developer surface includes authentication, documentation, changelog, sandbox, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Leanplum Plans Pricing
  plan_count: 3
  slug: leanplum-plans-pricing
- name: Leanplum Price Estimates
  plan_count: 0
  slug: leanplum-price-estimates
random_paper: 22
rate_limits:
- limit_count: 10
  name: Leanplum Rate Limits
  slug: leanplum-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Leanplum API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 4
  slug: leanplum-rules
score:
  band: exemplar
  composite: 67.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.3
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 48.5
    developer_ergonomics: 78.0
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/leanplum/leanplum-2026-07-25T224746.png
security:
- kind: authentication
  name: Leanplum Authentication
  slug: leanplum-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Leanplum Domain Security
  slug: leanplum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Leanplum Trust Center
  slug: leanplum-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, CCPA, HIPAA
skill_count: 3
skills:
- name: leanplum-export-data
  slug: leanplum-export-data
- name: leanplum-send-message
  slug: leanplum-send-message
- name: leanplum-track-behavior
  slug: leanplum-track-behavior
slug: leanplum
tags:
- Mobile Marketing
- Customer Engagement
- Push Notifications
- Messaging
- A/B Testing
- Analytics
- CleverTap
website: https://www.leanplum.com
---
