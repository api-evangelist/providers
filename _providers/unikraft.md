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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.0
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: This specification describes the Unikraft Cloud Platform API, which provides mechanisms to interact with Unikraft Cloud metros.
  name: Unikraft Cloud Platform API
  slug: unikraft-cloud-platform-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/unikraft/plans/unikraft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unikraft-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/unikraft/rules/unikraft-rules.yml
  title: ''
  type: Spectral
  url: rules/unikraft-rules.yml
- group: design
  href: https://artifacts.apis.io/unikraft/json-ld/unikraft-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unikraft-context.jsonld
- group: design
  href: https://artifacts.apis.io/unikraft/vocabulary/unikraft-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unikraft-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/unikraft/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/unikraft/data-model/unikraft-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unikraft-data-model.yml
- group: build
  href: https://artifacts.apis.io/unikraft/cli/unikraft-cli.yml
  title: ''
  type: CLI
  url: cli/unikraft-cli.yml
- group: design
  href: https://artifacts.apis.io/unikraft/conventions/unikraft-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unikraft-conventions.yml
- group: auth
  href: https://artifacts.apis.io/unikraft/authentication/unikraft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unikraft-authentication.yml
- group: design
  href: https://artifacts.apis.io/unikraft/errors/unikraft-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unikraft-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unikraft/conformance/unikraft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unikraft-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unikraft/llms/unikraft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unikraft-llms.txt
- group: agent
  href: https://artifacts.apis.io/unikraft/well-known/unikraft-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unikraft-well-known.yml
- group: other
  href: https://artifacts.apis.io/unikraft/hosts/unikraft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unikraft-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unikraft.com/company/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://github.com/moby/buildkit/security/advisories/GHSA-f2v9-hprr-32q3
- group: commercial
  title: ''
  type: Pricing
  url: https://unikraft.com/pricing
- group: start
  title: ''
  type: Login
  url: https://console.unikraft.com/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skuenzer
- group: operate
  title: ''
  type: ChangeLog
  url: https://unikraft.com/docs/releases/index
- group: start
  title: ''
  type: GettingStarted
  url: https://unikraft.com/docs/sdks/js
- group: auth
  href: https://artifacts.apis.io/unikraft/security/unikraft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unikraft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unikraft.com
- group: docs
  title: ''
  type: Documentation
  url: https://unikraft.org/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://unikraft.org
- group: company
  title: ''
  type: Blog
  url: https://unikraft.org/blog
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://unikraft.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Unikraft is an open-source unikernel library operating system (LibOS) that enables developers to build ultra‑lightweight, high‑performance virtual machines called unikernels. It provides a fast, secure, and customizable platform for cloud‑native, container‑less applications, supporting integration with Docker, Kubernetes, CI/CD pipelines, and various cloud providers. The project is community‑driven, offers extensive documentation, tooling, and a marketplace of pre‑built unikernel applications, aiming to deliver millisecond‑scale startup times and strong isolation.
image: https://unikraft.com/images/home-share.jpg
jsonld:
- class_count: 120
  name: Unikraft Context
  property_count: 174
  slug: unikraft-context
layout: provider
modified: '2026-10-29'
name: Unikraft
nav: Providers
network: true
overview: 'Unikraft publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Unikernel, Open Source, Cloud-Native, and Performance.


  The Unikraft catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Unikraft''s developer surface includes CLI, authentication, pricing, changelog, getting-started guide, documentation, engineering blog, and 19 more developer resources.'
plans:
- name: Unikraft Plans Pricing
  plan_count: 4
  slug: unikraft-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Unikraft API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: unikraft-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 37.5
    discoverability: 69.6
    operational_transparency: 15.8
  previous_composite: 45.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/unikraft/unikraft-2026-11-03T145425.png
security:
- kind: authentication
  name: Unikraft Authentication
  slug: unikraft-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unikraft Domain Security
  slug: unikraft-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 4
skills:
- name: unikraft-autoscale-create-with-policy
  slug: unikraft-autoscale-create-with-policy
- name: unikraft-create-and-attach-volume
  slug: unikraft-create-and-attach-volume
- name: unikraft-create-and-retrieve-service-group
  slug: unikraft-create-and-retrieve-service-group
- name: unikraft-create-start-stop-instance
  slug: unikraft-create-start-stop-instance
slug: unikraft
tags:
- Company
- Unikernel
- Open Source
- Cloud-Native
- Performance
website: https://unikraft.com
---
