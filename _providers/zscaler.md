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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: REST API for managing Zscaler Internet Access policies, URL filtering, cloud sandbox, DLP, location and user provisioning, and reporting on web traffic and threats across the Zscaler Cloud platform.
  name: Zscaler Internet Access (ZIA) API
  slug: zia-api
- description: REST API for managing Zscaler Private Access (ZPA) configurations including segment groups, application segments, connector groups, SCIM provisioning, policies, and access logs.
  name: Zscaler Private Access (ZPA) API
  slug: zpa-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zscaler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zscaler-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zscaler
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zscaler
- group: company
  title: ''
  type: Website
  url: https://www.zscaler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zscaler.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zscaler.com/pricing-and-plans
- group: start
  title: ''
  type: Signup
  url: https://www.zscaler.com/products/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.zscaler.com/blogs
created: '2026-05-11'
description: Zscaler is a cloud security platform delivering Zero Trust Exchange services including Zscaler Internet Access (ZIA), Zscaler Private Access (ZPA), and Zscaler Digital Experience (ZDX). Zscaler exposes REST APIs across its product suite for configuration, policy management, and reporting, authenticated via API keys, OAuth 2.0, or session-based authentication depending on the product and cloud (zsapi).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zscaler.png
layout: provider
modified: '2026-05-11'
name: Zscaler
nav: Providers
network: true
overview: 'Zscaler publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Security, Zero Trust, SASE, Network Security, and SWG.


  Zscaler''s developer surface includes documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.4
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zscaler/refs/heads/main/screenshots/zscaler-2026-06-20T201955.png
security:
- kind: domain-security
  name: Zscaler Domain Security
  slug: zscaler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zscaler Vulnerability Disclosure
  slug: zscaler-vulnerability-disclosure
  summary_line: Bugcrowd
slug: zscaler
tags:
- Cloud Security
- Zero Trust
- SASE
- Network Security
- SWG
website: https://www.zscaler.com/
---
