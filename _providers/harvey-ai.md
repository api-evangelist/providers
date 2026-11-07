---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Harvey does not currently publish a public, self-serve developer API. Integrations with document management systems, research tools, and firm workflows are delivered through Harvey's Ecosystem program
  name: Harvey Platform
  slug: harvey-platform
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/harvey-ai/rate-limits/harvey-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/harvey-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/harvey-ai/finops/harvey-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/harvey-ai-finops.yml
- group: commercial
  href: https://artifacts.apis.io/harvey-ai/plans/harvey-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/harvey-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/harvey-ai/security/harvey-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/harvey-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/harvey-ai/security/harvey-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/harvey-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/harvey-ai/security/harvey-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harvey-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.harvey.ai
- group: company
  title: ''
  type: Blog
  url: https://www.harvey.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harvey.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harvey.ai/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/harvey__ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harvey
created: '2026-05-23'
description: Harvey is a domain-specific AI platform built for elite law firms and in-house legal departments. Its product suite includes Assistant (question answering, document analysis, and drafting), Vault (secure document storage and bulk analysis), Knowledge (legal, regulatory, and tax research), Workflow Agents (pre-built and customizable legal agents), Harvey Mobile, and an Ecosystem of integrations with existing legal tools. Harvey is sold via enterprise contracts to large law firms and corporate legal teams, and does not currently publish a self-serve public developer API; integrations are arranged through direct sales and partnership engagements.
finops:
- has_sources: false
  method: generated
  name: Harvey Ai Finops
  primary_unit: ''
  service_category: API
  slug: harvey-ai-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harvey-ai.png
layout: provider
modified: '2026-05-23'
name: Harvey
nav: Providers
network: true
overview: 'Harvey is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Legal Tech, Law Firms, Legal Research, and Contract Analysis.


  Harvey''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Harvey Ai Plans Pricing
  plan_count: 0
  slug: harvey-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Harvey Ai Rate Limits
  slug: harvey-ai-rate-limits
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 16.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/harvey-ai/harvey-ai-2026-06-20T182535.png
security:
- kind: domain-security
  name: Harvey Ai Domain Security
  slug: harvey-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Harvey Ai Vulnerability Disclosure
  slug: harvey-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Harvey Ai Trust Center
  slug: harvey-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: harvey-ai
tags:
- Artificial Intelligence
- Legal Tech
- Law Firms
- Legal Research
- Contract Analysis
- Due Diligence
- Litigation
- Workflow Agents
- Enterprise
- Vault
website: https://www.harvey.ai
---
