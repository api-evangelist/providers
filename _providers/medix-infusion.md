---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medix-infusion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medixinfusion.com/
- group: operate
  title: ''
  type: Support
  url: https://medixinfusion.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medixinfusion.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medixinfusion.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medix-infusion
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medix-infusion-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/medix-infusion-conformance.yml
coverage:
  checked: '2026-08-25'
  detail: Medix Infusion runs ambulatory infusion suites and in-home infusion nursing — the product is clinical care billed through a patient's medical or pharmacy benefit — and its entire public surface is one WordPress marketing site with no /developers, /docs or /api path; the only machine-readable thing on the domain is the default WordPress wp-json REST index that ships with the CMS.
  evidence:
  - status: 404
    url: https://medixinfusion.com/developers
  - status: 404
    url: https://medixinfusion.com/openapi.json
  - status: 404
    url: https://medixinfusion.com/graphql
  - status: 404
    url: https://medixinfusion.com/.well-known/agent-card.json
  - status: 200
    url: https://medixinfusion.com/llms.txt
  - status: 200
    url: https://medixinfusion.com/wp-json
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Medix Infusion, Inc. is a technology-enabled infusion care provider headquartered in Addison, Texas, that administers infusion and injectable therapies — anti-infectives, biologics, IVIG and other specialty medications — to chronically and acutely ill patients through a network of ambulatory infusion suites and in the home. The company concentrates on rural, suburban and other under-served markets, coordinating benefits investigation, prior authorization, scheduling, pharmacy and nursing around each referral, and is accredited by the Accreditation Commission for Health Care (ACHC). It raised a $35M Series B led by Echo Health Ventures in January 2023 alongside existing investor Noro-Moseley Partners. Medix Infusion operates as a care-delivery organization: it publishes no developer portal, no API documentation and no machine-readable API contract on any public host as of this profile.'
image: https://medixinfusion.com/wp-content/uploads/2023/01/medix-infusion-logo-horizontal.svg
layout: provider
modified: '2026-08-25'
name: Medix Infusion
nav: Providers
network: true
overview: 'Medix Infusion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Infusion Therapy, Specialty Pharmacy, and Home Health.


  Medix Infusion''s developer surface includes support and 7 more developer resources.'
plans:
- name: Medix Infusion Plans Pricing
  plan_count: 0
  slug: medix-infusion-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Medix Infusion Rate Limits
  slug: medix-infusion-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/medix-infusion/refs/heads/main/screenshots/medix-infusion-2026-09-02T150455.png
security:
- kind: domain-security
  name: Medix Infusion Domain Security
  slug: medix-infusion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medix-infusion
tags:
- Company
- Healthcare
- Infusion Therapy
- Specialty Pharmacy
- Home Health
- Ambulatory Care
- Patient Care
- Texas
website: https://medixinfusion.com/
---
