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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Pantheon platform REST API (terminus.pantheon.io) underpins the Terminus CLI and enables programmatic management of sites, environments, deployments, domains, backups, teams, organizations, SSH ke
  name: Pantheon REST API
  slug: pantheon-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/pantheon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pantheon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pantheon.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pantheon.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pantheon-systems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getpantheon
- group: company
  title: ''
  type: Blog
  url: https://pantheon.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pantheon.io/plans/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pantheon.io
- group: other
  title: ''
  type: X
  url: https://x.com/getpantheon
- group: commercial
  title: ''
  type: Plans
  url: plans/pantheon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pantheon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pantheon-finops.yml
created: '2026-06-13'
description: Pantheon is a WebOps platform for WordPress and Drupal that provides a REST API and CLI (Terminus) for managing sites, environments, deployments, domains, backups, and team workflows. The platform serves over 700,000 sites with built-in dev/staging/production environments, Global CDN, automated updates, and portfolio governance tools.
finops:
- name: Pantheon Finops
  service_category: ''
  slug: pantheon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pantheon.png
layout: provider
modified: '2026-06-13'
name: Pantheon
nav: Providers
network: true
overview: 'Pantheon publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include WebOps, WordPress, Drupal, CMS, and Hosting.


  Pantheon''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Pantheon Plans Pricing
  plan_count: 0
  slug: pantheon-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Pantheon Rate Limits
  slug: pantheon-rate-limits
score:
  band: emerging
  composite: 24.3
  delta: -0.8
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pantheon/refs/heads/main/screenshots/pantheon-2026-06-20T191343.png
security:
- kind: domain-security
  name: Pantheon Domain Security
  slug: pantheon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pantheon Trust Center
  slug: pantheon-trust-center
  summary_line: SOC 2, GDPR
slug: pantheon
tags:
- WebOps
- WordPress
- Drupal
- CMS
- Hosting
- CDN
- DevOps
- Deployments
- Sites
- Environments
website: https://pantheon.io
---
