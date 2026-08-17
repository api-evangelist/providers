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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Tenant-scoped REST API for managing agents, threats, alerts, sites, accounts, exclusions, policies, and reporting in the SentinelOne Singularity Platform. Each customer accesses the API at their own m
  name: SentinelOne Management API
  slug: management-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sentinelone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sentinelone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentinelone-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sentinel-One
- group: company
  title: ''
  type: Website
  url: https://www.sentinelone.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.sentinelone.com/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sentinelone.com/platform-packages/
- group: start
  title: ''
  type: Signup
  url: https://www.sentinelone.com/request-demo/
- group: operate
  title: ''
  type: Support
  url: https://www.sentinelone.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.sentinelone.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sentinelone/
created: '2026-05-11'
description: SentinelOne is an AI-driven extended detection and response (XDR) cloud security platform delivering autonomous endpoint protection, EDR, identity security, cloud workload protection, and threat hunting through its Singularity Platform. The Management API exposes the same operations as the web console for agents, threats, alerts, sites, accounts, exclusions, and policy management. Authentication uses tenant-issued API tokens passed in the Authorization header as `ApiToken <token>`.
graphqls:
- description: SentinelOne is an AI-powered endpoint security platform. The API covers agent management, threat detection alerts, automated response actions, forensics, vulnerability data, deep visibility queries, t
  name: SentinelOne GraphQL API
  slug: sentinelone-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sentinelone.png
layout: provider
modified: '2026-05-11'
name: SentinelOne
nav: Providers
network: true
overview: 'SentinelOne publishes 1 API on the [APIs.io](https://apis.io/) network: Management API. Tagged areas include Security, XDR, EDR, Endpoint Protection, and Threat Detection.


  SentinelOne''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 145
score:
  band: emerging
  composite: 27.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 43.2
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 27.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Sentinelone Domain Security
  slug: sentinelone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sentinelone Vulnerability Disclosure
  slug: sentinelone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sentinelone Trust Center
  slug: sentinelone-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, GDPR
slug: sentinelone
tags:
- Security
- XDR
- EDR
- Endpoint Protection
- Threat Detection
- Incident Response
- Cloud Security
- Identity Security
website: https://www.sentinelone.com
---
