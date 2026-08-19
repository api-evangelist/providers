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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mailboxlayer Agentic Access
  operation_count: 1
  slug: mailboxlayer-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Email address validation and verification operations.
  name: mailboxlayer Verification API
  slug: mailboxlayer-verification-api
- description: 'REST/JSON API for real-time email validation: syntax check, typo suggestions, MX-record lookup, SMTP verification, catch-all/role/disposable/free detection, and quality score. Available via legacy api'
  name: Mailboxlayer Email Validation API
  slug: mailboxlayer-email-validation-api
artifact_total: 53
collections:
- collection_type: postman
  name: mailboxlayer Verification API
  slug: postman-mailboxlayer-verification-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: mailboxlayer Verification API
  slug: open-mailboxlayer-verification-api
- collection_type: open
  name: mailboxlayer API
  slug: open-mailboxlayer
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apilayer/mailboxlayer-API/issues
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
  url: https://apilayer.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://mailboxlayer.com/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/hgjA78638n
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apilayer.com/mailboxlayer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/mailboxlayer/docs/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apilayer.com/mailboxlayer/docs/mailboxlayer-api-v-1-0-0
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: operate
  title: ''
  type: FAQ
  url: https://mailboxlayer.com/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://mailboxlayer.com/api-status
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mailboxlayer-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: https://apilayer.com/playground/
- group: design
  title: ''
  type: Conventions
  url: conventions/mailboxlayer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mailboxlayer-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mailboxlayer-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mailboxlayer-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/mailboxlayer-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mailboxlayer-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mailboxlayer-verification-api-overlay.yaml
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
description: Real-time email validation and verification REST/JSON API operated by APILayer. Provides syntax checks, typo suggestions, MX-record lookup, SMTP verification, catch-all/role/disposable/free-provider detection, and a deliverability quality score.
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
modified: '2026-08-14'
name: Mailboxlayer
nav: Providers
network: true
overview: 'Mailboxlayer publishes 1 API on the [APIs.io](https://apis.io/) network: Verification API. Tagged areas include Email, Email Verification, Email Validation, SMTP, and MX Records.


  The Mailboxlayer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mailboxlayer''s developer surface includes authentication, developer portal, signup flow, pricing, getting-started guide, support, documentation, and 36 more developer resources.'
plans:
- name: Mailboxlayer Plans Pricing
  plan_count: 5
  slug: mailboxlayer-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 4
  name: Mailboxlayer Rate Limits
  slug: mailboxlayer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Mailboxlayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mailboxlayer-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Mailboxlayer API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: mailboxlayer-rules
score:
  band: exemplar
  composite: 74.5
  delta: -5.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 55.3
    contract_quality: 71.3
    developer_ergonomics: 86.3
    discoverability: 94.4
    governance: 55.3
    operational_transparency: 50.0
  previous_composite: 79.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mailboxlayer/refs/heads/main/screenshots/mailboxlayer-2026-08-17T124041.png
security:
- kind: authentication
  name: Mailboxlayer Authentication
  slug: mailboxlayer-authentication
  summary_line: apiKey · 2 schemes
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
- Data Quality
- Anti-Fraud
- Deliverability
- Communications
- Developer Tools
- Security
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
