---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
- group: commercial
  href: https://artifacts.apis.io/smtp/plans/smtp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smtp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smtp/rate-limits/smtp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smtp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/smtp/finops/smtp-finops.yml
  title: ''
  type: FinOps
  url: finops/smtp-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.ietf.org/
- group: auth
  href: https://artifacts.apis.io/smtp/security/smtp-domain-security.yml
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
- has_sources: false
  method: generated
  name: Smtp Finops
  primary_unit: request
  service_category: API
  slug: smtp-finops
  template: true
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
overview: 'SMTP is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SMTP, Email, Internet Standards, IETF, and Messaging.


  The SMTP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Smtp Plans Pricing
  plan_count: 3
  slug: smtp-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Smtp Rate Limits
  slug: smtp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: SMTP — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: smtp-jsonschema-spectral-rules
screenshot: https://apis.io/screenshots/smtp/smtp-2026-06-20T194059.png
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
- Protocol
- RFC 5321
website: https://www.ietf.org/
---
