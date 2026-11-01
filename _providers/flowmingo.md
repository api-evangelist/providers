---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flowmingo Agentic Access
  operation_count: 2
  slug: flowmingo-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://apis.flowmingo.ai
  baseurl_source: declared
  description: The Flowmingo API API from Flowmingo — 1 operation(s) for flowmingo api.
  name: Flowmingo Flowmingo API
  slug: flowmingo-flowmingo-api-api
- baseURL: https://apis.flowmingo.ai
  baseurl_source: declared
  description: The Scheduler API from Flowmingo — 1 operation(s) for scheduler.
  name: Flowmingo Scheduler API
  slug: flowmingo-scheduler-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/flowmingo/agentic-access/flowmingo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flowmingo-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/flowmingo/rules/flowmingo-rules.yml
  title: ''
  type: Spectral
  url: rules/flowmingo-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://flowmingo.ai/security
- group: design
  href: https://artifacts.apis.io/flowmingo/conformance/flowmingo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flowmingo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flowmingo/llms/flowmingo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowmingo-llms.txt
- group: other
  href: https://artifacts.apis.io/flowmingo/hosts/flowmingo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flowmingo-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://flowmingo.ai/integration/webhook
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flowmingo.ai/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://team.flowmingo.ai/company/sign-up
- group: auth
  title: ''
  type: Security
  url: https://flowmingo.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flowmingo.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://flowmingo.ai/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.flowmingo.ai/
- group: company
  title: ''
  type: Blog
  url: https://flowmingo.ai/blog
- group: auth
  href: https://artifacts.apis.io/flowmingo/security/flowmingo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flowmingo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/flowmingo/security/flowmingo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowmingo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flowmingo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://flowmingo.ai/integration/api-integration
created: '2026-10-20'
description: 'Flowmingo is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://flowmingo.ai/og-default.png?v=3
layout: provider
modified: '2026-10-20'
name: Flowmingo
nav: Providers
network: true
overview: 'Flowmingo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Flowmingo API and Scheduler API. Tagged areas include Company.


  The Flowmingo catalog on APIs.io includes 1 Spectral governance ruleset.


  Flowmingo''s developer surface includes signup flow, pricing, engineering blog, documentation, and 14 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Flowmingo API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: flowmingo-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 32.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flowmingo Domain Security
  slug: flowmingo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flowmingo Trust Center
  slug: flowmingo-trust-center
  summary_line: SOC 2, GDPR
slug: flowmingo
tags:
- Company
website: https://flowmingo.ai
---
