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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Cyber Library providing access to its structured knowledge base.
  name: Cyber Library API
  slug: cyber-library-api
- description: 'Cyber Library API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cyber Library API
  slug: cyberlibrary-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/cyberlibrary-com/rules/cyberlibrary-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cyberlibrary-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cyberlibrary-com/json-ld/cyberlibrary-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cyberlibrary-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cyberlibrary-com/vocabulary/cyberlibrary-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cyberlibrary-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cyberlibrary-com/data-model/cyberlibrary-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cyberlibrary-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cyberlibrary-com/conformance/cyberlibrary-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cyberlibrary-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/cyberlibrary-com/hosts/cyberlibrary-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyberlibrary-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyberlibrary-com/vendors/cyberlibrary-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyberlibrary-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyberlibrary.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyberlibrary.com/en/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.cyberlibrary.com/en/docs
- group: auth
  href: https://artifacts.apis.io/cyberlibrary-com/security/cyberlibrary-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyberlibrary-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyberlibrary.com/
coverage:
  checked: '2026-11-05'
  detail: Docs are served as a large JavaScript application with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://www.cyberlibrary.com/en/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Cyber Library is a community‑maintained, structured knowledge base that provides a comprehensive learning path for cybersecurity. It offers six tracks covering fundamentals to advanced attacker mindset, organized as a single tree of interconnected topics. The platform aims to make cybersecurity education accessible and systematic for learners of all levels.
image: https://www.cyberlibrary.com/og.png?v=2
json_schemas:
- name: Post20RepositoriesAcmePaymentsApiDeployKeysRequest
  property_count: 2
  slug: cyberlibrary-com-post20-repositories-acme-payments-api-deploy-keys-request
- name: Put20RepositoriesAcmePaymentsApiAccessTokensRequest
  property_count: 2
  slug: cyberlibrary-com-put20-repositories-acme-payments-api-access-tokens-request
jsonld:
- class_count: 2
  name: Cyberlibrary Com Context
  property_count: 4
  slug: cyberlibrary-com-context
layout: provider
modified: '2026-11-04'
name: Cyber Library
nav: Providers
network: true
overview: 'Cyber Library is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Education, Knowledge Base, Community, and Open Source.


  The Cyber Library catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cyber Library''s developer surface includes documentation and 11 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Cyber Library API Rules
  rule_count: 35
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 2
  slug: cyberlibrary-com-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 19.4
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cyberlibrary Com Domain Security
  slug: cyberlibrary-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyberlibrary-com
tags:
- Cybersecurity
- Education
- Knowledge Base
- Community
- Open Source
- Company
website: https://cyberlibrary.com/
---
