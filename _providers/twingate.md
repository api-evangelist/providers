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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: GraphQL Admin API for managing Twingate resources, remote networks, connectors, users, groups, devices, service accounts, security policies, certificate authorities, and DNS filtering profiles. Authen
  name: Twingate Admin API
  slug: admin-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twingate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.twingate.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.twingate.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.twingate.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://auth.twingate.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Twingate
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/Twingate/twingate/latest
- group: operate
  title: ''
  type: Support
  url: https://help.twingate.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twingate
created: '2026-05-11'
description: Twingate is a Zero Trust Network Access (ZTNA) platform that replaces legacy VPNs with software-defined perimeters, providing identity-based, least-privilege access to private resources without exposing them to the public internet. The Twingate Admin API is a GraphQL API authenticated via API key (X-API-KEY header) that enables programmatic management of remote networks, connectors, resources, users, groups, service accounts, devices, policies, and DNS filtering profiles.
graphqls:
- description: GraphQL Admin API for managing Twingate resources, remote networks, connectors, users, groups, devices, service accounts, security policies, certificate authorities, and DNS filtering profiles. Authen
  name: Twingate GraphQL API
  slug: twingate-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twingate.png
layout: provider
modified: '2026-05-11'
name: Twingate
nav: Providers
network: true
overview: 'Twingate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Zero Trust, ZTNA, Network Access, VPN Replacement, and Identity-Based Access.


  Twingate''s developer surface includes documentation, pricing, signup flow, support, and 5 more developer resources.'
random_paper: 51
score:
  band: minimal
  composite: 14.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twingate/refs/heads/main/screenshots/twingate-2026-06-20T195919.png
security:
- kind: domain-security
  name: Twingate Domain Security
  slug: twingate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: twingate
tags:
- Zero Trust
- ZTNA
- Network Access
- VPN Replacement
- Identity-Based Access
- Security
website: https://www.twingate.com
---
