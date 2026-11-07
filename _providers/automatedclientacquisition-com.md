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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Platform for cold email, LinkedIn campaigns, Microsoft 365 automation, content creation and lead capture.
  name: Automated Client Acquisition API
  slug: automated-client-acquisition-api
- description: 'Automated Client Acquisition API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Automated Client Acquisition API
  slug: automatedclientacquisition-com-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/automatedclientacquisition-com/plans/automatedclientacquisition-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/automatedclientacquisition-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/automatedclientacquisition-com/rules/automatedclientacquisition-com-rules.yml
  title: ''
  type: Spectral
  url: rules/automatedclientacquisition-com-rules.yml
- group: design
  href: https://artifacts.apis.io/automatedclientacquisition-com/json-ld/automatedclientacquisition-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/automatedclientacquisition-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/automatedclientacquisition-com/vocabulary/automatedclientacquisition-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/automatedclientacquisition-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/automatedclientacquisition-com/data-model/automatedclientacquisition-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/automatedclientacquisition-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/automatedclientacquisition-com/conformance/automatedclientacquisition-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automatedclientacquisition-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/automatedclientacquisition-com/llms/automatedclientacquisition-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automatedclientacquisition-com-llms.txt
- group: other
  href: https://artifacts.apis.io/automatedclientacquisition-com/hosts/automatedclientacquisition-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automatedclientacquisition-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/automatedclientacquisition-com/vendors/automatedclientacquisition-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automatedclientacquisition-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.automatedclientacquisition.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.automatedclientacquisition.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.automatedclientacquisition.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.automatedclientacquisition.com/blog
- group: auth
  href: https://artifacts.apis.io/automatedclientacquisition-com/security/automatedclientacquisition-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automatedclientacquisition-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.automatedclientacquisition.com/
coverage:
  checked: '2026-11-02'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://www.automatedclientacquisition.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Automated Client Acquisition provides a platform to run cold email and LinkedIn campaigns, manage Microsoft 365 infrastructure, create content and capture leads. Priced at $67 per month, it offers a one‑stop solution for lead generation and workflow automation, integrating with various APIs to extend functionality.
image: https://www.automatedclientacquisition.com/og-image-v2.png
json_schemas:
- name: DeleteV1ContactsResponse
  property_count: 3
  slug: automatedclientacquisition-com-delete-v1-contacts-response
- name: PatchV1ContactsIdRequest
  property_count: 1
  slug: automatedclientacquisition-com-patch-v1-contacts-id-request
- name: PatchV1ContactsIdResponse
  property_count: 2
  slug: automatedclientacquisition-com-patch-v1-contacts-id-response
jsonld:
- class_count: 3
  name: Automatedclientacquisition Com Context
  property_count: 5
  slug: automatedclientacquisition-com-context
layout: provider
modified: '2026-11-02'
name: Automated Client Acquisition
nav: Providers
network: true
overview: 'Automated Client Acquisition is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cold Email, LinkedIn Outreach, Lead Generation, Marketing Automation, and Content farming.


  The Automated Client Acquisition catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Automated Client Acquisition''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Automatedclientacquisition Com Plans Pricing
  plan_count: 2
  slug: automatedclientacquisition-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Automated Client Acquisition API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: automatedclientacquisition-com-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 24.1
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automatedclientacquisition Com Domain Security
  slug: automatedclientacquisition-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: automatedclientacquisition-com
tags:
- Cold Email
- LinkedIn Outreach
- Lead Generation
- Marketing Automation
- Content farming
- Email Infrastructure
- AI Agents
website: https://www.automatedclientacquisition.com/
---
