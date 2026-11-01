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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'eOne Solutions API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: eOne Solutions API
  slug: eonesolutions-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/eonesolutions/plans/eonesolutions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eonesolutions-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eonesolutions/rules/eonesolutions-rules.yml
  title: ''
  type: Spectral
  url: rules/eonesolutions-rules.yml
- group: design
  href: https://artifacts.apis.io/eonesolutions/json-ld/eonesolutions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eonesolutions-context.jsonld
- group: design
  href: https://artifacts.apis.io/eonesolutions/vocabulary/eonesolutions-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eonesolutions-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eonesolutions/data-model/eonesolutions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eonesolutions-data-model.yml
- group: design
  href: https://artifacts.apis.io/eonesolutions/conformance/eonesolutions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eonesolutions-conformance.yml
- group: other
  href: https://artifacts.apis.io/eonesolutions/hosts/eonesolutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eonesolutions-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eonesolutions
- group: auth
  href: https://artifacts.apis.io/eonesolutions/security/eonesolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eonesolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eonesolutions.com/
- group: company
  title: ''
  type: Blog
  url: https://www.eonesolutions.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eonesolutions.com/documentation/welcome-to-popdock-documentation/
- group: other
  title: ''
  type: SignIn
  url: https://www.eonesolutions.com/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eonesolutions.com/blog/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eonesolutions.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.eonesolutions.com/blog/register-soon-smartconnect-bootcamp-in-houston-in-january-2020/
- group: operate
  title: ''
  type: Support
  url: https://www.eonesolutions.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eonesolutions.com/terms-of-use/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.eonesolutions.com/trust-center/
coverage:
  checked: '2026-10-20'
  detail: Documentation pages are HTML with no machine‑readable OpenAPI/AsyncAPI spec discovered.
  evidence:
  - status: 200
    url: https://www.eonesolutions.com/documentation/welcome-to-popdock-documentation/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: eOne Solutions is the only no-code iPaaS that delivers virtual AND physical data integration. In the world of cloud apps and AI, both are vital. eOne provides a platform for seamless integration across systems, offering tools for data migration, reporting, and finance system integration, targeting enterprises seeking rapid, code‑free connectivity.
image: https://www.eonesolutions.com/wp-content/uploads/2023/11/eOne-Homepage-1024x549.webp
json_schemas:
- name: PostTokenResponse
  property_count: 2
  slug: eonesolutions-post-token-response
jsonld:
- class_count: 1
  name: Eonesolutions Context
  property_count: 2
  slug: eonesolutions-context
layout: provider
modified: '2026-10-20'
name: eOne Solutions
nav: Providers
network: true
overview: 'eOne Solutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, iPaaS, Integration, No-Code, and Enterprise.


  The eOne Solutions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  eOne Solutions'' developer surface includes engineering blog, documentation, pricing, signup flow, support, and 14 more developer resources.'
plans:
- name: Eonesolutions Plans Pricing
  plan_count: 3
  slug: eonesolutions-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: eOne Solutions API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: eonesolutions-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 18.3
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eonesolutions Domain Security
  slug: eonesolutions-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: eonesolutions
tags:
- Company
- iPaaS
- Integration
- No-Code
- Enterprise
website: https://eonesolutions.com/
---
