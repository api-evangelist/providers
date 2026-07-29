---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Metal3 extends Kubernetes with the BareMetalHost custom resource for managing physical servers. The API supports hardware inventory discovery, firmware configuration, BIOS settings, RAID configuration
  name: Metal3 BareMetalHost API
  slug: metal3-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metal3-io-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://metal3.io/documentation.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/metal3-io
- group: company
  title: ''
  type: Blog
  url: https://metal3.io/feed.xml
created: '2026-03-16'
description: Metal3 (Metal Kubed) is a CNCF incubating project that provides bare metal host provisioning for Kubernetes. It leverages Ironic for hardware management and integrates with the Cluster API to enable Kubernetes-native lifecycle management of bare metal infrastructure. Metal3 automates server discovery, inspection, provisioning, and deprovisioning using Kubernetes custom resources.
finops:
- name: Metal3 Io Finops
  service_category: API
  slug: metal3-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metal3-io.png
layout: provider
modified: '2026-04-28'
name: Metal3
nav: Providers
network: true
overview: 'Metal3 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bare Metal, Cloud Native, Incubating, Infrastructure, and Kubernetes.


  Metal3''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Metal3 Io Plans Pricing
  plan_count: 3
  slug: metal3-io-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Metal3 Io Rate Limits
  slug: metal3-io-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -1.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metal3-io/refs/heads/main/screenshots/metal3-io-2026-06-20T185242.png
security:
- kind: domain-security
  name: Metal3 Io Domain Security
  slug: metal3-io-domain-security
  summary_line: TLSv1.3
slug: metal3-io
tags:
- Bare Metal
- Cloud Native
- Incubating
- Infrastructure
- Kubernetes
- Provisioning
website: https://metal3.io
---
