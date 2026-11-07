---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Backend API for the Tolmo cloud security platform, consumed through the Tolmo CLI (SQL/Cypher queries over the infrastructure graph, security findings management, and a secure server-side proxy for co
  name: Tolmo Platform API
  slug: tolmo-platform-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tolmo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tolmo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tolmo.com/installation
- group: auth
  href: https://artifacts.apis.io/tolmo/authentication/tolmo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tolmo-authentication.yml
- group: build
  href: https://artifacts.apis.io/tolmo/cli/tolmo-cli.yml
  title: ''
  type: CLI
  url: cli/tolmo-cli.yml
- group: build
  href: https://artifacts.apis.io/tolmo/packages/tolmo-packages.yml
  title: ''
  type: Packages
  url: packages/tolmo-packages.yml
- group: design
  href: https://artifacts.apis.io/tolmo/conventions/tolmo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tolmo-conventions.yml
- group: design
  href: https://artifacts.apis.io/tolmo/lifecycle/tolmo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tolmo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tolmo.com
- group: operate
  href: https://artifacts.apis.io/tolmo/changelog/tolmo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tolmo-changelog.yml
- group: agent
  href: https://artifacts.apis.io/tolmo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/tolmo/llms/tolmo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tolmo-llms.txt
- group: agent
  href: https://artifacts.apis.io/tolmo/well-known/tolmo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tolmo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tolmo/well-known/tolmo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tolmo-security.txt
- group: auth
  title: ''
  type: Security
  url: https://tolmo.com/security
- group: auth
  href: https://artifacts.apis.io/tolmo/security/tolmo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tolmo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tolmo/security/tolmo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tolmo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tolmo/security/tolmo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tolmo-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tolmohq
- group: company
  title: ''
  type: Blog
  url: https://tolmo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://tolmo.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.tolmo.com/
- group: company
  title: ''
  type: Website
  url: https://tolmo.com/
created: '2026-07-17'
description: 'Tolmo builds AI-native cybersecurity for engineering teams. Its platform pairs automated cloud and SaaS discovery (AWS, GitHub, Datadog, Linear, Cloudflare, and more) with event-driven agents that run continuous pentesting, threat modeling, finding generation, and verified remediation against the customer''s real infrastructure graph. The primary developer surface is the Tolmo CLI: SQL and Cypher queries over the infrastructure graph, full-lifecycle security findings management, and a secure server-side proxy for GitHub/AWS/Linear/ Sentry/Datadog requests, plus a first-party agent skill for Claude Code and other AI agents. Backed by Accel and Y Combinator.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tolmo.png
layout: provider
modified: '2026-07-21'
name: Tolmo
nav: Providers
network: true
overview: 'Tolmo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Cloud Security, and Vulnerability Management.


  Tolmo''s developer surface includes documentation, getting-started guide, authentication, CLI, changelog, engineering blog, support, and 16 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 26.6
  provenance:
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tolmo/tolmo-2026-09-02T163853.png
security:
- kind: authentication
  name: Tolmo Authentication
  slug: tolmo-authentication
  summary_line: oauth2/http-bearer · 2 schemes
- kind: domain-security
  name: Tolmo Domain Security
  slug: tolmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tolmo Vulnerability Disclosure
  slug: tolmo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tolmo Trust Center
  slug: tolmo-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: Proxy requests to connected services
  slug: tolmo-proxy-connected-services
- name: Query the infrastructure graph and database
  slug: tolmo-query-infrastructure
- name: Triage and manage security findings
  slug: tolmo-triage-findings
slug: tolmo
tags:
- Company
- Security
- Cybersecurity
- Cloud Security
- Vulnerability Management
- CLI
- DevSecOps
- AI Agents
- Infrastructure Graph
website: https://tolmo.com/
---
