---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Mailosaur Agentic Access
  operation_count: 28
  slug: mailosaur-agentic-access
  summary_line: 28 operations · 13 acting
api_count: 1
apis:
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for analyzing the content and deliverability of an email, including SpamAssassin scoring and per-provider deliverability reports.
  name: Mailosaur Analysis API
  slug: mailosaur-analysis-api
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for managing virtual security devices and retrieving their current one-time passwords (OTPs), used to automate testing of app-based multi-factor authentication.
  name: Mailosaur Devices API
  slug: mailosaur-devices-api
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for downloading the raw content associated with a message — file attachments, the full EML source of an email, and rendered email previews.
  name: Mailosaur Files API
  slug: mailosaur-files-api
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for finding, retrieving, creating, forwarding, replying to, and deleting the email and SMS messages received by your Mailosaur inboxes.
  name: Mailosaur Messages API
  slug: mailosaur-messages-api
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for discovering the email clients available for generating email previews (screenshots of an email rendered in real clients).
  name: Mailosaur Previews API
  slug: mailosaur-previews-api
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for creating and managing your Mailosaur inboxes (servers). Inboxes group your tests together, each with its own domain and SMTP/POP3/IMAP credentials.
  name: Mailosaur Servers API
  slug: mailosaur-servers-api
- baseURL: https://mailosaur.com/api
  baseurl_source: declared
  description: Operations for inspecting your account's usage limits and recent transactional usage. These endpoints require authentication with an account-level API key.
  name: Mailosaur Usage API
  slug: mailosaur-usage-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mailosaur Analysis API
  slug: open-mailosaur-analysis-api
- collection_type: open
  name: Mailosaur Analysis Devices API
  slug: open-mailosaur-devices-api
- collection_type: open
  name: Mailosaur Analysis Files API
  slug: open-mailosaur-files-api
- collection_type: open
  name: Mailosaur Analysis Messages API
  slug: open-mailosaur-messages-api
- collection_type: open
  name: Mailosaur Analysis Servers API
  slug: open-mailosaur-servers-api
- collection_type: open
  name: Mailosaur Analysis Usage API
  slug: open-mailosaur-usage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailosaur-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mailosaur-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailosaur-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailosaur-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mailosaur.com
- group: docs
  title: ''
  type: Documentation
  url: https://mailosaur.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mailosaur
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailosaur
- group: other
  title: ''
  type: X
  url: https://x.com/mailosaur
- group: company
  title: ''
  type: Blog
  url: https://mailosaur.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://mailosaur.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailosaur.com
- group: commercial
  title: ''
  type: Plans
  url: plans/mailosaur-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailosaur-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailosaur-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/mailosaur-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mailosaur-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mailosaur-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mailosaur-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mailosaur-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/mailosaur-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mailosaur-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mailosaur-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mailosaur-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mailosaur-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mailosaur.com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mailosaur-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/mailosaur-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/mailosaur-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mailosaur-message.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mailosaur-server.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mailosaur-device.json
- group: build
  title: ''
  type: Examples
  url: examples/mailosaur-search-messages-example.json
- group: build
  title: ''
  type: Examples
  url: examples/mailosaur-create-server-example.json
- group: build
  title: ''
  type: Examples
  url: examples/mailosaur-get-otp-example.json
- group: build
  title: ''
  type: Examples
  url: examples/mailosaur-deliverability-report-example.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mailosaur.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mailosaur.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://mailosaur.com/docs/email-testing/sending-to-mailosaur
- group: operate
  title: ''
  type: Support
  url: https://mailosaur.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://mailosaur.com/app/signup
- group: start
  title: ''
  type: Login
  url: https://mailosaur.com/app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailosaur.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailosaur.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/mailosaur/mailosaur/documentation/6961255-6cc72dff-f576-451a-9023-b82dec84f95d
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://mailosaur.com/legal/enterprise-sla
created: 2026-06-13
description: Mailosaur is an email and SMS testing platform for developers and QA teams. It provides a REST API for creating test inboxes, capturing and retrieving messages, running assertions, performing deliverability analysis, and integrating email and SMS testing into CI/CD pipelines. The platform supports authentication testing (TOTP/2FA), spam analysis, SPF/DKIM/DMARC validation, and connects via SMTP, POP3, and IMAP protocols.
examples:
- key_count: 3
  name: Mailosaur Create Server Example
  slug: mailosaur-create-server-example
- key_count: 3
  name: Mailosaur Deliverability Report Example
  slug: mailosaur-deliverability-report-example
- key_count: 3
  name: Mailosaur Get Otp Example
  slug: mailosaur-get-otp-example
- key_count: 3
  name: Mailosaur Search Messages Example
  slug: mailosaur-search-messages-example
finops:
- name: Mailosaur Finops
  service_category: ''
  slug: mailosaur-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailosaur.png
json_schemas:
- name: Device
  property_count: 2
  slug: mailosaur-device
- name: Message
  property_count: 13
  slug: mailosaur-message
- name: Server
  property_count: 4
  slug: mailosaur-server
jsonld:
- class_count: 38
  name: Mailosaur Context
  property_count: 7
  slug: mailosaur-context
layout: provider
modified: 2026-08-14
name: Mailosaur
nav: Providers
network: true
overview: 'Mailosaur publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analysis API, Devices API, Files API, and 4 more. Tagged areas include Email Testing, SMS Testing, Developer Tools, QA Automation, and CI/CD.


  The Mailosaur catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mailosaur''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, code examples, API reference, and 40 more developer resources.'
plans:
- name: Mailosaur Plans Pricing
  plan_count: 3
  slug: mailosaur-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Mailosaur Rate Limits
  slug: mailosaur-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Mailosaur API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: mailosaur-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 76.5
    catalog_earned_first_party: 24.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 64.5
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 52.6
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailosaur/refs/heads/main/screenshots/mailosaur-2026-06-20T184900.png
security:
- kind: authentication
  name: Mailosaur Authentication
  slug: mailosaur-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailosaur Domain Security
  slug: mailosaur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mailosaur Trust Center
  slug: mailosaur-trust-center
  summary_line: ISO 27001:2022, PCI DSS, GDPR, UK Data Protection Act, CCPA
slug: mailosaur
tags:
- Email Testing
- SMS Testing
- Developer Tools
- QA Automation
- CI/CD
- SMTP
- TOTP
- Deliverability
website: https://mailosaur.com
---
