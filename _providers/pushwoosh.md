---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Pushwoosh Agentic Access
  operation_count: 4
  slug: pushwoosh-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: Send push notifications, email, SMS and in-app messages to user audiences.
  name: Pushwoosh Messaging API
  slug: pushwoosh-messaging-api
- description: Register and manage devices and end-user profiles.
  name: Pushwoosh Devices & Users API
  slug: pushwoosh-devices-users-api
- description: Tags, filters and segments for dynamic audience targeting.
  name: Pushwoosh Audience & Segmentation API
  slug: pushwoosh-audience-segmentation-api
- description: Read campaign and message performance statistics.
  name: Pushwoosh Statistics API
  slug: pushwoosh-statistics-api
- description: The Messages API from Pushwoosh — 4 operation(s) for messages.
  name: Pushwoosh Messages API
  slug: pushwoosh-messages-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pushwoosh Messaging Messages API
  slug: open-pushwoosh-messages-api
- collection_type: open
  name: Pushwoosh Messaging API
  slug: open-pushwoosh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pushwoosh-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pushwoosh-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pushwoosh-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pushwoosh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pushwoosh
- group: company
  title: ''
  type: Website
  url: https://www.pushwoosh.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/pushwoosh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pushwoosh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pushwoosh-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.pushwoosh.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.pushwoosh.com/blog/
created: '2026-05-08'
description: Pushwoosh is a customer engagement platform offering push notifications, in-app messaging, email, SMS, and Live Activities for mobile and web. Strong segmentation and journey-builder.
finops:
- name: Pushwoosh Finops
  service_category: Notifications
  slug: pushwoosh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pushwoosh.png
layout: provider
modified: '2026-05-08'
name: Pushwoosh
nav: Providers
network: true
overview: 'Pushwoosh publishes 1 API on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include Notification, Push, Email, SMS, and Multi-Channel.


  Pushwoosh''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Pushwoosh Plans Pricing
  plan_count: 1
  slug: pushwoosh-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Pushwoosh Rate Limits
  slug: pushwoosh-rate-limits
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 23.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pushwoosh/refs/heads/main/screenshots/pushwoosh-2026-06-20T192320.png
security:
- kind: domain-security
  name: Pushwoosh Domain Security
  slug: pushwoosh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pushwoosh Trust Center
  slug: pushwoosh-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: pushwoosh
tags:
- Notification
- Push
- Email
- SMS
- Multi-Channel
website: https://www.pushwoosh.com/
---
