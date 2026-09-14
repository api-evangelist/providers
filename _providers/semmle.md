---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.semmle.com'', ''status'': 301, ''note'': ''declared website redirects to https://github.blog/news-insights/company-news/github-welcomes-semmle/ — a different registrable domain (semmle.com -> github.blog), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semmle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.semmle.com
created: '2026-07-17'
description: Semmle was a semantic code-analysis company whose engine let developers write queries (in its QL query language) to find security vulnerabilities and their variants across large codebases, and which powered the free open-source code review platform LGTM.com. Its technology was adopted by Uber, NASA, Microsoft, and Google. GitHub acquired Semmle in September 2019 and folded the QL engine into what is now CodeQL and GitHub code scanning; the standalone Semmle and LGTM.com products were retired and www.semmle.com now redirects to the GitHub acquisition announcement. This profile is retained as a historical (acquired) company lead in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semmle.png
layout: provider
modified: '2026-07-21'
name: Semmle
nav: Providers
network: true
overview: Semmle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Code Analysis, Application Security, and Static Analysis.
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/semmle/refs/heads/main/screenshots/semmle-2026-09-02T154826.png
security:
- kind: domain-security
  name: Semmle Domain Security
  slug: semmle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: semmle
tags:
- Company
- Enterprise
- Code Analysis
- Application Security
- Static Analysis
- Developer Tools
- Acquired
website: http://www.semmle.com
---
