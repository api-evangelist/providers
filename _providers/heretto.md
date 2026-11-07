---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://thunderbird.deploy.heretto.com
  baseurl_source: declared
  description: 'Heretto API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Heretto API
  slug: heretto-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/heretto/rules/heretto-rules.yml
  title: ''
  type: Spectral
  url: rules/heretto-rules.yml
- group: design
  href: https://artifacts.apis.io/heretto/json-ld/heretto-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/heretto-context.jsonld
- group: design
  href: https://artifacts.apis.io/heretto/vocabulary/heretto-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/heretto-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/heretto/data-model/heretto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heretto-data-model.yml
- group: operate
  href: https://artifacts.apis.io/heretto/changelog/heretto-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/heretto-changelog.yml
- group: design
  href: https://artifacts.apis.io/heretto/lifecycle/heretto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/heretto-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/heretto/conformance/heretto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heretto-conformance.yml
- group: agent
  href: https://artifacts.apis.io/heretto/llms/heretto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heretto-llms.txt
- group: other
  href: https://artifacts.apis.io/heretto/hosts/heretto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heretto-hosts.yml
- group: other
  href: https://artifacts.apis.io/heretto/vendors/heretto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heretto-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.heretto.com/en/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Heretto
- group: auth
  href: https://artifacts.apis.io/heretto/security/heretto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heretto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heretto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.heretto.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.heretto.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://help.heretto.com/en/heretto-deploy-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.heretto.com/en/heretto-ccms/get-started
- group: operate
  title: ''
  type: Support
  url: https://help.heretto.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.heretto.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heretto.com/packages
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heretto.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heretto.com/privacy-policy
created: '2026-10-20'
description: Heretto provides an All‑In‑One Content Operations platform for technical documentation, offering capabilities such as creating, managing, publishing, and governing structured content, translation management, support team enablement, and API documentation. The solution includes AI‑powered assistance, analytics, and a headless Deploy API for content delivery, targeting teams that need scalable, collaborative documentation workflows.
json_schemas:
- name: GetV4DeploymentsI9Va3Klk1331IymehhuSearchResponse
  property_count: 2
  slug: heretto-get-v4-deployments-i9-va3-klk1331-iymehhu-search-response
- name: GetV4DeploymentsI9Va3Klk1331IymehhuStructureResponse
  property_count: 2
  slug: heretto-get-v4-deployments-i9-va3-klk1331-iymehhu-structure-response
jsonld:
- class_count: 2
  name: Heretto Context
  property_count: 2
  slug: heretto-context
layout: provider
modified: '2026-10-20'
name: Heretto
nav: Providers
network: true
overview: 'Heretto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ContentOps, Documentation, Artificial Intelligence, and Collaboration.


  The Heretto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Heretto''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Heretto API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: heretto-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 20.9
    developer_ergonomics: 22.6
    discoverability: 69.6
    operational_transparency: 10.5
  previous_composite: 32.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/heretto/heretto-2026-11-03T133351.png
security:
- kind: domain-security
  name: Heretto Domain Security
  slug: heretto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: heretto
tags:
- Company
- ContentOps
- Documentation
- Artificial Intelligence
- Collaboration
website: https://www.heretto.com/
---
