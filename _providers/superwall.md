---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 159
  human_in_the_loop: 5
  name: Superwall Agentic Access
  operation_count: 285
  slug: superwall-agentic-access
  summary_line: 285 operations · 159 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: CRUD for organization-scoped App Store Connect API key configurations. Pairs with the transparent proxy at `/app-store-connect/proxy/:team_id/*`.
  name: Superwall App Store Connect Configurations V2 API
  slug: superwall-app-store-connect-configurations-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Request, track and cancel the erasure of an end user's data (GDPR Art. 17).
  name: Superwall App User Erasures V2 API
  slug: superwall-app-user-erasures-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage the browser-origin allowlist used to authorize WEBAPP checkout for an application.
  name: Superwall Application Webapp Origins V2 API
  slug: superwall-application-webapp-origins-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage media assets (images and videos) for reuse across paywalls.
  name: Superwall Assets V2 API
  slug: superwall-assets-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'Query the V2 API audit log. Each entry records one served request: the caller, endpoint, outcome, and any auth/authz failure. Scoped to an organization.'
  name: Superwall Audit Logs V2 API
  slug: superwall-audit-logs-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage campaigns, placements, and audiences. A Campaign controls when and to whom paywalls are displayed. Campaigns are scoped to a specific application (per-platform) since triggers and audience rule
  name: Superwall Campaigns V2 API
  slug: superwall-campaigns-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Annotations mark what happened on an application's timeline, such as a release, a feature by the App Store or a marketing campaign. Every time-series chart for the application draws them, for everyone
  name: Superwall Chart Annotations API
  slug: superwall-chart-annotations-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Query chart data for analytics and reporting. Includes revenue metrics, subscription data, user analytics, and paywall performance. Chart data is read-only; annotations drawn on charts are managed wit
  name: Superwall Charts V2 API
  slug: superwall-charts-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Hosted, spend-capped AI inference for the Superwall CLI when no local coding agent is available.
  name: Superwall CLI Agent V2 API
  slug: superwall-cli-agent-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Report subscription lifecycle events from a custom store's own billing system.
  name: Superwall Custom Store Events API
  slug: superwall-custom-store-events-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'Manage the custom stores of a project: stores that sell through the customer''s own checkout.'
  name: Superwall Custom Stores API
  slug: superwall-custom-stores-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Demand Score analytics used by the dashboard. Requires charts:read scope.
  name: Superwall Demand Score V2 API
  slug: superwall-demand-score-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage entitlements and manual grants. An Entitlement represents a feature or capability that can be unlocked for users through product purchases or manual grants. Entitlements are scoped to a project
  name: Superwall Entitlements V2 API
  slug: superwall-entitlements-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: View event logs and retry failed event deliveries. Events represent messages sent to webhook endpoints.
  name: Superwall Events V2 API
  slug: superwall-events-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Configure an application's Google Play service-account credentials and Real-Time Developer Notification delivery.
  name: Superwall Google Play V2 API
  slug: superwall-google-play-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Query manual entitlement grants by device or user.
  name: Superwall Grants V2 API
  slug: superwall-grants-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Bulk import of users, aliases, attributes and subscription history into the subscriptions source of truth.
  name: Superwall Imports API
  slug: superwall-imports-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'Custom event names for one project/integration pair, read by integration-router on the webhook ingestion path. Authenticated with the internal service token as Authorization: Bearer <token>.'
  name: Superwall Integration Event Names (Service) API
  slug: superwall-integration-event-names-service-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: User-centric endpoints. These endpoints only require user authentication and do not require organization context.
  name: Superwall Me V2 API
  slug: superwall-me-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Onboarding milestone state for an application. Read-only; aggregates SDK events, product, and paywall signals for the dashboard quickstart guide.
  name: Superwall Onboarding V2 API
  slug: superwall-onboarding-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage dashboard member project access and organization API key project restrictions.
  name: Superwall Organization Access V2 API
  slug: superwall-organization-access-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage organization settings.
  name: Superwall Organizations V2 API
  slug: superwall-organizations-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'Resolve a numeric paywall id to its identifier. Authenticated with a preview capability (sat_ or API-minted pvt_) from the debugger deep link, sent as Authorization: Bearer <token>.'
  name: Superwall Paywall Resolver (Public) API
  slug: superwall-paywall-resolver-public-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Browse the global paywall template catalog. This endpoint is public and returns only globally-available templates.
  name: Superwall Paywall Templates (Public) API
  slug: superwall-paywall-templates-public-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage paywalls and paywall templates. A Paywall is a monetization screen shown to users. Paywalls are scoped to a specific application (per-platform) since their design and behavior are platform-spec
  name: Superwall Paywalls V2 API
  slug: superwall-paywalls-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'Manage products (in-app purchases and subscriptions). A Product represents a purchasable item shown on paywalls. Products are scoped to a project (cross-platform) rather than a single application, so '
  name: Superwall Products V2 API
  slug: superwall-products-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: The Project Transfers V2 API from Superwall — 6 operation(s) for project transfers v2.
  name: Superwall Project Transfers V2 API
  slug: superwall-project-transfers-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage projects for cross-platform app grouping. A Project groups multiple Applications (one per platform) for unified management.
  name: Superwall Projects V2 API
  slug: superwall-projects-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Proxy ClickHouse queries scoped to an organization. Compatible with the clickhouse-client CLI via --url flag.
  name: Superwall Query V2 API
  slug: superwall-query-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage retention configurations used by the realtime worker. Configurations are stored in Superwall and are not synced to Apple default-message APIs.
  name: Superwall Retention Configurations V2 API
  slug: superwall-retention-configurations-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage Apple default message mappings by environment, product, and locale.
  name: Superwall Retention Default Messages V2 API
  slug: superwall-retention-default-messages-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage retention messages for Apple subscription win-back. Messages are stored locally and uploaded to Apple for review.
  name: Superwall Retention Messages V2 API
  slug: superwall-retention-messages-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Dashboard onboarding actions for Apple retention messaging setup.
  name: Superwall Retention Messaging Onboarding V2 API
  slug: superwall-retention-messaging-onboarding-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: The retentionCampaignsV2 API from Superwall — 7 operation(s) for retentioncampaignsv2.
  name: Superwall Retention Campaigns V2 API
  slug: superwall-retentioncampaignsv2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'RevenueCat v1 API-compatible, read-only subscriber view backed by the subscription source of truth: the subscriber object with its entitlements, subscriptions, non-subscriptions, and attributes.'
  name: Superwall RevenueCat V1 (compatible) API
  slug: superwall-revenuecat-v1-compatible-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'RevenueCat v2 API-compatible, read-only customer views backed by the subscription source of truth: the customer object, their subscriptions, active entitlements, and identity-group aliases.'
  name: Superwall RevenueCat V2 (compatible) API
  slug: superwall-revenuecat-v2-compatible-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage surveys shown to users after paywall interactions. Surveys collect user feedback such as why they chose not to subscribe. Surveys are scoped to a specific application.
  name: Superwall Surveys V2 API
  slug: superwall-surveys-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage users, user attributes, events, and diagnostics for an application.
  name: Superwall Users V2 API
  slug: superwall-users-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Alias-aware user subscriptions, aliases, and synced attributes sourced from the subscriptions store.
  name: Superwall Users V3 API
  slug: superwall-users-v3-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Manage head script integrations for web2app paywall pages. Supports Facebook Pixel, Google Tag Manager, Console Logger, and custom scripts.
  name: Superwall Web2App Integrations V2 API
  slug: superwall-web2app-integrations-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: 'Manage webhook endpoints for receiving real-time event notifications. Delivery formats use dedicated Svix applications: `superwall` (default) and `superwall_v2`. Note: Webhook endpoints use iterator-b'
  name: Superwall Webhooks V2 API
  slug: superwall-webhooks-v2-api
