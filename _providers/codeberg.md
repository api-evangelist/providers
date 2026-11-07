---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Codeberg Agentic Access
  operation_count: 44
  slug: codeberg-agentic-access
  summary_line: 44 operations · 18 acting
api_count: 1
apis:
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Server metadata.
  name: Codeberg Miscellaneous API
  slug: codeberg-miscellaneous-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The activitypub API from Codeberg — 11 operation(s) for activitypub.
  name: Codeberg Activitypub API
  slug: codeberg-activitypub-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The admin API from Codeberg — 34 operation(s) for admin.
  name: Codeberg Admin API
  slug: codeberg-admin-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The issue API from Codeberg — 33 operation(s) for issue.
  name: Codeberg Issue API
  slug: codeberg-issue-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The notification API from Codeberg — 4 operation(s) for notification.
  name: Codeberg Notification API
  slug: codeberg-notification-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The organization API from Codeberg — 42 operation(s) for organization.
  name: Codeberg Organization API
  slug: codeberg-organization-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The package API from Codeberg — 5 operation(s) for package.
  name: Codeberg Package API
  slug: codeberg-package-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The repository API from Codeberg — 126 operation(s) for repository.
  name: Codeberg Repository API
  slug: codeberg-repository-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The settings API from Codeberg — 4 operation(s) for settings.
  name: Codeberg Settings API
  slug: codeberg-settings-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: The user API from Codeberg — 54 operation(s) for user.
  name: Codeberg User API
  slug: codeberg-user-api
artifact_total: 26
collections:
- collection_type: open
  name: Codeberg API (Forgejo) Git Content API
  slug: open-codeberg-git-content-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Issues API
  slug: open-codeberg-issues-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Miscellaneous API
  slug: open-codeberg-miscellaneous-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Organizations API
  slug: open-codeberg-organizations-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Pull Requests API
  slug: open-codeberg-pull-requests-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Releases API
  slug: open-codeberg-releases-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Repositories API
  slug: open-codeberg-repositories-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Users API
  slug: open-codeberg-users-api
- collection_type: open
  name: Codeberg API (Forgejo)
  slug: open-codeberg
common:
- group: other
  href: https://artifacts.apis.io/codeberg/capabilities/codeberg-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/codeberg-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/codeberg/agentic-access/codeberg-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/codeberg-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/codeberg/security/codeberg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codeberg-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/codeberg/authentication/codeberg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/codeberg-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgejo/forgejo
- group: other
  title: ''
  type: Fediverse
  url: https://social.anoxinon.de/@codeberg
- group: company
  title: ''
  type: Website
  url: https://codeberg.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codeberg.org
- group: commercial
  href: https://artifacts.apis.io/codeberg/plans/codeberg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codeberg-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/codeberg/rate-limits/codeberg-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/codeberg-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/codeberg/finops/codeberg-finops.yml
  title: ''
  type: FinOps
  url: finops/codeberg-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.codeberg.org/
created: '2026-07-12'
description: Codeberg is a community-run, non-profit platform for hosting Git repositories and collaborating on free and open source software, operated by the Codeberg e.V. association in Germany. It runs on Forgejo (a community fork of Gitea) and exposes the Forgejo/Gitea-compatible REST API at https://codeberg.org/api/v1 for repositories, issues, pull requests, releases, Git content, users, and organizations. Access is free and donation-funded; requests authenticate with a personal access token or OAuth2.
finops:
- has_sources: true
  method: generated
  name: Codeberg Finops
  primary_unit: ''
  service_category: Developer Tools and Code Hosting
  slug: codeberg-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeberg.png
layout: provider
modified: '2026-07-12'
name: Codeberg
nav: Providers
network: true
overview: 'Codeberg publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Miscellaneous API, Activitypub API, Admin API, and 7 more. Tagged areas include Code Hosting, Version Control, Git Hosting, Repositories, and Pull Requests.


  The Codeberg catalog on APIs.io includes 1 Spectral governance ruleset.


  Codeberg''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Codeberg Plans Pricing
  plan_count: 2
  slug: codeberg-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Codeberg Rate Limits
  slug: codeberg-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Codeberg API Rules
  rule_count: 58
  severity_counts:
    error: 39
    hint: 0
    info: 4
    warn: 15
  slug: codeberg-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 44.7
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 47.4
      derived: 0
      marker_coverage: 52.6
      total: 19
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/codeberg/codeberg-2026-07-25T205910.png
security:
- kind: authentication
  name: Codeberg Authentication
  slug: codeberg-authentication
  summary_line: apiKey/basic/oauth2 · 3 schemes
- kind: domain-security
  name: Codeberg Domain Security
  slug: codeberg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: codeberg
tags:
- Code Hosting
- Version Control
- Git Hosting
- Repositories
- Pull Requests
- Issue Tracking
- Open Source
- Forgejo
- Non-Profit
website: https://codeberg.org
---
