---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Project Nessie Agentic Access
  operation_count: 1
  slug: project-nessie-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.projectnessie.org
  baseurl_source: declared
  description: The Config API from Project Nessie — 1 operation(s) for config.
  name: Project Nessie Config API
  slug: project-nessie-config-api
artifact_total: 4
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/agentic-access/project-nessie-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/project-nessie-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/rules/project-nessie-rules.yml
  title: ''
  type: Spectral
  url: rules/project-nessie-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/changelog/project-nessie-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/project-nessie-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/errors/project-nessie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/project-nessie-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/conformance/project-nessie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/project-nessie-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/hosts/project-nessie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/project-nessie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/vendors/project-nessie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/project-nessie-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://projectnessie.org/nessie-0-101-3/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://projectnessie.org/releases/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/project-nessie/refs/heads/main/security/project-nessie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/project-nessie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://projectnessie.org
- group: docs
  title: ''
  type: Documentation
  url: https://projectnessie.org/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://projectnessie.org/develop/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://projectnessie.org/guides/try-nessie/
- group: company
  title: ''
  type: Blog
  url: https://projectnessie.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://projectnessie.org/community/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/projectnessie/nessie
created: '2026-10-13'
description: Project Nessie is an open-source project providing a transactional catalog for data lakes, offering Git‑like semantics for versioned data. It enables users to manage and query data across multiple storage systems, supports branching, tagging, and merging of data states, and integrates with tools such as Apache Iceberg, Spark, Flink, and Hive. The project aims to simplify data governance, reproducibility, and collaboration in modern data engineering workflows, fostering a community-driven ecosystem with extensive documentation, guides, and community support.
layout: provider
modified: '2026-10-13'
name: Project Nessie
nav: Providers
network: true
overview: 'Project Nessie publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Config API. Tagged areas include Company, Open Source, DataLake, Version Control, and Community.


  The Project Nessie catalog on APIs.io includes 1 Spectral governance ruleset.


  Project Nessie''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, and 13 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Project Nessie API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: project-nessie-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 29.4
    developer_ergonomics: 42.1
    discoverability: 62.5
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Project Nessie Domain Security
  slug: project-nessie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: project-nessie
tags:
- Company
- Open Source
- DataLake
- Version Control
- Community
website: https://projectnessie.org
---
