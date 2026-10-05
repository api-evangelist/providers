---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
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
  score: 15.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://repo.continuum.io
  baseurl_source: declared
  description: The Miniconda API from bodo.ai — 1 operation(s) for miniconda.
  name: bodo.ai Miniconda API
  slug: bodo-ai-miniconda-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/rules/bodo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bodo-ai-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/changelog/bodo-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bodo-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/conformance/bodo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bodo-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/well-known/bodo-ai-repo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bodo-ai-repo-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/well-known/bodo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bodo-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/hosts/bodo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bodo-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/vendors/bodo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bodo-ai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodo-ai/refs/heads/main/security/bodo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bodo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bodo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bodo.ai/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bodo.ai/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bodo.ai/latest/quick_start/
- group: company
  title: ''
  type: Blog
  url: https://www.bodo.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bodo-ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bodo.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.bodo.ai/contact
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bodo.ai provides a modern enterprise analytics platform that bridges data teams, business users, and AI agents. Built on open‑source foundations under the Apache 2.0 license, Bodo enables scalable, high‑performance analytics and AI workloads with familiar tools like Python, Pandas, and SQL. Its products include the Bodo Engine for distributed compute and PyDough for trusted answer layers, offering governance, performance, and modularity for enterprise AI workflows.
image: https://cdn.prod.website-files.com/6a107660da731c4732babfb0/6a5a4f581f99cf59c112e24d_ChatGPT%20Image%20Jul%2017%2C%202026%2C%2011_50_14%20AM.png
layout: provider
modified: '2026-10-02'
name: bodo.ai
nav: Providers
network: true
overview: 'bodo.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Miniconda API. Tagged areas include Analytics, Artificial Intelligence, Enterprise, Open Source, and Data Engineering.


  The bodo.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  bodo.ai''s developer surface includes changelog, documentation, getting-started guide, engineering blog, support, and 11 more developer resources.'
random_paper: 7
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: bodo.ai API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: bodo-ai-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.6
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Bodo Ai Domain Security
  slug: bodo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bodo-ai
tags:
- Analytics
- Artificial Intelligence
- Enterprise
- Open Source
- Data Engineering
website: https://www.bodo.ai/
---
