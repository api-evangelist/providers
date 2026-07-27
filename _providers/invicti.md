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
- description: The Invicti API provides programmatic access to Invicti security scanning capabilities, including API Discovery which helps build a complete inventory of an organization's internal and external API as
  name: Invicti API
  slug: invicti-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/invicti-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/invicti-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/invicti-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.invicti.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Invicti-Security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/invicti-security
- group: company
  title: ''
  type: Website
  url: https://www.invicti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.invicti.com/support/
- group: operate
  title: ''
  type: Support
  url: https://www.invicti.com/support/
created: '2025-01-08'
description: Invicti is an enterprise web application security solution providing automated vulnerability scanning, DAST, and API security testing. The Invicti platform includes API Discovery capabilities that help build a complete inventory of an organization's internal and external API assets.
finops:
- name: Invicti Finops
  service_category: API
  slug: invicti-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/invicti.png
layout: provider
modified: '2026-04-28'
name: Invicti
nav: Providers
network: true
overview: 'Invicti publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Security, DAST, Security, and Vulnerability Scanning.


  Invicti''s developer surface includes engineering blog, documentation, support, and 6 more developer resources.'
plans:
- name: Invicti Plans Pricing
  plan_count: 3
  slug: invicti-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Invicti Rate Limits
  slug: invicti-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/invicti/refs/heads/main/screenshots/invicti-2026-06-20T183522.png
security:
- kind: domain-security
  name: Invicti Domain Security
  slug: invicti-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Invicti Vulnerability Disclosure
  slug: invicti-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Invicti Trust Center
  slug: invicti-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: invicti
tags:
- API Security
- DAST
- Security
- Vulnerability Scanning
website: https://www.invicti.com/
---
