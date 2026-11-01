---
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Mailbridgeapi Agentic Access
  operation_count: 12
  slug: mailbridgeapi-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- description: Turn your own mailbox into a secure email API.
  name: MailBridgeAPI Email API
  slug: mailbridgeapi-email-api
- baseURL: https://api.mailbridgeapi.com/
  baseurl_source: declared
  description: Search messages and build delivery or usage reporting.
  name: MailBridgeAPI Activity API
  slug: mailbridgeapi-activity-api
- baseURL: https://api.mailbridgeapi.com/
  baseurl_source: declared
  description: Read unsubscribe information for your own contact workflows.
  name: MailBridgeAPI Compliance API
  slug: mailbridgeapi-compliance-api
- baseURL: https://api.mailbridgeapi.com/
  baseurl_source: declared
  description: Inspect mailbox readiness and operational health.
  name: MailBridgeAPI Mailbox API
  slug: mailbridgeapi-mailbox-api
- baseURL: https://api.mailbridgeapi.com/
  baseurl_source: declared
  description: Read incoming messages from the mailbox or the normalized received-message API.
  name: MailBridgeAPI Receiving API
  slug: mailbridgeapi-receiving-api
- baseURL: https://api.mailbridgeapi.com/
  baseurl_source: declared
  description: Send and validate email through the selected mailbox.
  name: MailBridgeAPI Sending API
  slug: mailbridgeapi-sending-api
- baseURL: https://api.mailbridgeapi.com/
  baseurl_source: declared
  description: Public service availability.
  name: MailBridgeAPI Service API
  slug: mailbridgeapi-service-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/mailbridgeapi/agentic-access/mailbridgeapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailbridgeapi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mailbridgeapi/rules/mailbridgeapi-rules.yml
  title: ''
  type: Spectral
  url: rules/mailbridgeapi-rules.yml
- group: design
  href: https://artifacts.apis.io/mailbridgeapi/json-ld/mailbridgeapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailbridgeapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailbridgeapi/vocabulary/mailbridgeapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailbridgeapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mailbridgeapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mailbridgeapi/data-model/mailbridgeapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailbridgeapi-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://mailbridgeapi.com/vulnerability-reporting/
- group: design
  href: https://artifacts.apis.io/mailbridgeapi/errors/mailbridgeapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailbridgeapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mailbridgeapi/conformance/mailbridgeapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailbridgeapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mailbridgeapi/llms/mailbridgeapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailbridgeapi-llms.txt
- group: auth
  href: https://artifacts.apis.io/mailbridgeapi/well-known/mailbridgeapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailbridgeapi-security.txt
- group: agent
  href: https://artifacts.apis.io/mailbridgeapi/well-known/mailbridgeapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailbridgeapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailbridgeapi/hosts/mailbridgeapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailbridgeapi-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mailbridgeapi/authentication/mailbridgeapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailbridgeapi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mailbridgeapi/security/mailbridgeapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mailbridgeapi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailbridgeapi/security/mailbridgeapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailbridgeapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailbridgeapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mailbridgeapi.com/doc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mailbridgeapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mailbridgeapi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://mailbridgeapi.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailbridgeapi.com/terms-and-conditions-of-sale/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailbridgeapi.com/privacy-policy/
created: '2026-10-21'
description: MailBridgeAPI provides a programmable email API that connects to SMTP and IMAP mailboxes, offering endpoints to send, receive, search and manage email without exposing mailbox passwords. It supports integrations with Gmail, Microsoft 365, Yahoo, Zoho, Apple iCloud, and custom mail servers, featuring AI-powered auto-reply, mobile app control, and detailed analytics. Developers can quickly test connections via a free trial, and companies gain secure, auditable email handling for critical communications.
image: https://mailbridgeapi.com/og.png
jsonld:
- class_count: 11
  name: Mailbridgeapi Context
  property_count: 52
  slug: mailbridgeapi-context
layout: provider
modified: '2026-10-21'
name: MailBridgeAPI
nav: Providers
network: true
overview: 'MailBridgeAPI publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Compliance API, Mailbox API, and 4 more. Tagged areas include Email API, SMTP, IMAP, mailbox integration, and Developer Tools.


  The MailBridgeAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MailBridgeAPI''s developer surface includes authentication, documentation, pricing, signup flow, and 19 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: MailBridgeAPI API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: mailbridgeapi-rules
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 55.6
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
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
  name: Mailbridgeapi Authentication
  slug: mailbridgeapi-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Mailbridgeapi Domain Security
  slug: mailbridgeapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mailbridgeapi Vulnerability Disclosure
  slug: mailbridgeapi-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: mailbridgeapi-send-email
  slug: mailbridgeapi-send-email
slug: mailbridgeapi
tags:
- Email API
- SMTP
- IMAP
- mailbox integration
- Developer Tools
- mailbox monitoring
website: https://mailbridgeapi.com/
---
