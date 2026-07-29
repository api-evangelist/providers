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
api_count: 5
apis:
- description: 'The CIP Kernel is a Super Long-Term Support (SLTS) Linux kernel branch maintained for ten or more years, providing a stable base for industrial systems that must remain in service across multi-decade '
  name: CIP SLTS Kernel
  slug: cip-kernel
- description: CIP Core provides a curated set of Debian-derived user-space packages aligned with the SLTS kernel to deliver a complete reference platform for civil infrastructure devices.
  name: CIP Core Packages
  slug: cip-core
- description: The CIP Software Update working group maintains tooling such as SWUpdate and hawkBit-based servers used to deliver secure over-the-air updates across long-lived industrial deployments.
  name: CIP Software Update
  slug: cip-software-update
- description: The CIP Security working group aligns the CIP base layer with IEC 62443-4-1 and 62443-4-2 industrial cybersecurity requirements and tracks CVE handling across the SLTS kernel and user-space.
  name: CIP Security
  slug: cip-security
- description: The CIP Testing working group runs continuous-integration and hardware-in-the-loop testing on member-supplied boards to validate kernel and core packages against the SLTS branch.
  name: CIP Testing
  slug: cip-testing
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civil-infrastructure-platform-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civil-infrastructure-platform
- group: company
  title: ''
  type: Website
  url: https://www.cip-project.org/
- group: other
  title: ''
  type: Wiki
  url: https://wiki.linuxfoundation.org/civilinfrastructureplatform
- group: build
  title: ''
  type: GitLab
  url: https://gitlab.com/cip-project
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cip-project
- group: other
  title: ''
  type: Mailing List
  url: https://lists.cip-project.org/g/cip-dev
- group: other
  title: ''
  type: Foundation
  url: https://www.linuxfoundation.org/projects/civil-infrastructure-platform/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/civil-infrastructure-platform-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/civil-infrastructure-platform-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://cip-project.org/blog/
created: '2026-03-16'
description: The Civil Infrastructure Platform (CIP) is a Linux Foundation collaborative project that builds an industrial-grade open source base layer for civil infrastructure systems such as transportation, power generation and distribution, building and city management, industrial control, and healthcare equipment. CIP curates a Super Long-Term Support (SLTS) kernel and core user-space packages that can be maintained for more than ten years, plus working groups for security (IEC 62443 alignment), software update, real-time, and testing. CIP does not publish a public REST API surface; its programmable interface is the source code, kernel, and tooling published through GitLab and Debian-derived package archives.
finops:
- name: Civil Infrastructure Platform Finops
  service_category: API
  slug: civil-infrastructure-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/civil-infrastructure-platform.png
jsonld:
- class_count: 13
  name: Civil Infrastructure Platform Context
  property_count: 0
  slug: civil-infrastructure-platform-context
layout: provider
modified: '2026-04-23'
name: Civil Infrastructure Platform
nav: Providers
network: true
overview: 'Civil Infrastructure Platform publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded, Industrial, Infrastructure, Linux, and Linux Foundation.


  The Civil Infrastructure Platform catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Civil Infrastructure Platform''s developer surface includes GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Civil Infrastructure Platform Plans Pricing
  plan_count: 3
  slug: civil-infrastructure-platform-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Civil Infrastructure Platform Rate Limits
  slug: civil-infrastructure-platform-rate-limits
rules:
- name: Civil Infrastructure Platform API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: civil-infrastructure-platform-rules
score:
  band: emerging
  composite: 25.3
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 28.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/civil-infrastructure-platform/refs/heads/main/screenshots/civil-infrastructure-platform-2026-06-20T174430.png
security:
- kind: domain-security
  name: Civil Infrastructure Platform Domain Security
  slug: civil-infrastructure-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: civil-infrastructure-platform
tags:
- Embedded
- Industrial
- Infrastructure
- Linux
- Linux Foundation
- Long-Term Support
- Open Source
website: https://www.cip-project.org/
---
