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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Heap Agentic Access
  operation_count: 5
  slug: heap-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 2
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
- baseURL: https://heapanalytics.com
  baseurl_source: spec
  description: The Add Account Properties API from Heap — 1 operation(s) for add account properties.
  name: Heap Add Account Properties API
  slug: heap-add-account-properties-api
- baseURL: https://heapanalytics.com
  baseurl_source: spec
  description: The Add User Properties API from Heap — 1 operation(s) for add user properties.
  name: Heap Add User Properties API
  slug: heap-add-user-properties-api
- baseURL: https://heapanalytics.com
  baseurl_source: spec
  description: The Identify API from Heap — 1 operation(s) for identify.
  name: Heap Identify API
  slug: heap-identify-api
- baseURL: https://heapanalytics.com
  baseurl_source: spec
  description: The Track API from Heap — 1 operation(s) for track.
  name: Heap Track API
  slug: heap-track-api
- baseURL: https://partner.example.com
  baseurl_source: spec
  description: 'Partner-registered webhook endpoints invoked by Heap. The only documented action type is `segment.users.sync`, which delivers delta adds/removes for a Heap behavioral segment. Signature verification: '
  name: Heap Webhooks API
  slug: heap-webhooks-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Heap Server-Side Add Account Properties API
  slug: open-heap-add-account-properties-api
- collection_type: open
  name: Heap Server-Side Add Account Properties Add User Properties API
  slug: open-heap-add-user-properties-api
- collection_type: open
  name: Heap Server-Side Add Account Properties Identify API
  slug: open-heap-identify-api
- collection_type: open
  name: Heap Server-Side Add Account Properties Track API
  slug: open-heap-track-api
- collection_type: open
  name: Heap Server-Side Add Account Properties Webhooks API
  slug: open-heap-webhooks-api
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
random_paper: 15
rate_limits:
- limit_count: 3
  name: Heap Rate Limits
  slug: heap-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 52.3
    developer_ergonomics: 41.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
