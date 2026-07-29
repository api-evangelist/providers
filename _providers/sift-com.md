---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Sift Com Agentic Access
  operation_count: 16
  slug: sift-com-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 6
apis:
- description: Apply and retrieve decisions on Sift entities.
  name: Sift Decisions API
  slug: sift-com-decisions-api
- description: Send fraud and abuse signals to Sift for scoring.
  name: Sift Events API
  slug: sift-com-events-api
- description: Apply and remove fraud labels on Sift users.
  name: Sift Labels API
  slug: sift-com-labels-api
- description: Retrieve and recompute Sift risk scores.
  name: Sift Scores API
  slug: sift-com-scores-api
- description: Send, resend, and check verification challenges.
  name: Sift Verification API
  slug: sift-com-verification-api
- description: Inspect Sift Workflow evaluations.
  name: Sift Workflows API
  slug: sift-com-workflows-api
arazzos:
- description: Record a chargeback, label the user as fraudulent, and force a fresh score.
  name: Sift Chargeback Label And Rescore
  slug: sift-com-chargeback-label-rescore-workflow
- description: Score a login for account takeover and require verification when risk is high.
  name: Sift Login Step-Up Verification
  slug: sift-com-login-step-up-verification-workflow
- description: Pull a user's score, resolve a valid decision, apply it, and confirm the result.
  name: Sift Manual Review And Decide User
  slug: sift-com-review-and-decide-user-workflow
- description: Score a new account on signup and decision the user when risk is high.
  name: Sift Screen Account Creation
  slug: sift-com-screen-account-creation-workflow
- description: Score an order, confirm payment risk with the user score, and decision the order.
  name: Sift Screen Order And Transaction
  slug: sift-com-screen-order-transaction-workflow
- description: Score a transaction, read the payment score, and decision the user or session.
  name: Sift Transaction Score And Decide
  slug: sift-com-transaction-score-decision-workflow
- description: Trigger a synchronous workflow evaluation, list the user's runs, and inspect one.
  name: Sift Workflow Run Evaluation
  slug: sift-com-workflow-run-evaluation-workflow
artifact_total: 68
collections:
- collection_type: postman
  name: Sift Decisions API
  slug: postman-sift-decisions-api
- collection_type: postman
  name: Sift Events API
  slug: postman-sift-events-api
- collection_type: postman
  name: Sift Labels API
  slug: postman-sift-labels-api
- collection_type: postman
  name: Sift Score API
  slug: postman-sift-score-api
- collection_type: postman
  name: Sift Verification API
  slug: postman-sift-verification-api
- collection_type: postman
  name: Sift Workflows API
  slug: postman-sift-workflows-api
- collection_type: open
  name: Sift Decisions API
  slug: open-sift-decisions-api
- collection_type: open
  name: Sift Events API
  slug: open-sift-events-api
- collection_type: open
  name: Sift Labels API
  slug: open-sift-labels-api
- collection_type: open
  name: Sift Score API
  slug: open-sift-score-api
- collection_type: open
  name: Sift Verification API
  slug: open-sift-verification-api
- collection_type: open
  name: Sift Workflows API
  slug: open-sift-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sift-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sift-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sift-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sift/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-chargeback-label-rescore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-login-step-up-verification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-review-and-decide-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-screen-account-creation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-screen-order-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-transaction-score-decision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sift-com-workflow-run-evaluation-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://sift.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sift.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.sift.com/docs/curl/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.sift.com/tutorials
- group: auth
  title: ''
  type: Authentication
  url: https://developers.sift.com/docs/curl/api-overview/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.sift.com/docs/curl/api-overview/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sift.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://status.sift.com/history
- group: operate
  title: ''
  type: Support
  url: https://support.sift.com
- group: company
  title: ''
  type: Blog
  url: https://engineering.sift.com
- group: company
  title: ''
  type: Blog
  url: https://sift.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sift.com/legal-and-compliance
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sift.com/privacy-policy
- group: start
  title: ''
  type: Console
  url: https://console.sift.com
- group: start
  title: ''
  type: Signup
  url: https://console.sift.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SiftScience
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SiftScience/sift-react-native
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/siftscience
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/GetSift
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/SiftScience
- group: design
  title: ''
  type: SpectralRules
  url: rules/sift-com-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sift-com-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sift-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/sift-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sift-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sift-com-finops.yml
