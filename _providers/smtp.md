---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: RFC 5321 is the IETF standard defining the Simple Mail Transfer Protocol. It specifies the client-server protocol used to transmit email across the internet, including the command set, response codes,
  name: RFC 5321 - Simple Mail Transfer Protocol
  slug: rfc5321
- description: 'RFC 5322 defines the format of electronic mail messages transmitted via SMTP. It specifies the syntax for message headers (From, To, Subject, Date, etc.) and body structure. Works in conjunction with '
  name: RFC 5322 - Internet Message Format
  slug: rfc5322
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smtp-domain-security.yml
- group: other
  title: ''
  type: IETF RFC
  url: https://datatracker.ietf.org/doc/html/rfc5321
- group: other
  title: ''
  type: RFC Editor
  url: https://www.rfc-editor.org/rfc/rfc5321.html
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
- group: other
  title: ''
  type: Related Standard
  url: https://datatracker.ietf.org/doc/html/rfc5322
- group: other
  title: ''
  type: Related Standard
  url: https://datatracker.ietf.org/doc/html/rfc3463
- group: other
  title: ''
  type: Related Standard
  url: https://datatracker.ietf.org/doc/html/rfc4409
- group: other
  title: ''
  type: IETF Working Group
  url: https://datatracker.ietf.org/wg/emailcore/
created: '2025-01-01'
description: Simple Mail Transfer Protocol (SMTP) is the foundational internet standard for transmitting electronic mail across networks. Defined in RFC 5321 (October 2008), SMTP uses a command-response model over TCP port 25 (or 587 for submission, 465 for SMTPS). It defines commands including EHLO, MAIL FROM, RCPT TO, and DATA, along with a comprehensive set of response codes. SMTP works in conjunction with RFC 5322 (Internet Message Format) which defines the structure of email messages.
examples:
- key_count: 4
  name: Smtp Message Example
  slug: smtp-message-example
- key_count: 5
  name: Smtp Session Example
  slug: smtp-session-example
finops:
- name: Smtp Finops
  service_category: API
  slug: smtp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smtp.png
json_schemas:
- name: SMTP Email Message
  property_count: 11
  slug: smtp-message
- name: SMTP Session
  property_count: 7
  slug: smtp-session
json_structures:
- name: Smtp Message Structure
  property_count: 0
  slug: smtp-message-structure
jsonld:
- class_count: 34
  name: Smtp Context
  property_count: 0
  slug: smtp-context
layout: provider
modified: '2026-05-02'
name: SMTP
nav: Providers
network: true
overview: 'SMTP publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SMTP, Email, Internet Standards, IETF, and Messaging.


  The SMTP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Smtp Plans Pricing
  plan_count: 3
  slug: smtp-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Smtp Rate Limits
  slug: smtp-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SMTP API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: smtp-jsonschema-spectral-rules
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 14.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smtp/refs/heads/main/screenshots/smtp-2026-06-20T194059.png
security:
- kind: domain-security
  name: Smtp Domain Security
  slug: smtp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: smtp
tags:
- SMTP
- Email
- Internet Standards
- IETF
- Messaging
- Protocols
- RFC 5321
---
