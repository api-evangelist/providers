---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 9
apis:
- description: GraphQL API for managing Git repositories, branches, commits, tags, artifacts, access control lists, and repository webhooks on SourceHut.
  name: git.sr.ht GraphQL API
  slug: git-sr-ht
- description: GraphQL API for managing Mercurial repositories on SourceHut, including repository operations, webhooks, and access control.
  name: hg.sr.ht GraphQL API
  slug: hg-sr-ht
- description: GraphQL API for submitting and managing continuous integration build jobs across Linux distributions and BSDs on SourceHut.
  name: builds.sr.ht GraphQL API
  slug: builds-sr-ht
- description: GraphQL API for managing bug trackers and ticket systems for software projects on SourceHut.
  name: todo.sr.ht GraphQL API
  slug: todo-sr-ht
- description: GraphQL API for managing mailing lists and email-based code review workflows on SourceHut, powered by git send-email conventions.
  name: lists.sr.ht GraphQL API
  slug: lists-sr-ht
- description: GraphQL API for account management, OAuth 2.0 token and client administration, SSH keys, PGP keys, and user profile operations on SourceHut.
  name: meta.sr.ht GraphQL API
  slug: meta-sr-ht
- description: GraphQL API for creating and managing text pastes on SourceHut.
  name: paste.sr.ht GraphQL API
  slug: paste-sr-ht
- description: GraphQL API for creating and managing wiki and manual pages hosted on SourceHut using git-backed Markdown content.
  name: man.sr.ht GraphQL API
  slug: man-sr-ht
- description: GraphQL API for managing static web hosting on SourceHut, deploying sites to srht.site domains.
  name: pages.sr.ht GraphQL API
  slug: pages-sr-ht
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourcehut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sourcehut.org
- group: docs
  title: ''
  type: Documentation
  url: https://man.sr.ht
- group: company
  title: ''
  type: Blog
  url: https://sourcehut.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sourcehut.org/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sr.ht
- group: build
  title: ''
  type: GitHubOrg
  url: https://git.sr.ht/~sircmpwn
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sourcehut/refs/heads/main/plans/sourcehut-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sourcehut/refs/heads/main/rate-limits/sourcehut-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sourcehut/refs/heads/main/finops/sourcehut-finops.yml
created: '2026-06-13'
description: Privacy-focused software development platform with GraphQL APIs for managing Git and Mercurial repositories, mailing lists, issue trackers, CI build services, wikis, paste, and static web hosting. All services expose OAuth 2.0-authenticated GraphQL endpoints with webhook support.
finops:
- name: Sourcehut Finops
  service_category: ''
  slug: sourcehut-finops
graphqls:
- description: 'Sourcehut (sr.ht) exposes GraphQL APIs for each of its services, including Git repository hosting, Mercurial hosting, continuous integration builds, issue tracking, mailing lists, account management, '
  name: Sourcehut GraphQL API
  slug: sourcehut-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sourcehut.png
layout: provider
modified: '2026-06-13'
name: SourceHut
nav: Providers
network: true
overview: 'SourceHut publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Git, Mercurial, Source Control, Continuous Integration, and Mailing Lists.


  SourceHut''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Sourcehut Plans Pricing
  plan_count: 3
  slug: sourcehut-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Sourcehut Rate Limits
  slug: sourcehut-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -0.8
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 37.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sourcehut/refs/heads/main/screenshots/sourcehut-2026-06-20T194223.png
security:
- kind: domain-security
  name: Sourcehut Domain Security
  slug: sourcehut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sourcehut
tags:
- Git
- Mercurial
- Source Control
- Continuous Integration
- Mailing Lists
- Issue Tracking
- Developer Tools
- Open Source
- Privacy
- GraphQL
website: https://sourcehut.org
---