created: '2025-09-15T00:00:00.000Z'
description: Sift (formerly Sift Science) is the San Francisco-based Digital Trust and Safety platform that protects more than 700 global brands from payment fraud, account takeover, content abuse, promotion abuse, and money movement risk. Sift's APIs ingest user, device, payment, content, and verification events, return real-time risk scores per abuse type, automate decisions through Workflows, ship a Verification API for step-up challenges, and operate a Console for analyst case management. Sift was founded in 2011, processes more than one trillion events per year, and reports a median annual loss prevented of about $4.2M per customer.
examples:
- key_count: 5
  name: Sift Apply Decision Example
  slug: sift-apply-decision-example
- key_count: 15
  name: Sift Create Order Example
  slug: sift-create-order-example
features:
- description: Unified 0 to 100 risk score per abuse type powered by Sift's global trust network.
  name: Sift Score
- description: Visual rule and ML composition that automates accept, review, and block decisions.
  name: Workflows
- description: Analyst workbench for case management, queue review, and decisioning.
  name: Console
- description: JavaScript snippet plus iOS, Android, and React Native SDKs for device telemetry.
  name: Device Fingerprinting
- description: Inline scoring on the Events API via `return_score=true` for real-time decisioning.
  name: Synchronous Scoring
- description: Built-in SMS, email, phone, push, biometric, and security key verification with risk hooks.
  name: Verification
- description: Automated chargeback representment with network-tuned evidence packages.
  name: Dispute Management
- description: Sandbox API keys for safe integration and load testing.
  name: Sandbox Environment
finops:
- name: Sift Com Finops
  service_category: Security and Identity
  slug: sift-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sift-com.png
integrations:
- description: Card-not-present scoring on Stripe transactions.
  name: Stripe
- description: Risk decisioning integrated with Adyen payment flows.
  name: Adyen
- description: Risk decisioning integrated with Braintree.
  name: Braintree
- description: Sift app for the Shopify ecosystem.
  name: Shopify
- description: Login risk decisioning via Sift signals.
  name: Auth0
- description: Sift signals surfaced into Salesforce customer records.
  name: Salesforce
- description: Event piping from Segment into the Sift Events API.
  name: Segment
json_schemas:
- name: Sift Decision
  property_count: 5
  slug: sift-decision
- name: Sift Event
  property_count: 11
  slug: sift-event
- name: Sift Score
  property_count: 7
  slug: sift-score
- name: Sift Verification
  property_count: 10
  slug: sift-verification
jsonld:
- class_count: 0
  name: Sift Context
  property_count: 5
  slug: sift-context
layout: provider
modified: '2026-05-25'
name: Sift
nav: Providers
network: true
overview: 'Sift publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Decisions API, Events API, Labels API, and 3 more. Tagged areas include Fraud Prevention, Trust And Safety, Risk Scoring, Identity Verification, and Chargebacks.


  The Sift catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sift''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, changelog, support, and 37 more developer resources.'
plans:
- name: Sift Com Plans Pricing
  plan_count: 5
  slug: sift-com-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 8
  name: Sift Com Rate Limits
  slug: sift-com-rate-limits
rules:
- name: Sift API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: sift-com-jsonschema-spectral-rules
- name: Sift API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: sift-com-rules
score:
  band: exemplar
  composite: 69.3
  delta: -4.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.8
    developer_ergonomics: 78.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 73.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sift-com/refs/heads/main/screenshots/sift-com-2026-06-20T193904.png
security:
- kind: authentication
  name: Sift Com Authentication
  slug: sift-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sift Com Domain Security
  slug: sift-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sift-com
solutions:
- name: Digital Commerce
- name: Internet And Software
- name: Finance And Fintech
- name: Online Gambling
- name: Travel And Transportation
- name: Food And Delivery
tags:
- Fraud Prevention
- Trust And Safety
- Risk Scoring
- Identity Verification
- Chargebacks
- Account Takeover
- Content Abuse
use_cases:
- description: Stop card-not-present fraud, stolen card use, and high-risk transactions at checkout.
  name: Payment Fraud
- description: Detect credential stuffing and ATO at login with device, behavior, and identity signals.
  name: Account Takeover
- description: Block fake account creation, fraud rings, and bot signups.
  name: Account Creation Abuse
- description: Detect referral, coupon, and promotion abuse across new and existing users.
  name: Promotion Abuse
- description: Catch spam, scams, and abusive content across messaging, listings, and reviews.
  name: Content Scams
- description: Risk score peer-to-peer transfers, withdrawals, and fintech money movement flows.
  name: Money Movement
- description: Automate dispute representment to recover chargeback revenue.
  name: Chargeback Dispute Management
website: https://sift.com
---
