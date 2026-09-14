---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Smarthr Agentic Access
  operation_count: 27
  slug: smarthr-agentic-access
  summary_line: 27 operations · 16 acting
api_count: 1
apis:
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Business establishments (jigyosho) registered for the tenant.
  name: SmartHR Business Establishments API
  slug: smarthr-business-establishments-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Employee ("crew") records - the core personnel objects in SmartHR.
  name: SmartHR Crews API
  slug: smarthr-crews-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Templates defining custom fields attached to crew records.
  name: SmartHR Custom Field Templates API
  slug: smarthr-custom-field-templates-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Organizational departments that crews belong to.
  name: SmartHR Departments API
  slug: smarthr-departments-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Employment type master data (full-time, part-time, contract, etc.).
  name: SmartHR Employment Types API
  slug: smarthr-employment-types-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Webhook subscriptions that notify external systems of changes.
  name: SmartHR Webhooks API
  slug: smarthr-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SmartHR Business Establishments API
  slug: open-smarthr-business-establishments-api
- collection_type: open
  name: SmartHR Business Establishments Crews API
  slug: open-smarthr-crews-api
- collection_type: open
  name: SmartHR Business Establishments Custom Field Templates API
  slug: open-smarthr-custom-field-templates-api
- collection_type: open
  name: SmartHR Business Establishments Departments API
  slug: open-smarthr-departments-api
- collection_type: open
  name: SmartHR Business Establishments Employment Types API
  slug: open-smarthr-employment-types-api
- collection_type: open
  name: SmartHR Business Establishments Webhooks API
  slug: open-smarthr-webhooks-api
- collection_type: open
  name: SmartHR API
  slug: open-smarthr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smarthr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smarthr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smarthr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kufu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smarthr
- group: company
  title: ''
  type: Website
  url: https://smarthr.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.smarthr.jp/
- group: commercial
  title: ''
  type: Plans
  url: plans/smarthr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smarthr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smarthr-finops.yml
created: '2026-07-12'
description: SmartHR is a leading Japanese cloud HR, labor, and personnel management SaaS (smarthr.jp). Its per-tenant REST API exposes an organization's employee ("crew") records and the master data around them - departments, employment types, business establishments, and custom field templates - plus webhook subscriptions for change notifications. The API is served from each customer's own tenant subdomain (https://{tenant}.smarthr.jp/api) under a /v1 path, and is authenticated with a per-tenant access token passed as a Bearer token.
finops:
- name: Smarthr Finops
  service_category: Human Resources and Personnel Management
  slug: smarthr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smarthr.png
layout: provider
modified: '2026-07-12'
name: SmartHR
nav: Providers
network: true
overview: 'SmartHR publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Business Establishments API, Crews API, Custom Field Templates API, and 3 more. Tagged areas include HR, Human Resources, HRIS, Labor Management, and Payroll.


  SmartHR''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Smarthr Plans Pricing
  plan_count: 4
  slug: smarthr-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Smarthr Rate Limits
  slug: smarthr-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/smarthr/refs/heads/main/screenshots/smarthr-2026-09-02T155924.png
security:
- kind: authentication
  name: Smarthr Authentication
  slug: smarthr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smarthr Domain Security
  slug: smarthr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smarthr
tags:
- HR
- Human Resources
- HRIS
- Labor Management
- Payroll
- Japan
- Employees
- Personnel
- Onboarding
- Software-as-a-Service
website: https://smarthr.jp/
---
