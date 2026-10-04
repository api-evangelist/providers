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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- baseURL: https://api.aspireapp.com
  baseurl_source: declared
  description: The Public API from Aspiresingapore — 3 operation(s) for public.
  name: Aspiresingapore Public API
  slug: aspiresingapore-public-api
artifact_total: 9
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/plans/aspiresingapore-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aspiresingapore-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/rules/aspiresingapore-rules.yml
  title: ''
  type: Spectral
  url: rules/aspiresingapore-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/json-ld/aspiresingapore-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aspiresingapore-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/vocabulary/aspiresingapore-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aspiresingapore-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/data-model/aspiresingapore-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aspiresingapore-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/authentication/aspiresingapore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aspiresingapore-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/conformance/aspiresingapore-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aspiresingapore-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/llms/aspiresingapore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aspiresingapore-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/well-known/aspiresingapore-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aspiresingapore-help-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/well-known/aspiresingapore-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aspiresingapore-app-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/well-known/aspiresingapore-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aspiresingapore-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/hosts/aspiresingapore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspiresingapore-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/vendors/aspiresingapore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aspiresingapore-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.aspireapp.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aspireapp.com/tnc/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://aspireapp.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://aspireapp.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://aspireapp.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.aspireapp.com/en/articles/15433833-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.aspireapp.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/scopes/aspiresingapore-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aspiresingapore-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspiresingapore/refs/heads/main/security/aspiresingapore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspiresingapore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aspireapp.com
coverage:
  checked: 2026-09-26
  detail: Documentation at https://docs.api.aspireapp.com returns HTML pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.api.aspireapp.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aspiresingapore provides a comprehensive financial platform for businesses in Singapore, offering multi‑currency accounts, corporate cards, expense management, payroll, and global payment solutions. Their API suite enables developers to integrate banking, accounting, and compliance features into SaaS products, automating finance operations and supporting growth across SMEs and larger enterprises.
image: https://cdn.prod.website-files.com/5ed5b60be1889f546024ada0/6a10208767972cc962cd715f_Website-Preview.webp
json_schemas:
- name: PostPublicV1LoginRequest
  property_count: 3
  slug: aspiresingapore-post-public-v1-login-request
- name: PostPublicV1LoginResponse
  property_count: 3
  slug: aspiresingapore-post-public-v1-login-response
jsonld:
- class_count: 2
  name: Aspiresingapore Context
  property_count: 6
  slug: aspiresingapore-context
layout: provider
modified: '2026-09-26'
name: Aspiresingapore
nav: Providers
network: true
overview: 'Aspiresingapore publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Finance, Banking, Singapore, and Software-as-a-Service.


  The Aspiresingapore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aspiresingapore''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Aspiresingapore Plans Pricing
  plan_count: 2
  slug: aspiresingapore-plans-pricing
random_paper: 6
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Aspiresingapore API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: aspiresingapore-rules
scopes:
- name: Aspiresingapore Scopes
  scope_count: 0
  slug: aspiresingapore-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 21.0
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aspiresingapore Authentication
  slug: aspiresingapore-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aspiresingapore Domain Security
  slug: aspiresingapore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aspiresingapore
tags:
- Finance
- Banking
- Singapore
- Software-as-a-Service
website: https://aspireapp.com
---
