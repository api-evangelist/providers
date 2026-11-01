---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Linkace Agentic Access
  operation_count: 38
  slug: linkace-agentic-access
  summary_line: 38 operations · 21 acting
api_count: 1
apis:
- description: LinkAce offers a REST API for all features, enabling programmatic access to bookmarks, tags, lists, and user management.
  name: LinkAce API
  slug: linkace-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Bulk API from LinkAce — 4 operation(s) for bulk.
  name: LinkAce Bulk API
  slug: linkace-bulk-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The General API from LinkAce — 1 operation(s) for general.
  name: LinkAce General API
  slug: linkace-general-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Links API from LinkAce — 4 operation(s) for links.
  name: LinkAce Links API
  slug: linkace-links-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Lists API from LinkAce — 4 operation(s) for lists.
  name: LinkAce Lists API
  slug: linkace-lists-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Notes API from LinkAce — 3 operation(s) for notes.
  name: LinkAce Notes API
  slug: linkace-notes-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Search API from LinkAce — 3 operation(s) for search.
  name: LinkAce Search API
  slug: linkace-search-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Tags API from LinkAce — 4 operation(s) for tags.
  name: LinkAce Tags API
  slug: linkace-tags-api
- baseURL: https://www.linkace.org/api
  baseurl_source: declared
  description: The Trash API from LinkAce — 6 operation(s) for trash.
  name: LinkAce Trash API
  slug: linkace-trash-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/linkace/agentic-access/linkace-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linkace-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/linkace/rules/linkace-rules.yml
  title: ''
  type: Spectral
  url: rules/linkace-rules.yml
- group: design
  href: https://artifacts.apis.io/linkace/json-ld/linkace-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkace-context.jsonld
- group: design
  href: https://artifacts.apis.io/linkace/vocabulary/linkace-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linkace-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/linkace/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/linkace/data-model/linkace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linkace-data-model.yml
- group: operate
  href: https://artifacts.apis.io/linkace/changelog/linkace-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/linkace-changelog.yml
- group: design
  href: https://artifacts.apis.io/linkace/errors/linkace-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linkace-problem-types.yml
- group: design
  href: https://artifacts.apis.io/linkace/conformance/linkace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linkace-conformance.yml
- group: other
  href: https://artifacts.apis.io/linkace/hosts/linkace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkace-hosts.yml
- group: other
  href: https://artifacts.apis.io/linkace/vendors/linkace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkace-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kovah
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.linkace.org/docs/v2/general/changelog/
- group: auth
  href: https://artifacts.apis.io/linkace/authentication/linkace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linkace-authentication.yml
- group: auth
  href: https://artifacts.apis.io/linkace/security/linkace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.linkace.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.linkace.org/docs/v2/
- group: docs
  title: ''
  type: APIReference
  url: https://www.linkace.org/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.linkace.org/docs/v2/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.linkace.org/support
- group: company
  title: ''
  type: Blog
  url: https://www.linkace.org/blog
created: '2026-10-28'
description: LinkAce is an open-source, self‑hosted bookmark archive that lets users save, organize, and share web links. It offers features like tagging, lists, multi‑user support with SSO, automatic archiving via the Internet Archive, and a REST API for full integration. The platform is available via Docker, Kubernetes, or direct PHP installation and supports 15 languages.
image: https://www.linkace.org/images/linkace-social.jpg
json_schemas:
- name: GetResponse
  property_count: 9
  slug: linkace-get-response
- name: PostApiV2LinksResponse
  property_count: 9
  slug: linkace-post-api-v2-links-response
jsonld:
- class_count: 16
  name: Linkace Context
  property_count: 33
  slug: linkace-context
layout: provider
modified: '2026-10-28'
name: LinkAce
nav: Providers
network: true
overview: 'LinkAce publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk API, General API, Links API, and 6 more. Tagged areas include Company, OpenSource, Bookmarking, SelfHosted, and API.


  The LinkAce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LinkAce''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: LinkAce API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: linkace-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 47.3
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 81.8
      derived: 3
      marker_coverage: 27.3
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Linkace Authentication
  slug: linkace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Linkace Domain Security
  slug: linkace-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: linkace-bulk-manage-links
  slug: linkace-bulk-manage-links
- name: linkace-create-and-view-tag
  slug: linkace-create-and-view-tag
- name: linkace-notes-create-and-list
  slug: linkace-notes-create-and-list
slug: linkace
tags:
- Company
- OpenSource
- Bookmarking
- SelfHosted
- API
website: https://www.linkace.org/
---
