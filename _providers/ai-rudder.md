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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.airudder.com
  baseurl_source: declared
  description: 'AI Rudder API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: AI Rudder API
  slug: ai-rudder-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ai-rudder/rules/ai-rudder-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-rudder-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-rudder/json-ld/ai-rudder-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ai-rudder-context.jsonld
- group: design
  href: https://artifacts.apis.io/ai-rudder/vocabulary/ai-rudder-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-rudder-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ai-rudder/data-model/ai-rudder-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-rudder-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ai-rudder/authentication/ai-rudder-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai-rudder-authentication.yml
- group: design
  href: https://artifacts.apis.io/ai-rudder/conformance/ai-rudder-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-rudder-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-rudder/llms/ai-rudder-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-rudder-llms.txt
- group: other
  href: https://artifacts.apis.io/ai-rudder/hosts/ai-rudder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-rudder-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-rudder/vendors/ai-rudder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-rudder-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airudder.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airudder.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://airudder.com/news/voicegpt-launched-pioneering-ai-powered-customer-service/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.airudder.com/
- group: company
  title: ''
  type: Blog
  url: https://airudder.com/Blog
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.airudder.com/doc-1918333
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.airudder.com/
- group: auth
  href: https://artifacts.apis.io/ai-rudder/security/ai-rudder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-rudder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airudder.com/
coverage:
  checked: '2026-10-25'
  detail: No public API documentation or machine-readable contract was found on ai-rudder.com.
  evidence:
  - status: 404
    url: https://ai-rudder.com/developers
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: AI Rudder provides AI-powered voice and chat agents, botlab, omnichannel solutions, and industry-specific AI services for banking, insurance, logistics, and more. Their platform enables enterprises to deploy conversational AI for customer service, quality assurance, and compliance, offering customizable agents and integration tools.
json_schemas:
- name: GetServiceCloudIcDetailResponse
  property_count: 12
  slug: ai-rudder-get-service-cloud-ic-detail-response
- name: GetServiceCloudWorkflowInstancelistResponse
  property_count: 3
  slug: ai-rudder-get-service-cloud-workflow-instancelist-response
- name: GetServiceCloudWorkflowNodetasklistResponse
  property_count: 3
  slug: ai-rudder-get-service-cloud-workflow-nodetasklist-response
- name: GetServiceCloudWorkflowTemplatelistResponse
  property_count: 3
  slug: ai-rudder-get-service-cloud-workflow-templatelist-response
- name: PostServiceCloudWorkflowUpdatedetailsRequest
  property_count: 2
  slug: ai-rudder-post-service-cloud-workflow-updatedetails-request
- name: PostServiceCloudWorkflowUploaddetailsRequest
  property_count: 2
  slug: ai-rudder-post-service-cloud-workflow-uploaddetails-request
jsonld:
- class_count: 27
  name: Ai Rudder Context
  property_count: 23
  slug: ai-rudder-context
layout: provider
modified: '2026-10-25'
name: AI Rudder
nav: Providers
network: true
overview: 'AI Rudder is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, ConversationalAI, Enterprise, Automation, and Platform.


  The AI Rudder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Rudder''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AI Rudder API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: ai-rudder-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 26.3
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai Rudder Authentication
  slug: ai-rudder-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ai Rudder Domain Security
  slug: ai-rudder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ai-rudder
tags:
- AI
- ConversationalAI
- Enterprise
- Automation
- Platform
website: https://airudder.com/
---
