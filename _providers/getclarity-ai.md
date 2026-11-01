---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Getclarity Ai Agentic Access
  operation_count: 4
  slug: getclarity-ai-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL_template: https://api.getclarity.ai/{version}
  baseurl_source: spec_template
  description: The Media Statement API from Clarity — 2 operation(s) for media statement.
  name: Clarity Media Statement API
  slug: getclarity-ai-media-statement-api
- baseURL_template: https://api.getclarity.ai/{version}
  baseurl_source: spec_template
  description: The Users API from Clarity — 1 operation(s) for users.
  name: Clarity Users API
  slug: getclarity-ai-users-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/getclarity-ai/agentic-access/getclarity-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getclarity-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/getclarity-ai/rules/getclarity-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/getclarity-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/getclarity-ai/json-ld/getclarity-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getclarity-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/getclarity-ai/vocabulary/getclarity-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getclarity-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getclarity-ai/data-model/getclarity-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getclarity-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/getclarity-ai/authentication/getclarity-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getclarity-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/getclarity-ai/errors/getclarity-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getclarity-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getclarity-ai/conformance/getclarity-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getclarity-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getclarity-ai/llms/getclarity-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getclarity-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/getclarity-ai/hosts/getclarity-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getclarity-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/getclarity-ai/vendors/getclarity-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getclarity-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.getclarity.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getclarity.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://clarityai.readme.io/reference/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.getclarity.ai/
- group: auth
  href: https://artifacts.apis.io/getclarity-ai/security/getclarity-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getclarity-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getclarity.ai/
created: '2026-10-21'
description: Clarity provides an end‑to‑end platform that protects organizations’ hiring and onboarding processes from fraud. The solution combines application verification, AI deepfake detection, identity confirmation and proxy‑identity detection to secure candidates and employees throughout the talent acquisition lifecycle. It is sold to companies that need to verify the authenticity of hires and prevent hiring fraud.
image: https://cdn.prod.website-files.com/675ab8df2b03654f8aad5a6e/6882258cd8c20471cdbe7745_OpenGraph-home.jpg
jsonld:
- class_count: 21
  name: Getclarity Ai Context
  property_count: 54
  slug: getclarity-ai-context
layout: provider
modified: '2026-10-21'
name: Clarity
nav: Providers
network: true
overview: 'Clarity publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Media Statement API and Users API. Tagged areas include Hiring fraud, Identity verification, Deepfake detection, Talent acquisition security, and AI hiring security.


  The Clarity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clarity''s developer surface includes authentication, API reference, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Clarity API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: getclarity-ai-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 22.0
    contract_quality: 53.1
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getclarity Ai Authentication
  slug: getclarity-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Getclarity Ai Domain Security
  slug: getclarity-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getclarity-ai
tags:
- Hiring fraud
- Identity verification
- Deepfake detection
- Talent acquisition security
- AI hiring security
website: https://www.getclarity.ai/
---
