---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The NoctHost API provides REST endpoints for provisioning cloud servers, managing billing, and deploying resources across multiple providers. Documentation is at the API Docs page.
  name: NoctHost API
  slug: nocthost-api-2
- baseURL: https://api.nocthost.com
  baseurl_source: declared
  description: 'NoctHost API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: NoctHost API
  slug: nocthost-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/nocthost/plans/nocthost-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nocthost-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nocthost/rules/nocthost-rules.yml
  title: ''
  type: Spectral
  url: rules/nocthost-rules.yml
- group: design
  href: https://artifacts.apis.io/nocthost/json-ld/nocthost-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nocthost-context.jsonld
- group: design
  href: https://artifacts.apis.io/nocthost/vocabulary/nocthost-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nocthost-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nocthost/data-model/nocthost-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nocthost-data-model.yml
- group: auth
  href: https://artifacts.apis.io/nocthost/authentication/nocthost-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nocthost-authentication.yml
- group: design
  href: https://artifacts.apis.io/nocthost/conformance/nocthost-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nocthost-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nocthost/llms/nocthost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nocthost-llms.txt
- group: other
  href: https://artifacts.apis.io/nocthost/hosts/nocthost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nocthost-hosts.yml
- group: other
  href: https://artifacts.apis.io/nocthost/vendors/nocthost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nocthost-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nocthost/security/nocthost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nocthost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nocthost.com
- group: docs
  title: ''
  type: Documentation
  url: https://nocthost.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://nocthost.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nocthost.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nocthost.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nocthost.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://nocthost.com/register
- group: start
  title: ''
  type: Login
  url: https://nocthost.com/login
coverage:
  checked: '2026-11-02'
  detail: API documentation page is a JavaScript‑rendered SPA, no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://nocthost.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: NoctHost is a multi-cloud VPS and GPU service, paid in crypto or card and run by a small team of engineers. It offers hourly billing on top‑tier infrastructure from Vultr, DigitalOcean, Hetzner and Linode, with transparent pricing and open API for provisioning.
image: https://nocthost.com/opengraph-image
json_schemas:
- name: GetBackupsResponse
  property_count: 8
  slug: nocthost-get-backups-response
- name: PostBackupsIdRestoreRequest
  property_count: 2
  slug: nocthost-post-backups-id-restore-request
- name: PostBackupsIdRestoreResponse
  property_count: 2
  slug: nocthost-post-backups-id-restore-response
- name: PostServersBulkRequest
  property_count: 6
  slug: nocthost-post-servers-bulk-request
- name: PostServersIdRootPasswordResponse
  property_count: 3
  slug: nocthost-post-servers-id-root-password-response
- name: PostServersIdStartResponse
  property_count: 2
  slug: nocthost-post-servers-id-start-response
jsonld:
- class_count: 25
  name: Nocthost Context
  property_count: 25
  slug: nocthost-context
layout: provider
modified: '2026-11-02'
name: NoctHost
nav: Providers
network: true
overview: 'NoctHost is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VPS, Cloud, Crypto Payments, and GPU.


  The NoctHost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NoctHost''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Nocthost Plans Pricing
  plan_count: 8
  slug: nocthost-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: NoctHost API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: nocthost-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nocthost Authentication
  slug: nocthost-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Nocthost Domain Security
  slug: nocthost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nocthost
tags:
- Company
- VPS
- Cloud
- Crypto Payments
- GPU
website: https://nocthost.com
---
