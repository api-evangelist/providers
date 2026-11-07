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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API integration for document workflows provided by airSlate's Altaflow platform.
  name: Altaflow API
  slug: altaflow-api-2
- description: 'airSlate API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: airSlate API
  slug: altaflow-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/altaflow/well-known/altaflow-updates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altaflow-updates-security.txt
- group: auth
  href: https://artifacts.apis.io/altaflow/well-known/altaflow-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altaflow-support-security.txt
- group: auth
  href: https://artifacts.apis.io/altaflow/well-known/altaflow-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altaflow-status-security.txt
- group: agent
  href: https://artifacts.apis.io/altaflow/well-known/altaflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altaflow-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/altaflow/plans/altaflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/altaflow-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/altaflow/rules/altaflow-rules.yml
  title: ''
  type: Spectral
  url: rules/altaflow-rules.yml
- group: design
  href: https://artifacts.apis.io/altaflow/json-ld/altaflow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/altaflow-context.jsonld
- group: design
  href: https://artifacts.apis.io/altaflow/vocabulary/altaflow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/altaflow-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/altaflow/data-model/altaflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/altaflow-data-model.yml
- group: design
  href: https://artifacts.apis.io/altaflow/conformance/altaflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altaflow-conformance.yml
- group: agent
  href: https://artifacts.apis.io/altaflow/llms/altaflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altaflow-llms.txt
- group: other
  href: https://artifacts.apis.io/altaflow/hosts/altaflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altaflow-hosts.yml
- group: other
  href: https://artifacts.apis.io/altaflow/vendors/altaflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altaflow-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.altaflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.altaflow.com/
- group: auth
  href: https://artifacts.apis.io/altaflow/security/altaflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altaflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altaflow.com/
- group: company
  title: ''
  type: Blog
  url: https://altaflow.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.airslate.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://altaflow.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.airslate.com/
- group: start
  title: ''
  type: SignUp
  url: https://my.altaflow.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altaflow.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altaflow.com/legal
coverage:
  checked: '2026-10-19'
  detail: The developer portal at https://developers.altaflow.com/docs provides HTML documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found.
  evidence:
  - status: 200
    url: https://developers.altaflow.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: airSlate, operating under the brand airSlate, provides a comprehensive no-code workflow automation platform that enables businesses to create, automate, and manage document workflows across various applications. The platform offers features such as drag-and-drop workflow builder, e-signature integration, document generation, and AI-powered data extraction, helping organizations streamline processes, reduce manual effort, and improve operational efficiency. airSlate serves a wide range of industries including finance, legal, HR, and sales, and emphasizes security, compliance, and scalability for enterprise customers.
image: https://altaflow.com/hubfs/altaFlow.png
json_schemas:
- name: PostV1OrganizationsOrgIdTemplatesRequest
  property_count: 2
  slug: altaflow-post-v1-organizations-org-id-templates-request
- name: PostV1OrganizationsOrgIdTemplatesTemplateIdDocumentgroupsReq
  property_count: 1
  slug: altaflow-post-v1-organizations-org-id-templates-template-id-documentgroups-req
- name: PostV1OrganizationsOrgIdTemplatesTemplateIdDocumentsRequest
  property_count: 3
  slug: altaflow-post-v1-organizations-org-id-templates-template-id-documents-request
jsonld:
- class_count: 3
  name: Altaflow Context
  property_count: 5
  slug: altaflow-context
layout: provider
modified: '2026-10-19'
name: airSlate
nav: Providers
network: true
overview: 'airSlate is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, No-Code, Workflows, and Document Management.


  The airSlate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  airSlate''s developer surface includes engineering blog, documentation, pricing, support, signup flow, and 19 more developer resources.'
plans:
- name: Altaflow Plans Pricing
  plan_count: 3
  slug: altaflow-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: airSlate API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: altaflow-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 13.1
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 37.8
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/altaflow/altaflow-2026-11-03T120736.png
security:
- kind: domain-security
  name: Altaflow Domain Security
  slug: altaflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altaflow
tags:
- Company
- Automation
- No-Code
- Workflows
- Document Management
website: https://altaflow.com/
---
