---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.cyral.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.varonis.com/platform/database-activity-monitoring — a different registrable domain (cyral.com -> varonis.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.cyral.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyralinc
- group: docs
  title: ''
  type: Documentation
  url: https://registry.terraform.io/providers/cyralinc/cyral/latest/docs
- group: build
  title: ''
  type: Packages
  url: packages/cyral-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cyral-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyral-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cyral-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cyral-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cyral-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyral-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyral-llms.txt
created: '2026-07-17'
description: 'Cyral is a data security and governance platform (founded 2018, Milpitas CA; acquired by Varonis in March 2025) that provides an agentless, stateless data-layer sidecar for monitoring and governing access to data repositories such as Snowflake, PostgreSQL, MySQL, MongoDB, Amazon S3, Kafka, and Oracle. Cyral was built API-first: its Control Plane exposes a REST API secured with OAuth2 client-credentials, fully automatable through the official Cyral Terraform provider (cyralinc/cyral) and supporting Terraform modules for AWS, Azure, and Okta. Following the Varonis acquisition, cyral.com now redirects to Varonis'' Database Activity Monitoring product, but the first-party developer tooling remains published on the cyralinc GitHub organization and the Terraform Registry.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyral.png
layout: provider
modified: '2026-07-18'
name: Cyral
nav: Providers
network: true
overview: 'Cyral is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Data Security, Database Activity Monitoring, and Data Governance.


  Cyral''s developer surface includes documentation, authentication, changelog, and 8 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/cyral/refs/heads/main/screenshots/cyral-2026-07-25T211100.png
security:
- kind: authentication
  name: Cyral Authentication
  slug: cyral-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cyral Domain Security
  slug: cyral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyral
tags:
- Company
- Cybersecurity
- Data Security
- Database Activity Monitoring
- Data Governance
- Access Control
- Terraform
- SCIM
- Authentication
website: https://www.cyral.com/
---
