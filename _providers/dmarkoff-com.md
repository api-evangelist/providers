---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dmarkoff-com/plans/dmarkoff-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dmarkoff-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/dmarkoff-com/security/dmarkoff-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dmarkoff-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dmarkoff-com/llms/dmarkoff-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dmarkoff-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dmarkoff-com/well-known/dmarkoff-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dmarkoff-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dmarkoff-com/well-known/dmarkoff-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dmarkoff-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dmarkoff-com/hosts/dmarkoff-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dmarkoff-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dmarkoff-com/vendors/dmarkoff-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dmarkoff-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dmarkoff-com/security/dmarkoff-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dmarkoff-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dmarkoff-com/security/dmarkoff-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dmarkoff-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dmarkoff.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dmarkoff.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://dmarkoff.com/what-is-dmarc
- group: operate
  title: ''
  type: Support
  url: https://dmarkoff.com/contact
- group: company
  title: ''
  type: Blog
  url: https://dmarkoff.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dmarkoff.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dmarkoff.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dmarkoff.com/privacy-policy
coverage:
  checked: '2026-11-05'
  detail: OpenAPI endpoint returned HTML page instead of a machine‑readable spec
  evidence:
  - status: 200
    url: https://app.dmarkoff.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DMARKOFF provides an AI‑powered DMARC management platform that helps organizations monitor, analyze, and enforce email authentication policies. The service offers tools such as DMARC report analysis, SPF/DKIM checking, BIMI validation, and DNSSEC monitoring, all presented through an intuitive dashboard. With flexible pricing and integrations, DMARKOFF aims to simplify email security for both small businesses and enterprises, reducing phishing risks and improving deliverability.
layout: provider
modified: '2026-11-05'
name: DMARKOFF
nav: Providers
network: true
overview: 'DMARKOFF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Email Security, DMARC, Artificial Intelligence, Software-as-a-Service, and Email Authentication.


  DMARKOFF''s developer surface includes getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Dmarkoff Com Plans Pricing
  plan_count: 3
  slug: dmarkoff-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dmarkoff Com Domain Security
  slug: dmarkoff-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dmarkoff Com Vulnerability Disclosure
  slug: dmarkoff-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dmarkoff-com
tags:
- Email Security
- DMARC
- Artificial Intelligence
- Software-as-a-Service
- Email Authentication
website: https://dmarkoff.com/
---
