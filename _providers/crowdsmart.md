---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://csgcip.onrender.com
  baseurl_source: spec
  description: API for CrowdSmart Labs platform, providing trust layer for AI collective intelligence.
  name: CrowdSmart API
  slug: crowdsmart-api
- baseURL: https://csgcip.onrender.com
  baseurl_source: declared
  description: The Agents API from CrowdSmart — 2 operation(s) for agents.
  name: CrowdSmart Agents API
  slug: crowdsmart-agents-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/crowdsmart/rules/crowdsmart-rules.yml
  title: ''
  type: Spectral
  url: rules/crowdsmart-rules.yml
- group: design
  href: https://artifacts.apis.io/crowdsmart/json-ld/crowdsmart-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crowdsmart-context.jsonld
- group: design
  href: https://artifacts.apis.io/crowdsmart/vocabulary/crowdsmart-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crowdsmart-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crowdsmart/data-model/crowdsmart-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crowdsmart-data-model.yml
- group: design
  href: https://artifacts.apis.io/crowdsmart/conformance/crowdsmart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crowdsmart-conformance.yml
- group: other
  href: https://artifacts.apis.io/crowdsmart/hosts/crowdsmart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdsmart-hosts.yml
- group: other
  href: https://artifacts.apis.io/crowdsmart/vendors/crowdsmart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdsmart-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.crowdsmart.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crowdsmart
- group: auth
  href: https://artifacts.apis.io/crowdsmart/security/crowdsmart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdsmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdsmart.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crowdsmart.ai/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://csgcip.onrender.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://csgcip.onrender.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://crowdsmart.ai/developers.html
coverage:
  checked: '2026-10-11'
  detail: OpenAPI endpoint returns HTML SPA instead of a machine‑readable spec
  evidence:
  - status: 200
    url: https://app.crowdsmart.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: CrowdSmart Labs provides a trust layer for human and AI collective intelligence, offering products such as Collective Reasoning Foresight, Knowledge Agent, and Collective IQ. The platform enables organizations to build auditable, transparent AI reasoning with confidence scores, provenance, and a full audit trail, addressing governance challenges of AI deployment.
json_schemas:
- name: PostApiAgentsIdIdidRequest
  property_count: 2
  slug: crowdsmart-post-api-agents-id-idid-request
- name: PostApiAgentsRequest
  property_count: 2
  slug: crowdsmart-post-api-agents-request
jsonld:
- class_count: 2
  name: Crowdsmart Context
  property_count: 4
  slug: crowdsmart-context
layout: provider
modified: '2026-10-11'
name: CrowdSmart
nav: Providers
network: true
overview: 'CrowdSmart is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Agents API, and 1 more. Tagged areas include Artificial Intelligence, Governance, TrustLayer, Collective Intelligence, and Platform.


  The CrowdSmart catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CrowdSmart''s developer surface includes engineering blog, documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CrowdSmart API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: crowdsmart-rules
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 20.2
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 20.7
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/crowdsmart/crowdsmart-2026-11-03T125657.png
security:
- kind: domain-security
  name: Crowdsmart Domain Security
  slug: crowdsmart-domain-security
  summary_line: TLSv1.3
slug: crowdsmart
tags:
- Artificial Intelligence
- Governance
- TrustLayer
- Collective Intelligence
- Platform
website: https://crowdsmart.ai/
---
