---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Firebase Agentic Access
  operation_count: 6
  slug: google-firebase-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 2
apis:
- description: The Firebase Authentication REST API enables developers to manage user authentication using email/password, phone, and federated identity providers such as Google, Facebook, and Apple. The API support
  name: Firebase Authentication REST API
  slug: firebase-authentication-rest-api
- description: 'The Firebase Hosting REST API allows developers to programmatically manage web hosting deployments on Firebase. It supports creating new releases, managing site versions, uploading files, configuring '
  name: Firebase Hosting REST API
  slug: firebase-hosting-rest-api
- description: The Firebase Remote Config API enables developers to change the behavior and appearance of their apps without requiring users to download an update. The API allows publishing new Remote Config templat
  name: Firebase Remote Config API
  slug: firebase-remote-config-api
- description: Operations for reading and writing database nodes
  name: Google Firebase Data API
  slug: google-firebase-data-api
- description: Send messages to devices and topics
  name: Google Firebase Messages API
  slug: google-firebase-messages-api
artifact_total: 33
collections:
- collection_type: postman
  name: Google Firebase Firebase Cloud Messaging API (FCM) Data API
  slug: postman-google-firebase-data-api
- collection_type: postman
  name: Google Firebase Firebase Cloud Messaging API (FCM) Data Messages API
  slug: postman-google-firebase-messages-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Firebase Firebase Cloud Messaging API (FCM)
  slug: open-firebase-cloud-messaging
- collection_type: open
  name: Google Firebase Firebase Realtime Database API
  slug: open-firebase-realtime-database
- collection_type: open
  name: Google Firebase Firebase Cloud Messaging API (FCM) Data API
  slug: open-google-firebase-data-api
- collection_type: open
  name: Google Firebase Firebase Cloud Messaging API (FCM) Data Messages API
  slug: open-google-firebase-messages-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-firebase/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-firebase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-firebase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-firebase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-firebase-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-firebase-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firebase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/firebase
- group: start
  title: ''
  type: GettingStarted
  url: https://firebase.google.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://firebase.google.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://firebase.google.com/docs/admin/setup
- group: start
  title: ''
  type: Console
  url: https://console.firebase.google.com
- group: build
  title: ''
  type: SDKs
  url: https://firebase.google.com/docs/libraries
- group: operate
  title: ''
  type: Support
  url: https://firebase.google.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firebase.google.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-firebase-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://firebase.blog/rss.xml
created: '2026-03-13'
description: Google Firebase is a comprehensive app development platform that provides backend services, SDKs, and APIs for building and scaling mobile and web applications, including authentication, real-time databases, cloud messaging, hosting, and analytics.
finops:
- name: Google Firebase Finops
  service_category: Mobile / Web Backend
  slug: google-firebase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-firebase.png
json_schemas:
- name: AndroidConfig
  property_count: 4
  slug: google-firebase-androidconfig
- name: ApnsConfig
  property_count: 2
  slug: google-firebase-apnsconfig
- name: Firebase Realtime Database Node
  property_count: 4
  slug: google-firebase-database-node
- name: DatabaseNode
  property_count: 0
  slug: google-firebase-databasenode
- name: Firebase Cloud Messaging Message
  property_count: 2
  slug: google-firebase-fcm-message
- name: Message
  property_count: 9
  slug: google-firebase-message
- name: Notification
  property_count: 3
  slug: google-firebase-notification
- name: SendMessageRequest
  property_count: 2
  slug: google-firebase-sendmessagerequest
- name: WebpushConfig
  property_count: 2
  slug: google-firebase-webpushconfig
json_structures:
- name: Google Firebase Structure
  property_count: 0
  slug: google-firebase-structure
jsonld:
- class_count: 0
  name: Google Firebase Context
  property_count: 5
  slug: google-firebase-context
layout: provider
modified: '2026-05-19'
name: Google Firebase
nav: Providers
network: true
overview: 'Google Firebase publishes 2 APIs on the [APIs.io](https://apis.io/) network: Data API and Messages API. Tagged areas include Analytics, Authentication, Backend-as-a-Service, Cloud Messaging, and Google Cloud.


  The Google Firebase catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Firebase''s developer surface includes authentication, getting-started guide, pricing, developer console, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Firebase Plans Pricing
  plan_count: 2
  slug: google-firebase-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 11
  name: Google Firebase Rate Limits
  slug: google-firebase-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Firebase API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: google-firebase-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Google Firebase API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 7
  slug: google-firebase-spectral-rules
scopes:
- name: Google Firebase Scopes
  scope_count: 1
  slug: google-firebase-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 66.0
    developer_ergonomics: 59.5
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-firebase/refs/heads/main/screenshots/google-firebase-2026-06-20T182200.png
security:
- kind: authentication
  name: Google Firebase Authentication
  slug: google-firebase-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Firebase Domain Security
  slug: google-firebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Firebase Vulnerability Disclosure
  slug: google-firebase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-firebase
tags:
- Analytics
- Authentication
- Backend-as-a-Service
- Cloud Messaging
- Google Cloud
- Hosting
- Mobile
- Real-Time Database
---
