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
api_count: 2
apis:
- description: 'The Salt Security API Protection Platform provides full lifecycle API security including automated API discovery, posture governance, real-time threat protection, and remediation insights. It uses AI '
  name: Salt Security API Protection Platform
  slug: salt-security-platform
- description: 'The Salt Security Developer Portal provides REST APIs for automating API security practices. The portal offers comprehensive documentation with request/response structures, parameters, authentication '
  name: Salt Security Developer Portal API
  slug: salt-developer-portal-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salt-security-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Secful
- group: company
  title: ''
  type: Website
  url: https://salt.security
- group: other
  title: ''
  type: Platform
  url: https://salt.security/platform
- group: docs
  title: ''
  type: Documentation
  url: https://salt.security/api-security-platform
- group: company
  title: ''
  type: Blog
  url: https://salt.security/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://salt.security/pricing
- group: company
  title: ''
  type: Partners
  url: https://salt.security/partners
- group: company
  title: ''
  type: About
  url: https://salt.security/about
- group: operate
  title: ''
  type: Contact
  url: https://salt.security/contact
- group: start
  title: ''
  type: Demo
  url: https://salt.security/demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saltsecurity/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/salaboreal
- group: other
  title: ''
  type: Resources
  url: https://salt.security/resources
- group: other
  title: ''
  type: WhyUs
  url: https://salt.security/why-salt
- group: agent
  title: ''
  type: AgenticSecurity
  url: https://salt.security/platform
created: '2025-01-08'
description: Salt Security provides an AI-powered API security platform that discovers all APIs, stops API attacks in real-time, and provides remediation insights. The platform delivers full lifecycle API security through API discovery, posture governance, and advanced threat protection using patented AI and ML technology. Salt Security announced an Agentic AI Security platform and MCP Discovery capabilities in 2026.
finops:
- name: Salt Security Finops
  service_category: API
  slug: salt-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salt-security.png
json_schemas:
- name: Salt Security API Endpoint
  property_count: 16
  slug: salt-security-api-endpoint
- name: Salt Security API Attack
  property_count: 15
  slug: salt-security-attack
json_structures:
- name: Salt Security Api Endpoint Structure
  property_count: 0
  slug: salt-security-api-endpoint-structure
jsonld:
- class_count: 0
  name: Salt Security Context
  property_count: 4
  slug: salt-security-context
layout: provider
modified: '2026-05-02'
name: Salt Security
nav: Providers
network: true
overview: 'Salt Security publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Security, AI, API Discovery, Posture Governance, and Threat Protection.


  The Salt Security catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Salt Security''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Salt Security Plans Pricing
  plan_count: 3
  slug: salt-security-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Salt Security Rate Limits
  slug: salt-security-rate-limits
rules:
- name: Salt Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: salt-security-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.9
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 36.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salt-security/refs/heads/main/screenshots/salt-security-2026-06-20T193357.png
security:
- kind: domain-security
  name: Salt Security Domain Security
  slug: salt-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: salt-security
tags:
- API Security
- AI
- API Discovery
- Posture Governance
- Threat Protection
- Security
website: https://salt.security
---
