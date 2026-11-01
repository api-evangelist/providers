---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Domainee Dev Agentic Access
  operation_count: 51
  slug: domainee-dev-agentic-access
  summary_line: 51 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Verify that DNS records resolve to the expected values.
  name: domainee-dev DNS API
  slug: domainee-dev-dns-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Search, register, renew, and manage domains bought through Domainee.
  name: domainee-dev Domain purchases API
  slug: domainee-dev-domain-purchases-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Connect and verify your customers' custom domains.
  name: domainee-dev Domains API
  slug: domainee-dev-domains-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Keyless diagnostic lookups. No Authorization header required.
  name: domainee-dev Free tools API
  slug: domainee-dev-free-tools-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Prove to your origin that a request came through Domainee.
  name: domainee-dev Origin secret API
  slug: domainee-dev-origin-secret-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Generic workspace-scoped objects.
  name: domainee-dev Projects API
  slug: domainee-dev-projects-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Health and discovery endpoints.
  name: domainee-dev Service API
  slug: domainee-dev-service-api
- baseURL: https://api.domainee.dev
  baseurl_source: declared
  description: Subscribe to domain lifecycle events.
  name: domainee-dev Webhooks API
  slug: domainee-dev-webhooks-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/domainee-dev/agentic-access/domainee-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/domainee-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/domainee-dev/plans/domainee-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domainee-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/rules/domainee-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/domainee-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/json-ld/domainee-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domainee-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/domainee-dev/vocabulary/domainee-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domainee-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/domainee-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/data-model/domainee-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domainee-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/conventions/domainee-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/domainee-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/conventions/domainee-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/domainee-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/domainee-dev/authentication/domainee-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domainee-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/errors/domainee-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domainee-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domainee-dev/conformance/domainee-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domainee-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domainee-dev/llms/domainee-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domainee-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/domainee-dev/well-known/domainee-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domainee-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/domainee-dev/hosts/domainee-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainee-dev-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://domainee.dev/webhooks
- group: start
  title: ''
  type: Login
  url: https://domainee.dev/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://domainee.dev/developers
- group: auth
  href: https://artifacts.apis.io/domainee-dev/security/domainee-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainee-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domainee.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://domainee.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://domainee.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://domainee.dev/docs
- group: operate
  title: ''
  type: Support
  url: https://domainee.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://domainee.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://domainee.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domainee.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domainee.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CommonNinja
created: '2026-10-30'
description: Domainee provides a Custom Domains API for SaaS applications, enabling developers to let their users connect personal domains to their products with a single API call. The service offers automatic SSL certificates via Let’s Encrypt, supports up to 20 free domains and 100 GB of bandwidth per month, and includes features such as DNS verification, domain registration through Stripe, webhooks, and a native Model Context Protocol (MCP) server for AI‑driven management. Backed by Common Ninja, Domainee aims to simplify white‑label domain provisioning for developers worldwide.
image: https://domainee.dev/logo.png
json_schemas:
- name: DomainPurchase
  property_count: 20
  slug: domainee-dev-domain-purchase
- name: Domain
  property_count: 25
  slug: domainee-dev-domain
- name: PreflightWarning
  property_count: 5
  slug: domainee-dev-preflight-warning
- name: Project
  property_count: 8
  slug: domainee-dev-project
- name: Registrant
  property_count: 11
  slug: domainee-dev-registrant
- name: RegistrarDnsRecord
  property_count: 5
  slug: domainee-dev-registrar-dns-record
jsonld:
- class_count: 13
  name: Domainee Dev Context
  property_count: 76
  slug: domainee-dev-context
layout: provider
modified: '2026-10-30'
name: domainee-dev
nav: Providers
network: true
overview: 'domainee-dev publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including DNS API, Domain purchases API, Domains API, and 5 more. Tagged areas include API, SaaS, Custom-Domains, Free-Tier, and MCP.


  The domainee-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  domainee-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Domainee Dev Plans Pricing
  plan_count: 2
  slug: domainee-dev-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Domainee Dev Rate Limits
  slug: domainee-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: domainee-dev API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: domainee-dev-rules
scopes:
- name: Domainee Dev Scopes
  scope_count: 0
  slug: domainee-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 59.8
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 13.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Domainee Dev Authentication
  slug: domainee-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Domainee Dev Domain Security
  slug: domainee-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: create-domain
  slug: domainee-dev-create-domain
slug: domainee-dev
tags:
- API
- SaaS
- Custom-Domains
- Free-Tier
- MCP
website: https://domainee.dev/
---
