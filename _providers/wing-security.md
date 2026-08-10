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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'The Wing Security platform API provides programmatic access to SaaS discovery, risk assessment, identity threat detection, and remediation capabilities. The platform supports webhook integrations and '
  name: Wing Security Platform API
  slug: wing-security-platform-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/wing-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wing-security-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wing-security
- group: company
  title: ''
  type: Website
  url: https://www.wing.security
- group: docs
  title: ''
  type: Documentation
  url: https://www.wing.security/resources
- group: other
  title: ''
  type: Platform
  url: https://wing.security/platform/
- group: company
  title: ''
  type: Blog
  url: https://wing.security/blog/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.wing.security/
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wing-security/refs/heads/main/json-ld/wing-security-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wing-security/refs/heads/main/vocabulary/wing-security-vocabulary.yml
created: '2026-03-27'
description: Wing Security is an AI security platform providing automated discovery, risk assessment, and governance of AI agents, SaaS applications, and app-to-app integrations. The platform delivers SaaS Security Posture Management (SSPM), Identity Threat Detection and Response (ITDR), and continuous observability for AI tools across enterprise environments.
examples:
- key_count: 13
  name: Wing Security Saas App Example
  slug: wing-security-saas-app-example
finops:
- name: Wing Security Finops
  service_category: API
  slug: wing-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wing-security.png
json_schemas:
- name: AI Agent
  property_count: 14
  slug: wing-security-ai-agent
- name: SaaS Application
  property_count: 13
  slug: wing-security-saas-app
json_structures:
- name: Wing Security Ai Agent Structure
  property_count: 0
  slug: wing-security-ai-agent-structure
- name: Wing Security Saas App Structure
  property_count: 0
  slug: wing-security-saas-app-structure
jsonld:
- class_count: 26
  name: Wing Security Context
  property_count: 0
  slug: wing-security-context
layout: provider
modified: '2026-05-03'
name: Wing Security
nav: Providers
network: true
overview: 'Wing Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Security, Identity Threat Detection, ITDR, SaaS Security, and SSPM.


  The Wing Security catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wing Security''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Wing Security Plans Pricing
  plan_count: 3
  slug: wing-security-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Wing Security Rate Limits
  slug: wing-security-rate-limits
rules:
- name: Wing Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wing-security-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 34.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wing-security/refs/heads/main/screenshots/wing-security-2026-06-20T201514.png
security:
- kind: domain-security
  name: Wing Security Domain Security
  slug: wing-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Wing Security Trust Center
  slug: wing-security-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: wing-security
tags:
- AI Security
- Identity Threat Detection
- ITDR
- SaaS Security
- SSPM
- Supply Chain Security
website: https://www.wing.security
---
