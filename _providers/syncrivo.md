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
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://syncrivo.ai/en/trust
- group: agent
  href: https://artifacts.apis.io/syncrivo/llms/syncrivo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syncrivo-llms.txt
- group: other
  href: https://artifacts.apis.io/syncrivo/hosts/syncrivo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syncrivo-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syncrivo.ai/en/terms
- group: auth
  title: ''
  type: Security
  url: https://syncrivo.ai/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syncrivo.ai/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://syncrivo.ai/en/pricing
- group: start
  title: ''
  type: Login
  url: https://syncrivo.ai/en/login
- group: docs
  title: ''
  type: Documentation
  url: https://syncrivo.ai/en/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://syncrivo.ai/en/changelog
- group: company
  title: ''
  type: Blog
  url: https://syncrivo.ai/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://syncrivo.ai/en/blog/hr-hris-event-workflow-messaging-automation
- group: auth
  href: https://artifacts.apis.io/syncrivo/security/syncrivo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/syncrivo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/syncrivo/security/syncrivo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/syncrivo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/syncrivo/security/syncrivo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syncrivo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syncrivo.ai/
coverage:
  checked: '2026-10-19'
  detail: The API host returns HTML for openapi.json and no OpenAPI, AsyncAPI, GraphQL, or other contract is available.
  evidence:
  - status: 200
    url: https://api.syncrivo.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: SyncRivo (KXN Technologies) provides enterprise messaging reliability solutions, enabling seamless interoperability across platforms like Slack, Microsoft Teams, Zoom, and Google Workspace. Founded in 2024, the company offers a unified messaging hub, advanced routing, compliance features, and analytics for businesses worldwide.
image: https://syncrivo.ai/og-image.webp
layout: provider
modified: '2026-10-19'
name: KXN Technologies
nav: Providers
network: true
overview: 'KXN Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  KXN Technologies'' developer surface includes pricing, documentation, changelog, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 13.2
  previous_composite: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/syncrivo/syncrivo-2026-11-03T144241.png
security:
- kind: domain-security
  name: Syncrivo Domain Security
  slug: syncrivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Syncrivo Vulnerability Disclosure
  slug: syncrivo-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Syncrivo Trust Center
  slug: syncrivo-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: syncrivo
tags:
- Company
website: https://syncrivo.ai/
---
