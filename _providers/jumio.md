---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.7
  scored_at: '2026-08-24'
api_count: 14
apis:
- description: Initiates and retrieves ID verification transactions. Issues a token used to start the SDK or hosted web flow, accepts callback events when the verification is complete, and exposes endpoints to retri
  name: Jumio ID Verification API
  slug: id-verification
- description: Validates supporting documents beyond government ID - utility bills, bank statements, leases, and other proof-of-address artifacts. Returns extracted structured data and an authenticity decision.
  name: Jumio Document Verification API
  slug: document-verification
- description: Selfie-driven biometric reverification of returning customers. Compares a fresh selfie against the previously enrolled face graph for the same user and returns a match decision, used for high-risk eve
  name: Jumio Authentication API
  slug: authentication
- description: Frictionless reverification flow that recognizes returning trusted users with a single selfie - no need to rescan ID. Backed by the Jumio Identity Graph and reusable identity records.
  name: Jumio selfie.DONE API
  slug: selfie-done
- description: AI-powered AML, sanctions, PEP, and adverse-media screening. Supports one-off screening calls and ongoing monitoring of enrolled identities. Returns hits, categories, and risk-score metadata to feed c
  name: Jumio Screening API (AML / Watchlist)
  slug: screening
- description: Returns enriched risk-signal data on a user (device, behavioural, network, and identity-graph signals) for layered risk scoring without requiring a full verification round-trip.
  name: Jumio Risk Signals API
  slug: risk-signals
- description: Retrieves stored transaction details, scanned documents, similarity scores, and decision audit history for an existing transaction. Used by compliance teams for regulatory recordkeeping and dispute re
  name: Jumio Retrieval API
  slug: retrieval
- description: Server-to-server callback delivering verification results. Jumio POSTs the final decision and metadata to a customer-configured URL once a transaction reaches a terminal state. Customers verify the so
  name: Jumio Callback / Webhook
  slug: callback
- description: Browser-based client SDK that hosts the verification UI, captures documents and selfies, and streams them to Jumio. Initialised with a token from the ID Verification API and configured per-customer fo
  name: Jumio Web SDK
  slug: web-sdk
- description: Native iOS SDK (Swift) that captures ID, supporting documents, and selfie biometrics, with on-device pre-checks before streaming to Jumio.
  name: Jumio Mobile SDK (iOS)
  slug: mobile-sdk-ios
- description: Native Android SDK (Java/Kotlin) that captures ID, supporting documents, and selfie biometrics, with on-device pre-checks before streaming to Jumio.
  name: Jumio Mobile SDK (Android)
  slug: mobile-sdk-android
- description: React Native plugin wrapping the iOS and Android SDKs for cross-platform mobile apps.
  name: Jumio React Native Plugin
  slug: mobile-react
- description: Flutter plugin wrapping the iOS and Android SDKs for Flutter applications. MIT-licensed.
  name: Jumio Flutter Plugin
  slug: mobile-flutter
- description: Apache Cordova plugin wrapping the iOS and Android SDKs for hybrid Cordova apps.
  name: Jumio Cordova Plugin
  slug: mobile-cordova
artifact_total: 21
asyncapis:
- description: Server-to-server callback delivered by the Jumio KYX Platform once a workflow execution reaches a terminal or notable state. Jumio POSTs a JSON document to a customer-configured callback URL (set eith
  name: Jumio KYX Workflow Callback
  slug: jumio-callback-asyncapi
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Jumio/web-sdk/issues
- group: auth
  title: ''
  type: TrustCenter
  url: security/jumio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jumio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jumio-corporation
- group: company
  title: ''
  type: Website
  url: https://www.jumio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.jumio.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Jumio
- group: commercial
  title: ''
  type: Plans
  url: plans/jumio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jumio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jumio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.jumio.com/feed/
created: '2026-05-08'
description: Jumio operates the KYX Platform, an end-to-end AI-driven identity verification, fraud prevention, and compliance suite. Backend APIs orchestrate ID verification, document verification, biometric authentication, AML and watchlist screening, risk signals, and reusable identity (selfie.DONE). Web client and native iOS / Android / React Native / Flutter / Cordova SDKs front the platform; backend Java and .NET SDKs wrap the REST API for server-side flows.
finops:
- name: Jumio Finops
  service_category: Identity Verification
  slug: jumio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jumio.png
layout: provider
modified: '2026-05-30'
name: Jumio
nav: Providers
network: true
overview: 'Jumio publishes 1 API on the [APIs.io](https://apis.io/) network: Callback / Webhook. Tagged areas include KYC, Identity Verification, Biometrics, AML, and Fraud Prevention.


  The Jumio catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Jumio''s developer surface includes documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Jumio Plans Pricing
  plan_count: 1
  slug: jumio-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Jumio Rate Limits
  slug: jumio-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Jumio API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: jumio-asyncapi-spectral-rules
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 28.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jumio/refs/heads/main/screenshots/jumio-2026-06-20T183827.png
security:
- kind: domain-security
  name: Jumio Domain Security
  slug: jumio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Jumio Trust Center
  slug: jumio-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: jumio
tags:
- KYC
- Identity Verification
- Biometrics
- AML
- Fraud Prevention
- KYX
website: https://www.jumio.com/
---
