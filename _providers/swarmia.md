---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Swarmia Agentic Access
  operation_count: 12
  slug: swarmia-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Ingestion of usage data from external AI assistant tools.
  name: Swarmia Additional AI integrations API
  slug: swarmia-additional-ai-integrations-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Machine-readable versions of major reports found in the Swarmia app.
  name: Swarmia Built-in reports API
  slug: swarmia-built-in-reports-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Saved custom reports created in the Swarmia explore view.
  name: Swarmia Custom reports API
  slug: swarmia-custom-reports-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Deployment and fix-deployment event ingestion for delivery and DORA metrics.
  name: Swarmia Deployments API
  slug: swarmia-deployments-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Programmatic management of teams and memberships.
  name: Swarmia Team management API
  slug: swarmia-team-management-api
- baseURL: https://app.swarmia.com/api/v1
  baseurl_source: declared
  description: Create, read, update, and delete employee time-off periods.
  name: Swarmia Time off API
  slug: swarmia-time-off-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swarmia Additional AI integrations API
  slug: open-swarmia-additional-ai-integrations-api
- collection_type: open
  name: Swarmia Additional AI integrations Built-in reports API
  slug: open-swarmia-built-in-reports-api
- collection_type: open
  name: Swarmia Additional AI integrations Custom reports API
  slug: open-swarmia-custom-reports-api
- collection_type: open
  name: Swarmia Additional AI integrations Deployments API
  slug: open-swarmia-deployments-api
- collection_type: open
  name: Swarmia Additional AI integrations Team management API
  slug: open-swarmia-team-management-api
- collection_type: open
  name: Swarmia Additional AI integrations Time off API
  slug: open-swarmia-time-off-api
- collection_type: open
  name: Swarmia API
  slug: open-swarmia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swarmia-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swarmia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swarmia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swarmia-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swarmia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swarmia
- group: company
  title: ''
  type: Website
  url: https://www.swarmia.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.swarmia.com
- group: commercial
  title: ''
  type: Plans
  url: plans/swarmia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swarmia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swarmia-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.swarmia.com/rss.xml
created: '2026-06-21'
description: Swarmia is an engineering-effectiveness analytics platform that combines software delivery metrics (DORA), developer experience, investment balance, and AI adoption insights. Its REST API lets teams export built-in and custom reports, ingest deployment and events data, manage teams and memberships, and record time off, authenticated with Bearer API tokens.
finops:
- name: Swarmia Finops
  service_category: Developer Tools
  slug: swarmia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swarmia.png
layout: provider
modified: '2026-06-21'
name: Swarmia
nav: Providers
network: true
overview: 'Swarmia publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Additional AI integrations API, Built-in reports API, Custom reports API, and 3 more. Tagged areas include Engineering Effectiveness, Developer Productivity, DORA, Software Delivery, and Analytics.


  Swarmia''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Swarmia Plans Pricing
  plan_count: 4
  slug: swarmia-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Swarmia Rate Limits
  slug: swarmia-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/swarmia/refs/heads/main/screenshots/swarmia-2026-09-02T161344.png
security:
- kind: authentication
  name: Swarmia Authentication
  slug: swarmia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Swarmia Domain Security
  slug: swarmia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Swarmia Vulnerability Disclosure
  slug: swarmia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swarmia
tags:
- Engineering Effectiveness
- Developer Productivity
- DORA
- Software Delivery
- Analytics
website: https://www.swarmia.com
---
