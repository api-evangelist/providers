---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The CrowdStrike API provides access to platform services and data for enterprise integration and automation.
  name: CrowdStrike API
  slug: crowdstrike-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/crowdstrike-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdstrike-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdstrike-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrowdStrike
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crowdstrike
- group: company
  title: ''
  type: Website
  url: https://www.crowdstrike.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.crowdstrike.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.crowdstrike.com/blog/feed/
created: '2026-04-19'
description: CrowdStrike is a major US corporation and Fortune 1000 company. The CrowdStrike API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Crowdstrike Finops
  service_category: Cybersecurity
  slug: crowdstrike-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the CrowdStrike Falcon platform. CrowdStrike exposes its capabilities through an OAuth2-based REST API; this schema models that surface as Graph
  name: CrowdStrike GraphQL Schema
  slug: crowdstrike-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdstrike.png
layout: provider
modified: '2026-04-19'
name: CrowdStrike
nav: Providers
network: true
overview: 'CrowdStrike publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity and Endpoint Security.


  CrowdStrike''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Crowdstrike Plans Pricing
  plan_count: 4
  slug: crowdstrike-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 2
  name: Crowdstrike Rate Limits
  slug: crowdstrike-rate-limits
score:
  band: emerging
  composite: 21.3
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/screenshots/crowdstrike-2026-06-20T175254.png
security:
- kind: domain-security
  name: Crowdstrike Domain Security
  slug: crowdstrike-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crowdstrike Vulnerability Disclosure
  slug: crowdstrike-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Crowdstrike Trust Center
  slug: crowdstrike-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: crowdstrike
tags:
- Cybersecurity
- Endpoint Security
website: https://www.crowdstrike.com
---
