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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/good-manufacturing-practices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fda.gov/drugs/pharmaceutical-quality-resources/facts-about-current-good-manufacturing-practices-cgmps
coverage:
  checked: '2026-09-12'
  detail: 'Good Manufacturing Practices is a US FDA regulatory quality regime (21 CFR 210/211), not a vendor: the only host this record names is fda.gov, whose cGMP page serves human regulatory prose while /openapi.json, /llms.txt and every /.well-known/ path return the FDA 404 page — the agency''s own openFDA contracts are profiled separately under all/food-and-drug-administration.'
  evidence:
  - status: 200
    url: https://www.fda.gov/drugs/pharmaceutical-quality-resources/facts-about-current-good-manufacturing-practices-cgmps
  - status: 404
    url: https://www.fda.gov/openapi.json
  - status: 404
    url: https://www.fda.gov/.well-known/api-catalog
  - status: 404
    url: https://www.fda.gov/llms.txt
  reason: not-a-software-company
  state: none
created: '2025-01-01'
description: A system of processes, procedures, and documentation that ensures products are consistently produced and controlled according to quality standards, commonly used in pharmaceutical, food, and medical device manufacturing. Proper implementation reduces legal and operational risk while supporting audit readiness.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/good-manufacturing-practices.png
layout: provider
modified: '2026-09-12'
name: Good Manufacturing Practices
nav: Providers
network: true
overview: Good Manufacturing Practices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Manufacturing, Pharmaceuticals, Quality Assurance, and Regulatory.
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/good-manufacturing-practices/refs/heads/main/screenshots/good-manufacturing-practices-2026-06-20T181957.png
security:
- kind: domain-security
  name: Good Manufacturing Practices Domain Security
  slug: good-manufacturing-practices-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: good-manufacturing-practices
tags:
- Compliance
- Manufacturing
- Pharmaceuticals
- Quality Assurance
- Regulatory
website: https://www.fda.gov/drugs/pharmaceutical-quality-resources/facts-about-current-good-manufacturing-practices-cgmps
---
