---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 11
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mailchannels.com/email-api/curl/quickstart
- group: commercial
  href: https://artifacts.apis.io/mailchannels/plans/mailchannels-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailchannels-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/mailchannels/security/mailchannels-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mailchannels-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailchannels/authentication/mailchannels-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailchannels-authentication.yml
- group: design
  href: https://artifacts.apis.io/mailchannels/conformance/mailchannels-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailchannels-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mailchannels/llms/mailchannels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailchannels-llms.txt
- group: other
  href: https://artifacts.apis.io/mailchannels/a2a/mailchannels-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mailchannels-a2a.yml
- group: auth
  href: https://artifacts.apis.io/mailchannels/well-known/mailchannels-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailchannels-status-security.txt
- group: auth
  href: https://artifacts.apis.io/mailchannels/well-known/mailchannels-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailchannels-security.txt
- group: auth
  href: https://artifacts.apis.io/mailchannels/well-known/mailchannels-mailchannels-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailchannels-mailchannels-security.txt
- group: auth
  href: https://artifacts.apis.io/mailchannels/well-known/mailchannels-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailchannels-blog-security.txt
- group: agent
  href: https://artifacts.apis.io/mailchannels/well-known/mailchannels-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailchannels-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailchannels/hosts/mailchannels-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailchannels-hosts.yml
- group: other
  href: https://artifacts.apis.io/mailchannels/vendors/mailchannels-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailchannels-vendors.yml
- group: build
  href: https://artifacts.apis.io/mailchannels/packages/mailchannels-packages.yml
  title: ''
  type: SDKs
  url: packages/mailchannels-packages.yml
- group: build
  href: https://artifacts.apis.io/mailchannels/packages/mailchannels-packages.yml
  title: ''
  type: Packages
  url: packages/mailchannels-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.mailchannels.net/tx/v1
- group: auth
  href: https://artifacts.apis.io/mailchannels/security/mailchannels-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mailchannels-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailchannels/security/mailchannels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailchannels-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailchannels.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mailchannels.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mailchannels.com/email-api/overview
- group: operate
  title: ''
  type: Support
  url: https://support.mailchannels.com/hc/en-us/requests/new
- group: company
  title: ''
  type: Blog
  url: https://blog.mailchannels.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailchannels
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailchannels.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mailchannels.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mailchannels.com/privacy-policy/
- group: operate
  title: ''
  type: Status
  url: https://status.mailchannels.net/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://mailchannels.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: MailChannels provides a transactional email service for platforms, multi‑tenant applications, and hosting providers. It offers both SMTP relay and a robust RESTful Email API, along with inbound/outbound spam filtering, reputation management, and abuse isolation. The service is designed to protect sender reputation, detect compromised accounts, and give per‑sender controls, helping developers and hosting companies reliably deliver email without building their own infrastructure.
image: https://www.mailchannels.com/wp-content/uploads/2014/04/m-logo.jpg
json_schemas:
- name: DeleteTxV1WebhookResponse
  property_count: 2
  slug: mailchannels-delete-tx-v1-webhook-response
- name: GetTxV1WebhookPublicKeyResponse
  property_count: 2
  slug: mailchannels-get-tx-v1-webhook-public-key-response
- name: GetTxV1WebhookResponse
  property_count: 1
  slug: mailchannels-get-tx-v1-webhook-response
- name: PostTxV1WebhookValidateResponse
  property_count: 2
  slug: mailchannels-post-tx-v1-webhook-validate-response
jsonld:
- class_count: 4
  name: Mailchannels Context
  property_count: 5
  slug: mailchannels-context
layout: provider
modified: '2026-10-27'
name: MailChannels
nav: Providers
network: true
overview: 'MailChannels is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, API, SMTP, and Platform.


  The MailChannels catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MailChannels'' developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Mailchannels Plans Pricing
  plan_count: 4
  slug: mailchannels-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Mailchannels Rate Limits
  slug: mailchannels-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: MailChannels API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: mailchannels-rules
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.8
    catalog_earned_first_party: 20.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 29.5
    contract_quality: 8.3
    developer_ergonomics: 64.3
    discoverability: 48.2
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mailchannels Authentication
  slug: mailchannels-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mailchannels Domain Security
  slug: mailchannels-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mailchannels Vulnerability Disclosure
  slug: mailchannels-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mailchannels
tags:
- Company
- Email
- API
- SMTP
- Platform
website: https://mailchannels.com/
---
