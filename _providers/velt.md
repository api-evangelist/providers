---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 35
  human_in_the_loop: 1
  name: Velt Agentic Access
  operation_count: 35
  slug: velt-agentic-access
  summary_line: 35 operations · 35 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: Workspace API keys and auth tokens.
  name: Velt Auth API
  slug: velt-auth-api
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: Comment threads and annotations rendered by the SDK.
  name: Velt Comments API
  slug: velt-comments-api
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: Documents and folders that collaboration attaches to.
  name: Velt Documents API
  slug: velt-documents-api
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: Notifications and inbox/email configuration.
  name: Velt Notifications API
  slug: velt-notifications-api
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: Top-level tenancy boundary.
  name: Velt Organizations API
  slug: velt-organizations-api
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: End users and user-group membership.
  name: Velt Users API
  slug: velt-users-api
- baseURL: https://api.velt.dev/v2
  baseurl_source: declared
  description: Advanced webhook endpoints and event subscriptions.
  name: Velt Webhooks API
  slug: velt-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Velt Data (REST) Auth API
  slug: open-velt-auth-api
- collection_type: open
  name: Velt Data (REST) Auth Comments API
  slug: open-velt-comments-api
- collection_type: open
  name: Velt Data (REST) Auth Documents API
  slug: open-velt-documents-api
- collection_type: open
  name: Velt Data (REST) Auth Notifications API
  slug: open-velt-notifications-api
- collection_type: open
  name: Velt Data (REST) Auth Organizations API
  slug: open-velt-organizations-api
- collection_type: open
  name: Velt Data (REST) Auth Users API
  slug: open-velt-users-api
- collection_type: open
  name: Velt Data (REST) Auth Webhooks API
  slug: open-velt-webhooks-api
- collection_type: open
  name: Velt Data (REST) API
  slug: open-velt
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/velt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/velt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/velt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/velt-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veltdev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/velt-dev
- group: company
  title: ''
  type: Website
  url: https://velt.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://velt.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/velt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/velt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/velt-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://velt.dev/blog
created: '2026-07-01'
description: Velt is a real-time collaboration platform delivered primarily as a client SDK (React components and framework wrappers) for adding presence, live cursors, comments, notifications, huddles, recordings, and live selection to applications. Its server-side surface is the Velt Data (REST) API at api.velt.dev plus signed, retried webhooks, letting backends read and write comments, users, organizations, folders, documents, notifications, and user groups programmatically.
finops:
- name: Velt Finops
  service_category: Developer Tools and Collaboration
  slug: velt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/velt.png
layout: provider
modified: '2026-07-01'
name: Velt
nav: Providers
network: true
overview: 'Velt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Comments API, Documents API, and 4 more. Tagged areas include Real-Time Collaboration, Comments, Presence, Notification, and SDK.


  Velt''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Velt Plans Pricing
  plan_count: 3
  slug: velt-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Velt Rate Limits
  slug: velt-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.6
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/velt/refs/heads/main/screenshots/velt-2026-09-02T165630.png
security:
- kind: authentication
  name: Velt Authentication
  slug: velt-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Velt Domain Security
  slug: velt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Velt Trust Center
  slug: velt-trust-center
  summary_line: SOC 2, HIPAA
slug: velt
tags:
- Real-Time Collaboration
- Comments
- Presence
- Notification
- SDK
- Webhook
website: https://velt.dev/
---
