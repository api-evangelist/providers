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
- description: Moogsoft is an AIOps platform that uses AI to reduce alert noise, correlate incidents, and automate root cause analysis.
  name: Moogsoft
  slug: moogsoft
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/moogsoft-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moogsoft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moogsoft-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moogsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moogsoft
- group: company
  title: ''
  type: Website
  url: https://www.moogsoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moogsoft.com
- group: company
  title: ''
  type: Blog
  url: https://moogsoft.com/feed/
created: '2026-03-27'
description: Moogsoft is an AIOps platform that uses AI to reduce alert noise, correlate incidents, and automate root cause analysis.
finops:
- name: Moogsoft Finops
  service_category: API
  slug: moogsoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moogsoft.png
layout: provider
modified: '2026-03-27'
name: Moogsoft
nav: Providers
network: true
overview: 'Moogsoft publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps and Incident Management.


  Moogsoft''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Moogsoft Plans Pricing
  plan_count: 3
  slug: moogsoft-plans-pricing
random_paper: 133
rate_limits:
- limit_count: 5
  name: Moogsoft Rate Limits
  slug: moogsoft-rate-limits
score:
  band: emerging
  composite: 12.6
  delta: -0.1
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moogsoft/refs/heads/main/screenshots/moogsoft-2026-06-20T185754.png
security:
- kind: domain-security
  name: Moogsoft Domain Security
  slug: moogsoft-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Moogsoft Vulnerability Disclosure
  slug: moogsoft-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Moogsoft Trust Center
  slug: moogsoft-trust-center
  summary_line: SOC 2, GDPR, CSA STAR
slug: moogsoft
tags:
- AIOps
- Incident Management
website: https://www.moogsoft.com
---
