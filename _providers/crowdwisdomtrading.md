---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Crowdwisdomtrading Agentic Access
  operation_count: 9
  slug: crowdwisdomtrading-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: Structured weekly and intraday prediction signals for B2B partners.
  name: CrowdWisdom Signals API
  slug: crowdwisdom-signals-api
- baseURL: https://api.crowdwisdomtrading.com
  baseurl_source: declared
  description: The Account API from CrowdWisdom Signals API — 2 operation(s) for account.
  name: CrowdWisdom Signals API Account API
  slug: crowdwisdomtrading-account-api
- baseURL: https://api.crowdwisdomtrading.com
  baseurl_source: declared
  description: The Health API from CrowdWisdom Signals API — 2 operation(s) for health.
  name: CrowdWisdom Signals API Health API
  slug: crowdwisdomtrading-health-api
- baseURL: https://api.crowdwisdomtrading.com
  baseurl_source: declared
  description: The Signals API from CrowdWisdom Signals API — 3 operation(s) for signals.
  name: CrowdWisdom Signals API Signals API
  slug: crowdwisdomtrading-signals-api
- baseURL: https://api.crowdwisdomtrading.com
  baseurl_source: declared
  description: The Socialmap API from CrowdWisdom Signals API — 1 operation(s) for socialmap.
  name: CrowdWisdom Signals API Socialmap API
  slug: crowdwisdomtrading-socialmap-api
- baseURL: https://api.crowdwisdomtrading.com
  baseurl_source: declared
  description: The Socialmap Preview API from CrowdWisdom Signals API — 1 operation(s) for socialmap preview.
  name: CrowdWisdom Signals API Socialmap Preview API
  slug: crowdwisdomtrading-socialmap-preview-api
artifact_total: 13
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/agentic-access/crowdwisdomtrading-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crowdwisdomtrading-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/plans/crowdwisdomtrading-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crowdwisdomtrading-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/rules/crowdwisdomtrading-rules.yml
  title: ''
  type: Spectral
  url: rules/crowdwisdomtrading-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/json-ld/crowdwisdomtrading-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crowdwisdomtrading-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/vocabulary/crowdwisdomtrading-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crowdwisdomtrading-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/data-model/crowdwisdomtrading-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crowdwisdomtrading-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/errors/crowdwisdomtrading-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crowdwisdomtrading-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/conformance/crowdwisdomtrading-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crowdwisdomtrading-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/llms/crowdwisdomtrading-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdwisdomtrading-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/a2a/crowdwisdomtrading-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/crowdwisdomtrading-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/hosts/crowdwisdomtrading-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdwisdomtrading-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/vendors/crowdwisdomtrading-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdwisdomtrading-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/authentication/crowdwisdomtrading-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crowdwisdomtrading-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdwisdomtrading/refs/heads/main/security/crowdwisdomtrading-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdwisdomtrading-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crowdwisdomtrading.com/api-program
- group: docs
  title: ''
  type: Documentation
  url: https://api.crowdwisdomtrading.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.crowdwisdomtrading.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crowdwisdomtrading.com/api-program#quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.crowdwisdomtrading.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crowdwisdomtrading.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.crowdwisdomtrading.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crowdwisdomtrading.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crowdwisdomtrading.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/crowdwisdomtrading/workspace/api
created: '2026-10-02'
description: CrowdWisdom Signals API provides REST access to crowd‑consensus trade setups generated by thousands of professional traders. The platform delivers machine‑readable signals for fintech applications, trading terminals, and quantitative research, enabling developers to integrate curated trade ideas, performance metrics, and risk assessments directly into their products. It offers tiered pricing, API keys with bearer authentication, and comprehensive documentation for rapid onboarding.
image: https://www.crowdwisdomtrading.com/og-image.jpg
jsonld:
- class_count: 2
  name: Crowdwisdomtrading Context
  property_count: 6
  slug: crowdwisdomtrading-context
layout: provider
modified: '2026-10-02'
name: CrowdWisdom Signals API
nav: Providers
network: true
overview: 'CrowdWisdom Signals API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Health API, Signals API, and 3 more. Tagged areas include Finance, Trading, Signals, and B2B.


  The CrowdWisdom Signals API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CrowdWisdom Signals API''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Crowdwisdomtrading Plans Pricing
  plan_count: 0
  slug: crowdwisdomtrading-plans-pricing
- name: Crowdwisdomtrading Plans
  plan_count: 0
  slug: crowdwisdomtrading-plans
random_paper: 11
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: CrowdWisdom Signals API API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: crowdwisdomtrading-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 42.1
    developer_ergonomics: 49.4
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Crowdwisdomtrading Authentication
  slug: crowdwisdomtrading-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crowdwisdomtrading Domain Security
  slug: crowdwisdomtrading-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: crowdwisdomtrading
tags:
- Finance
- Trading
- Signals
- B2B
website: https://www.crowdwisdomtrading.com/api-program
---
