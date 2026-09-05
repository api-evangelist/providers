---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Token-authenticated REST API for building in-app chat, split into User APIs and Admin APIs (users, contacts, recent/history chat, groups, media, metadata, presence, block/unblock, call logs, device to
  name: MirrorFly Chat Platform API
  slug: mirrorfly-chat-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.mirrorfly.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/custom-chat-api-mirrorfly-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/custom-chat-api-mirrorfly-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/custom-chat-api-mirrorfly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/custom-chat-api-mirrorfly-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/custom-chat-api-mirrorfly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/custom-chat-api-mirrorfly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/custom-chat-api-mirrorfly-problem-types.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/custom-chat-api-mirrorfly-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/custom-chat-api-mirrorfly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mirrorfly.com/chat-security.php
- group: commercial
  title: ''
  type: Plans
  url: plans/custom-chat-api-mirrorfly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/custom-chat-api-mirrorfly-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/custom-chat-api-mirrorfly-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/custom-chat-api-mirrorfly-lifecycle.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.mirrorfly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mirrorfly.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.mirrorfly.com/docs/platformapi/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mirrorfly.com/docs/platformapi/adminapis/get-started/
- group: operate
  title: ''
  type: Support
  url: https://www.mirrorfly.com/faq.php
- group: company
  title: ''
  type: Blog
  url: https://www.mirrorfly.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MirrorFly
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mirrorfly.com/pricing.php
- group: start
  title: ''
  type: SignUp
  url: https://console.mirrorfly.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mirrorfly.com/terms-and-conditions.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mirrorfly.com/privacy-policy.php
created: '2026-07-21'
description: MirrorFly is a self-hosted CPaaS providing token-authenticated REST Chat Platform APIs (User and Admin) plus SDKs for in-app chat, HD video/voice calling, VoIP, contact center, chatbot/conversational AI, and live streaming for web and mobile apps.
layout: provider
modified: '2026-09-03'
name: Custom Chat API | MirrorFly
nav: Providers
network: true
overview: 'Custom Chat API | MirrorFly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Chat API, Messaging, CPaaS, VoIP, and Voice.


  Custom Chat API | MirrorFly''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Custom Chat Api Mirrorfly Plans Pricing
  plan_count: 4
  slug: custom-chat-api-mirrorfly-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Custom Chat Api Mirrorfly Rate Limits
  slug: custom-chat-api-mirrorfly-rate-limits
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 43.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/custom-chat-api-mirrorfly/refs/heads/main/screenshots/custom-chat-api-mirrorfly-2026-07-25T211005.png
security:
- kind: authentication
  name: Custom Chat Api Mirrorfly Authentication
  slug: custom-chat-api-mirrorfly-authentication
  summary_line: custom-token · 1 scheme
- kind: domain-security
  name: Custom Chat Api Mirrorfly Domain Security
  slug: custom-chat-api-mirrorfly-domain-security
  summary_line: TLSv1.2 · DMARC
slug: custom-chat-api-mirrorfly
tags:
- Chat API
- Messaging
- CPaaS
- VoIP
- Voice
- Video Calling
- Contact Center
- Conversational AI
- Chatbots
- Live Streaming
website: https://www.mirrorfly.com
---
