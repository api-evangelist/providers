---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pluga Agentic Access
  operation_count: 12
  slug: pluga-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 1
apis:
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: The Actions API from Pluga — 4 operation(s) for actions.
  name: Pluga Actions API
  slug: pluga-actions-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: The BasicInfo API from Pluga — 2 operation(s) for basicinfo.
  name: Pluga Basic Info API
  slug: pluga-basicinfo-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: The Helpers API from Pluga — 1 operation(s) for helpers.
  name: Pluga Helpers API
  slug: pluga-helpers-api
- baseURL_template: '{server}'
  baseurl_source: spec_template
  description: The Triggers API from Pluga — 5 operation(s) for triggers.
  name: Pluga Triggers API
  slug: pluga-triggers-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/pluga/agentic-access/pluga-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pluga-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/pluga/rules/pluga-rules.yml
  title: ''
  type: Spectral
  url: rules/pluga-rules.yml
- group: design
  href: https://artifacts.apis.io/pluga/json-ld/pluga-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pluga-context.jsonld
- group: design
  href: https://artifacts.apis.io/pluga/vocabulary/pluga-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pluga-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pluga/data-model/pluga-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pluga-data-model.yml
- group: design
  href: https://artifacts.apis.io/pluga/conventions/pluga-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pluga-conventions.yml
- group: auth
  href: https://artifacts.apis.io/pluga/authentication/pluga-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pluga-authentication.yml
- group: design
  href: https://artifacts.apis.io/pluga/errors/pluga-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pluga-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pluga/conformance/pluga-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pluga-conformance.yml
- group: other
  href: https://artifacts.apis.io/pluga/overlays/pluga-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/pluga-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/pluga/llms/pluga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pluga-llms.txt
- group: other
  href: https://artifacts.apis.io/pluga/hosts/pluga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pluga-hosts.yml
- group: other
  href: https://artifacts.apis.io/pluga/vendors/pluga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pluga-vendors.yml
- group: auth
  href: https://artifacts.apis.io/pluga/security/pluga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pluga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pluga.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pluga.co/integre-sua-empresa/
- group: docs
  title: ''
  type: Documentation
  url: https://pluga.co/integre-sua-empresa/
- group: docs
  title: ''
  type: APIReference
  url: https://pluga.co/integre-sua-empresa/
- group: start
  title: ''
  type: GettingStarted
  url: https://pluga.co/integre-sua-empresa/
- group: operate
  title: ''
  type: Support
  url: https://pluga.zendesk.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://blog.pluga.co
- group: commercial
  title: ''
  type: Pricing
  url: https://pluga.co/precos/
created: '2026-10-21'
description: Pluga is a Brazilian automation platform that enables businesses to connect apps and automate workflows without code. It offers a visual builder, scheduling, data formatting, routing, looping, delays, code execution, and webhooks to integrate over 130 tools. Users can create custom automations, leverage AI toolkits, and manage integrations through a unified dashboard, helping teams streamline processes and improve efficiency.
image: https://assets.pluga.co/pluga-og.png
jsonld:
- class_count: 10
  name: Pluga Context
  property_count: 25
  slug: pluga-context
layout: provider
modified: '2026-10-21'
name: Pluga
nav: Providers
network: true
overview: 'Pluga publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Basic Info API, Helpers API, and 1 more. Tagged areas include Company, Automation, Integration, No-Code, and Brazil.


  The Pluga catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pluga''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Pluga API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: pluga-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 50.3
    developer_ergonomics: 34.5
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pluga/pluga-2026-11-03T141312.png
security:
- kind: authentication
  name: Pluga Authentication
  slug: pluga-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pluga Domain Security
  slug: pluga-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pluga
tags:
- Company
- Automation
- Integration
- No-Code
- Brazil
website: https://pluga.co/
---
