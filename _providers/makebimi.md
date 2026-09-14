---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: Single unauthenticated endpoint that validates a remotely hosted SVG for BIMI suitability (SVG Tiny P/S). Described by the provider's own llms.txt as "the unauthenticated SVG validation endpoint", con
  name: makeBIMI SVG Validation API
  slug: makebimi-validation-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/makebimi-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: security/makebimi-security.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/makebimi-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/makebimi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/makebimi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makebimi-llms.txt
- group: auth
  title: ''
  type: SecurityPolicy
  url: security/makebimi-security.txt
- group: company
  title: ''
  type: Website
  url: https://makebimi.com
- group: docs
  title: ''
  type: Documentation
  url: https://makebimi.com/standard
- group: operate
  title: ''
  type: Support
  url: https://veribimi.com/services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veribimi.com/privacy
created: '2026-08-21'
description: makeBIMI is a free web tool for preparing and validating brand logos for BIMI (Brand Indicators for Message Identification). It converts supported image inputs to SVG Tiny P/S, checks SVG suitability, audits a domain's DMARC configuration, and suggests a BIMI DNS TXT record. It does not issue certificates and does not guarantee mailbox-provider logo display. The public API is a single unauthenticated endpoint, GET /api/validate, for validating a remotely hosted SVG in an automated workflow. Operated alongside veriBIMI, an independent BIMI certificate-brokerage and implementation-support service, and DMARCSwiss, a Swiss-hosted DMARC monitoring service.
layout: provider
modified: '2026-09-03'
name: makeBIMI
nav: Providers
network: true
overview: 'makeBIMI publishes 1 API on the [APIs.io](https://apis.io/) network: SVG Validation API. Tagged areas include BIMI, DMARC, Email Authentication, SVG, and brand indicators.


  makeBIMI''s developer surface includes documentation, support, and 9 more developer resources.'
plans:
- name: Makebimi Plans Pricing
  plan_count: 1
  slug: makebimi-plans-pricing
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/makebimi/refs/heads/main/screenshots/makebimi-2026-09-02T150427.png
security:
- kind: domain-security
  name: Makebimi Domain Security
  slug: makebimi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Makebimi Vulnerability Disclosure
  slug: makebimi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: makebimi
tags:
- BIMI
- DMARC
- Email Authentication
- SVG
- brand indicators
- SVG validation
website: https://makebimi.com
---
