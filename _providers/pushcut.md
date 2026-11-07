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
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Pushcut Agentic Access
  operation_count: 9
  slug: pushcut-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.pushcut.io/v1
  baseurl_source: declared
  description: For executing Automation Server actions
  name: Pushcut Automation Server API
  slug: pushcut-automation-server-api
- baseURL: https://api.pushcut.io/v1
  baseurl_source: declared
  description: For sending smart notifications
  name: Pushcut Notifications API
  slug: pushcut-notifications-api
- baseURL: https://api.pushcut.io/v1
  baseurl_source: declared
  description: For registering online actions
  name: Pushcut Subscriptions API
  slug: pushcut-subscriptions-api
artifact_total: 8
asyncapis:
- description: ''
  name: Pushcut Webhooks
  slug: pushcut-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/pushcut/agentic-access/pushcut-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pushcut-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/pushcut/rules/pushcut-rules.yml
  title: ''
  type: Spectral
  url: rules/pushcut-rules.yml
- group: design
  href: https://artifacts.apis.io/pushcut/vocabulary/pushcut-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pushcut-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pushcut/asyncapi/pushcut-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pushcut-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/pushcut/authentication/pushcut-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pushcut-authentication.yml
- group: design
  href: https://artifacts.apis.io/pushcut/errors/pushcut-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pushcut-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pushcut/conformance/pushcut-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pushcut-conformance.yml
- group: other
  href: https://artifacts.apis.io/pushcut/hosts/pushcut-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pushcut-hosts.yml
- group: other
  href: https://artifacts.apis.io/pushcut/vendors/pushcut-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pushcut-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://pushcut.io/release-notes/2022-6
- group: docs
  title: ''
  type: APIReference
  url: https://pushcut.io/assets/swagger/oauth2-redirect.html
- group: auth
  href: https://artifacts.apis.io/pushcut/security/pushcut-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pushcut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pushcut.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pushcut.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pushcut.io/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pushcut.io/guides
- group: operate
  title: ''
  type: Support
  url: https://www.pushcut.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.pushcut.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pushcut.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pushcut.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pushcut.io/privacy
created: '2026-10-28'
description: Pushcut provides a platform for iOS shortcut automation, enabling users to trigger shortcuts, notifications, and actions from various sources such as location, time, HomeKit, and webhooks. It integrates with services like IFTTT, Zapier, Flow, and Make, offering a webhook API for custom integrations and allowing smart notifications to be sent to devices without opening the app.
image: https://pushcut.io/assets/pushcut-icon.png
layout: provider
modified: '2026-10-28'
name: Pushcut
nav: Providers
network: true
overview: 'Pushcut publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Automation Server API, Notifications API, and Subscriptions API. Tagged areas include Company, Automation, iOS, Shortcuts, and Webhook.


  The Pushcut catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Pushcut''s developer surface includes authentication, changelog, API reference, documentation, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Pushcut API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: pushcut-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 59.9
    developer_ergonomics: 34.5
    discoverability: 66.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pushcut/pushcut-2026-11-03T141724.png
security:
- kind: authentication
  name: Pushcut Authentication
  slug: pushcut-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pushcut Domain Security
  slug: pushcut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pushcut
tags:
- Company
- Automation
- iOS
- Shortcuts
- Webhook
- Integration
website: https://pushcut.io/
---
