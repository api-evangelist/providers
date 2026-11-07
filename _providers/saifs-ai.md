---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/saifs-ai/hosts/saifs-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saifs-ai-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saifs.ai/privacy_page
- group: auth
  href: https://artifacts.apis.io/saifs-ai/security/saifs-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saifs-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saifs.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://saifs.ai/mw_pricing/0
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saifs.ai/terms
coverage:
  checked: '2026-10-29'
  detail: Pricing page lists tools but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://saifs.ai/mw_pricing/0
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Saifs AI provides a suite of professional AI tools for content creation, enabling users to generate videos, images, text, and audio effortlessly. The platform offers AI video generation, text-to-video, AI sound effect generation, and image-to-video capabilities, targeting creators, marketers, and businesses seeking automated multimedia production.
image: https://multiplewords.nyc3.cdn.digitaloceanspaces.com/mw_assets/index_introduction-removebg.png
layout: provider
modified: '2026-10-29'
name: saifs-ai
nav: Providers
network: true
overview: 'saifs-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Content Creation, Video Generation, and Image Generation.


  saifs-ai''s developer surface includes pricing and 5 more developer resources.'
plans:
- name: Saifs Ai Plans Pricing
  plan_count: 0
  slug: saifs-ai-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Saifs Ai Rate Limits
  slug: saifs-ai-rate-limits
scopes:
- name: Saifs Ai Scopes
  scope_count: 0
  slug: saifs-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/saifs-ai/saifs-ai-2026-11-03T142643.png
security:
- kind: authentication
  name: Saifs Ai Authentication
  slug: saifs-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Saifs Ai Domain Security
  slug: saifs-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: saifs-ai
tags:
- Company
- Artificial Intelligence
- Content Creation
- Video Generation
- Image Generation
- Audio Generation
website: https://saifs.ai/
---
