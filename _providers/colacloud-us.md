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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Colacloud Us Agentic Access
  operation_count: 1
  slug: colacloud-us-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://app.colacloud.us/api/v1
  baseurl_source: declared
  description: Certificate of Label Approval operations
  name: COLA Cloud COLAs API
  slug: colacloud-us-colas-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/colacloud-us/agentic-access/colacloud-us-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/colacloud-us-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/colacloud-us/plans/colacloud-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/colacloud-us-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/colacloud-us/rules/colacloud-us-rules.yml
  title: ''
  type: Spectral
  url: rules/colacloud-us-rules.yml
- group: design
  href: https://artifacts.apis.io/colacloud-us/vocabulary/colacloud-us-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/colacloud-us-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/colacloud-us/cli/colacloud-us-cli.yml
  title: ''
  type: CLI
  url: cli/colacloud-us-cli.yml
- group: auth
  href: https://artifacts.apis.io/colacloud-us/authentication/colacloud-us-authentication.yml
  title: ''
  type: Authentication
  url: authentication/colacloud-us-authentication.yml
- group: design
  href: https://artifacts.apis.io/colacloud-us/conformance/colacloud-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/colacloud-us-conformance.yml
- group: agent
  href: https://artifacts.apis.io/colacloud-us/llms/colacloud-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/colacloud-us-llms.txt
- group: other
  href: https://artifacts.apis.io/colacloud-us/a2a/colacloud-us-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/colacloud-us-a2a.yml
- group: agent
  href: https://artifacts.apis.io/colacloud-us/well-known/colacloud-us-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/colacloud-us-well-known.yml
- group: other
  href: https://artifacts.apis.io/colacloud-us/hosts/colacloud-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colacloud-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/colacloud-us/vendors/colacloud-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/colacloud-us-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colacloud.us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colacloud.us/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://colacloud.us/pricing
- group: start
  title: ''
  type: Login
  url: https://app.colacloud.us/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cola-cloud-us
- group: company
  title: ''
  type: Blog
  url: https://colacloud.us/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.colacloud.us/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.colacloud.us/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.colacloud.us/api-reference/colas/search-colas
- group: auth
  href: https://artifacts.apis.io/colacloud-us/security/colacloud-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colacloud-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://colacloud.us/
created: '2026-11-04'
description: COLA Cloud provides searchable, enriched data on public alcohol label approvals from the U.S. Alcohol and Tobacco Tax and Trade Bureau (TTB). It aggregates millions of label records into an API, MCP, and data warehouse, enabling developers to query label information, integrate it into applications, and build compliance or analytics solutions. The platform offers a public web interface and programmatic access to facilitate product data discovery and regulatory compliance.
image: https://colacloud.us/static/images/marketing/cola-cloud-link-preview-202607.png
layout: provider
modified: '2026-11-04'
name: COLA Cloud
nav: Providers
network: true
overview: 'COLA Cloud publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: COLAs API. Tagged areas include Company, Data, Alcohol, Compliance, and Open Data.


  The COLA Cloud catalog on APIs.io includes 1 Spectral governance ruleset.


  COLA Cloud''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 16 more developer resources.'
plans:
- name: Colacloud Us Plans Pricing
  plan_count: 3
  slug: colacloud-us-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: COLA Cloud API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: colacloud-us-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 44.7
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Colacloud Us Authentication
  slug: colacloud-us-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Colacloud Us Domain Security
  slug: colacloud-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: colacloud-us
tags:
- Company
- Data
- Alcohol
- Compliance
- Open Data
website: https://colacloud.us/
---
