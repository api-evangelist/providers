---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://naftiko.io/
- group: docs
  title: ''
  type: Documentation
  url: https://shipyard.naftiko.io/ikanos/1.0.0-beta3/
- group: docs
  title: ''
  type: APIReference
  url: https://shipyard.naftiko.io/ikanos/1.0.0-beta3/spec/
- group: start
  title: ''
  type: GettingStarted
  url: https://shipyard.naftiko.io/ikanos/1.0.0-beta3/installation/
- group: build
  title: ''
  type: CLI
  url: cli/naftiko-cli.yml
- group: build
  title: ''
  type: CLI
  url: https://shipyard.naftiko.io/ikanos/1.0.0-beta3/guide/cli/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/naftiko-ikanos-capability-schema.json
- group: design
  title: ''
  type: Rules
  url: rules/naftiko-ikanos-ruleset.yml
- group: other
  title: ''
  type: Glossary
  url: https://naftiko.io/resources/glossary
- group: build
  title: ''
  type: Packages
  url: packages/naftiko-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/naftiko-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/naftiko-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/naftiko-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://shipyard.naftiko.io/ikanos/1.0.0-beta3/releases/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/naftiko-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/naftiko/ikanos/releases
- group: operate
  title: ''
  type: Roadmap
  url: https://shipyard.naftiko.io/ikanos/1.0.0-beta3/roadmap/
- group: commercial
  title: ''
  type: Plans
  url: plans/naftiko-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://naftiko.io/platform/editions/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/naftiko-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naftiko-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/naftiko
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/naftiko/ikanos
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/naftiko/polychro
- group: other
  title: ''
  type: OpenSource
  url: https://naftiko.io/community/open-source/
- group: operate
  title: ''
  type: Support
  url: https://naftiko.io/company/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://naftiko.io/community/
- group: company
  title: ''
  type: Blog
  url: https://naftiko.io/resources/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://naftiko.io/feed.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://naftiko.io/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://naftiko.io/legal/privacy/
created: '2026-08-17'
description: 'Naftiko builds spec-driven integration software for AI agents. Its two Apache 2.0 Java engines — Ikanos, a capability engine, and Polychro, a polyglot spec linter — let a team declare a slice of its business in a single YAML capability file and serve it simultaneously over MCP, Agent Skill, REST and a Control port without writing or compiling code. A capability consumes the HTTP APIs an organisation already has, structures their responses into clean JSON, then aggregates and orchestrates those operations into one governed contract for agents, applications and partners. Naftiko operates no hosted API of its own: it distributes software customers run on their own infrastructure, so this profile catalogs a published JSON Schema, a governance ruleset, a CLI, container images and Maven artifacts rather than endpoints and API keys. Four editions are published — Community (free forever, Apache 2.0), Developer and Team (managed hosting, in development) and Enterprise (Warden and Skipper,
  design partners) — none of them carrying a published price.'
image: https://naftiko.github.io/docs/images/logo/logo_full_color_512.png
json_schemas:
- name: Naftiko Ikanos Capability
  property_count: 7
  slug: naftiko-ikanos-capability
layout: provider
modified: '2026-08-17'
name: Naftiko
nav: Providers
network: true
overview: 'Naftiko is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, API Integration, API Governance, and MCP.


  The Naftiko catalog on APIs.io includes 1 Spectral governance ruleset.


  Naftiko''s developer surface includes documentation, API reference, getting-started guide, CLI, changelog, pricing, support, and 25 more developer resources.'
plans:
- name: Naftiko Plans Pricing
  plan_count: 4
  slug: naftiko-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Naftiko Rate Limits
  slug: naftiko-rate-limits
rules:
- effective_rule_count: 33
  extends: []
  name: Naftiko API Rules
  rule_count: 33
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 16
  slug: naftiko-ikanos-ruleset
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 72.7
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 72.7
    operational_transparency: 31.6
  previous_composite: 40.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Naftiko Domain Security
  slug: naftiko-domain-security
  summary_line: TLSv1.3 · DMARC
slug: naftiko
tags:
- Company
- Ai Data
- API Integration
- API Governance
- MCP
- Agent Skills
- Open-Source
- Developer Tools
- API Specifications
- Spec-Driven Integration
- Capability Engine
- API Linting
website: https://naftiko.io/
---