- baseURL: https://api.superwall.com
  baseurl_source: declared
  description: Mint WorkOS Admin Portal links for organization administrators to self-configure SSO, Directory Sync, audit log streaming, and domain verification.
  name: Superwall WorkOS Organization Admin API
  slug: superwall-workos-organization-admin-api
artifact_total: 56
common:
- group: agent
  href: https://artifacts.apis.io/superwall/agentic-access/superwall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/superwall-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/superwall/plans/superwall-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/superwall-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/superwall/rules/superwall-rules.yml
  title: ''
  type: Spectral
  url: rules/superwall-rules.yml
- group: design
  href: https://artifacts.apis.io/superwall/json-ld/superwall-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/superwall-context.jsonld
- group: design
  href: https://artifacts.apis.io/superwall/vocabulary/superwall-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/superwall-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/superwall/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/superwall/data-model/superwall-data-model.yml
  title: ''
  type: DataModel
  url: data-model/superwall-data-model.yml
- group: design
  href: https://artifacts.apis.io/superwall/components/superwall-components.yml
  title: ''
  type: Components
  url: components/superwall-components.yml
- group: build
  href: https://artifacts.apis.io/superwall/cli/superwall-cli.yml
  title: ''
  type: CLI
  url: cli/superwall-cli.yml
