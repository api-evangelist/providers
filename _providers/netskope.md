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
api_count: 2
apis:
- description: Tenant-scoped REST API for retrieving events, alerts, incidents, audit logs, network and application telemetry, and for managing policies, IoCs, and configuration on the Netskope platform. Authenticat
  name: Netskope REST API v2
  slug: rest-api-v2
- description: SCIM 2.0 provisioning API for users and groups, enabling identity providers and IGA platforms to synchronize directory state into Netskope using a dedicated SCIM token issued from the Security Cloud P
  name: Netskope SCIM API
  slug: scim-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netskope-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netskope-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netskopeoss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netskope
- group: company
  title: ''
  type: Website
  url: https://www.netskope.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netskope.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netskope.com/request-pricing
- group: start
  title: ''
  type: Signup
  url: https://www.netskope.com/request-demo
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.netskope.com/llms.txt
created: '2026-05-11'
description: Netskope is a security service edge (SSE) and SASE platform delivering cloud-native Secure Web Gateway, CASB, Zero Trust Network Access, data loss prevention, and threat protection from its NewEdge global network. The Netskope REST API v2 provides tenant-level programmatic access to events, alerts, incidents, policies, IoCs, SCIM provisioning, and configuration so SOC and platform teams can automate SOAR, SIEM, and IGA workflows using service-account bearer tokens in the Netskope-Api-Token header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netskope.png
layout: provider
modified: '2026-05-11'
name: Netskope
nav: Providers
network: true
overview: 'Netskope publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, SASE, SSE, CASB, and Zero Trust.


  Netskope''s developer surface includes documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/netskope/refs/heads/main/screenshots/netskope-2026-06-20T190208.png
security:
- kind: domain-security
  name: Netskope Domain Security
  slug: netskope-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Netskope Vulnerability Disclosure
  slug: netskope-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: netskope
tags:
- Security
- SASE
- SSE
- CASB
- Zero Trust
- SWG
- DLP
- Cloud Security
website: https://www.netskope.com/
---
