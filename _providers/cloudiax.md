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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cloudiax/llms/cloudiax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudiax-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloudiax/well-known/cloudiax-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudiax-well-known.yml
- group: other
  href: https://artifacts.apis.io/cloudiax/hosts/cloudiax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudiax-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.cloudiax.com/register-for-infos/
- group: auth
  href: https://artifacts.apis.io/cloudiax/security/cloudiax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudiax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudiax.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudiax.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.cloudiax.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.cloudiax.com/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudiax.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudiax.com/price-list/
coverage:
  checked: '2026-10-20'
  detail: The website loads HTML but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found at common locations.
  evidence:
  - status: 200
    url: https://www.cloudiax.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Cloudiax provides cloud hosting, infrastructure, AI services, and ERP solutions for businesses. Their platform offers customizable SAP Business One cloud deployments, AI integration layers, and a suite of applications for manufacturing, logistics, and document management. The company targets enterprises seeking scalable, secure cloud environments with advanced AI and ERP capabilities, delivering flexible pricing and extensive support.
image: https://www.cloudiax.com/wp-content/uploads/sites/38/2026/02/26-WP-background-SM-1200-x-627.jpg
layout: provider
modified: '2026-10-20'
name: Cloudiax
nav: Providers
network: true
overview: 'Cloudiax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Hosting, Artificial Intelligence, ERP, and Enterprise.


  Cloudiax''s developer surface includes signup flow, engineering blog, support, pricing, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloudiax/cloudiax-2026-11-03T124518.png
security:
- kind: domain-security
  name: Cloudiax Domain Security
  slug: cloudiax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudiax
tags:
- Cloud
- Hosting
- Artificial Intelligence
- ERP
- Enterprise
website: https://cloudiax.com/
---
