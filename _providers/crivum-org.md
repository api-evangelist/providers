---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Crivum Org Agentic Access
  operation_count: 6
  slug: crivum-org-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://crivum.org
  baseurl_source: declared
  description: The Avaliacoes API from Crivum — 2 operation(s) for avaliacoes.
  name: Crivum Avaliacoes API
  slug: crivum-org-avaliacoes-api
- baseURL: https://crivum.org
  baseurl_source: declared
  description: The Criterios API from Crivum — 1 operation(s) for criterios.
  name: Crivum Criterios API
  slug: crivum-org-criterios-api
- baseURL: https://crivum.org
  baseurl_source: declared
  description: The Records API from Crivum — 1 operation(s) for records.
  name: Crivum Records API
  slug: crivum-org-records-api
- baseURL: https://crivum.org
  baseurl_source: declared
  description: The Saldo API from Crivum — 1 operation(s) for saldo.
  name: Crivum Saldo API
  slug: crivum-org-saldo-api
- baseURL: https://crivum.org
  baseurl_source: declared
  description: The Triagem API from Crivum — 1 operation(s) for triagem.
  name: Crivum Triagem API
  slug: crivum-org-triagem-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/crivum-org/agentic-access/crivum-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crivum-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crivum-org/rules/crivum-org-rules.yml
  title: ''
  type: Spectral
  url: rules/crivum-org-rules.yml
- group: design
  href: https://artifacts.apis.io/crivum-org/errors/crivum-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crivum-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crivum-org/conformance/crivum-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crivum-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crivum-org/llms/crivum-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crivum-org-llms.txt
- group: other
  href: https://artifacts.apis.io/crivum-org/hosts/crivum-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crivum-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/crivum-org/vendors/crivum-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crivum-org-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://crivum.org/login
- group: auth
  href: https://artifacts.apis.io/crivum-org/authentication/crivum-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crivum-org-authentication.yml
- group: auth
  href: https://artifacts.apis.io/crivum-org/security/crivum-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crivum-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crivum.org/
created: '2026-11-04'
description: Crivum offers a platform to submit your material and receive a rapid reading with type of work, estimated level, and findings. The full evaluation, using three reference models with editorial supervision, provides a score and transforms your work into a published, registered, and citable piece. This service enables authors to quickly assess and improve their submissions before formal presentation.
layout: provider
modified: '2026-11-04'
name: Crivum
nav: Providers
network: true
overview: 'Crivum publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Avaliacoes API, Criterios API, Records API, and 2 more. Tagged areas include Platform, Evaluation, Publishing, Artificial Intelligence, and Portuguese.


  The Crivum catalog on APIs.io includes 1 Spectral governance ruleset.


  Crivum''s developer surface includes authentication and 10 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Crivum API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: crivum-org-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 48.4
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 0.0
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
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crivum Org Authentication
  slug: crivum-org-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crivum Org Domain Security
  slug: crivum-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crivum-org
tags:
- Platform
- Evaluation
- Publishing
- Artificial Intelligence
- Portuguese
website: https://crivum.org/
---
