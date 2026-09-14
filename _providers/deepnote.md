---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Deepnote Agentic Access
  operation_count: 12
  slug: deepnote-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: Publish and embed Deepnote notebooks and data apps in external sites and dashboards via shareable embed/app URLs. This is a publishing/embedding surface rather than a JSON REST API.
  name: Deepnote Embed
  slug: embed-api
- baseURL: https://api.deepnote.com/v2
  baseurl_source: declared
  description: Legacy endpoint to trigger execution of an existing notebook.
  name: Deepnote Execute (v1) API
  slug: deepnote-execute-v1-api
- baseURL: https://api.deepnote.com/v2
  baseurl_source: declared
  description: Information about the calling API key and its workspace.
  name: Deepnote Me API
  slug: deepnote-me-api
- baseURL: https://api.deepnote.com/v2
  baseurl_source: declared
  description: Notebooks, their blocks, runs, and schedules.
  name: Deepnote Notebooks API
  slug: deepnote-notebooks-api
- baseURL: https://api.deepnote.com/v2
  baseurl_source: declared
  description: Projects and their contents.
  name: Deepnote Projects API
  slug: deepnote-projects-api
- baseURL: https://api.deepnote.com/v2
  baseurl_source: declared
  description: Notebook executions.
  name: Deepnote Runs API
  slug: deepnote-runs-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Execute (v1) API
  slug: open-deepnote-execute-v1-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Me API
  slug: open-deepnote-me-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Notebooks API
  slug: open-deepnote-notebooks-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Projects API
  slug: open-deepnote-projects-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Runs API
  slug: open-deepnote-runs-api
- collection_type: open
  name: Deepnote Public API
  slug: open-deepnote
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepnote-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepnote-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepnote-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepnote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepnote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepnote
- group: company
  title: ''
  type: Website
  url: https://deepnote.com
- group: docs
  title: ''
  type: Documentation
  url: https://deepnote.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/deepnote-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepnote-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deepnote-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://deepnote.com/blog
created: '2026-06-20'
description: Deepnote is a collaborative data-science notebook and analytics/app platform. Its Public API v2 (preview) lets you programmatically run notebooks, poll execution runs, and manage projects, notebooks, files, and integrations, with notebooks also embeddable as data apps. Authentication is a workspace API key sent as a Bearer token.
finops:
- name: Deepnote Finops
  service_category: Analytics and Data Science
  slug: deepnote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepnote.png
layout: provider
modified: '2026-06-20'
name: Deepnote
nav: Providers
network: true
overview: 'Deepnote publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Execute (v1) API, Me API, Notebooks API, and 2 more. Tagged areas include Data Science, Notebooks, Analytics, Collaboration, and Data Apps.


  Deepnote''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Deepnote Plans Pricing
  plan_count: 3
  slug: deepnote-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Deepnote Rate Limits
  slug: deepnote-rate-limits
security:
- kind: authentication
  name: Deepnote Authentication
  slug: deepnote-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepnote Domain Security
  slug: deepnote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deepnote Vulnerability Disclosure
  slug: deepnote-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deepnote
tags:
- Data Science
- Notebooks
- Analytics
- Collaboration
- Data Apps
website: https://deepnote.com
---
