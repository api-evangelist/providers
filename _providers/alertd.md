---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: AlertD provides a REST API for monitoring and alerting on AWS resources; the API is gated behind authentication and not publicly documented.
  name: AlertD API
  slug: alertd-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/alertd/cli/alertd-cli.yml
  title: ''
  type: CLI
  url: cli/alertd-cli.yml
- group: auth
  href: https://artifacts.apis.io/alertd/authentication/alertd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alertd-authentication.yml
- group: other
  href: https://artifacts.apis.io/alertd/hosts/alertd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alertd-hosts.yml
- group: other
  href: https://artifacts.apis.io/alertd/vendors/alertd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alertd-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alertd.ai/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alertd.ai/getting-started/overview
- group: auth
  href: https://artifacts.apis.io/alertd/security/alertd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alertd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alertd.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alertd.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.alertd.ai/blog
coverage:
  checked: '2026-10-29'
  detail: The API endpoints require authentication tokens and return 403 Missing Authentication Token, indicating the contract is behind a login wall.
  evidence:
  - status: 403
    url: https://api.alertd.ai/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-29'
description: AlertD is an AI‑powered conversational agent platform designed for DevOps and SRE teams to manage AWS infrastructure. It provides read‑only, natural‑language queries across services like EC2, S3, RDS, and CloudWatch, delivering structured, actionable insights without requiring scripts or CLI commands. Founded in 2024, AlertD aims to reduce toil, improve reliability, and enhance team collaboration by acting as a “Slack for production uptime,” offering transparent execution plans, multi‑service support, and secure read‑only AWS access.
image: https://cdn.prod.website-files.com/683d1ccbb236320c5058d927/6a8b559ea9b496536e93d014_alertd-og-card.png
layout: provider
modified: '2026-10-29'
name: AlertD
nav: Providers
network: true
overview: 'AlertD is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Security, Cloud, and DevOps.


  AlertD''s developer surface includes CLI, authentication, getting-started guide, documentation, engineering blog, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alertd Authentication
  slug: alertd-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alertd Domain Security
  slug: alertd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alertd
tags:
- AI
- Security
- Cloud
- DevOps
website: https://alertd.ai
---
