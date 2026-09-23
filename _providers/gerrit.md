---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GerritCodeReview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gerrit/refs/heads/main/security/gerrit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gerrit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gerritcodereview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gerrit-documentation.storage.googleapis.com/Documentation/3.14.2/index.html
- group: operate
  title: ''
  type: Roadmap
  url: https://www.gerritcodereview.com/roadmap.html
- group: operate
  title: ''
  type: Support
  url: https://www.gerritcodereview.com/support.html
- group: company
  title: ''
  type: Blog
  url: https://www.gerritcodereview.com/news.html
created: '2026-09-21'
description: Gerrit Code Review is an open‑source, web‑based code review system built for Git repositories. It enables teams to collaborate on patch‑set based reviews with fine‑grained permissions, extensive plugin architecture, and REST API integration. The platform scales to thousands of developers, supports enterprise‑grade security, and offers extensive documentation, roadmaps, and community resources.
layout: provider
modified: '2026-09-21'
name: Gerrit Code Review
nav: Providers
network: true
overview: 'Gerrit Code Review is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Code Review, Open-Source, Git, and Collaboration.


  Gerrit Code Review''s developer surface includes documentation, support, engineering blog, and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.3
    operational_transparency: 10.5
  previous_composite: 9.3
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gerrit Domain Security
  slug: gerrit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: gerrit
tags:
- Company
- Code Review
- Open-Source
- Git
- Collaboration
- CI/CD
website: https://www.gerritcodereview.com/
---
