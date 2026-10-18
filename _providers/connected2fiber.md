---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Developer portal provides API reference and documentation. No OpenAPI spec discovered.
  name: Connected2fiber API
  slug: connected2fiber-api-2
- baseURL: https://api.connectbase.com
  baseurl_source: declared
  description: The Address API from Connected2fiber — 1 operation(s) for address.
  name: Connected2fiber Address API
  slug: connected2fiber-address-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/rules/connected2fiber-rules.yml
  title: ''
  type: Spectral
  url: rules/connected2fiber-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/json-ld/connected2fiber-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/connected2fiber-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/vocabulary/connected2fiber-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/connected2fiber-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/data-model/connected2fiber-data-model.yml
  title: ''
  type: DataModel
  url: data-model/connected2fiber-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/conformance/connected2fiber-conformance.yml
  title: ''
  type: Conformance
  url: conformance/connected2fiber-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/well-known/connected2fiber-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connected2fiber-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/well-known/connected2fiber-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connected2fiber-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/well-known/connected2fiber-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connected2fiber-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/hosts/connected2fiber-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connected2fiber-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/vendors/connected2fiber-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connected2fiber-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectbase.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.jira.connectbase.com/servicedesk/customer/user/login?destination=portals
- group: operate
  title: ''
  type: StatusPage
  url: https://status.connectbase.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.connectbase.com/tcwlive/register/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.connectbase.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.connectbase.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.connectbase.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.connectbase.com/blog/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/cpq-getting-started
  title: ''
  type: GettingStarted
  url: /cpq-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.connectbase.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connected2fiber/refs/heads/main/security/connected2fiber-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connected2fiber-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connectbase.com
created: '2026-10-10'
description: Connectbase (formerly Connected2Fiber) provides a B2B SaaS platform for the connectivity industry, offering location intelligence, automated workflows, and a suite of tools such as Circuit Inventory Manager, IPAM, and spend optimization. The platform helps carriers, wholesale partners, and sales teams discover opportunities, quote, order, and manage network assets across the globe.
image: https://www.connectbase.com/wp-content/uploads/2022/02/Home-Hero-1024x704.png
json_schemas:
- name: PostAddressV5ValidateRequest
  property_count: 3
  slug: connected2fiber-post-address-v5-validate-request
jsonld:
- class_count: 1
  name: Connected2Fiber Context
  property_count: 3
  slug: connected2fiber-context
layout: provider
modified: '2026-10-10'
name: Connected2fiber
nav: Providers
network: true
overview: 'Connected2fiber is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Address API, and 1 more. Tagged areas include Connectivity, Software-as-a-Service, B2B, Platform, and Networks.


  The Connected2fiber catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Connected2fiber''s developer surface includes support, signup flow, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Connected2fiber API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: connected2fiber-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 28.6
    discoverability: 60.7
    operational_transparency: 15.8
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
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Connected2Fiber Domain Security
  slug: connected2fiber-domain-security
  summary_line: TLSv1.3 · DMARC
slug: connected2fiber
tags:
- Connectivity
- Software-as-a-Service
- B2B
- Platform
- Networks
website: https://www.connectbase.com
---
