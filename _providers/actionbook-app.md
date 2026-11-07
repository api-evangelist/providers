---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
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
  score: 11.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Actionbook provides AI‑powered coworker features accessible via its web dashboard and integrations.
  name: Actionbook API
  slug: actionbook-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/actionbook-app/plans/actionbook-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actionbook-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/actionbook-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/actionbook-app/cli/actionbook-app-cli.yml
  title: ''
  type: CLI
  url: cli/actionbook-app-cli.yml
- group: auth
  href: https://artifacts.apis.io/actionbook-app/authentication/actionbook-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/actionbook-app-authentication.yml
- group: agent
  href: https://artifacts.apis.io/actionbook-app/llms/actionbook-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actionbook-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/actionbook-app/well-known/actionbook-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actionbook-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/actionbook-app/hosts/actionbook-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actionbook-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/actionbook-app/vendors/actionbook-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actionbook-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/actionbook-app/security/actionbook-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actionbook-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actionbook.app/
- group: docs
  title: ''
  type: Documentation
  url: https://actionbook.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://actionbook.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://actionbook.app/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://actionbook.app/discord
- group: company
  title: ''
  type: Blog
  url: https://actionbook.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actionbook
- group: commercial
  title: ''
  type: Pricing
  url: https://actionbook.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actionbook.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actionbook.app/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://actionbook.app/sign-up
coverage:
  checked: '2026-10-31'
  detail: The OpenAPI file found in the GitHub repo is a sample Plant Store spec, not related to Actionbook, so no valid contract belongs to this provider.
  evidence:
  - status: 200
    url: https://raw.githubusercontent.com/actionbook/docs/main/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Actionbook provides an AI‑powered coworker that runs in your browser, aggregating data from web sources and connected apps into a unified dashboard. It offers automation tools, quick‑start guides, and integrations to help teams streamline research, prospecting, and social auditing, delivering actionable insights without manual browsing.
image: https://actionbook.app/opengraph-image.jpg
layout: provider
modified: '2026-10-31'
name: Actionbook
nav: Providers
network: true
overview: 'Actionbook is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Productivity, Browser, and Dashboards.


  Actionbook''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 13 more developer resources.'
plans:
- name: Actionbook App Plans Pricing
  plan_count: 3
  slug: actionbook-app-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.3
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 34.4
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Actionbook App Authentication
  slug: actionbook-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Actionbook App Domain Security
  slug: actionbook-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: actionbook-app
tags:
- Artificial Intelligence
- Automation
- Productivity
- Browser
- Dashboards
website: https://actionbook.app/
---
