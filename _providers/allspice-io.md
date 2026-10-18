---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: API for AllSpice platform to manage hardware design data.
  name: AllSpice API
  slug: allspice-api
- baseURL: https://hub.allspice.io
  baseurl_source: declared
  description: The Repos API from AllSpice.io — 2 operation(s) for repos.
  name: AllSpice.io Repos API
  slug: allspice-io-repos-api
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/plans/allspice-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allspice-io-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/rules/allspice-io-rules.yml
  title: ''
  type: Spectral
  url: rules/allspice-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/json-ld/allspice-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allspice-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/vocabulary/allspice-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allspice-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/data-model/allspice-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allspice-io-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/authentication/allspice-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allspice-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/conformance/allspice-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allspice-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/llms/allspice-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allspice-io-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/well-known/allspice-io-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allspice-io-partner-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/well-known/allspice-io-hub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/allspice-io-hub-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/well-known/allspice-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allspice-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/hosts/allspice-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allspice-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/vendors/allspice-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allspice-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allspice.io/terms
- group: start
  title: ''
  type: Login
  url: https://hub.allspice.io/user/login
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.allspice.io/docs/getting-started-with-allpice-actions
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allspice-io/refs/heads/main/security/allspice-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allspice-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allspice.io
- group: docs
  title: ''
  type: Documentation
  url: https://learn.allspice.io/docs
- group: company
  title: ''
  type: Blog
  url: https://allspice.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://allspice.io/plans
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allspice.io/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.allspice.io
coverage:
  checked: '2026-09-24'
  detail: The AllSpice.io website returns HTML shells and no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://allspice.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: AllSpice.io provides a platform for hardware engineering teams to manage design data, collaborate on schematics, and automate releases with AI assistance. The service offers version control, design review tools, secure document sharing, and integration with issue trackers. It targets electrical engineering workflows from capture through manufacturing handoff, emphasizing speed, security, and collaboration across the product development lifecycle.
image: https://cdn.prod.website-files.com/6a8dac3f4f80c9b7ed03a8d1/6aa68c69323ef39a7a461d7b_meta%20image.jpg
json_schemas:
- name: GetApiV1ReposResponse
  property_count: 1
  slug: allspice-io-get-api-v1-repos-response
- name: PostApiV1ReposOwnerRepoPullsRequest
  property_count: 4
  slug: allspice-io-post-api-v1-repos-owner-repo-pulls-request
- name: PostApiV1ReposOwnerRepoPullsResponse
  property_count: 1
  slug: allspice-io-post-api-v1-repos-owner-repo-pulls-response
jsonld:
- class_count: 3
  name: Allspice Io Context
  property_count: 6
  slug: allspice-io-context
layout: provider
modified: '2026-09-24'
name: AllSpice.io
nav: Providers
network: true
overview: 'AllSpice.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Repos API, and 1 more. Tagged areas include Company, Hardware, Collaboration, Artificial Intelligence, and Design.


  The AllSpice.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AllSpice.io''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Allspice Io Plans Pricing
  plan_count: 3
  slug: allspice-io-plans-pricing
- name: Allspice Io Plans
  plan_count: 4
  slug: allspice-io-plans
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AllSpice.io API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: allspice-io-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 38.0
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 1.1
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
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Allspice Io Authentication
  slug: allspice-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Allspice Io Domain Security
  slug: allspice-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allspice-io
tags:
- Company
- Hardware
- Collaboration
- Artificial Intelligence
- Design
website: https://allspice.io
---
