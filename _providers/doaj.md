---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Doaj Agentic Access
  operation_count: 17
  slug: doaj-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 1
apis:
- description: DOAJ provides a REST API for accessing journal and article metadata.
  name: DOAJ API
  slug: doaj-api
- baseURL: https://doaj.org/api/v4
  baseurl_source: declared
  description: The Bulk API API from DOAJ — 3 operation(s) for bulk api.
  name: DOAJ Bulk API
  slug: doaj-bulk-api-api
- baseURL: https://doaj.org/api/v4
  baseurl_source: declared
  description: The CRUD Applications API from DOAJ — 2 operation(s) for crud applications.
  name: DOAJ CRUD Applications API
  slug: doaj-crud-applications-api
- baseURL: https://doaj.org/api/v4
  baseurl_source: declared
  description: The CRUD Articles API from DOAJ — 2 operation(s) for crud articles.
  name: DOAJ CRUD Articles API
  slug: doaj-crud-articles-api
- baseURL: https://doaj.org/api/v4
  baseurl_source: declared
  description: The CRUD Journals API from DOAJ — 1 operation(s) for crud journals.
  name: DOAJ CRUD Journals API
  slug: doaj-crud-journals-api
- baseURL: https://doaj.org/api/v4
  baseurl_source: declared
  description: The Search API from DOAJ — 3 operation(s) for search.
  name: DOAJ Search API
  slug: doaj-search-api
artifact_total: 9
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/agentic-access/doaj-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doaj-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/rules/doaj-rules.yml
  title: ''
  type: Spectral
  url: rules/doaj-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/errors/doaj-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doaj-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/conformance/doaj-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doaj-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/hosts/doaj-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doaj-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/vendors/doaj-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doaj-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DOAJ
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/doaj/refs/heads/main/security/doaj-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doaj-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doaj.org
- group: docs
  title: ''
  type: APIReference
  url: https://doaj.org/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://doaj.org/docs/api/
- group: operate
  title: ''
  type: Support
  url: https://doaj.org/support/
- group: company
  title: ''
  type: Blog
  url: https://blog.doaj.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doaj.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doaj.org/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://doaj.org/apply/
created: '2026-10-14'
description: The Directory of Open Access Journals (DOAJ) provides a searchable database of peer‑reviewed open access journals and articles, offering free access to scholarly content, metadata, and APIs for developers. It supports publishers, libraries, funders, and researchers by promoting transparency, best practices, and open science. DOAJ also offers premium services, tools for journal evaluation, and a commitment to preserving open scholarly communication.
layout: provider
modified: '2026-10-14'
name: DOAJ
nav: Providers
network: true
overview: 'DOAJ publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk API, CRUD Applications API, CRUD Articles API, and 3 more. Tagged areas include OpenAccess, Journals, ScholarlyPublishing, and Metadata.


  The DOAJ catalog on APIs.io includes 1 Spectral governance ruleset.


  DOAJ''s developer surface includes API reference, getting-started guide, support, engineering blog, signup flow, and 11 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: DOAJ API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: doaj-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 40.0
    developer_ergonomics: 26.2
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Doaj Domain Security
  slug: doaj-domain-security
  summary_line: TLSv1.3
slug: doaj
tags:
- OpenAccess
- Journals
- ScholarlyPublishing
- Metadata
website: https://doaj.org
---
