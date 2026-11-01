---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/strandsagents/changelog/strandsagents-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/strandsagents-changelog.yml
- group: auth
  href: https://artifacts.apis.io/strandsagents/authentication/strandsagents-authentication.yml
  title: ''
  type: Authentication
  url: authentication/strandsagents-authentication.yml
- group: agent
  href: https://artifacts.apis.io/strandsagents/llms/strandsagents-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strandsagents-llms.txt
- group: auth
  href: https://artifacts.apis.io/strandsagents/well-known/strandsagents-openrouter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/strandsagents-openrouter-security.txt
- group: agent
  href: https://artifacts.apis.io/strandsagents/well-known/strandsagents-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/strandsagents-well-known.yml
- group: other
  href: https://artifacts.apis.io/strandsagents/hosts/strandsagents-hosts.yml
  title: ''
  type: Hosts
  url: hosts/strandsagents-hosts.yml
- group: other
  href: https://artifacts.apis.io/strandsagents/vendors/strandsagents-vendors.yml
  title: ''
  type: Vendors
  url: vendors/strandsagents-vendors.yml
- group: build
  href: https://artifacts.apis.io/strandsagents/packages/strandsagents-packages.yml
  title: ''
  type: SDKs
  url: packages/strandsagents-packages.yml
- group: build
  href: https://artifacts.apis.io/strandsagents/packages/strandsagents-packages.yml
  title: ''
  type: Packages
  url: packages/strandsagents-packages.yml
- group: auth
  href: https://artifacts.apis.io/strandsagents/security/strandsagents-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strandsagents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strandsagents.com/
- group: docs
  title: ''
  type: Documentation
  url: https://strandsagents.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://strandsagents.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strands-agents
- group: start
  title: ''
  type: DeveloperPortal
  url: https://strandsagents.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://strandsagents.com/docs/user-guide/harness/quickstart/
coverage:
  checked: '2026-10-22'
  detail: Documentation pages return HTML shells and redirect scripts, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://strandsagents.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Strands Agents provides an open-source toolkit for building, deploying, and managing production AI agents. It offers a modular harness, SDKs for multiple languages, sandboxing, evaluation tools, and a marketplace of integrations. The platform enables developers to compose complex multi-agent systems, enforce policy, and monitor performance, aiming to accelerate AI agent adoption in real-world applications.
image: https://strandsagents.com/og-image.png
layout: provider
modified: '2026-10-21'
name: Strands Agents
nav: Providers
network: true
overview: 'Strands Agents is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, OpenSource, Toolkit, and Agents.


  Strands Agents'' developer surface includes changelog, authentication, documentation, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Strandsagents Authentication
  slug: strandsagents-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Strandsagents Domain Security
  slug: strandsagents-domain-security
  summary_line: TLSv1.3 · HSTS
slug: strandsagents
tags:
- Company
- AI
- OpenSource
- Toolkit
- Agents
website: https://strandsagents.com/
---
