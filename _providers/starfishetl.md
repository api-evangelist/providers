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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Technology Advisors API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Technology Advisors API
  slug: starfishetl-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/starfishetl/plans/starfishetl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/starfishetl-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/starfishetl/rules/starfishetl-rules.yml
  title: ''
  type: Spectral
  url: rules/starfishetl-rules.yml
- group: design
  href: https://artifacts.apis.io/starfishetl/json-ld/starfishetl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/starfishetl-context.jsonld
- group: design
  href: https://artifacts.apis.io/starfishetl/vocabulary/starfishetl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/starfishetl-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/starfishetl/data-model/starfishetl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/starfishetl-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.starfishetl.com/services/StarfishETL-Security
- group: design
  href: https://artifacts.apis.io/starfishetl/conformance/starfishetl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/starfishetl-conformance.yml
- group: other
  href: https://artifacts.apis.io/starfishetl/hosts/starfishetl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/starfishetl-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.starfishetl.com/portal/en/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starfishetl.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/starfishetl/security/starfishetl-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/starfishetl-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/starfishetl/security/starfishetl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starfishetl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.starfishetl.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.starfishetl.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.starfishetl.com/blog
coverage:
  checked: '2026-10-21'
  detail: The provider's documentation pages contain no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 404
    url: https://api.starfishetl.com/openapi.json
  - status: 404
    url: https://api.starfishetl.com/openapi.yaml
  - status: 404
    url: https://api.starfishetl.com/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Technology Advisors provides consulting and advisory services focused on technology strategy, digital transformation, and API integration for enterprises. The firm assists clients in evaluating, selecting, and implementing technology solutions, ensuring alignment with business goals and fostering innovation. Their expertise spans cloud services, data analytics, cybersecurity, and modern software development practices, helping organizations navigate complex technology landscapes and achieve operational excellence.
json_schemas:
- name: PostTokenRequest
  property_count: 3
  slug: starfishetl-post-token-request
- name: PostTokenResponse
  property_count: 3
  slug: starfishetl-post-token-response
jsonld:
- class_count: 2
  name: Starfishetl Context
  property_count: 6
  slug: starfishetl-context
layout: provider
modified: '2026-10-21'
name: Technology Advisors
nav: Providers
network: true
overview: 'Technology Advisors is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Technology, Advisory, and API Integration.


  The Technology Advisors catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Technology Advisors'' developer surface includes support, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Starfishetl Plans Pricing
  plan_count: 5
  slug: starfishetl-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Technology Advisors API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: starfishetl-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
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
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Starfishetl Domain Security
  slug: starfishetl-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: trust-center
  name: Starfishetl Trust Center
  slug: starfishetl-trust-center
  summary_line: GDPR
slug: starfishetl
tags:
- Company
- Consulting
- Technology
- Advisory
- API Integration
website: https://www.starfishetl.com/
---
