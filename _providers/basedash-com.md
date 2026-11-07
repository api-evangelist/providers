---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Basedash provides an AI‑powered analytics platform with a developer API documented at the public docs site.
  name: Basedash API
  slug: basedash-api
- baseURL: https://charts.basedash.com
  baseurl_source: declared
  description: 'Basedash API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Basedash API
  slug: basedash-com-api
artifact_total: 13
common:
- group: start
  title: ''
  type: Login
  url: https://charts.basedash.com/login
- group: commercial
  href: https://artifacts.apis.io/basedash-com/plans/basedash-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/basedash-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/basedash-com/rules/basedash-com-rules.yml
  title: ''
  type: Spectral
  url: rules/basedash-com-rules.yml
- group: design
  href: https://artifacts.apis.io/basedash-com/json-ld/basedash-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/basedash-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/basedash-com/vocabulary/basedash-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/basedash-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/basedash-com/data-model/basedash-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/basedash-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/basedash-com/changelog/basedash-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/basedash-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.basedash.com/security
- group: design
  href: https://artifacts.apis.io/basedash-com/conformance/basedash-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basedash-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basedash-com/llms/basedash-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basedash-com-llms.txt
- group: other
  href: https://artifacts.apis.io/basedash-com/a2a/basedash-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/basedash-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/basedash-com/well-known/basedash-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basedash-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/basedash-com/hosts/basedash-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basedash-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/basedash-com/vendors/basedash-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basedash-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.basedash.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Basedash
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.basedash.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.basedash.com/docs/getting-started/welcome
- group: auth
  href: https://artifacts.apis.io/basedash-com/security/basedash-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/basedash-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/basedash-com/security/basedash-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basedash-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basedash.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.basedash.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.basedash.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.basedash.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.basedash.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.basedash.com/privacy-policy
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public documentation pages.
  evidence:
  - status: 200
    url: https://www.basedash.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Basedash provides AI‑powered analytics platform that lets users ask natural‑language questions and get live dashboards, data warehouse, and AI models. It offers features like AI Data Analyst, self‑serve answers, dashboards from prompts, managed data warehouse, data ingestion from 750+ sources, embedding analytics, insights, anomaly detection, and an MCP server for AI agents. The company focuses on delivering semantic layer and context engine for modern AI‑driven decision making.
image: https://www.basedash.com/og/home.png
json_schemas:
- name: GetApiPublicBillingAccountsBillingaccountidOrganizationsOrgi
  property_count: 1
  slug: basedash-com-get-api-public-billing-accounts-billingaccountid-organizations-orgi
- name: GetApiPublicBillingAccountsResponse
  property_count: 2
  slug: basedash-com-get-api-public-billing-accounts-response
- name: PostApiPublicMcpRequest
  property_count: 1
  slug: basedash-com-post-api-public-mcp-request
- name: PostApiPublicOrganizationsOrgidAutomationsIdRunsResponse
  property_count: 6
  slug: basedash-com-post-api-public-organizations-orgid-automations-id-runs-response
- name: PostApiPublicOrganizationsResponse
  property_count: 1
  slug: basedash-com-post-api-public-organizations-response
- name: PostPngResponse
  property_count: 1
  slug: basedash-com-post-png-response
jsonld:
- class_count: 7
  name: Basedash Com Context
  property_count: 10
  slug: basedash-com-context
layout: provider
modified: '2026-11-02'
name: Basedash
nav: Providers
network: true
overview: 'Basedash is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Data, Platform, and Basedash.


  The Basedash catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Basedash''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Basedash Com Plans Pricing
  plan_count: 2
  slug: basedash-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Basedash API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: basedash-com-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Basedash Com Domain Security
  slug: basedash-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Basedash Com Trust Center
  slug: basedash-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: basedash-com
tags:
- Artificial Intelligence
- Analytics
- Data
- Platform
- Basedash
website: https://basedash.com/
---
