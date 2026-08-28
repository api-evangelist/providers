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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Decap CMS communicates with Git hosting providers (GitHub, GitLab, Bitbucket, Azure, Gitea) through their REST and GraphQL APIs to read, create, update, and delete content entries, manage media file u
  name: Decap CMS Git Backend API
  slug: decap-cms-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decapcms.org/
- group: docs
  title: ''
  type: Documentation
  url: https://decapcms.org/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/decaporg
- group: company
  title: ''
  type: Blog
  url: https://decapcms.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://decapcms.org/turbo/
- group: other
  title: ''
  type: X
  url: https://x.com/Decap_CMS
- group: commercial
  title: ''
  type: Plans
  url: plans/decap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/decap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/decap-finops.yml
created: '2026-06-13'
description: Decap CMS (formerly Netlify CMS) is an open-source, Git-based headless content management system for static site generators and modern frontend frameworks. It provides a web-based editorial UI for managing content stored directly in Git repositories, supporting collections of entries and media files, rich-text editing, editorial workflows (draft/review/publish), and i18n. Content operations are proxied to Git hosting backends (GitHub, GitLab, Bitbucket, Azure, Gitea) via their respective REST and GraphQL APIs. Decap Turbo adds a managed cloud layer with a database proxy, centralized authentication, user roles, real-time collaboration presence, and priority support.
finops:
- name: Decap Finops
  service_category: ''
  slug: decap-finops
graphqls:
- description: Decap CMS (formerly Netlify CMS) is a Git-based headless CMS that does not expose a native GraphQL API of its own. All content operations are performed by the client-side JavaScript library communicat
  name: Decap CMS GraphQL API
  slug: decap-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decap.png
layout: provider
modified: '2026-06-13'
name: Decap CMS
nav: Providers
network: true
overview: 'Decap CMS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Headless CMS, Git-based CMS, Content Management, and Static Site Generator.


  Decap CMS''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Decap Plans Pricing
  plan_count: 4
  slug: decap-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Decap Rate Limits
  slug: decap-rate-limits
score:
  band: thin
  composite: 33.7
  delta: 4.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decap/refs/heads/main/screenshots/decap-2026-06-20T175749.png
security:
- kind: domain-security
  name: Decap Domain Security
  slug: decap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: decap
tags:
- CMS
- Headless CMS
- Git-based CMS
- Content Management
- Static Site Generator
- JAMstack
- Open-Source
- Editorial Workflow
website: https://decapcms.org/
---
