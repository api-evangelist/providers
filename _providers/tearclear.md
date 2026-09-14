---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tearclear
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/tearclear-stock
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tearclear-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tearclear-llms.txt
coverage:
  checked: '2026-08-29'
  detail: TearClear is a clinical-stage ophthalmic pharmaceutical company whose product is a BAK-removing eye-drop bottle filter and the latanoprost/timolol/brimonidine drugs dispensed through it, so there is no software product to expose an API on; separately, its own domain tearclear.com now answers 403 from an unprovisioned SiteGround default vhost, and no api./developer./docs. subdomain resolves at all.
  evidence:
  - status: 403
    url: https://tearclear.com/
  - status: 403
    url: https://tearclear.com/openapi.json
  - status: 403
    url: https://tearclear.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/tearclear
  - status: 200
    url: https://www.linkedin.com/company/tearclear
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'TearClear Corp. is a clinical-stage ophthalmic pharmaceutical company founded in 2015 that develops a preservative-removing drug delivery platform: a chemical filter built into a conventional multi-dose eye-drop bottle that captures benzalkonium chloride (BAK) at the point of instillation, so the medication stays preserved in the bottle but reaches the ocular surface preservative-free. Its lead candidate TC-002 (latanoprost ophthalmic solution 0.005%) met the primary and all secondary endpoints in the CLEAR Phase 3 pivotal glaucoma trial, with TC-001 (timolol), TC-003 (brimonidine/timolol) and TC-004 (brimonidine) behind it. TearClear ships drug products and delivery hardware, not software: it operates no developer program and publishes no API, SDK or machine-readable contract, and its own corporate domain no longer resolves to a served website.'
layout: provider
modified: '2026-08-29'
name: Tearclear
nav: Providers
network: true
overview: Tearclear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Ophthalmology, Drug Delivery, and Life Sciences.
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/tearclear/refs/heads/main/screenshots/tearclear-2026-09-02T162658.png
security:
- kind: domain-security
  name: Tearclear Domain Security
  slug: tearclear-domain-security
  summary_line: no transport/DNS hardening detected
slug: tearclear
tags:
- Company
- Pharmaceuticals
- Ophthalmology
- Drug Delivery
- Life Sciences
- Medical Devices
- Glaucoma
- Clinical Stage
---
