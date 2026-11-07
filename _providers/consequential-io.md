---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.consequential.io
  baseurl_source: declared
  description: 'Consequential API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Consequential API
  slug: consequential-io-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/consequential-io/plans/consequential-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consequential-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consequential-io/rules/consequential-io-rules.yml
  title: ''
  type: Spectral
  url: rules/consequential-io-rules.yml
- group: design
  href: https://artifacts.apis.io/consequential-io/json-ld/consequential-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/consequential-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/consequential-io/vocabulary/consequential-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/consequential-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/consequential-io/data-model/consequential-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consequential-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/consequential-io/authentication/consequential-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consequential-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/consequential-io/conformance/consequential-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consequential-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/consequential-io/llms/consequential-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consequential-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/consequential-io/mcp/consequential-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/consequential-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/consequential-io/well-known/consequential-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consequential-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/consequential-io/hosts/consequential-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consequential-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/consequential-io/vendors/consequential-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consequential-io-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://consequential.io/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://consequential.io/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.consequential.io/signup?utm_source=website&utm_medium=cta&utm_content=navbar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://consequential.io/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.consequential.io/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.consequential.io/guides/send-your-first-request/
- group: auth
  href: https://artifacts.apis.io/consequential-io/security/consequential-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consequential-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consequential.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.consequential.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.consequential.io/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://consequential.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://consequential.io/blog
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.consequential.io/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Consequential provides an AI‑powered revenue intelligence layer for eCommerce brands running ads at scale. It unifies paid media, store, and pixel data to surface leaks, attribute revenue, and recommend actions, promising $10K+ recoverable revenue in the first week or no charge. The platform serves D2C brands, agencies, and operators, backed by alumni from PayPal, eBay, and Target, handling over $15B GMV.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/0ed465d4-46c2-4dfd-a114-5e2e0209497d/id-preview-0c315b68--7cf336c6-7ef8-418f-a45b-e283331c5706.lovable.app-1781104814105.png
json_schemas:
- name: GetPartnerDataAcquisitionViewResponse
  property_count: 3
  slug: consequential-io-get-partner-data-acquisition-view-response
- name: PostPartnerConnectRequest
  property_count: 3
  slug: consequential-io-post-partner-connect-request
- name: PostPartnerConnectResponse
  property_count: 7
  slug: consequential-io-post-partner-connect-response
- name: PostV190AudienceidUsersRequest
  property_count: 2
  slug: consequential-io-post-v190-audienceid-users-request
jsonld:
- class_count: 4
  name: Consequential Io Context
  property_count: 14
  slug: consequential-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at consequential.io.
  name: Consequential MCP Server
  slug: consequential-io-mcp-yml
modified: '2026-11-04'
name: Consequential
nav: Providers
network: true
overview: 'Consequential is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, E-Commerce, Revenue Intelligence, and Software-as-a-Service.


  The Consequential catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Consequential''s developer surface includes authentication, signup flow, changelog, getting-started guide, documentation, API reference, pricing, and 17 more developer resources.'
plans:
- name: Consequential Io Plans Pricing
  plan_count: 4
  slug: consequential-io-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Consequential API Rules
  rule_count: 45
  severity_counts:
    error: 41
    hint: 0
    info: 3
    warn: 1
  slug: consequential-io-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Consequential Io Authentication
  slug: consequential-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Consequential Io Domain Security
  slug: consequential-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consequential-io
tags:
- Artificial Intelligence
- Advertising
- E-Commerce
- Revenue Intelligence
- Software-as-a-Service
website: https://consequential.io/
---
