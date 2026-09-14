---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://highfive.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.dialpad.com/highfive/ — a different registrable domain (highfive.com -> dialpad.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highfive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://highfive.com
created: '2026-07-17'
description: 'Highfive was a video collaboration and conferencing company (highfive.com) surfaced in the API Evangelist network as a portfolio company of gv and lightspeed-venture-partners. The brand was acquired by and folded into Dialpad: highfive.com now issues a 301 redirect to dialpad.com/highfive, and developer.highfive.com no longer resolves (NXDOMAIN). Highfive exposes no independent developer portal, API documentation, OpenAPI, SDKs, MCP server, or /.well-known/ discovery surface of its own; any current programmatic capability lives under the Dialpad platform. This profile is retained as an enrichment lead; only a domain-security probe of the surviving highfive.com domain yielded real data.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highfive.png
layout: provider
modified: '2026-07-19'
name: Highfive
nav: Providers
network: true
overview: Highfive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Video Conferencing, Collaboration, and Acquired.
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/highfive/refs/heads/main/screenshots/highfive-2026-07-25T221202.png
security:
- kind: domain-security
  name: Highfive Domain Security
  slug: highfive-domain-security
  summary_line: TLSv1.3
slug: highfive
tags:
- Company
- Enterprise
- Video Conferencing
- Collaboration
- Acquired
- Dialpad
website: http://highfive.com
---
