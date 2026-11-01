---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for managing domain registrations, DNS, and SSL provisioning.
  name: Kissdomain API
  slug: kissdomain-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/kissdomain/rules/kissdomain-rules.yml
  title: ''
  type: Spectral
  url: rules/kissdomain-rules.yml
- group: design
  href: https://artifacts.apis.io/kissdomain/json-ld/kissdomain-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kissdomain-context.jsonld
- group: design
  href: https://artifacts.apis.io/kissdomain/vocabulary/kissdomain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kissdomain-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/kissdomain/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kissdomain/data-model/kissdomain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kissdomain-data-model.yml
- group: design
  href: https://artifacts.apis.io/kissdomain/errors/kissdomain-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kissdomain-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kissdomain/conformance/kissdomain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kissdomain-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kissdomain/llms/kissdomain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kissdomain-llms.txt
- group: other
  href: https://artifacts.apis.io/kissdomain/hosts/kissdomain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kissdomain-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://kissdomain.de/tld-wiki/help/
- group: auth
  title: ''
  type: Security
  url: https://kissdomain.de/tld-wiki/security/
- group: company
  title: ''
  type: Newsroom
  url: https://kissdomain.de/tld-wiki/news/
- group: other
  title: ''
  type: Leadership
  url: https://kissdomain.de/tld-wiki/team/
- group: company
  title: ''
  type: Blog
  url: https://kissdomain.de/tld-wiki/blog/
- group: auth
  href: https://artifacts.apis.io/kissdomain/security/kissdomain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kissdomain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kissdomain.de/
coverage:
  checked: '2026-10-30'
  detail: API reference page https://kissdomain.de/api/ returns 403 Forbidden, indicating authentication is required.
  evidence:
  - status: 403
    url: https://kissdomain.de/api/
  reason: auth-required
  state: gated
created: '2026-10-30'
description: kissdomain is a Berlin‑based domain registration provider operating under 1blu business GmbH. It offers domain names for business customers with personal support, focusing on reliable DNS management, SSL provisioning, and flexible contract terms. The service targets enterprises seeking professional domain services, emphasizing security, local German support, and integration with 1blu’s broader hosting solutions.
image: https://kissdomain.de/kd/kissdomain-logo.svg
jsonld:
- class_count: 5
  name: Kissdomain Context
  property_count: 11
  slug: kissdomain-context
layout: provider
modified: '2026-10-30'
name: kissdomain
nav: Providers
network: true
overview: 'kissdomain publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Domain, Hosting, Business, Germany, and Provider.


  The kissdomain catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kissdomain''s developer surface includes support, engineering blog, and 14 more developer resources.'
plans:
- name: Kissdomain Plans Pricing
  plan_count: 0
  slug: kissdomain-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Kissdomain Rate Limits
  slug: kissdomain-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: kissdomain API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: kissdomain-rules
scopes:
- name: Kissdomain Scopes
  scope_count: 0
  slug: kissdomain-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 63.7
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 79.1
    contract_quality: 14.7
    developer_ergonomics: 13.6
    discoverability: 60.7
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kissdomain Authentication
  slug: kissdomain-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kissdomain Domain Security
  slug: kissdomain-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 5
skills:
- name: get-info
  slug: kissdomain-get-info
- name: get-tld
  slug: kissdomain-get-tld
- name: list-tlds
  slug: kissdomain-list-tlds
- name: smtp-check
  slug: kissdomain-smtp-check
- name: traceroute
  slug: kissdomain-traceroute
slug: kissdomain
tags:
- Domain
- Hosting
- Business
- Germany
- Provider
website: https://kissdomain.de/
---
