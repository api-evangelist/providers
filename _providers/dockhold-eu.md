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
- description: Dockhold API provides deployment and management capabilities for web applications. Documentation is available at the Dockhold docs site.
  name: Dockhold API
  slug: dockhold-api
- description: 'Dockhold API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dockhold API
  slug: dockhold-eu-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/dockhold-eu/plans/dockhold-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dockhold-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dockhold-eu/rules/dockhold-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/dockhold-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/dockhold-eu/vocabulary/dockhold-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dockhold-eu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dockhold-eu/conformance/dockhold-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dockhold-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dockhold-eu/llms/dockhold-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dockhold-eu-llms.txt
- group: other
  href: https://artifacts.apis.io/dockhold-eu/hosts/dockhold-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dockhold-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/dockhold-eu/vendors/dockhold-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dockhold-eu-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://dockhold.eu/trust
- group: commercial
  title: ''
  type: Pricing
  url: https://dockhold.eu/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://dockhold.eu/docs
- group: company
  title: ''
  type: Blog
  url: https://dockhold.eu/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://dockhold.eu/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/dockhold-eu/security/dockhold-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dockhold-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dockhold.eu/
created: '2026-11-05'
description: Dockhold provides a platform to deploy web applications directly from a GitHub repository or local folder with a single command. It offers always‑on, secure hosting hosted in the EU, targeting developers, indie hackers, and teams who want to focus on code rather than infrastructure. The service includes automated builds, HTTPS URLs, built‑in isolation, secret management, and compliance with EU data residency requirements.
image: https://dockhold.eu/og-image.png
layout: provider
modified: '2026-11-05'
name: Dockhold
nav: Providers
network: true
overview: 'Dockhold is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Hosting, Developer Tools, Low-Code, EU Data Residency, and Continuous Deployment.


  The Dockhold catalog on APIs.io includes 1 Spectral governance ruleset.


  Dockhold''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 10 more developer resources.'
plans:
- name: Dockhold Eu Plans Pricing
  plan_count: 4
  slug: dockhold-eu-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Dockhold API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: dockhold-eu-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
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
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dockhold Eu Domain Security
  slug: dockhold-eu-domain-security
  summary_line: TLSv1.3
slug: dockhold-eu
tags:
- Cloud Hosting
- Developer Tools
- Low-Code
- EU Data Residency
- Continuous Deployment
- Company
website: https://dockhold.eu/
---
