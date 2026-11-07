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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.asking.com.br
  baseurl_source: declared
  description: 'Asking API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Asking API
  slug: asking-com-br-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/asking-com-br/rules/asking-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/asking-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/asking-com-br/vocabulary/asking-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asking-com-br-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/asking-com-br/conformance/asking-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asking-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asking-com-br/llms/asking-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asking-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/asking-com-br/well-known/asking-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asking-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/asking-com-br/hosts/asking-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asking-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/asking-com-br/vendors/asking-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asking-com-br-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asking.com.br/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://app.asking.com.br/signup?locale=en-US&cta_source=pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asking.com.br/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asking.com.br/hc/asking-documentation/en/categories/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.asking.com.br/
- group: auth
  href: https://artifacts.apis.io/asking-com-br/security/asking-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asking-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asking.com.br/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contracts were found.
  evidence:
  - status: 200
    url: https://docs.asking.com.br/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Asking provides a unified customer support platform integrating WhatsApp, Instagram, email, and chat into a single inbox. Businesses can manage conversations across multiple channels, assign owners, and reply with context, improving response efficiency and customer satisfaction. The service offers features like multi-channel messaging, team collaboration, automated workflows, and analytics, targeting small to enterprise-level companies seeking streamlined support operations.
layout: provider
modified: '2026-11-01'
name: Asking
nav: Providers
network: true
overview: 'Asking is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Service, Unified Inbox, Team Collaboration, AI Assistant, and Reporting.


  The Asking catalog on APIs.io includes 1 Spectral governance ruleset.


  Asking''s developer surface includes signup flow, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 64
  extends:
  - spectral:oas
  name: Asking API Rules
  rule_count: 23
  severity_counts:
    error: 21
    hint: 0
    info: 1
    warn: 1
  slug: asking-com-br-rules
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 10.7
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asking Com Br Domain Security
  slug: asking-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asking-com-br
tags:
- Customer Service
- Unified Inbox
- Team Collaboration
- AI Assistant
- Reporting
- Integration
website: https://asking.com.br/
---
