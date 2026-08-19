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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Keepit is a SaaS backup and recovery platform providing independent cloud-to-cloud data protection for Microsoft 365, Google Workspace, Salesforce, and other SaaS applications.
  name: Keepit
  slug: keepit
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/keepit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keepit-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keepit-official
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keepit-a-s
- group: company
  title: ''
  type: Website
  url: https://www.keepit.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.keepit.com/resources
- group: agent
  title: ''
  type: LlmsText
  url: https://www.keepit.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.keepit.com/blog/
created: '2026-03-27'
description: Keepit is a SaaS backup and recovery platform providing independent cloud-to-cloud data protection for Microsoft 365, Google Workspace, Salesforce, and other SaaS applications.
finops:
- name: Keepit Finops
  service_category: API
  slug: keepit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keepit.png
layout: provider
modified: '2026-04-28'
name: Keepit
nav: Providers
network: true
overview: 'Keepit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Protection, SaaS Backup, Backup And Recovery, and Cloud.


  Keepit''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Keepit Plans Pricing
  plan_count: 3
  slug: keepit-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Keepit Rate Limits
  slug: keepit-rate-limits
score:
  band: emerging
  composite: 14.2
  delta: -0.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keepit/refs/heads/main/screenshots/keepit-2026-06-20T183941.png
security:
- kind: domain-security
  name: Keepit Domain Security
  slug: keepit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Keepit Trust Center
  slug: keepit-trust-center
  summary_line: ISO 27001, GDPR
slug: keepit
tags:
- Data Protection
- SaaS Backup
- Backup And Recovery
- Cloud
website: https://www.keepit.com
---
