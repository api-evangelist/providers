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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free, no‑login API for the ARC open agentic commerce benchmark.
  name: ARC public API
  slug: arc-public-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/arcreport-ai/rules/arcreport-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/arcreport-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/arcreport-ai/vocabulary/arcreport-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcreport-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/arcreport-ai/conformance/arcreport-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcreport-ai-conformance.yml
- group: build
  href: https://artifacts.apis.io/arcreport-ai/cli/arcreport-ai-cli.yml
  title: ''
  type: CLI
  url: cli/arcreport-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/arcreport-ai/security/arcreport-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arcreport-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/arcreport-ai/errors/arcreport-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arcreport-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/arcreport-ai/llms/arcreport-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcreport-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/arcreport-ai/a2a/arcreport-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/arcreport-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/arcreport-ai/well-known/arcreport-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcreport-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/arcreport-ai/well-known/arcreport-ai-arcreport-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcreport-ai-arcreport-security.txt
- group: agent
  href: https://artifacts.apis.io/arcreport-ai/well-known/arcreport-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcreport-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcreport-ai/hosts/arcreport-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcreport-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcreport-ai/vendors/arcreport-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcreport-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.arcreport.ai/press/latest
- group: start
  title: ''
  type: Login
  url: https://www.arcreport.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.arcreport.ai/docs/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.arcreport.ai/methodology/changelog
- group: auth
  href: https://artifacts.apis.io/arcreport-ai/security/arcreport-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcreport-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arcreport-ai/security/arcreport-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcreport-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcreport.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.arcreport.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.arcreport.ai/docs/precheck
- group: docs
  title: ''
  type: Documentation
  url: https://www.arcreport.ai/docs/connect
- group: company
  title: ''
  type: Blog
  url: https://www.arcreport.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.arcreport.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arcreport.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arcreport.ai/privacy
created: '2026-10-29'
description: ArcReport AI provides a platform that evaluates whether AI agents can successfully navigate e‑commerce checkout flows. By running automated pre‑checks across thousands of online stores, it offers insights into agent capabilities, highlights friction points, and helps developers improve AI‑driven shopping experiences. The service is free, open‑source, and continuously updated with new store data and methodology documentation.
image: https://www.arcreport.ai/opengraph-image?6bf456a4ce1093a3
layout: provider
modified: '2026-10-29'
name: arcreport-ai
nav: Providers
network: true
overview: 'arcreport-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, E-Commerce, Analytics, and Checkout.


  The arcreport-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  arcreport-ai''s developer surface includes CLI, getting-started guide, changelog, documentation, engineering blog, pricing, and 21 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: arcreport-ai API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: arcreport-ai-rules
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 22.4
    contract_governance: 19.7
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/arcreport-ai/arcreport-ai-2026-11-03T121106.png
security:
- kind: domain-security
  name: Arcreport Ai Domain Security
  slug: arcreport-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcreport Ai Vulnerability Disclosure
  slug: arcreport-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arcreport-ai
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Analytics
- Checkout
website: https://arcreport.ai/
---
