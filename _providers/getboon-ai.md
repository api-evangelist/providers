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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.getboon.ai/trust
- group: agent
  href: https://artifacts.apis.io/getboon-ai/llms/getboon-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getboon-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/getboon-ai/well-known/getboon-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getboon-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/getboon-ai/hosts/getboon-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getboon-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/getboon-ai/vendors/getboon-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getboon-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.getboon.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getboon
- group: auth
  href: https://artifacts.apis.io/getboon-ai/security/getboon-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getboon-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/getboon-ai/security/getboon-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getboon-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getboon.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.getboon.ai/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getboon.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.getboon.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getboon.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getboon.ai/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: No public machine‑readable API specification (OpenAPI, GraphQL, AsyncAPI, or gRPC) was found on the provider's API host.
  evidence:
  - status: 404
    url: https://api.getboon.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Boon AI delivers AI‑powered construction estimating software that reads architectural drawings and specifications, automatically performs takeoffs, detects conflicts, and levels bids for general contractors and specialty subcontractors. The platform offers accuracy metrics, pricing tiers for teams of any size, and tools such as ROI calculators, RFI generators, and bid‑leveling templates, positioning Boon as a modern, AI‑driven solution for the construction industry.
image: https://www.getboon.ai/legacy/images/boon-3.svg
layout: provider
modified: '2026-10-28'
name: Boon
nav: Providers
network: true
overview: 'Boon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Construction, Estimating, Software, and Startups.


  Boon''s developer surface includes engineering blog, pricing, support, and 12 more developer resources.'
random_paper: 13
scopes:
- name: Getboon Ai Scopes
  scope_count: 0
  slug: getboon-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getboon-ai/getboon-ai-2026-11-03T132650.png
security:
- kind: authentication
  name: Getboon Ai Authentication
  slug: getboon-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Getboon Ai Domain Security
  slug: getboon-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getboon Ai Trust Center
  slug: getboon-ai-trust-center
  summary_line: SOC 2, GDPR
slug: getboon-ai
tags:
- Artificial Intelligence
- Construction
- Estimating
- Software
- Startups
website: https://www.getboon.ai/
---
