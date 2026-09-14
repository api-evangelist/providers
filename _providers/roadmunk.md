---
access_model:
  confidence: medium
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - '{''url'': ''https://roadmunk.com'', ''status'': 308, ''note'': ''declared website redirects to https://www.tempo.io/products/roadmaps — a different registrable domain (roadmunk.com -> tempo.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: true
  try_now: true
api_count: 1
apis:
- description: The Roadmunk (Strategic Roadmaps) GraphQL API provides programmatic access to roadmaps, items, milestones, key dates, portfolios, feedback, ideas, customers, contacts, accounts, and user management. T
  name: Roadmunk GraphQL API
  slug: roadmunk-graphql-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/roadmunk-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roadmunk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roadmunk.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.tempo.io/roadmaps/latest/getting-started-with-the-strategic-roadmaps-graphq
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/roadmunk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roadmunk
- group: company
  title: ''
  type: Blog
  url: https://www.tempo.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.capterra.com/p/145895/Roadmunk/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.roadmunk.com/
- group: other
  title: ''
  type: X
  url: https://x.com/roadmunkapp
- group: commercial
  title: ''
  type: Plans
  url: plans/roadmunk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roadmunk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/roadmunk-finops.yml
created: 2026-06-13
description: Roadmunk (now Strategic Roadmaps by Tempo) is a product roadmapping tool with a GraphQL API for managing roadmaps, items, milestones, swimlanes, feedback, and ideas. The API enables programmatic access to nearly all platform functions across regional gateways covering North America, Europe, and Asia-Pacific, using Bearer token authentication.
finops:
- name: Roadmunk Finops
  service_category: Product Roadmapping / SaaS
  slug: roadmunk-finops
graphqls:
- description: Roadmunk (now Strategic Roadmaps by Tempo) provides a GraphQL API for programmatic access to roadmaps, items, milestones, key dates, fields, notifications, users, and account management. The API suppo
  name: Roadmunk GraphQL API
  slug: roadmunk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roadmunk.png
jsonld:
- class_count: 11
  name: Roadmunk Context
  property_count: 14
  slug: roadmunk-context
layout: provider
modified: 2026-06-13
name: Roadmunk
nav: Providers
network: true
overview: 'Roadmunk publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Product Roadmapping, GraphQL, Roadmaps, Project Management, and Product Management.


  The Roadmunk catalog on APIs.io includes 1 JSON-LD context.


  Roadmunk''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Roadmunk Plans Pricing
  plan_count: 4
  slug: roadmunk-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Roadmunk Rate Limits
  slug: roadmunk-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/roadmunk/refs/heads/main/screenshots/roadmunk-2026-06-20T193137.png
security:
- kind: domain-security
  name: Roadmunk Domain Security
  slug: roadmunk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Roadmunk Trust Center
  slug: roadmunk-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: roadmunk
tags:
- Product Roadmapping
- GraphQL
- Roadmaps
- Project Management
- Product Management
- Feedback
- Ideas
- Milestones
- Swimlanes
- Timelines
website: https://roadmunk.com
---
