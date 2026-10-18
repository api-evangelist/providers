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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://api.useburrow.com
  baseurl_source: declared
  description: The Events API from Burrow — 2 operation(s) for events.
  name: Burrow Events API
  slug: burrow-events-api
- baseURL: https://api.useburrow.com
  baseurl_source: declared
  description: The Mcp API from Burrow — 1 operation(s) for mcp.
  name: Burrow MCP API
  slug: burrow-mcp-api
artifact_total: 9
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/plans/burrow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/burrow-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/rules/burrow-rules.yml
  title: ''
  type: Spectral
  url: rules/burrow-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/json-ld/burrow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/burrow-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/vocabulary/burrow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/burrow-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/data-model/burrow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/burrow-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/changelog/burrow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/burrow-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/conventions/burrow-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/burrow-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/conventions/burrow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/burrow-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/authentication/burrow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/burrow-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/conformance/burrow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/burrow-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/llms/burrow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/burrow-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/hosts/burrow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/burrow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/vendors/burrow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/burrow-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useburrow.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.useburrow.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useburrow.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://useburrow.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://useburrow.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://useburrow.com/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/burrow/refs/heads/main/security/burrow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/burrow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://useburrow.com/
coverage:
  checked: '2026-10-06'
  detail: Burrow's developer docs render via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://useburrow.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Burrow provides a client reporting and operations platform for web agencies, offering an event‑driven orchestration layer that ingests data from tools like WordPress, Shopify, Stripe, and many others. It supplies SDKs, plugins, and a JSON‑RPC MCP for AI agents to automate agency workflows, generate reports, and query analytics. The platform is self‑funded, independent, and built for long‑term agency operations.
image: https://useburrow.com/images/og-home.jpg
json_schemas:
- name: PostApiV1EventsRequest
  property_count: 7
  slug: burrow-post-api-v1-events-request
- name: PostV1EventsRequest
  property_count: 4
  slug: burrow-post-v1-events-request
jsonld:
- class_count: 2
  name: Burrow Context
  property_count: 10
  slug: burrow-context
layout: provider
modified: '2026-10-06'
name: Burrow
nav: Providers
network: true
overview: 'Burrow is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Events API and MCP API. Tagged areas include Company, Software-as-a-Service, Reporting, and Automation.


  The Burrow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Burrow''s developer surface includes changelog, authentication, signup flow, pricing, getting-started guide, and 16 more developer resources.'
plans:
- name: Burrow Plans Pricing
  plan_count: 1
  slug: burrow-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Burrow API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: burrow-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 8.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Burrow Authentication
  slug: burrow-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Burrow Domain Security
  slug: burrow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: burrow
tags:
- Company
- Software-as-a-Service
- Reporting
- Automation
website: https://useburrow.com/
---
