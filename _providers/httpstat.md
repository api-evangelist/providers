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
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Httpstat Agentic Access
  operation_count: 2
  slug: httpstat-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://httpstat.us
  baseurl_source: declared
  description: The Httpstat API from Httpstat.us — 1 operation(s) for httpstat.
  name: Httpstat.us Httpstat API
  slug: httpstat-httpstat-api
- baseURL: https://httpstat.us
  baseurl_source: declared
  description: The Random API from Httpstat.us — 1 operation(s) for random.
  name: Httpstat.us Random API
  slug: httpstat-random-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Httpstat API
  slug: open-httpstat-httpstat-api
- collection_type: open
  name: Httpstat Random API
  slug: open-httpstat-random-api
- collection_type: open
  name: httpstat
  slug: open-httpstat
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Readify/httpstatus/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Readify/httpstatus/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/httpstat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/httpstat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://httpstat.us/
- group: other
  title: ''
  type: Repository
  url: https://github.com/Readify/httpstatus
created: '2024-11-15'
description: httpstat.us is a super simple service for generating different HTTP status codes. It is useful for testing how your own scripts and applications deal with varying HTTP responses, allowing developers to simulate different server response scenarios.
finops:
- name: Httpstat Finops
  service_category: API
  slug: httpstat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/httpstat.png
layout: provider
modified: '2026-05-19'
name: Httpstat.us
nav: Providers
network: true
overview: 'Httpstat.us publishes 2 APIs on the [APIs.io](https://apis.io/) network: Httpstat API and Random API. Tagged areas include HTTP, Status-Codes, Testing, and Utilities.


  The Httpstat.us catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Httpstat Plans Pricing
  plan_count: 3
  slug: httpstat-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Httpstat Rate Limits
  slug: httpstat-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Httpstat.us API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: httpstat-rules
security:
- kind: domain-security
  name: Httpstat Domain Security
  slug: httpstat-domain-security
  summary_line: TLSv1.2
slug: httpstat
tags:
- HTTP
- Status-Codes
- Testing
- Utilities
website: https://httpstat.us/
---
