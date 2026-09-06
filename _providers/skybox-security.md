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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skybox-security-domain-security.yml
coverage:
  checked: '2026-08-28'
  detail: Skybox Security ceased operations on 2026-02-24 and Tufin bought a limited part of its assets; www.skyboxsecurity.com and docs.skyboxsecurity.com now 301 to tufin.com/tufin-expresspath-program and tufin.com/developers, api. and developer.skyboxsecurity.com no longer resolve, and every /.well-known/* path returns the same catch-all Tufin HTML page rather than a Skybox document.
  evidence:
  - status: 301
    url: https://www.skyboxsecurity.com/
  - status: 301
    url: https://docs.skyboxsecurity.com/OnlineDocs/Content
  - status: 200
    url: https://www.skyboxsecurity.com/.well-known/agent-card.json
  - status: 0
    url: https://api.skyboxsecurity.com/
  reason: defunct
  state: none
created: '2026-08-28'
description: Skybox Security was a cybersecurity vendor, headquartered in San Jose, California with R&D in Israel, whose Security Posture Management Platform combined attack surface visibility, network modelling and attack-path analysis, firewall assurance and change management, vulnerability and exposure management, and its own threat intelligence feed for large hybrid enterprise and OT networks. It raised roughly $335 million in venture and private-equity funding, including a $50 million round in February 2023, before ceasing operations on February 24, 2025 and laying off approximately 300 employees across the United States and Israel. Tufin acquired a limited portion of Skybox's business and technology and retained select personnel, but did not assume Skybox's customer contracts or support obligations; it instead runs an "ExpressPath for Skybox Customers" migration programme onto the Tufin Orchestration Suite. Skybox exposed a REST API and integrations (Splunk, ServiceNow, Elasticsearch)
  to its customers, but the reference lived behind customer/partner credentials at docs.skyboxsecurity.com and no machine-readable contract was ever published publicly. Every skyboxsecurity.com host now 301-redirects into tufin.com, so nothing served on those hosts can be attributed to Skybox any longer.
layout: provider
modified: '2026-08-28'
name: Skybox Security
nav: Providers
network: true
overview: Skybox Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Network Security, and Vulnerability Management.
random_paper: 9
security:
- kind: domain-security
  name: Skybox Security Domain Security
  slug: skybox-security-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skybox-security
tags:
- Company
- Security
- Cybersecurity
- Network Security
- Vulnerability Management
- Firewall Management
- Security Posture Management
- Threat Intelligence
- Attack Surface Management
---
