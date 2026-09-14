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
api_count: 1
apis:
- description: The Degreed REST API provides HTTP-based access to manage learning data within the Degreed platform. It covers user management, learning content (articles, books, courses, videos, podcasts, events), p
  name: Degreed API
  slug: degreed-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/degreed-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/degreed-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/plans/degreed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/rate-limits/degreed-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/finops/degreed-finops.yml
created: 2026-06-13
description: Degreed is a learning experience platform with a REST API for managing learning pathways, tracking skill development, accessing content integrations, and reporting workforce upskilling data. The API enables organizations to manage users, content, completions, skills, pathways, accomplishments, and social learning features using OAuth 2.0 authentication. Multi-region deployments are supported across US, EU, and Canada data centers.
finops:
- name: Degreed Finops
  service_category: ''
  slug: degreed-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/degreed.png
jsonld:
- class_count: 0
  name: Degreed Context
  property_count: 8
  slug: degreed-context
layout: provider
modified: 2026-06-13
name: Degreed
nav: Providers
network: true
overview: 'Degreed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Learning Experience Platform, Skill Development, Learning Pathways, Workforce Upskilling, and E-Learning.


  The Degreed catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Degreed Plans Pricing
  plan_count: 3
  slug: degreed-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Degreed Rate Limits
  slug: degreed-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/degreed/refs/heads/main/screenshots/degreed-2026-06-20T175855.png
security:
- kind: domain-security
  name: Degreed Domain Security
  slug: degreed-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Degreed Trust Center
  slug: degreed-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: degreed
tags:
- Learning Experience Platform
- Skill Development
- Learning Pathways
- Workforce Upskilling
- E-Learning
- HR Technology
---
