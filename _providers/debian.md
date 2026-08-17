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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Debian Agentic Access
  operation_count: 17
  slug: debian-agentic-access
  summary_line: 17 operations
api_count: 6
apis:
- description: The Debian Sources API at sources.debian.org provides programmatic access to source code, package metadata, copyright records, and Debian patches for every source package in the archive.
  name: Debian Sources API
  slug: debian-sources-api
- description: The Bugs API from Debian — 4 operation(s) for bugs.
  name: Debian Bugs API
  slug: debian-bugs-api
- description: The Copyright API from Debian — 2 operation(s) for copyright.
  name: Debian Copyright API
  slug: debian-copyright-api
- description: The Maintainers API from Debian — 1 operation(s) for maintainers.
  name: Debian Maintainers API
  slug: debian-maintainers-api
- description: The Patches API from Debian — 1 operation(s) for patches.
  name: Debian Patches API
  slug: debian-patches-api
- description: The Reproducibility API from Debian — 1 operation(s) for reproducibility.
  name: Debian Reproducibility API
  slug: debian-reproducibility-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Debian Bug Tracking System API
  slug: open-debian-bts-api
- collection_type: open
  name: Debian Bug Tracking System Bugs API
  slug: open-debian-bugs-api
- collection_type: open
  name: Debian Bug Tracking System Bugs Copyright API
  slug: open-debian-copyright-api
- collection_type: open
  name: Debian Bug Tracking System Bugs Maintainers API
  slug: open-debian-maintainers-api
- collection_type: open
  name: Debian Bug Tracking System Bugs Patches API
  slug: open-debian-patches-api
- collection_type: open
  name: Debian Bug Tracking System Bugs Reproducibility API
  slug: open-debian-reproducibility-api
- collection_type: open
  name: Debian Bug Tracking System Bugs Sources API
  slug: open-debian-sources-api
- collection_type: open
  name: Debian Ultimate Database (UDD) Web Tools
  slug: open-debian-udd-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/debian-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/debian-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debian-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://bits.debian.org/feeds/atom.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Debian
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/debian
- group: company
  title: ''
  type: Website
  url: https://www.debian.org/
- group: other
  title: ''
  type: Wiki
  url: https://wiki.debian.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.debian.org/doc/
- group: build
  title: ''
  type: GitLab
  url: https://salsa.debian.org/
- group: other
  title: ''
  type: Mailing Lists
  url: https://lists.debian.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.debian.org/legal/privacy
- group: commercial
  title: ''
  type: License
  url: https://www.debian.org/social_contract
- group: design
  title: ''
  type: JSONLD
  url: json-ld/debian-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/debian-vocabulary.yml
created: '2025-01-01'
description: Debian is a free operating system distribution maintained by the Debian Project, a community of more than a thousand volunteers worldwide. Debian provides a number of developer-facing services including a source-code browsing API at sources.debian.org, the Bug Tracking System (BTS) at bugs.debian.org, and the Ultimate Debian Database (UDD) - a single Postgres database aggregating package, bug, Lintian, popcon, and reproducibility data for cross-cutting queries.
finops:
- name: Debian Finops
  service_category: API
  slug: debian-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/debian.png
json_schemas:
- name: Debian Bug Report
  property_count: 11
  slug: debian-bug
- name: Debian Source Package
  property_count: 10
  slug: debian-package
jsonld:
- class_count: 3
  name: Debian Context
  property_count: 12
  slug: debian-context
layout: provider
modified: '2026-05-19'
name: Debian
nav: Providers
network: true
overview: 'Debian publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Sources API, Bugs API, Copyright API, and 3 more. Tagged areas include Bug Tracker, Debian, Linux, Open Source, and Operating System.


  The Debian catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Debian''s developer surface includes engineering blog, documentation, and 13 more developer resources.'
plans:
- name: Debian Plans Pricing
  plan_count: 3
  slug: debian-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Debian Rate Limits
  slug: debian-rate-limits
rules:
- name: Debian API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: debian-jsonschema-spectral-rules
- name: Debian API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: debian-sources-api-rules
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 57.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debian/refs/heads/main/screenshots/debian-2026-06-20T175746.png
security:
- kind: domain-security
  name: Debian Domain Security
  slug: debian-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Debian Vulnerability Disclosure
  slug: debian-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: debian
tags:
- Bug Tracker
- Debian
- Linux
- Open Source
- Operating System
- Package Management
- Source Code
website: https://www.debian.org/
---
