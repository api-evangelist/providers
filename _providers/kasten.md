---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://kasten.io/'', ''status'': 301, ''note'': ''declared website redirects to https://www.veeam.com/products/cloud/kubernetes-data-protection.html — a different registrable domain (kasten.io -> veeam.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/veeam/
- group: company
  title: ''
  type: Website
  url: https://kasten.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kasten.io/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kasten.io/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kasten.io/latest/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kasten.io/latest/install/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kastenhq
- group: operate
  title: ''
  type: Support
  url: https://community.veeam.com/groups/kubernetes-korner-90
- group: start
  title: ''
  type: SignUp
  url: https://www.veeam.com/products/cloud/kubernetes-backup/download-trial.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.veeam.com/products/cloud/kubernetes-data-protection.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veeam.com/legal/eula.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veeam.com/privacy-notice.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kasten.io/latest/releasenotes.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kasten-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kasten-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kasten-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kasten-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kasten-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kasten-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kasten-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kasten-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kasten-domain-security.yml
created: '2026-07-17'
description: Veeam Kasten (formerly Kasten K10) is an enterprise-grade, Kubernetes-native data protection platform. It delivers backup and recovery, disaster recovery, application mobility, ransomware resilience, and virtual-machine (KubeVirt) protection through policy-driven automation, and runs inside the customer's own Kubernetes cluster. Its programmable surface is a set of Kubernetes Custom Resources (policies, restore points, backup/restore/export actions) plus an in-cluster REST API served through the K10 gateway, authenticated with Kubernetes bearer tokens. Kasten was acquired by Veeam and its brand now sits under Veeam's Kubernetes data-protection line.
image: https://docs.kasten.io/img/docusaurus-social-card.jpg
layout: provider
modified: '2026-07-20'
name: Kasten
nav: Providers
network: true
overview: 'Kasten is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Kubernetes, Backup, and Disaster Recovery.


  Kasten''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, changelog, and 15 more developer resources.'
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/kasten/refs/heads/main/screenshots/kasten-2026-07-25T223520.png
security:
- kind: authentication
  name: Kasten Authentication
  slug: kasten-authentication
  summary_line: http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Kasten Domain Security
  slug: kasten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kasten
tags:
- Company
- Cybersecurity
- Kubernetes
- Backup
- Disaster Recovery
- Data Protection
- Cloud-Native
- DevOps
website: https://kasten.io/
---
