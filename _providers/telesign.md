---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
- acting_count: 5
  human_in_the_loop: 0
  name: Telesign Agentic Access
  operation_count: 7
  slug: telesign-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 5
apis:
- description: Send voice messages including OTPs, alerts, and notifications to phone numbers worldwide. Supports text-to-speech message delivery and call status tracking.
  name: Telesign Voice API
  slug: voice-api
- description: Phone number reputation and fraud risk scoring
  name: Telesign Fraud Scoring API
  slug: telesign-fraud-scoring-api
- description: Send and track SMS messages
  name: Telesign Messaging API
  slug: telesign-messaging-api
- description: Phone number lookup and intelligence operations
  name: Telesign Phone Intelligence API
  slug: telesign-phone-intelligence-api
- description: Create, retrieve, and update verification processes
  name: Telesign Verification API
  slug: telesign-verification-api
artifact_total: 36
collections:
- collection_type: open
  name: Telesign PhoneID API
  slug: open-telesign-phoneid
- collection_type: open
  name: Telesign Score API
  slug: open-telesign-score
- collection_type: open
  name: Telesign SMS API
  slug: open-telesign-sms
- collection_type: open
  name: Telesign Verify API
  slug: open-telesign-verify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telesign-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/telesign-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telesign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telesign-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telesign
- group: company
  title: ''
  type: Website
  url: https://www.telesign.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.telesign.com/enterprise
- group: auth
  title: ''
  type: Authentication
  url: https://developer.telesign.com/enterprise/docs/authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telesign.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telesign.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telesign.com/terms-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TeleSign
- group: company
  title: ''
  type: Blog
  url: https://www.telesign.com/blog
description: Telesign provides a comprehensive suite of communications and security APIs enabling businesses to verify phone numbers, send SMS and voice messages, and assess fraud risk. Core offerings include SMS messaging, voice calls, multi-channel verification (OTP/MFA), phone number intelligence (PhoneID), reputation scoring, and silent verification. Telesign serves thousands of enterprises globally for account security, fraud prevention, and customer communications.
examples:
- key_count: 4
  name: Telesign Create Verification Example
  slug: telesign-create-verification-example
- key_count: 4
  name: Telesign Phoneid Lookup Example
  slug: telesign-phoneid-lookup-example
- key_count: 4
  name: Telesign Send Sms Example
  slug: telesign-send-sms-example
finops:
- name: Telesign Finops
  service_category: Communications
  slug: telesign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telesign.png
json_schemas:
- name: LocationInfo
  property_count: 7
  slug: telesign-locationinfo
- name: Telesign Messaging Response
  property_count: 2
  slug: telesign-messaging-response
- name: MessagingResponse
  property_count: 2
  slug: telesign-messagingresponse
- name: NumberingInfo
  property_count: 2
  slug: telesign-numberinginfo
- name: Telesign PhoneID Response
  property_count: 5
  slug: telesign-phoneid-response
- name: PhoneIdResponse
  property_count: 5
  slug: telesign-phoneidresponse
- name: PhoneType
  property_count: 2
  slug: telesign-phonetype
- name: RiskScore
  property_count: 3
  slug: telesign-riskscore
- name: ScoreResponse
  property_count: 4
  slug: telesign-scoreresponse
- name: TransactionStatus
  property_count: 3
  slug: telesign-transactionstatus
- name: VerificationStatus
  property_count: 3
  slug: telesign-verificationstatus
- name: VerifyResponse
  property_count: 2
  slug: telesign-verifyresponse
json_structures:
- name: Telesign Messaging Structure
  property_count: 0
  slug: telesign-messaging-structure
- name: Telesign Structure
  property_count: 0
  slug: telesign-structure
jsonld:
- class_count: 3
  name: Telesign Context
  property_count: 5
  slug: telesign-context
layout: provider
modified: '2026-05-19'
name: Telesign
nav: Providers
network: true
overview: 'Telesign publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Fraud Scoring API, Messaging API, Phone Intelligence API, and 1 more. Tagged areas include Authentication, Communications, Fraud Prevention, Phone Intelligence, and SMS.


  The Telesign catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telesign''s developer surface includes authentication, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Telesign Plans Pricing
  plan_count: 3
  slug: telesign-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 1
  name: Telesign Rate Limits
  slug: telesign-rate-limits
rules:
- name: Telesign API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: telesign-jsonschema-spectral-rules
- name: Telesign API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 7
  slug: telesign-rules
score:
  band: developing
  composite: 51.3
  delta: -6.7
  facets:
    commercial_clarity: 68.4
    contract_quality: 64.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/telesign/refs/heads/main/screenshots/telesign-2026-06-20T195043.png
security:
- kind: authentication
  name: Telesign Authentication
  slug: telesign-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Telesign Domain Security
  slug: telesign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Telesign Trust Center
  slug: telesign-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: telesign
tags:
- Authentication
- Communications
- Fraud Prevention
- Phone Intelligence
- SMS
- Verification
website: https://www.telesign.com/
---
