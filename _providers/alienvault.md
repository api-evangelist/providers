---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://otx.alienvault.com/api/v1
  baseurl_source: declared
  description: Indicator of compromise detail lookups and submission
  name: AlienVault Indicators API
  slug: alienvault-indicators-api
- baseURL: https://otx.alienvault.com/api/v1
  baseurl_source: declared
  description: Threat pulses (curated indicator collections)
  name: AlienVault Pulses API
  slug: alienvault-pulses-api
- baseURL: https://otx.alienvault.com/api/v1
  baseurl_source: declared
  description: Search across pulses and users
  name: AlienVault Search API
  slug: alienvault-search-api
- baseURL: https://otx.alienvault.com/api/v1
  baseurl_source: declared
  description: OTX community users
  name: AlienVault Users API
  slug: alienvault-users-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AlienVault OTX DirectConnect Indicators API
  slug: open-alienvault-indicators-api
- collection_type: open
  name: AlienVault OTX DirectConnect Indicators Pulses API
  slug: open-alienvault-pulses-api
- collection_type: open
  name: AlienVault OTX DirectConnect Indicators Search API
  slug: open-alienvault-search-api
- collection_type: open
  name: AlienVault OTX DirectConnect Indicators Users API
  slug: open-alienvault-users-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/att/
- group: other
  title: ''
  type: Overlay
  url: overlays/alienvault-otx-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://otx.alienvault.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://otx.alienvault.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://otx.alienvault.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlienVault-Labs
- group: start
  title: ''
  type: SignUp
  url: https://otx.alienvault.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://otx.alienvault.com/terms/
- group: build
  title: ''
  type: Packages
  url: packages/alienvault-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alienvault-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alienvault-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alienvault-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alienvault-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alienvault-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alienvault-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alienvault-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alienvault-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alienvault-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: AlienVault is the security company behind the Open Threat Exchange (OTX), one of the largest open threat-intelligence communities in the world. OTX lets security practitioners and researchers create and share "pulses" — curated collections of indicators of compromise (IOCs) such as malicious IPs, domains, hostnames, URLs, file hashes, and CVEs — and consume that shared intelligence to automatically update their defensive infrastructure. The OTX DirectConnect API provides programmatic access to subscribed pulses, indicator detail lookups across multiple facets (general, geo, malware, passive DNS, reputation, URL lists), pulse and user search, and indicator submission for analysis. Authentication is via an X-OTX-API-KEY header. AlienVault was acquired by AT&T in 2018, becoming AT&T Cybersecurity, and OTX now operates under the LevelBlue brand. An official Python SDK (OTXv2) is published on PyPI and GitHub.
image: https://otx.alienvault.com/static/otx/img/otx_logo.png
layout: provider
modified: '2026-07-17'
name: AlienVault
nav: Providers
network: true
overview: 'AlienVault publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Indicators API, Pulses API, Search API, and 1 more. Tagged areas include Company, Security, Threat Intelligence, Cybersecurity, and Open Threat Exchange.


  AlienVault''s developer surface includes documentation, API reference, signup flow, authentication, and 15 more developer resources.'
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/alienvault/refs/heads/main/screenshots/alienvault-2026-07-25T195617.png
security:
- kind: authentication
  name: Alienvault Authentication
  slug: alienvault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alienvault Domain Security
  slug: alienvault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alienvault
tags:
- Company
- Security
- Threat Intelligence
- Cybersecurity
- Open Threat Exchange
- Indicators of Compromise
- Threat Feeds
website: https://otx.alienvault.com/api
---
