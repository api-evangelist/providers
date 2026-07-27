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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'The official public API for the Manifest Cyber platform v1. Used by Manifest''s frontend apps and internal ETL processes to access SBOM data, vulnerability analysis, and software supply chain security '
  name: Manifest Cyber API
  slug: manifest-cyber-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/manifest-cyber-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manifest-cyber-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manifest-cyber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manifestcyber
- group: company
  title: ''
  type: Website
  url: https://manifestcyber.com/
- group: company
  title: ''
  type: Blog
  url: https://manifestcyber.com/blog/rss.xml
created: '2025-02-12'
description: Manifest Cyber provides a cybersecurity platform with an official public API for accessing software bill of materials (SBOM) data, vulnerability analysis, and supply chain security information used by Manifest's frontend apps and internal ETL pipelines.
finops:
- name: Manifest Cyber Finops
  service_category: API
  slug: manifest-cyber-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manifest-cyber.png
layout: provider
modified: '2026-04-28'
name: Manifest Cyber
nav: Providers
network: true
overview: 'Manifest Cyber publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, SBOM, Supply Chain Security, and Vulnerability Management.


  Manifest Cyber''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Manifest Cyber Plans Pricing
  plan_count: 3
  slug: manifest-cyber-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Manifest Cyber Rate Limits
  slug: manifest-cyber-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 37.7
    developer_ergonomics: 2.2
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manifest-cyber/refs/heads/main/screenshots/manifest-cyber-2026-06-20T184923.png
security:
- kind: domain-security
  name: Manifest Cyber Domain Security
  slug: manifest-cyber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Manifest Cyber Trust Center
  slug: manifest-cyber-trust-center
  summary_line: ISO 27001, FedRAMP, GDPR
slug: manifest-cyber
tags:
- Cybersecurity
- SBOM
- Supply Chain Security
- Vulnerability Management
website: https://manifestcyber.com/
---
