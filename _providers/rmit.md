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
  trial: false
  try_now: true
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Rmit Agentic Access
  operation_count: 157
  slug: rmit-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The RMIT Research Repository is RMIT University's open access research portal, powered by Clarivate's Esploro research information management platform. It provides public web-based discovery of RMIT p
  name: RMIT Research Repository (Esploro)
  slug: research-repository
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-rmit-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-rmit-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-rmit-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-rmit-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-rmit-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-rmit-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-rmit-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-rmit-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-rmit-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-rmit-symplectic-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rmit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rmit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rmit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rmit.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RMIT-University
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/rmit-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RMIT
- group: commercial
  title: ''
  type: Plans
  url: plans/rmit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rmit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rmit-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rmit.edu.au/news/all-news
coverage:
  detail: 1 institution-operated surface(s) remain, none of which publishes a machine-readable contract.
  reason: no_published_contract
  state: none
created: '2026-06-03'
description: 'RMIT University is a public research university in Melbourne, Australia, specializing in technology, design and enterprise, and ranked #123 in the QS World University Rankings 2025. RMIT does not operate a centralized, publicly documented developer portal. Its most accessible programmatic surface is its research output: the RMIT Research Repository runs on Clarivate''s Esploro platform, and RMIT''s research data is published via a Figshare-hosted repository whose records are exposed through the public Figshare REST API (api.figshare.com) and syndicated to Research Data Australia. Student-facing systems such as timetables, the curriculum catalogue, and identity/SSO sit behind authentication and are not offered as public APIs.'
finops:
- name: Rmit Finops
  service_category: Education
  slug: rmit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rmit.png
layout: provider
modified: '2026-06-03'
name: RMIT University
nav: Providers
network: true
overview: 'RMIT University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  RMIT University''s developer surface includes GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Rmit Plans Pricing
  plan_count: 2
  slug: rmit-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Rmit Rate Limits
  slug: rmit-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/rmit/refs/heads/main/screenshots/rmit-2026-06-20T193137.png
security:
- kind: domain-security
  name: Rmit Domain Security
  slug: rmit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rmit Vulnerability Disclosure
  slug: rmit-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: rmit
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Australia
website: https://www.rmit.edu.au/
---
