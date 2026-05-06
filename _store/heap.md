---
aid: heap
name: Heap
description: Heap is a digital analytics platform that automatically captures every user interaction on web and mobile applications without requiring manual event tracking code. It provides product analytics, session replay, and behavioral data science capabilities to help teams understand user behavior and improve digital experiences.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Autocapture
  - Digital Analytics
  - Product Analytics
  - Session Replay
  - User Behavior
url: https://raw.githubusercontent.com/api-evangelist/heap/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: heap:server-side-api
    name: Heap Server-Side API
    description: The Heap Server-Side API allows developers to send track, identify, and add user properties events to Heap from backend servers. It supports sending custom events and user properties that cannot be captured through Heap's automatic client-side tracking, such as server-side transactions, subscription changes, and backend process completions.
    humanURL: https://developers.heap.io/reference/server-side-apis-overview
    tags:
      - Analytics
      - Events
      - Server-Side
      - Tracking
    properties:
      - type: Documentation
        url: https://developers.heap.io/reference/server-side-apis-overview
      - type: GettingStarted
        url: https://developers.heap.io/docs/getting-started
  - aid: heap:track-api
    name: Heap Track API
    description: The Heap Track API enables developers to send custom track events from server-side applications to Heap. Each event includes an identity, event name, and optional properties. This API is used to capture important backend events such as purchases, subscription upgrades, or other server-side actions that supplement Heap's automatic client-side tracking.
    humanURL: https://developers.heap.io/reference/track-1
    tags:
      - Analytics
      - Events
      - Tracking
    properties:
      - type: Documentation
        url: https://developers.heap.io/reference/track-1
  - aid: heap:identify-api
    name: Heap Identify API
    description: The Heap Identify API allows developers to associate a user identity with Heap's automatically captured data from the server side. This enables linking anonymous user sessions to known user identities when authentication or identification occurs on the backend rather than the client side.
    humanURL: https://developers.heap.io/reference/identify-1
    tags:
      - Analytics
      - Identity
      - Users
    properties:
      - type: Documentation
        url: https://developers.heap.io/reference/identify-1
  - aid: heap:add-user-properties-api
    name: Heap Add User Properties API
    description: The Heap Add User Properties API enables developers to attach custom properties to user profiles from server-side applications. These properties can include attributes such as subscription tier, account type, company name, or any other user-level data that enriches Heap's behavioral analytics and segmentation capabilities.
    humanURL: https://developers.heap.io/reference/add-user-properties-1
    tags:
      - Analytics
      - Properties
      - Users
    properties:
      - type: Documentation
        url: https://developers.heap.io/reference/add-user-properties-1
  - aid: heap:add-account-properties-api
    name: Heap Add Account Properties API
    description: The Heap Add Account Properties API allows developers to attach custom properties to account-level profiles from server-side applications. This is used for B2B analytics scenarios where users belong to organizations or accounts, enabling analysis at the account level in addition to the individual user level.
    humanURL: https://developers.heap.io/reference/add-account-properties-1
    tags:
      - Accounts
      - Analytics
      - B2B
      - Properties
    properties:
      - type: Documentation
        url: https://developers.heap.io/reference/add-account-properties-1
common:
  - type: Website
    url: https://www.heap.io
  - type: Documentation
    url: https://developers.heap.io
  - type: GettingStarted
    url: https://developers.heap.io/docs/getting-started
  - type: Authentication
    url: https://developers.heap.io/reference/authentication
  - type: Blog
    url: https://www.heap.io/blog
  - type: Pricing
    url: https://www.heap.io/pricing
  - type: Login
    url: https://heapanalytics.com/app/login
  - type: Signup
    url: https://heapanalytics.com/signup
  - type: Support
    url: https://help.heap.io
  - type: TermsOfService
    url: https://www.heap.io/terms-of-service
  - type: PrivacyPolicy
    url: https://www.heap.io/privacy-policy
  - type: StatusPage
    url: https://status.heap.io
  - type: Features
    data:
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
    sources:
      - https://heap.io/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
