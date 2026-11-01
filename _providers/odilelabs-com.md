---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Odilelabs Com Agentic Access
  operation_count: 4
  slug: odilelabs-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.odilelabs.com/v1
  baseurl_source: declared
  description: The Account API from odilelabs-com — 1 operation(s) for account.
  name: odilelabs-com Account API
  slug: odilelabs-com-account-api
- baseURL: https://api.odilelabs.com/v1
  baseurl_source: declared
  description: The Lines API from odilelabs-com — 2 operation(s) for lines.
  name: odilelabs-com Lines API
  slug: odilelabs-com-lines-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/odilelabs-com/vocabulary/odilelabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/odilelabs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/odilelabs-com/data-model/odilelabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/odilelabs-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/odilelabs-com/agentic-access/odilelabs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/odilelabs-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/odilelabs-com/plans/odilelabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/odilelabs-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/odilelabs-com/rules/odilelabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/odilelabs-com-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://odilelabs.com/security
- group: design
  href: https://artifacts.apis.io/odilelabs-com/errors/odilelabs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/odilelabs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/odilelabs-com/conformance/odilelabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/odilelabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/odilelabs-com/llms/odilelabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/odilelabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/odilelabs-com/a2a/odilelabs-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/odilelabs-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/odilelabs-com/well-known/odilelabs-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/odilelabs-com-security.txt
- group: agent
  href: https://artifacts.apis.io/odilelabs-com/well-known/odilelabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/odilelabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/odilelabs-com/hosts/odilelabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/odilelabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/odilelabs-com/vendors/odilelabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/odilelabs-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://odilelabs.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://odilelabs.com/signup
- group: auth
  title: ''
  type: Security
  url: https://odilelabs.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://odilelabs.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://odilelabs.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://odilelabs.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://gate.odilelabs.com/guides/openshell-gate
- group: operate
  title: ''
  type: ChangeLog
  url: https://odilelabs.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://odilelabs.com/developers
- group: auth
  href: https://artifacts.apis.io/odilelabs-com/security/odilelabs-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/odilelabs-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/odilelabs-com/security/odilelabs-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/odilelabs-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/odilelabs-com/security/odilelabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/odilelabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://odilelabs.com/
created: '2026-10-30'
description: Odile Labs provides communication infrastructure that connects people, businesses, and AI agents. It offers AI‑powered call answering and texting services, a one‑page website product, and developer tools such as an API gateway and phone‑number provisioning for AI agents. The solutions target businesses that miss calls, developers building AI agents, and agencies needing automated reception.
image: https://odilelabs.com/media/labs-og.png
json_schemas:
- name: LineSetupResult
  property_count: 0
  slug: odilelabs-com-line-setup-result
- name: LineSetup
  property_count: 0
  slug: odilelabs-com-line-setup
layout: provider
modified: '2026-10-30'
name: odilelabs-com
nav: Providers
network: true
overview: 'odilelabs-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API and Lines API. Tagged areas include Communication Infrastructure, AI Receptionist, Phone Answering, and Developer API.


  The odilelabs-com catalog on APIs.io includes 1 Spectral governance ruleset.


  odilelabs-com''s developer surface includes signup flow, pricing, documentation, changelog, API reference, and 22 more developer resources.'
plans:
- name: Odilelabs Com Plans Pricing
  plan_count: 8
  slug: odilelabs-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: odilelabs-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: odilelabs-com-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 72.5
    catalog_earned_first_party: 0.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 88.9
    contract_governance: 79.1
    contract_quality: 48.4
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Odilelabs Com Domain Security
  slug: odilelabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Odilelabs Com Vulnerability Disclosure
  slug: odilelabs-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Odilelabs Com Trust Center
  slug: odilelabs-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: odilelabs-com
tags:
- Communication Infrastructure
- AI Receptionist
- Phone Answering
- Developer API
website: https://odilelabs.com/
---
