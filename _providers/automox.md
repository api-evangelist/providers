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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing the Automox endpoint management platform including organizations, zones, devices, groups, policies, packages, worklets, commands, events, reports, and user accounts. Authenticati
  name: Automox API
  slug: api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/automox-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/automox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automox-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/automox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/automox
- group: company
  title: ''
  type: Website
  url: https://www.automox.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automox.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.automox.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://console.automox.com/signup
created: '2026-05-11'
description: Automox is a cloud-native IT operations and endpoint management platform that automates patching, configuration, and software deployment across Windows, macOS, and Linux devices from a single console. The Automox API is a REST API that gives developers programmatic access to organizations, zones, devices, groups, policies, packages, worklets, commands, events, reports, and users for building integrations and automating endpoint management workflows, authenticated with API keys.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automox.png
layout: provider
modified: '2026-05-11'
name: Automox
nav: Providers
network: true
overview: 'Automox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Endpoint Management, Patch Management, IT Operations, Device Management, and Configuration Management.


  Automox''s developer surface includes documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 43
score:
  band: emerging
  composite: 13.0
  delta: -2.4
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automox/refs/heads/main/screenshots/automox-2026-06-20T172659.png
security:
- kind: domain-security
  name: Automox Domain Security
  slug: automox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Automox Vulnerability Disclosure
  slug: automox-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Automox Trust Center
  slug: automox-trust-center
  summary_line: SOC 2, PCI DSS, GDPR, CSA STAR
slug: automox
tags:
- Endpoint Management
- Patch Management
- IT Operations
- Device Management
- Configuration Management
- Security
website: https://www.automox.com
---
