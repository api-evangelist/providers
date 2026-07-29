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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Every.org API is a powerful tool that allows developers to access and interact with a wide range of charitable giving data. By integrating the API into their applications, developers can retrieve '
  name: Every.org API
  slug: every-org
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/every-org-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everydotorg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everydotorg
- group: operate
  title: ''
  type: Support
  url: https://support.every.org/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.every.org/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.every.org/press
- group: operate
  title: ''
  type: Support
  url: https://support.every.org/hc/en-us
created: '2025-03-01'
description: Every.org is a platform that empowers individuals to give back and support causes they care about. Users can create fundraising campaigns, donate to verified nonprofits, and track their impact through personalized giving dashboards. Every.org also partners with companies to facilitate workplace giving programs and corporate social responsibility initiatives.
finops:
- name: Every Org Finops
  service_category: API
  slug: every-org-finops
graphqls:
- description: Every.org is a nonprofit giving platform that enables individuals, companies, and developers to discover verified nonprofits, create fundraising campaigns, and process donations. The platform serves d
  name: Every.org GraphQL API
  slug: every-org-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/every-org.png
layout: provider
modified: '2026-03-16'
name: Every.org
nav: Providers
network: true
overview: 'Every.org publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Charities, Donations, and Fundraising.


  Every.org''s developer surface includes support, engineering blog, and 5 more developer resources.'
plans:
- name: Every Org Plans Pricing
  plan_count: 3
  slug: every-org-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Every Org Rate Limits
  slug: every-org-rate-limits
score:
  band: thin
  composite: 31.9
  delta: 9.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.1
    developer_ergonomics: 6.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/every-org/refs/heads/main/screenshots/every-org-2026-06-20T180910.png
security:
- kind: domain-security
  name: Every Org Domain Security
  slug: every-org-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: every-org
tags:
- Charities
- Donations
- Fundraising
---
