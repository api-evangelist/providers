---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://spindle.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.salesforce.com/agentforce/?bc=DB — a different registrable domain (spindle.ai -> salesforce.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spindle-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spindle.ai/
created: '2026-07-17'
description: Spindle Technologies (spindle.ai) was an Accel-backed AI startup that was acquired by Salesforce; as of this enrichment pass its entire domain — including the docs, developer, api, and app subdomains — issues a 301 redirect to salesforce.com/agentforce, so it no longer operates an independent developer portal, API, documentation, or SDK surface. This profile is retained as a network record of the company and its acquisition. No standalone API artifacts could be harvested. Domain-level security posture (TLS/DNSSEC/SPF/DMARC on spindle.ai) was probed and captured.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spindle-technologies.png
layout: provider
modified: '2026-08-21'
name: Spindle Technologies
nav: Providers
network: true
overview: Spindle Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Salesforce, and Acquired.
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/spindle-technologies/refs/heads/main/screenshots/spindle-technologies-2026-09-02T160440.png
security:
- kind: domain-security
  name: Spindle Technologies Domain Security
  slug: spindle-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spindle-technologies
tags:
- Company
- Artificial Intelligence
- Agents
- Salesforce
- Acquired
website: https://spindle.ai/
---
