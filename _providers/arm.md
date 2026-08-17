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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://developer.arm.com/Arm%20Security%20Center
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/arm-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.arm.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.arm.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.arm.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.arm.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ARM-software
- group: operate
  title: ''
  type: Support
  url: https://community.arm.com
- group: company
  title: ''
  type: Blog
  url: https://www.arm.com/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arm.com/company/policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arm.com/company/policies/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arm-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arm-llms.txt
created: '2026-07-17'
description: 'Arm Holdings plc (NASDAQ: ARM) is the semiconductor and software design company behind the energy-efficient Arm architecture that powers the majority of the world''s smartphones and billions of chips across mobile, automotive, IoT, edge AI, servers, and cloud. Arm licenses processor IP (Cortex, Neoverse, Ethos, Mali) and Compute Subsystems rather than manufacturing chips itself. For developers, Arm operates a developer hub, technical documentation, learning paths, community forums, and a large open-source GitHub organization (ARM-software) publishing firmware, compute libraries, and ML tooling. Arm does not currently expose a public REST API product; this profile catalogs its developer surface and web properties.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arm.png
layout: provider
modified: '2026-07-18'
name: Arm
nav: Providers
network: true
overview: 'Arm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Chip Design, Processor IP, and Arm Architecture.


  Arm''s developer surface includes documentation, getting-started guide, support, engineering blog, and 11 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 19.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arm/refs/heads/main/screenshots/arm-2026-07-25T201213.png
security:
- kind: domain-security
  name: Arm Domain Security
  slug: arm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arm Vulnerability Disclosure
  slug: arm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arm
tags:
- Company
- Semiconductors
- Chip Design
- Processor IP
- Arm Architecture
- Embedded
- Edge AI
- Frontier Tech
website: https://www.arm.com
---
