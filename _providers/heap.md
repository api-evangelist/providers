---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Heap Agentic Access
  operation_count: 5
  slug: heap-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 10
apis:
- description: The Heap Server-Side API allows developers to send track, identify, and add user properties events to Heap from backend servers. It supports sending custom events and user properties that cannot be ca
  name: Heap Server-Side API
  slug: server-side-api
- description: The Heap Track API enables developers to send custom track events from server-side applications to Heap. Each event includes an identity, event name, and optional properties. This API is used to captu
  name: Heap Track API
  slug: track-api
- description: The Heap Identify API allows developers to associate a user identity with Heap's automatically captured data from the server side. This enables linking anonymous user sessions to known user identities
  name: Heap Identify API
  slug: identify-api
- description: The Heap Add User Properties API enables developers to attach custom properties to user profiles from server-side applications. These properties can include attributes such as subscription tier, accou
  name: Heap Add User Properties API
  slug: add-user-properties-api
- description: The Heap Add Account Properties API allows developers to attach custom properties to account-level profiles from server-side applications. This is used for B2B analytics scenarios where users belong t
  name: Heap Add Account Properties API
  slug: add-account-properties-api
- description: The Add Account Properties API from Heap — 1 operation(s) for add account properties.
  name: Heap Add Account Properties API
  slug: heap-add-account-properties-api
- description: The Add User Properties API from Heap — 1 operation(s) for add user properties.
  name: Heap Add User Properties API
  slug: heap-add-user-properties-api
- description: The Identify API from Heap — 1 operation(s) for identify.
  name: Heap Identify API
  slug: heap-identify-api
- description: The Track API from Heap — 1 operation(s) for track.
  name: Heap Track API
  slug: heap-track-api
- description: 'Partner-registered webhook endpoints invoked by Heap. The only documented action type is `segment.users.sync`, which delivers delta adds/removes for a Heap behavioral segment. Signature verification: '
  name: Heap Webhooks API
  slug: heap-webhooks-api
artifact_total: 34
collections:
- collection_type: open
  name: Heap Partner Webhooks (Data-out API)
  slug: open-heap-webhooks
- collection_type: open
  name: Heap Server-Side API
  slug: open-heap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/heap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/heap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heap-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heap-inc-
- group: company
  title: ''
  type: Website
  url: https://www.heap.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.heap.io
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.heap.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.heap.io/reference/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.heap.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heap.io/pricing
- group: start
  title: ''
  type: Login
  url: https://heapanalytics.com/app/login
- group: start
  title: ''
  type: Signup
  url: https://heapanalytics.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.heap.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heap.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heap.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.heap.io
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.heap.io/llms.txt
created: '2026-03-26'
description: Heap is a digital analytics platform that automatically captures every user interaction on web and mobile applications without requiring manual event tracking code. It provides product analytics, session replay, and behavioral data science capabilities to help teams understand user behavior and improve digital experiences.
features:
- 'Free: 10K monthly sessions, 6 months history, SSO'
- 'Growth: custom sessions, Sense AI Assistant, 12 months history'
- 'Pro: account analytics, engagement matrix, session replay add-on'
- 'Premier: data warehouse integration, region-specific storage, dedicated CSM'
- Auto-capture for click/page-view tracking
- Define events retroactively
- Funnels, retention, paths analysis
- Account-based analytics (Pro+)
- Behavioral cohorts
- REST API at heapanalytics.com/api
- 'Track API: high-throughput (auto-scales)'
- 'REST: 60 req/min/project'
- 'Bulk identify: 1,000 users/request'
- Webhooks for cohorts and segments
- Acquired by Contentsquare (2023)
- OAuth + API tokens
finops:
- name: Heap Finops
  service_category: Product Analytics
  slug: heap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heap.png
layout: provider
modified: '2026-05-30'
name: Heap
nav: Providers
network: true
overview: 'Heap publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Add Account Properties API, Add User Properties API, Identify API, and 2 more. Tagged areas include Analytics, Autocapture, Digital Analytics, Product Analytics, and Session Replay.


  Heap''s developer surface includes documentation, getting-started guide, authentication, engineering blog, pricing, signup flow, support, and 11 more developer resources.'
plans:
- name: Heap Plans Pricing
  plan_count: 4
  slug: heap-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Heap Rate Limits
  slug: heap-rate-limits
score:
  band: developing
  composite: 54.6
  delta: 2.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 52.6
    developer_ergonomics: 37.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 52.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heap/refs/heads/main/screenshots/heap-2026-06-20T182602.png
security:
- kind: domain-security
  name: Heap Domain Security
  slug: heap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Heap Trust Center
  slug: heap-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: heap
tags:
- Analytics
- Autocapture
- Digital Analytics
- Product Analytics
- Session Replay
- User Behavior
website: https://www.heap.io
---
