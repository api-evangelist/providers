---
access_model:
  confidence: medium
  label: Enterprise contact-sales only; no published pricing and no self-service signup
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.fisglobal.com/products/fis-data-integrity-manager
  trial: false
  try_now: false
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.fisglobal.com/products/fis-data-integrity-manager
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intellimatch-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/intellimatch-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/intellimatch-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/intellimatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fisglobal.com/en/responsible-disclosure
- group: design
  title: ''
  type: Conformance
  url: conformance/intellimatch-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intellimatch-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intellimatch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intellimatch-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/intellimatch-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intellimatch-llms.txt
coverage:
  checked: '2026-09-13'
  detail: 'FIS ships IntelliMatch — renamed FIS Data Integrity Manager — as an end-user enterprise reconciliation application with no developer program of its own: the live product page offers brochures and "Connect with sales" and links to no reference, spec or portal, while the URL this record previously carried as its Website is now a hard 404 after the rename.'
  evidence:
  - status: 200
    url: https://www.fisglobal.com/products/fis-data-integrity-manager
  - status: 404
    url: https://www.fisglobal.com/en/products/intellimatch-reconciliation-software
  - status: 403
    url: https://codeconnect.fisglobal.com/fisccp/apisbytag
  - status: 200
    url: https://fisglobal.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2024-01-01'
description: IntelliMatch is a transaction and account reconciliation platform originally developed by SunGard, now offered by FIS, and since renamed FIS Data Integrity Manager. It performs account-level balance and transaction proofing at high volume and drives review, approval, exception management and escalation through an integrated workflow engine, so financial institutions and corporates can reconcile cash, securities and intercompany activity and track data integrity centrally. The product is SWIFT-accredited, embeds machine learning through an AI Virtual Reconciler, and is sold either customer-hosted or as the FIS Optimized Reconciliation Service (formerly Managed Reconciliation Service). FIS publishes no developer program, documentation, OpenAPI or any other machine-readable contract for it; integration is arranged commercially. FIS's public API marketplace, Code Connect, carries a different product line and is profiled separately.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intellimatch.png
layout: provider
modified: '2026-09-13'
name: IntelliMatch
nav: Providers
network: true
overview: IntelliMatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Reconciliation, Financial-Services, Matching, Exception Management, and Banking.
plans:
- name: Intellimatch Plans Pricing
  plan_count: 0
  slug: intellimatch-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Intellimatch Rate Limits
  slug: intellimatch-rate-limits
security:
- kind: domain-security
  name: Intellimatch Domain Security
  slug: intellimatch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Intellimatch Vulnerability Disclosure
  slug: intellimatch-vulnerability-disclosure
  summary_line: Bugcrowd
slug: intellimatch
tags:
- Reconciliation
- Financial-Services
- Matching
- Exception Management
- Banking
- Treasury
- SWIFT
- Data Integrity
website: https://www.fisglobal.com/products/fis-data-integrity-manager
---
