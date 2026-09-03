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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Optic CLI provides OpenAPI diffing, linting and breaking-change detection from the command line, comparing two versions of an OpenAPI specification with behaviour-aware diffing and applying style-
  name: Optic CLI
  slug: optic-cli
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/opticdev/optic
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/opticdev/optic/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/opticdev/optic/wiki
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/opticdev/optic
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opticdev
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/opticdev/optic/issues
- group: operate
  title: ''
  type: Support
  url: https://github.com/opticdev/optic/discussions
- group: operate
  title: ''
  type: Releases
  url: https://github.com/opticdev/optic/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/opticdev/optic/blob/main/LICENSE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useoptic
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optic-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optic-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/optic-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/optic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/optic-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optic-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/optic-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/optic-security.txt
- group: auth
  title: ''
  type: Security
  url: security/optic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optic-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Optic never shipped a callable API and the company no longer exists as an independent surface — Optic Labs was absorbed by Atlassian in April 2024, the Optic Cloud REST backend named in its own open-source client (api.useoptic.com) and the docs host (www.useoptic.com) both return NXDOMAIN, useoptic.com 301s to the GitHub repository, and that repository was archived read-only in January 2026 with no sunset notice.
  evidence:
  - status: 301
    url: https://useoptic.com/
  - status: 0
    url: https://www.useoptic.com/docs
  - status: 0
    url: https://api.useoptic.com/openapi.json
  - status: 200
    url: https://github.com/opticdev/optic
  - status: 200
    url: https://github.com/opticdev/optic/wiki
  reason: defunct
  state: none
created: '2026-03-25'
description: Optic is an MIT-licensed command-line tool for OpenAPI linting, diffing and testing. It compares two versions of an OpenAPI document with behaviour-aware diffing to catch breaking changes before they ship, enforces style-guide rulesets (breaking-changes, documentation, examples, naming-changes, Spectral and lintgpt), and generates or verifies OpenAPI from captured test traffic via HAR files, Postman collections or a local proxy. Optic Labs was acquired by Atlassian in April 2024; the hosted Optic Cloud service was disconnected from the CLI at v1.0.0 in August 2024, the documentation site was retired in favour of the GitHub Wiki, and the source repository was archived read-only in January 2026 after a final v1.0.9 release. Optic publishes no callable API of its own — it is a tool that consumes and governs other people's contracts.
finops:
- name: Optic Finops
  service_category: API
  slug: optic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optic.png
layout: provider
modified: '2026-08-29'
name: Optic
nav: Providers
network: true
overview: 'Optic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Governance, Breaking Changes, Contract Testing, Diff, and Linting.


  Optic''s developer surface includes documentation, getting-started guide, support, changelog, CLI, and 18 more developer resources.'
plans:
- name: Optic Plans Pricing
  plan_count: 0
  slug: optic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Optic Rate Limits
  slug: optic-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 21.1
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optic/refs/heads/main/screenshots/optic-2026-08-07T190759.png
security:
- kind: domain-security
  name: Optic Domain Security
  slug: optic-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Optic Vulnerability Disclosure
  slug: optic-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: optic
tags:
- API Governance
- Breaking Changes
- Contract Testing
- Diff
- Linting
- OpenAPI
- Testing
- CLI
- Open-Source
- Archived
---