- group: operate
  href: https://artifacts.apis.io/superwall/changelog/superwall-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/superwall-changelog.yml
- group: design
  href: https://artifacts.apis.io/superwall/conventions/superwall-conventions.yml
  title: ''
  type: Conventions
  url: conventions/superwall-conventions.yml
- group: auth
  href: https://artifacts.apis.io/superwall/authentication/superwall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/superwall-authentication.yml
- group: design
  href: https://artifacts.apis.io/superwall/errors/superwall-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/superwall-problem-types.yml
- group: design
  href: https://artifacts.apis.io/superwall/conformance/superwall-conformance.yml
  title: ''
  type: Conformance
  url: conformance/superwall-conformance.yml
- group: agent
  href: https://artifacts.apis.io/superwall/llms/superwall-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/superwall-llms.txt
- group: other
  href: https://artifacts.apis.io/superwall/hosts/superwall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/superwall-hosts.yml
- group: other
  href: https://artifacts.apis.io/superwall/vendors/superwall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/superwall-vendors.yml
- group: build
  href: https://artifacts.apis.io/superwall/packages/superwall-packages.yml
  title: ''
  type: SDKs
  url: packages/superwall-packages.yml
- group: build
  href: https://artifacts.apis.io/superwall/packages/superwall-packages.yml
  title: ''
  type: Packages
  url: packages/superwall-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://superwall.com/integrations/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superwall.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://superwall.com/case-studies/rizz-god
- group: auth
  href: https://artifacts.apis.io/superwall/security/superwall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superwall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superwall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://superwall.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://superwall.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://superwall.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://superwall.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://superwall.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://superwall.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superwall.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superwall.com/legal/privacy-policy
- group: operate
  title: ''
  type: Changelog
  url: https://superwall.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superwall
- group: start
  title: ''
  type: SignUp
  url: https://superwall.com/signup
- group: start
  title: ''
  type: Login
  url: https://superwall.com/login
created: '2026-10-28'
description: Superwall is a remote paywall platform for mobile apps, offering AI‑powered monetization tools that let developers build, A/B test, and optimize in‑app paywalls and subscription experiences without shipping an app update. It provides SDKs for iOS, Android, and Web, along with analytics, audience targeting, and flexible pricing plans to help apps grow revenue.
image: https://superwall.com/assets/og/default.png
json_schemas:
- name: AuditLogEntryWithActor
  property_count: 32
  slug: superwall-audit-log-entry-with-actor
- name: AuditLogList
  property_count: 5
  slug: superwall-audit-log-list
- name: CustomStoreEvent
  property_count: 15
  slug: superwall-custom-store-event
- name: DoctorReport
  property_count: 6
  slug: superwall-doctor-report
- name: Rule Conditions
  property_count: 3
  slug: superwall-rule-conditions-1
- name: Rule Conditions
  property_count: 3
  slug: superwall-rule-conditions
jsonld:
- class_count: 12
  name: Superwall Context
  property_count: 79
  slug: superwall-context
layout: provider
modified: '2026-10-28'
name: Superwall
nav: Providers
network: true
overview: 'Superwall publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Store Connect Configurations V2 API, App User Erasures V2 API, Application Webapp Origins V2 API, and 39 more. Tagged areas include Company, Monetization, Mobile, SDK, and Payments.


  The Superwall catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Superwall''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, API reference, support, and 29 more developer resources.'
plans:
- name: Superwall Plans Pricing
  plan_count: 4
  slug: superwall-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Superwall Rate Limits
  slug: superwall-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Superwall API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 4
  slug: superwall-rules
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 61.0
    developer_ergonomics: 77.9
    discoverability: 66.1
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Superwall Authentication
  slug: superwall-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Superwall Domain Security
  slug: superwall-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: create-project
  slug: superwall-create-project
slug: superwall
tags:
- Company
- Monetization
- Mobile
- SDK
- Payments
- Analytics
website: https://superwall.com/
---
