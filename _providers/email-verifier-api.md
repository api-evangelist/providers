---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Email Verifier Api Agentic Access
  operation_count: 2
  slug: email-verifier-api-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Real-time email-address verification operations.
  name: Email Verifier API Verification API
  slug: email-verifier-api-verification-api
artifact_total: 40
collections:
- collection_type: postman
  name: Email Verifier Verification API
  slug: postman-email-verifier-api-verification-api
- collection_type: open
  name: Email Verifier API
  slug: open-email-verifier-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/email-verifier-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/email-verifier-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/email-verifier-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/email-verifier-api-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://emailverifierapi.com/api-docs/
- group: start
  title: ''
  type: Signup
  url: https://emailverifierapi.com/register/
- group: start
  title: ''
  type: Login
  url: https://emailverifierapi.com/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://emailverifierapi.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://emailverifierapi.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emailverifierapi.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emailverifierapi.com/privacy-policy/
- group: build
  title: ''
  type: FreeTool
  url: https://emailverifierapi.com/free-email-verifier/
- group: other
  title: ''
  type: Directory
  url: https://emailverifierapi.com/verify-company-emails/
- group: operate
  title: ''
  type: Support
  url: mailto:support@emailverifierapi.com
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: build
  title: ''
  type: SDKs
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://emailverifierapi.com/llms.txt
created: '2026-05-06'
description: Email Verifier API is a real-time email verification service offering a 16-point engine that validates deliverability through syntax checking, DNS / MX lookups, real-time SMTP handshakes, mailbox existence probing, catch-all and greylisting detection, disposable address detection, role-account flagging, spam-trap and complainer detection, gibberish and offensive-language scanning, B2B / B2C classification, typo correction, and SMTP provider identification. The service is delivered as a single REST endpoint that accepts GET or POST requests, returns JSON or XML, and meters usage against a credit-pack balance that never expires. The product targets growth teams, ESPs, and lead-generation operators that need to eliminate hard bounces and protect sender reputation before they send.
examples:
- key_count: 18
  name: Email Verifier Api Disposable Example
  slug: email-verifier-api-disposable-example
- key_count: 18
  name: Email Verifier Api Mailbox Does Not Exist Example
  slug: email-verifier-api-mailbox-does-not-exist-example
- key_count: 18
  name: Email Verifier Api Mailbox Exists Example
  slug: email-verifier-api-mailbox-exists-example
- key_count: 18
  name: Email Verifier Api Typo Suggest Example
  slug: email-verifier-api-typo-suggest-example
features:
- description: Composite engine combining syntax, DNS, MX, SMTP handshake, mailbox existence, catch-all, greylisting, disposable, role, spam-trap, gibberish, offensive, B2B, typo, complainer, and SMTP-provider checks.
  name: 16-Point Verification Engine
- description: Live RCPT TO probe against the destination MX to confirm mailbox existence in real time.
  name: Real-Time SMTP Verification
- description: Match against 50,000+ known disposable / burner email providers.
  name: Disposable Detection
- description: Flag departmental aliases such as info@, sales@, support@, marketing@.
  name: Role-Account Detection
- description: Identify domains whose MX accepts all addresses regardless of mailbox existence.
  name: Catch-All Detection
- description: Distinguish temporary SMTP defenses from outright rejections so they can be retried.
  name: Greylisting Handling
- description: Detect domain misspellings (gmial.com -> gmail.com) and return a corrected address.
  name: Typo Suggestion
- description: Identify honeypots and chronic spam-complainer addresses before they damage sender reputation.
  name: Spam-Trap and Complainer Detection
- description: Classify addresses as corporate (B2B) versus consumer (B2C) free-mailbox providers.
  name: B2B / B2C Classification
- description: Pay-as-you-go credit packs that never expire; only Paid (mailbox-level) events consume credits.
  name: Credit-Based Metering
- description: JSON by default; XML available with `xml=true`.
  name: JSON or XML Response
- description: Both GET and POST supported on the single endpoint for ad-hoc and server-to-server use.
  name: GET or POST
finops:
- name: Email Verifier Api Finops
  service_category: Email Verification
  slug: email-verifier-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/email-verifier-api.png
integrations:
- description: Apex HTTP-callout integration for lead validation inside Salesforce.
  name: Salesforce
- description: Spreadsheet workflow for ad-hoc list verification.
  name: Google Sheets
- description: Spreadsheet workflow for ad-hoc list verification.
  name: Microsoft Excel
- description: Marketing-platform integration for list cleansing.
  name: HubSpot
- description: CRM integration for inbound lead validation.
  name: Pipedrive
json_schemas:
- name: VerificationResult
  property_count: 18
  slug: email-verifier-api-verification-result
json_structures:
- name: Email Verifier Api Verification Result Structure
  property_count: 18
  slug: email-verifier-api-verification-result-structure
jsonld:
- class_count: 18
  name: Email Verifier Api Context
  property_count: 3
  slug: email-verifier-api-context
layout: provider
modified: '2026-05-19'
name: Email Verifier API
nav: Providers
network: true
overview: 'Email Verifier API publishes 1 API on the [APIs.io](https://apis.io/) network: Verification API. Tagged areas include Email Verification, Deliverability, SMTP Check, Bounce Prevention, and Lead Validation.


  The Email Verifier API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Email Verifier API''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 9 more developer resources.'
plans:
- name: Email Verifier Api Plans Pricing
  plan_count: 14
  slug: email-verifier-api-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Email Verifier Api Rate Limits
  slug: email-verifier-api-rate-limits
rules:
- name: Email Verifier API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: email-verifier-api-jsonschema-spectral-rules
- name: Email Verifier API API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 3
  slug: email-verifier-api-rules
score:
  band: strong
  composite: 61.5
  delta: -3.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 77.1
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 64.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/email-verifier-api/refs/heads/main/screenshots/email-verifier-api-2026-06-20T180621.png
security:
- kind: authentication
  name: Email Verifier Api Authentication
  slug: email-verifier-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Email Verifier Api Domain Security
  slug: email-verifier-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: email-verifier-api
tags:
- Email Verification
- Deliverability
- SMTP Check
- Bounce Prevention
- Lead Validation
- Disposable Detection
- Spam Trap Detection
- Catch-All Detection
- Greylisting
- Role Account Detection
- Typo Suggestion
- B2B Lead Scoring
use_cases:
- description: Block disposable, role, and invalid addresses at registration to keep user lists clean.
  name: Signup Validation
- description: Run marketing lists through verification before a send to lower bounce rate and protect IP / domain reputation.
  name: Pre-Send List Cleaning
- description: Score inbound leads on B2B vs B2C, role-account, and disposable signals to prioritize sales follow-up.
  name: Lead Quality Scoring
- description: Reduce hard bounces on transactional and marketing sends to maintain ISP reputation.
  name: ESP Bounce Prevention
- description: Use `emailSuggested` to prompt users with the corrected address inline at signup.
  name: Typo Recovery at Form Submit
---
