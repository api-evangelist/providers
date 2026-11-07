---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/citedornot-com/plans/citedornot-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citedornot-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/citedornot-com/security/citedornot-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/citedornot-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/citedornot-com/conformance/citedornot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citedornot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citedornot-com/llms/citedornot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citedornot-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/citedornot-com/well-known/citedornot-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citedornot-com-security.txt
- group: agent
  href: https://artifacts.apis.io/citedornot-com/well-known/citedornot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citedornot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/citedornot-com/hosts/citedornot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citedornot-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://citedornot.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://citedornot.com/guides/generative-engine-optimization
- group: auth
  href: https://artifacts.apis.io/citedornot-com/security/citedornot-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citedornot-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citedornot-com/security/citedornot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citedornot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citedornot.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://citedornot.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citedornot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citedornot.com/privacy
coverage:
  checked: '2026-11-04'
  detail: The site provides marketing pages but no public API documentation or machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://citedornot.com/guides/generative-engine-optimization
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: CitedOrNot provides an AI visibility tool that helps brands understand how AI systems reference them across search engines and large language models. By analyzing AI-generated answers, the platform identifies competitor mentions, gaps in AI knowledge, and actionable insights to improve brand presence in AI outputs. Users can add competitor keywords, track changes over time, and receive recommendations to enhance AI visibility, ensuring their brand is accurately represented in AI-driven content.
image: https://citedornot.com/og-image.png
layout: provider
modified: '2026-11-03'
name: CitedOrNot
nav: Providers
network: true
overview: 'CitedOrNot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Brands, Analytics, and Visibility.


  CitedOrNot''s developer surface includes documentation, pricing, and 13 more developer resources.'
plans:
- name: Citedornot Com Plans Pricing
  plan_count: 3
  slug: citedornot-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citedornot Com Domain Security
  slug: citedornot-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Citedornot Com Vulnerability Disclosure
  slug: citedornot-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: citedornot-com
tags:
- Artificial Intelligence
- Marketing
- Brands
- Analytics
- Visibility
website: https://citedornot.com/
---
