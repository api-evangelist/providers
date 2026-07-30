---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mailboxlayer Agentic Access
  operation_count: 1
  slug: mailboxlayer-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Email address validation and verification operations.
  name: mailboxlayer Verification API
  slug: mailboxlayer-verification-api
artifact_total: 50
collections:
- collection_type: postman
  name: mailboxlayer Verification API
  slug: postman-mailboxlayer-verification-api
- collection_type: open
  name: mailboxlayer API
  slug: open-mailboxlayer
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mailboxlayer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailboxlayer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailboxlayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailboxlayer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mailboxlayer.com
- group: start
  title: ''
  type: Portal
  url: https://mailboxlayer.com/dashboard
- group: start
  title: ''
  type: Signup
  url: https://mailboxlayer.com/product
- group: commercial
  title: ''
  type: Pricing
  url: https://mailboxlayer.com/product
- group: start
  title: ''
  type: GettingStarted
  url: https://mailboxlayer.com/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailboxlayer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailboxlayer.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://mailboxlayer.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apilayer/mailboxlayer-API
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ash-jc-allen/laravel-mailboxlayer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/actfong/mailboxlayer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/damienmarchandfr/mailboxlayer-node-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ylly/mailboxlayerbundle
- group: design
  title: ''
  type: SpectralRules
  url: rules/mailboxlayer-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mailboxlayer-vocabulary.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/mailboxlayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailboxlayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailboxlayer-finops.yml
created: '2026-05-28'
description: mailboxlayer is an apilayer-owned REST JSON API for email address verification. It performs syntax and typo checks, MX-record lookup, real-time SMTP verification, catch-all detection, role-address detection, free and disposable provider detection, and returns a numeric deliverability quality score. Useful for signup-form validation, list hygiene, lead enrichment, and fraud prevention.
examples:
- key_count: 2
  name: Mailboxlayer Check Disposable Example
  slug: mailboxlayer-check-disposable-example
- key_count: 2
  name: Mailboxlayer Check Error Example
  slug: mailboxlayer-check-error-example
- key_count: 12
  name: Mailboxlayer Check Result Example
  slug: mailboxlayer-check-result-example
- key_count: 12
  name: Mailboxlayer Check Result Free Example
  slug: mailboxlayer-check-result-free-example
- key_count: 2
  name: Mailboxlayer Check Success Example
  slug: mailboxlayer-check-success-example
- key_count: 2
  name: Mailboxlayer Check Typo Example
  slug: mailboxlayer-check-typo-example
features:
- description: Thorough RFC 5322 syntax validation with did-you-mean suggestions for likely typos.
  name: Syntax And Typo Check
- description: Each address is pinged via SMTP to confirm the mailbox actually accepts mail.
  name: Real-Time SMTP Verification
- description: Verifies that the email domain has functioning MX records.
  name: MX Record Lookup
- description: Determines whether the recipient domain accepts mail for any local part (paid plans only).
  name: Catch-All Detection
- description: Flags addresses associated with a function rather than a person (support@, admin@, etc.).
  name: Role Address Detection
- description: Identifies addresses on free webmail providers (Gmail, Yahoo, Outlook.com, etc.).
  name: Free Provider Detection
- description: Identifies addresses on throwaway / disposable providers (mailinator.com, etc.).
  name: Disposable Provider Detection
- description: A 0.0 to 1.0 numeric score expressing overall deliverability and quality.
  name: Quality Score
- description: 256-bit HTTPS transport on paid plans (Basic and above).
  name: HTTPS Encryption
- description: Submit 25 addresses (Pro Plus) or 100 addresses (Enterprise Plus) in a single request.
  name: Bulk Endpoint
- description: JSONP wrapper via the `callback` query parameter.
  name: JSONP Support
finops:
- name: Mailboxlayer Finops
  service_category: ''
  slug: mailboxlayer-finops
image: https://mailboxlayer.com/site_images/mailboxlayer_logo_white.svg
integrations:
- description: Plugin scoring incoming PostHog user emails via the mailboxlayer API.
  name: PostHog
- description: Connector for incorporating email verification into security orchestration playbooks.
  name: Fortinet FortiSOAR
- description: Multiple community Laravel packages wrap mailboxlayer for PHP web applications.
  name: Laravel
- description: Symfony bundle for mailboxlayer-backed email validation.
  name: Symfony
- description: Node and TypeScript client libraries for serverside email verification.
  name: Node.js / TypeScript
- description: Ruby client gem.
  name: Ruby
- description: Delphi sample demonstrating the API for desktop application validation.
  name: Delphi
json_schemas:
- name: mailboxlayer Email Check Result
  property_count: 12
  slug: mailboxlayer-check-result
- name: mailboxlayer Error Response
  property_count: 2
  slug: mailboxlayer-error
json_structures:
- name: Mailboxlayer Check Result Structure
  property_count: 12
  slug: mailboxlayer-check-result-structure
jsonld:
- class_count: 2
  name: Mailboxlayer Context
  property_count: 17
  slug: mailboxlayer-context
layout: provider
modified: '2026-05-30'
name: mailboxlayer
nav: Providers
network: true
overview: 'mailboxlayer publishes 1 API on the [APIs.io](https://apis.io/) network: Verification API. Tagged areas include Email, Email Verification, Email Validation, SMTP, and MX Records.


  The mailboxlayer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  mailboxlayer''s developer surface includes authentication, developer portal, signup flow, pricing, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Mailboxlayer Plans Pricing
  plan_count: 5
  slug: mailboxlayer-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Mailboxlayer Rate Limits
  slug: mailboxlayer-rate-limits
rules:
- name: mailboxlayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mailboxlayer-jsonschema-spectral-rules
- name: mailboxlayer API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: mailboxlayer-rules
score:
  band: strong
  composite: 60.5
  delta: -2.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 75.4
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 63.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/mailboxlayer/refs/heads/main/screenshots/mailboxlayer-2026-06-20T184850.png
security:
- kind: authentication
  name: Mailboxlayer Authentication
  slug: mailboxlayer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mailboxlayer Domain Security
  slug: mailboxlayer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mailboxlayer
solutions:
- description: 100 requests/month, HTTP only, no support, no catch-all detection.
  name: Free
- description: $14.99/mo for 5,000 requests; HTTPS, catch-all detection, standard support.
  name: Basic
- description: $74.99/mo for 50,000 requests; adds bulk endpoint (25 emails).
  name: Professional Plus
- description: $249.99/mo for 250,000 requests; adds bulk endpoint (100 emails) and richer SLAs.
  name: Enterprise Plus
- description: Contact sales for higher volumes and bespoke arrangements.
  name: Custom
tags:
- Email
- Email Verification
- Email Validation
- SMTP
- MX Records
- Catch-All Detection
- Disposable Email
- Free Email Provider
- Role Address
- Quality Score
- apilayer
- Public APIs
use_cases:
- description: Catch typos and disposable addresses at signup before they hit your user database.
  name: Signup Form Validation
- description: Clean existing email marketing lists to lift deliverability and sender reputation.
  name: List Hygiene
- description: Enrich CRM and lead-capture records with deliverability scores and role flags.
  name: Lead Enrichment
- description: Block disposable email providers commonly used for trial abuse and chargebacks.
  name: Fraud And Abuse Prevention
- description: Reduce hard-bounces from order receipts, password resets, and notifications.
  name: Transactional Email Hygiene
- description: Separate role addresses and free-provider addresses from individual corporate inboxes.
  name: B2B Sales Qualification
website: https://mailboxlayer.com
---
