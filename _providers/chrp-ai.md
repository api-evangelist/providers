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
    mcp_server: false
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
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/chrp-ai/llms/chrp-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chrp-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/chrp-ai/hosts/chrp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chrp-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/chrp-ai/vendors/chrp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chrp-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://chrp.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://chrp.ai/press
- group: other
  title: ''
  type: Leadership
  url: https://chrp.ai/team
- group: auth
  href: https://artifacts.apis.io/chrp-ai/security/chrp-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chrp-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chrp-ai/security/chrp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chrp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chrp.ai/
- group: other
  title: ''
  type: Image
  url: https://chrp.ai/images/chrp-icon-black.png
- group: docs
  title: ''
  type: Documentation
  url: https://chrp.ai/mcp/docs
- group: operate
  title: ''
  type: Support
  url: https://chrp.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chrp.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chrp.ai/terms
coverage:
  checked: '2026-11-04'
  detail: Provider documentation is public HTML without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://chrp.ai/mcp/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CHRP gives leaders anonymous team-level Emotional Performance Intelligence built from music behavior — no surveys, no wearables. Individuals get private insight first. Deployed with OSU, US Navy EOD, and demanding military readiness environments. The platform provides aggregate anonymous trends for organizations while keeping individual data private, creating a new category of emotional performance intelligence derived from everyday behavior.
image: https://chrp.ai/api/og
layout: provider
modified: '2026-11-03'
name: CHRP
nav: Providers
network: true
overview: 'CHRP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Emotional Intelligence, Team Performance, and Analytics.


  CHRP''s developer surface includes documentation, support, and 12 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chrp Ai Domain Security
  slug: chrp-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chrp Ai Vulnerability Disclosure
  slug: chrp-ai-vulnerability-disclosure
  summary_line: no policy recorded
slug: chrp-ai
tags:
- Company
- Artificial Intelligence
- Emotional Intelligence
- Team Performance
- Analytics
website: https://chrp.ai/
---
