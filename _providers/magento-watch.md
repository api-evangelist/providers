---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Magento Watch Agentic Access
  operation_count: 22
  slug: magento-watch-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: Free unauthenticated API providing version, patch, security bulletin and health data for Magento Open Source, Adobe Commerce and Mage‑OS.
  name: Magento Lifecycle API
  slug: magento-lifecycle-api
- baseURL: https://magento.watch
  baseurl_source: declared
  description: Service metadata
  name: magento-watch Meta API
  slug: magento-watch-meta-api
- baseURL: https://magento.watch
  baseurl_source: declared
  description: Adobe Quality Patches Tool patches with resolved applicability
  name: magento-watch Patches API
  slug: magento-watch-patches-api
- baseURL: https://magento.watch
  baseurl_source: declared
  description: Security bulletin lookups
  name: magento-watch Security API
  slug: magento-watch-security-api
- baseURL: https://magento.watch
  baseurl_source: declared
  description: Community fixes merged upstream, not yet in a release line; not Adobe Quality Patches
  name: magento-watch Upstream Fixes API
  slug: magento-watch-upstream-fixes-api
- baseURL: https://magento.watch
  baseurl_source: declared
  description: Version lifecycle lookups
  name: magento-watch Versions API
  slug: magento-watch-versions-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/magento-watch/agentic-access/magento-watch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/magento-watch-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/magento-watch/rules/magento-watch-rules.yml
  title: ''
  type: Spectral
  url: rules/magento-watch-rules.yml
- group: design
  href: https://artifacts.apis.io/magento-watch/json-ld/magento-watch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/magento-watch-context.jsonld
- group: design
  href: https://artifacts.apis.io/magento-watch/vocabulary/magento-watch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/magento-watch-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/magento-watch/data-model/magento-watch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/magento-watch-data-model.yml
- group: design
  href: https://artifacts.apis.io/magento-watch/errors/magento-watch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/magento-watch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/magento-watch/conformance/magento-watch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/magento-watch-conformance.yml
- group: agent
  href: https://artifacts.apis.io/magento-watch/llms/magento-watch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/magento-watch-llms.txt
- group: auth
  href: https://artifacts.apis.io/magento-watch/well-known/magento-watch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/magento-watch-security.txt
- group: agent
  href: https://artifacts.apis.io/magento-watch/well-known/magento-watch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/magento-watch-well-known.yml
- group: other
  href: https://artifacts.apis.io/magento-watch/hosts/magento-watch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/magento-watch-hosts.yml
- group: other
  href: https://artifacts.apis.io/magento-watch/vendors/magento-watch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/magento-watch-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://magento.watch/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://magento.watch/changelog
- group: auth
  href: https://artifacts.apis.io/magento-watch/security/magento-watch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/magento-watch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/magento-watch/security/magento-watch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/magento-watch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://magento.watch/
created: '2026-10-30'
description: magento-watch provides a free JSON API and MCP server that tracks Magento Open Source, Adobe Commerce, and Mage‑OS lifecycle information. It offers endpoints for versions, patches, security bulletins, and health checks without authentication, enabling engineers, DevOps, and business analysts to integrate Magento lifecycle data into tools and workflows. The service includes a web UI with documentation, a changelog, and links to related resources.
image: https://magento.watch/og-image.png
jsonld:
- class_count: 49
  name: Magento Watch Context
  property_count: 140
  slug: magento-watch-context
layout: provider
modified: '2026-10-30'
name: magento-watch
nav: Providers
network: true
overview: 'magento-watch publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Meta API, Patches API, Security API, and 3 more. Tagged areas include Company, Magento, API, Lifecycle, and OpenSource.


  The magento-watch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  magento-watch''s developer surface includes changelog and 16 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: magento-watch API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: magento-watch-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
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
- kind: domain-security
  name: Magento Watch Domain Security
  slug: magento-watch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Magento Watch Vulnerability Disclosure
  slug: magento-watch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: magento-watch
tags:
- Company
- Magento
- API
- Lifecycle
- OpenSource
website: https://magento.watch/
---
