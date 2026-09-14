---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://transform.co/'', ''status'': 308, ''note'': ''declared website redirects to https://www.getdbt.com/ — a different registrable domain (transform.co -> getdbt.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transform-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transform.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transform-data
- group: build
  title: ''
  type: Packages
  url: packages/transform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/transform-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transform-llms.txt
created: '2026-07-17'
description: Transform (Transform Data) was a metrics-store and semantic-layer company backed by Redpoint Ventures that offered a metrics framework, a metrics catalog, and the MQL (Metrics Query Language) API, and open-sourced the MetricFlow metrics framework. Transform was acquired by dbt Labs (announced February 2023), and its technology lives on as MetricFlow and the dbt Semantic Layer. transform.co now returns a 308 Permanent Redirect to getdbt.com on every path, and the company no longer operates an independent API or developer surface — see the dbt provider profile in this network for the successor APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transform.png
layout: provider
modified: '2026-07-21'
name: Transform
nav: Providers
network: true
overview: Transform is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Metrics, Semantic Layer, Analytics, and Data.
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/transform/refs/heads/main/screenshots/transform-2026-09-02T164126.png
security:
- kind: domain-security
  name: Transform Domain Security
  slug: transform-domain-security
  summary_line: TLSv1.3 · HSTS
slug: transform
tags:
- Company
- Metrics
- Semantic Layer
- Analytics
- Data
- Business Intelligence
- Acquired
website: https://transform.co/
---
