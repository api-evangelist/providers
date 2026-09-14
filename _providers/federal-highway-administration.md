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
api_count: 2
apis:
- description: The Federal Highway Administration provides stewardship over the Nation's highways, bridges and tunnels.
  name: Federal Highway Administration
  slug: federal-highway-administration
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Open-source REST API published by the FHWA Saxton Transportation Operations Laboratory (STOL). It sits between mobile applications and a Multi-Access Edge Computing V2X broker, and provides Keycloak-b
  name: FHWA V2X App API
  slug: v2x-app-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-highway-administration-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-highway-administration-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FHWA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-highway-administration
- group: company
  title: ''
  type: Website
  url: https://highways.dot.gov
- group: docs
  title: ''
  type: Documentation
  url: https://usdot-fhwa-stol.github.io/documentation/
- group: operate
  title: ''
  type: Support
  url: https://github.com/usdot-fhwa-stol/v2x-app-api/issues
- group: design
  title: ''
  type: Conventions
  url: conventions/federal-highway-administration-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/federal-highway-administration-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/federal-highway-administration-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federal-highway-administration-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federal-highway-administration-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/federal-highway-administration-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/federal-highway-administration-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-highway-administration-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federal-highway-administration-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/federal-highway-administration-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-highway-administration-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-highway-administration-mcp.yml
created: '2024-12-03'
description: The Federal Highway Administration (FHWA) provides stewardship over the construction, maintenance and preservation of the Nations highways, bridges and tunnels. FHWA also conducts research and provides technical assistance to state and local agencies to improve safety, mobility, and to encourage innovation.
finops:
- name: Federal Highway Administration Finops
  service_category: API
  slug: federal-highway-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-highway-administration.png
layout: provider
modified: '2026-09-09'
name: Federal Highway Administration
nav: Providers
network: true
overview: 'Federal Highway Administration publishes 1 API on the [APIs.io](https://apis.io/) network: FHWA V2X App API. Tagged areas include Federal-Government, Transportation, Highways, Bridges, and Connected-Vehicles.


  Federal Highway Administration''s developer surface includes authentication, documentation, support, changelog, and 16 more developer resources.'
plans:
- name: Federal Highway Administration Plans Pricing
  plan_count: 0
  slug: federal-highway-administration-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Federal Highway Administration Rate Limits
  slug: federal-highway-administration-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/screenshots/federal-highway-administration-2026-06-20T181115.png
security:
- kind: authentication
  name: Federal Highway Administration Authentication
  slug: federal-highway-administration-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Federal Highway Administration Domain Security
  slug: federal-highway-administration-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: federal-highway-administration
tags:
- Federal-Government
- Transportation
- Highways
- Bridges
- Connected-Vehicles
- V2X
- Open-Source
- Open-Data
website: https://highways.dot.gov
---
