---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Git AI providing AI‑powered Git integration tools.
  name: Git AI API
  slug: git-ai-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/git-ai/cli/git-ai-cli.yml
  title: ''
  type: CLI
  url: cli/git-ai-cli.yml
- group: other
  href: https://artifacts.apis.io/git-ai/hosts/git-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/git-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/git-ai/vendors/git-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/git-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usegitai.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usegitai.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://usegitai.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/svarlamov
- group: operate
  title: ''
  type: ChangeLog
  url: https://usegitai.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://usegitai.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://usegitai.com/docs/get-started/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://usegitai.com/docs/team-usage/setup
- group: docs
  title: ''
  type: Documentation
  url: https://dev.usegitai.com/
- group: auth
  href: https://artifacts.apis.io/git-ai/security/git-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/git-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usegitai.com/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but no OpenAPI/AsyncAPI/GraphQL spec could be retrieved.
  evidence:
  - status: 0
    url: https://api.usegitai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Git AI provides AI-powered tools that integrate directly with Git repositories to automate code review, generate documentation, and suggest improvements. By leveraging large language models, Git AI helps developers write higher-quality code faster, offering features such as automated pull‑request comments, commit message generation, and repository insights. The platform is designed for seamless integration into existing CI/CD pipelines and supports multiple Git hosting services, aiming to enhance developer productivity and code quality across teams.
image: https://usegitai.com/opengraph-image-12jlf3?ffdf9fbaf76a0327
layout: provider
modified: '2026-10-29'
name: Git AI
nav: Providers
network: true
overview: 'Git AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Version Control, DevOps, and Code Review.


  Git AI''s developer surface includes CLI, changelog, engineering blog, API reference, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/git-ai/git-ai-2026-11-03T132826.png
security:
- kind: domain-security
  name: Git Ai Domain Security
  slug: git-ai-domain-security
  summary_line: TLSv1.3
slug: git-ai
tags:
- Company
- Artificial Intelligence
- Version Control
- DevOps
- Code Review
- Automation
website: https://usegitai.com/
---
