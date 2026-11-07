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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Alter's privileged access management platform, documented at the reference guide.
  name: Alter API
  slug: alter-api
- description: 'Alter API as documented publicly: 157 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Alter API
  slug: alterauth-com-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/alterauth-com/plans/alterauth-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alterauth-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alterauth-com/rules/alterauth-com-rules.yml
  title: ''
  type: Spectral
  url: rules/alterauth-com-rules.yml
- group: design
  href: https://artifacts.apis.io/alterauth-com/vocabulary/alterauth-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alterauth-com-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/alterauth-com/cli/alterauth-com-cli.yml
  title: ''
  type: CLI
  url: cli/alterauth-com-cli.yml
- group: design
  href: https://artifacts.apis.io/alterauth-com/conformance/alterauth-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alterauth-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alterauth-com/llms/alterauth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alterauth-com-llms.txt
- group: other
  href: https://artifacts.apis.io/alterauth-com/hosts/alterauth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alterauth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alterauth-com/vendors/alterauth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alterauth-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alterauth.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alterauth.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://alterauth.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlterAIDev
- group: company
  title: ''
  type: Blog
  url: https://blog.alterauth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alterauth.com/reference/cli/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alterauth.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alterauth.com/
- group: auth
  href: https://artifacts.apis.io/alterauth-com/security/alterauth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alterauth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alterauth.com/
created: '2026-11-01'
description: Alter provides privileged access management (PAM) for AI agents, enforcing runtime policies, vaulted credentials, approval workflows, and audit trails. Their platform secures AI-driven actions with fine-grained controls, policy engine, and credential vault, targeting developers integrating AI tools.
image: https://alterauth.com/og-image.png
layout: provider
modified: '2026-11-01'
name: Alter
nav: Providers
network: true
overview: 'Alter is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Artificial Intelligence, Privileged Access Management, Identity and Access Management, and Privileged.


  The Alter catalog on APIs.io includes 1 Spectral governance ruleset.


  Alter''s developer surface includes CLI, pricing, engineering blog, API reference, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Alterauth Com Plans Pricing
  plan_count: 4
  slug: alterauth-com-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Alter API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: alterauth-com-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 7.8
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 31.6
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alterauth Com Domain Security
  slug: alterauth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alterauth-com
tags:
- Security
- Artificial Intelligence
- Privileged Access Management
- Identity and Access Management
- Privileged
website: https://alterauth.com/
---
