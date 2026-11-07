---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation is presented via a JavaScript-rendered page that cannot be parsed for a machine-readable contract.
  name: DNS Spy API
  slug: dns-spy-api
- description: 'DNS Spy API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DNS Spy API
  slug: dnsspy-io-api
artifact_total: 8
asyncapis:
- description: ''
  name: Dnsspy Io Webhooks
  slug: dnsspy-io-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/dnsspy-io/plans/dnsspy-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dnsspy-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dnsspy-io/rules/dnsspy-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dnsspy-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dnsspy-io/json-ld/dnsspy-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dnsspy-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dnsspy-io/vocabulary/dnsspy-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dnsspy-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dnsspy-io/asyncapi/dnsspy-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dnsspy-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dnsspy-io/data-model/dnsspy-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dnsspy-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dnsspy-io/changelog/dnsspy-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dnsspy-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/dnsspy-io/conformance/dnsspy-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dnsspy-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dnsspy-io/well-known/dnsspy-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dnsspy-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dnsspy-io/hosts/dnsspy-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dnsspy-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dnsspy-io/vendors/dnsspy-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dnsspy-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dnsspy.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dnsspy.io/pricing
- group: start
  title: ''
  type: Login
  url: https://dnsspy.io/app/login
- group: docs
  title: ''
  type: Documentation
  url: https://dnsspy.io/docs/api
- group: operate
  title: ''
  type: ChangeLog
  url: https://dnsspy.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://dnsspy.io/blog
- group: auth
  href: https://artifacts.apis.io/dnsspy-io/security/dnsspy-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dnsspy-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dnsspy.io/
- group: other
  title: ''
  type: Image
  url: https://dnsspy.io/img/asset/YmxvZy9kbnNzcHlfbG9nb19zaW5nbGUucG5n/dnsspy_logo_single.png?p=seo_pro_og&s=92781fcba8f49969f2a24870fbd1fa73
coverage:
  checked: '2026-11-05'
  detail: API docs page is a JavaScript shell that blocks parsing of a machine‑readable contract.
  evidence:
  - status: 200
    url: https://dnsspy.io/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DNS Spy provides DNS monitoring, domain security, and API access for individuals and managed service providers. It watches DNS records worldwide, tracks domain and SSL expirations, audits security, and protects brands from phishing. Features include free tools, learning resources, and a 7‑day free trial for MSPs.
image: https://dnsspy.io/img/asset/YmxvZy9kbnNzcHlfbG9nb19zaW5nbGUucG5n/dnsspy_logo_single.png?p=seo_pro_og&s=92781fcba8f49969f2a24870fbd1fa73
json_schemas:
- name: PostApiV1DomainsRequest
  property_count: 2
  slug: dnsspy-io-post-api-v1-domains-request
jsonld:
- class_count: 1
  name: Dnsspy Io Context
  property_count: 2
  slug: dnsspy-io-context
layout: provider
modified: '2026-11-05'
name: DNS Spy
nav: Providers
network: true
overview: 'DNS Spy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DNS, Monitoring, Security, and MSP.


  The DNS Spy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DNS Spy''s developer surface includes changelog, pricing, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Dnsspy Io Plans Pricing
  plan_count: 2
  slug: dnsspy-io-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: DNS Spy API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: dnsspy-io-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.2
    catalog_earned_first_party: 8.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 25.4
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 23.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dnsspy Io Domain Security
  slug: dnsspy-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dnsspy-io
tags:
- DNS
- Monitoring
- Security
- MSP
website: https://dnsspy.io/
---
