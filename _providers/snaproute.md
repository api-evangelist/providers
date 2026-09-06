---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://snaproute.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.infoblox.com/ — a different registrable domain (snaproute.com -> infoblox.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snaproute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snaproute.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snaproute
created: '2026-07-17'
description: 'SnapRoute was a cloud-native networking startup, backed by Lightspeed Venture Partners and Norwest Venture Partners, that built a containerized, microservices-based network operating system (its FlexSwitch / Cloud-Native Network OS) aimed at running switch software with the same DevOps tooling used for application infrastructure. Its public GitHub organization (github.com/snaproute) reflects that focus — OpenConfig and YANG tooling (pyang/pyangbind), OpenNetworkLinux, netlink, sFlow, and a Docker-based training lab — but it has been dormant since 2020 and ships no published REST/OpenAPI interface, SDKs, or developer portal. The company no longer operates independently: the snaproute.com domain now 301-redirects to infoblox.com, so there is no live API surface to enrich. This profile records the verifiable remnants (GitHub organization, domain posture) rather than a working developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snaproute.png
layout: provider
modified: '2026-07-21'
name: Snaproute
nav: Providers
network: true
overview: Snaproute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Network Operating System, Cloud-Native, and SDN.
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/snaproute/refs/heads/main/screenshots/snaproute-2026-09-02T160008.png
security:
- kind: domain-security
  name: Snaproute Domain Security
  slug: snaproute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snaproute
tags:
- Company
- Networking
- Network Operating System
- Cloud-Native
- SDN
- Infrastructure
- Defunct
website: https://snaproute.com
---
