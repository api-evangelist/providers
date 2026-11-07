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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/pindropsecurity-com/well-known/pindropsecurity-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pindropsecurity-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/pindropsecurity-com/llms/pindropsecurity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pindropsecurity-com-llms.txt
- group: other
  href: https://artifacts.apis.io/pindropsecurity-com/hosts/pindropsecurity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pindropsecurity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pindropsecurity-com/vendors/pindropsecurity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pindropsecurity-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.pindrop.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.pindrop.com/newsroom
- group: auth
  href: https://artifacts.apis.io/pindropsecurity-com/security/pindropsecurity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pindropsecurity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.pindropsecurity.com/
- group: operate
  title: ''
  type: Support
  url: https://support.pindrop.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pindrop.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pindrop.com/legal/pindrop-security-website-terms-of-use
- group: docs
  title: ''
  type: Documentation
  url: https://www.pindrop.com/resources
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or developer portal is available on the company's website.
  evidence:
  - status: 200
    url: https://www.pindrop.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Pindrop provides real‑time voice and video authentication, deepfake detection, and fraud risk assessment for contact centers and virtual meetings. Its platform combines synthetic‑engine analysis, AI‑driven voice biometrics, and multi‑signal verification to protect enterprises from AI‑generated attacks, spoofed calls, and fraudulent interactions. The company serves financial services, healthcare, insurance, and retail sectors, offering products such as Pulse, BotStopper, Protect, and Passport to secure communications and verify identities at scale.
image: https://www.pindrop.com/favicon.ico
layout: provider
modified: '2026-10-28'
name: Pindrop Security
nav: Providers
network: true
overview: 'Pindrop Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Fraud Prevention, Deepfake Defense, Voice Authentication, and Enterprise.


  Pindrop Security''s developer surface includes support, documentation, and 10 more developer resources.'
plans:
- name: Pindropsecurity Com Plans Pricing
  plan_count: 0
  slug: pindropsecurity-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Pindropsecurity Com Rate Limits
  slug: pindropsecurity-com-rate-limits
scopes:
- name: Pindropsecurity Com Scopes
  scope_count: 0
  slug: pindropsecurity-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pindropsecurity-com/pindropsecurity-com-2026-11-03T141223.png
security:
- kind: authentication
  name: Pindropsecurity Com Authentication
  slug: pindropsecurity-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pindropsecurity Com Domain Security
  slug: pindropsecurity-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pindropsecurity-com
tags:
- Security
- Fraud Prevention
- Deepfake Defense
- Voice Authentication
- Enterprise
website: http://www.pindropsecurity.com/
---
