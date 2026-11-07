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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Bunstation API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bunstation API
  slug: bunstation-com-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bunstation-com/plans/bunstation-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bunstation-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bunstation-com/rules/bunstation-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bunstation-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bunstation-com/vocabulary/bunstation-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bunstation-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bunstation-com/conformance/bunstation-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bunstation-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bunstation-com/llms/bunstation-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bunstation-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bunstation-com/well-known/bunstation-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bunstation-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bunstation-com/hosts/bunstation-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bunstation-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bunstation-com/vendors/bunstation-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bunstation-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bunstation.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://bunstation.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kryszczan
- group: docs
  title: ''
  type: Documentation
  url: https://bunstation.com/docs
- group: company
  title: ''
  type: Blog
  url: https://bunstation.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://bunstation.com/docs/quick-start
- group: auth
  href: https://artifacts.apis.io/bunstation-com/security/bunstation-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bunstation-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bunstation.com/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://bunstation.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Bunstation AI Website Builder provides a modern, responsive website creation platform powered by artificial intelligence. Users can generate, customize, and launch websites in minutes without coding, with options for free starter plans and paid Pro plans that add custom domains, increased storage, and advanced features. The service emphasizes ease of use, AI-driven design suggestions, and rapid deployment for individuals and businesses seeking an online presence.
image: https://cdn.bunstation.com/projects/2130a972-d1a2-4ee0-b110-994011dee2b1/7293573f-36a6-4a61-ba4f-cc0db38873f2/og-image.png
layout: provider
modified: '2026-11-03'
name: Bunstation
nav: Providers
network: true
overview: 'Bunstation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Website Builder, No-Code, Software-as-a-Service, and Marketing.


  The Bunstation catalog on APIs.io includes 1 Spectral governance ruleset.


  Bunstation''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Bunstation Com Plans Pricing
  plan_count: 3
  slug: bunstation-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Bunstation API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: bunstation-com-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 2.6
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
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bunstation Com Domain Security
  slug: bunstation-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bunstation-com
tags:
- Artificial Intelligence
- Website Builder
- No-Code
- Software-as-a-Service
- Marketing
website: https://bunstation.com/
---
