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
  name: National Science Foundation Agentic Access
  operation_count: 3
  slug: national-science-foundation-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.nsf.gov/services/v1/
  baseurl_source: declared
  description: The Awards API from National Science Foundation — 2 operation(s) for awards.
  name: National Science Foundation Awards API
  slug: national-science-foundation-awards-api
- baseURL: https://api.nsf.gov/services/v1/
  baseurl_source: declared
  description: The Awards.{format} API from National Science Foundation — 1 operation(s) for awards.{format}.
  name: National Science Foundation Awards.{format} API
  slug: national-science-foundation-awards-format-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: National Science Foundation Awards API
  slug: open-national-science-foundation-awards-api
- collection_type: open
  name: National Science Foundation Awards Awards.{format} API
  slug: open-national-science-foundation-awards-format-api
- collection_type: open
  name: National Science Foundation Awards API
  slug: open-national-science-foundation
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/national-science-foundation-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-science-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-science-foundation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nsf-open
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-science-foundation
- group: company
  title: ''
  type: Website
  url: https://www.nsf.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.nsf.gov/developer
- group: company
  title: ''
  type: Blog
  url: https://www.nsf.gov/rss/rss_www_news.xml
created: '2024-12-03'
description: The National Science Foundation (NSF) is an independent federal agency that supports fundamental research and education in all the non-medical fields of science and engineering. NSF provides grants and funding to researchers and institutions to drive innovation, discovery, and progress.
finops:
- name: National Science Foundation Finops
  service_category: API
  slug: national-science-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-science-foundation.png
layout: provider
modified: '2026-05-19'
name: National Science Foundation
nav: Providers
network: true
overview: 'National Science Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network: Awards API and Awards.{format} API. Tagged areas include Federal-Government, Research, and Science.


  National Science Foundation''s developer surface includes developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: National Science Foundation Plans Pricing
  plan_count: 3
  slug: national-science-foundation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: National Science Foundation Rate Limits
  slug: national-science-foundation-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/national-science-foundation/refs/heads/main/screenshots/national-science-foundation-2026-06-20T190040.png
security:
- kind: domain-security
  name: National Science Foundation Domain Security
  slug: national-science-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-science-foundation
tags:
- Federal-Government
- Research
- Science
website: https://www.nsf.gov/
---
