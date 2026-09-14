---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
api_count: 2
apis:
- baseURL: https://calendar-api.ma
  baseurl_source: declared
  description: National Open business days
  name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python Business Days API
  slug: calendar-api-ma-business-days-api
- baseURL: https://calendar-api.ma
  baseurl_source: declared
  description: National holidays of any year and Religious holidays of past years
  name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python Holidays API
  slug: calendar-api-ma-holidays-api
- baseURL: https://calendar-api.ma
  baseurl_source: declared
  description: Misc endpoints
  name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python Misc API
  slug: calendar-api-ma-misc-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.calendar-api.ma/
- group: other
  title: ''
  type: Overlay
  url: overlays/calendar-api-ma-calendar-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://calendar-api.ma
- group: docs
  title: ''
  type: Documentation
  url: https://docs.calendar-api.ma
- group: docs
  title: ''
  type: APIReference
  url: https://calendar-api.ma/api/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://calendar-api.ma/holidays-api.html
- group: operate
  title: ''
  type: Support
  url: https://calendar-api.ma/contacts.html
- group: start
  title: ''
  type: SignUp
  url: https://calendar-api.ma/console/register
- group: start
  title: ''
  type: Login
  url: https://calendar-api.ma/console/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calendar-api.ma/privacy.html
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/ud-labs/py-calendar-api
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/9897118/2sBYArSrTN
- group: build
  title: ''
  type: Packages
  url: packages/calendar-api-ma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/calendar-api-ma-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/pycalendar-api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/calendar-api-ma-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/calendar-api-ma-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/calendar-api-ma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/calendar-api-ma-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/calendar-api-ma-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/calendar-api-ma-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/calendar-api-ma-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/calendar-api-ma-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/calendar-api-ma-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/calendar-api-ma-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calendar-api-ma-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calendar-api-ma-domain-security.yml
created: '2026-08-18'
description: 'Calendar API is a REST service from Unravel Designs (Casablanca, Morocco) that turns the Moroccan economic calendar into a callable contract. It returns national, religious and exceptional public holidays with an explicit Estimated/Official status — religious feasts are dated astronomically and only become Official after moon sighting — and it calculates open business days: next and previous working day, counts and listings between two dates, and CalSpan, a chainable business-day [start_date, end_date] interval for a month, quarter, semester or year that drops straight into a SQL BETWEEN. Fourteen read-only GET operations are described by a published OpenAPI 3.1 document, authenticated with an X-API-KEY header, and wrapped by a typed first-party Python SDK (pycalendar-api). It is aimed at data engineers wiring Moroccan holiday logic into ETL pipelines and orchestrators such as Airflow and Dagster, and at regulated-market reporting where a hardcoded holiday table quietly goes
  stale every year.'
image: https://calendar-api.ma/assets/img/logos/cal-api-logo%20small.webp
layout: provider
modified: '2026-08-18'
name: API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python
nav: Providers
network: true
overview: 'API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python publishes 3 APIs on the [APIs.io](https://apis.io/) network: Business Days API, Holidays API, and Misc API. Tagged areas include Holidays, Morocco, Calendar, Business Days, and date-utilities.


  API Calendrier Marocain | Jours Fériés & Ouvrables REST + SDK Python''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, changelog, and 21 more developer resources.'
plans:
- name: Calendar Api Ma Plans Pricing
  plan_count: 1
  slug: calendar-api-ma-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Calendar Api Ma Rate Limits
  slug: calendar-api-ma-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/calendar-api-ma/refs/heads/main/screenshots/calendar-api-ma-2026-09-02T145004.png
security:
- kind: authentication
  name: Calendar Api Ma Authentication
  slug: calendar-api-ma-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Calendar Api Ma Domain Security
  slug: calendar-api-ma-domain-security
  summary_line: TLSv1.3
slug: calendar-api-ma
tags:
- Holidays
- Morocco
- Calendar
- Business Days
- date-utilities
- Data Engineering
- ETL
- Python SDK
- Localization
- Reference Data
- Public Holidays
- Scheduling
website: https://www.calendar-api.ma/
---
