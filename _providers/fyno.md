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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Fyno Agentic Access
  operation_count: 23
  slug: fyno-agentic-access
  summary_line: 23 operations · 20 acting
api_count: 1
apis:
- description: REST API for creating, reading, updating, and deleting user profiles within the Fyno platform. Supports adding and updating channel-specific destination data, merging user profiles, and managing chann
  name: Fyno User Profiles API
  slug: user-profiles
- description: REST API for managing user notification preferences and subscription settings. Allows retrieval and updates of per-user channel preferences and opt-in/opt-out controls for notification categories.
  name: Fyno User Subscriptions API
  slug: user-subscriptions
- description: 'REST API for managing the global suppression list to prevent unwanted notifications from being sent to specific users. Supports fetching the list, adding users to suppression, and removing suppressed '
  name: Fyno Suppression List API
  slug: suppression-list
- description: 'OTP and TOTP-based verification API for authenticating users via SMS, email, or authenticator apps. Bundled with Growth and above plans at no additional cost. Supports mobile SDKs for iOS (Swift) and '
  name: Fyno Verify API
  slug: verify
- baseURL: https://api.fyno.io/v1
  baseurl_source: declared
  description: The Fire an Event API from Fyno — 2 operation(s) for fire an event.
  name: Fyno Fire an Event API
  slug: fyno-fire-an-event-api
- baseURL: https://api.fyno.io/v1
  baseurl_source: declared
  description: The Fyno Verify API from Fyno — 1 operation(s) for fyno verify.
  name: Fyno Fyno Verify API
  slug: fyno-fyno-verify-api
- baseURL: https://api.fyno.io/v1
  baseurl_source: declared
  description: The Manage User Profiles API from Fyno — 6 operation(s) for manage user profiles.
  name: Fyno Manage User Profiles API
  slug: fyno-manage-user-profiles-api
- baseURL: https://api.fyno.io/v1
  baseurl_source: declared
  description: The Manage User Subscriptions & Preferences API from Fyno — 2 operation(s) for manage user subscriptions & preferences.
  name: Fyno Manage User Subscriptions & Preferences API
  slug: fyno-manage-user-subscriptions-preferences-api
- baseURL: https://api.fyno.io/v1
  baseurl_source: declared
  description: The Suppression List API from Fyno — 1 operation(s) for suppression list.
  name: Fyno Suppression List API
  slug: fyno-suppression-list-api
- baseURL: https://api.fyno.io/v1
  baseurl_source: declared
  description: The User Properties API from Fyno — 7 operation(s) for user properties.
  name: Fyno User Properties API
  slug: fyno-user-properties-api
artifact_total: 38
collections:
- collection_type: postman
  name: Fyno Rest Fire an Event API
  slug: postman-fyno-fire-an-event-api
- collection_type: postman
  name: Fyno Rest Fire an Event Fyno Verify API
  slug: postman-fyno-fyno-verify-api
- collection_type: postman
  name: Fyno Rest Fire an Event Manage User Profiles API
  slug: postman-fyno-manage-user-profiles-api
- collection_type: postman
  name: Fyno Rest Fire an Event Manage User Subscriptions & Preferences API
  slug: postman-fyno-manage-user-subscriptions-preferences-api
- collection_type: postman
  name: Fyno Rest Fire an Event Suppression List API
  slug: postman-fyno-suppression-list-api
- collection_type: postman
  name: Fyno Rest Fire an Event User Properties API
  slug: postman-fyno-user-properties-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fyno Rest Fire an Event API
  slug: open-fyno-fire-an-event-api
- collection_type: open
  name: Fyno Rest Fire an Event Fyno Verify API
  slug: open-fyno-fyno-verify-api
- collection_type: open
  name: Fyno Rest Fire an Event Manage User Profiles API
  slug: open-fyno-manage-user-profiles-api
- collection_type: open
  name: Fyno Rest Fire an Event Manage User Subscriptions & Preferences API
  slug: open-fyno-manage-user-subscriptions-preferences-api
- collection_type: open
  name: Fyno Rest Fire an Event Suppression List API
  slug: open-fyno-suppression-list-api
- collection_type: open
  name: Fyno Rest Fire an Event User Properties API
  slug: open-fyno-user-properties-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fyno/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fyno-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fyno-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fyno-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fyno-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fyno.io/
- group: docs
  title: ''
  type: Documentation
  url: https://fyno.io/docs/home
- group: docs
  title: ''
  type: APIReference
  url: https://fyno.io/docs/api-reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fynoio
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/fyno-io
- group: other
  title: ''
  type: X
  url: https://x.com/fynohq
- group: company
  title: ''
  type: Blog
  url: https://fyno.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fyno.io/ratecard
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fyno.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://fyno.io/docs/release-notes
- group: commercial
  title: ''
  type: Plans
  url: plans/fyno-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fyno-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fyno-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fyno-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/fyno-context.jsonld
created: '2026-06-12'
description: Fyno is a notification routing and orchestration platform that provides a single unified REST API for sending and managing notifications across 10+ communication channels including email, SMS, push, WhatsApp, in-app, RCS, voice, and iMessage. Engineering teams integrate once to gain access to 100+ pre-built provider integrations, a no-code workflow builder, and an advanced routing engine with automated throttling. The platform provides detailed analytics, delivery tracking, user profile management, suppression lists, and campaign management capabilities with a 99.99% uptime SLA. Fyno also includes Fyno Verify (OTP/TOTP authentication) and Fyno Shorty (URL shortener) as bundled services.
examples:
- key_count: 4
  name: Fyno Bulk Notify Example
  slug: fyno-bulk-notify-example
- key_count: 4
  name: Fyno Create User Profile Example
  slug: fyno-create-user-profile-example
- key_count: 4
  name: Fyno Notify Single User Example
  slug: fyno-notify-single-user-example
- key_count: 4
  name: Fyno Notify With Explicit Channels Example
  slug: fyno-notify-with-explicit-channels-example
finops:
- name: Fyno Finops
  service_category: ''
  slug: fyno-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fyno.png
json_schemas:
- name: Fyno Notification Event
  property_count: 6
  slug: fyno-notification-event
- name: Fyno User Profile
  property_count: 5
  slug: fyno-user-profile
jsonld:
- class_count: 0
  name: Fyno Context
  property_count: 26
  slug: fyno-context
layout: provider
modified: '2026-06-12'
name: Fyno
nav: Providers
network: true
overview: 'Fyno publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Fire an Event API, Fyno Verify API, Manage User Profiles API, and 3 more. Tagged areas include Notification, Messaging, Communications, Push Notifications, and Email.


  The Fyno catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fyno''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, changelog, and 14 more developer resources.'
plans:
- name: Fyno Plans Pricing
  plan_count: 5
  slug: fyno-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Fyno Rate Limits
  slug: fyno-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Fyno API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fyno-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 24.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 25.0
    contract_quality: 69.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fyno/refs/heads/main/screenshots/fyno-2026-06-20T181627.png
security:
- kind: authentication
  name: Fyno Authentication
  slug: fyno-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fyno Domain Security
  slug: fyno-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fyno Trust Center
  slug: fyno-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: fyno
tags:
- Notification
- Messaging
- Communications
- Push Notifications
- Email
- SMS
- WhatsApp
- In-App
- Orchestration
- Multi-Channel
website: https://fyno.io/
---
