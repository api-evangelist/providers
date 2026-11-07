---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Domaincanary Com Agentic Access
  operation_count: 2
  slug: domaincanary-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Check a domain's email authentication and test SPF changes, with no key.
  name: DomainCanary Free API
  slug: domaincanary-free-api
- baseURL: https://domaincanary.com
  baseurl_source: declared
  description: The C API from DomainCanary — 1 operation(s) for c.
  name: DomainCanary C API
  slug: domaincanary-com-c-api
- baseURL: https://domaincanary.com
  baseurl_source: declared
  description: The Spf Preflight API from DomainCanary — 1 operation(s) for spf preflight.
  name: DomainCanary Spf Preflight API
  slug: domaincanary-com-spf-preflight-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/domaincanary-com/agentic-access/domaincanary-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/domaincanary-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/domaincanary-com/plans/domaincanary-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domaincanary-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/domaincanary-com/rules/domaincanary-com-rules.yml
  title: ''
  type: Spectral
  url: rules/domaincanary-com-rules.yml
- group: design
  href: https://artifacts.apis.io/domaincanary-com/json-ld/domaincanary-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domaincanary-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/domaincanary-com/vocabulary/domaincanary-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domaincanary-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/domaincanary-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/domaincanary-com/data-model/domaincanary-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domaincanary-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/domaincanary-com/errors/domaincanary-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domaincanary-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domaincanary-com/conformance/domaincanary-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domaincanary-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domaincanary-com/llms/domaincanary-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domaincanary-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/domaincanary-com/well-known/domaincanary-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domaincanary-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/domaincanary-com/hosts/domaincanary-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domaincanary-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/domaincanary-com/vendors/domaincanary-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domaincanary-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domaincanary.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domaincanary.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://domaincanary.com/pricing
- group: start
  title: ''
  type: Login
  url: https://domaincanary.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/domaincanary
- group: docs
  title: ''
  type: Documentation
  url: https://domaincanary.com/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://domaincanary.com/guides/dmarc-setup
- group: docs
  title: ''
  type: APIReference
  url: https://domaincanary.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/domaincanary-com/security/domaincanary-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domaincanary-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domaincanary.com/
created: '2026-11-05'
description: 'domaincanary-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://domaincanary.com/card.png?v=3fd87df1
jsonld:
- class_count: 6
  name: Domaincanary Com Context
  property_count: 22
  slug: domaincanary-com-context
layout: provider
modified: '2026-11-05'
name: DomainCanary
nav: Providers
network: true
overview: 'DomainCanary publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including C API, Spf Preflight API, and 1 more. Tagged areas include DMARC, Hosted SPF, Hosted MTA-STS, and MSP Tools.


  The DomainCanary catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DomainCanary''s developer surface includes pricing, documentation, getting-started guide, API reference, and 19 more developer resources.'
plans:
- name: Domaincanary Com Plans Pricing
  plan_count: 5
  slug: domaincanary-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: DomainCanary API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: domaincanary-com-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.8
    catalog_earned_first_party: 12.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 35.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domaincanary Com Domain Security
  slug: domaincanary-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: domaincanary-com
tags:
- DMARC
- Hosted SPF
- Hosted MTA-STS
- MSP Tools
website: https://domaincanary.com/
---
