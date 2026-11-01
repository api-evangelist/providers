---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/fonzi-ai/llms/fonzi-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fonzi-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/fonzi-ai/well-known/fonzi-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fonzi-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/fonzi-ai/hosts/fonzi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fonzi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/fonzi-ai/vendors/fonzi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fonzi-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fonzi.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fonzi.ai/privacy
- group: auth
  href: https://artifacts.apis.io/fonzi-ai/security/fonzi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fonzi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fonzi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://fonzi.ai/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fonzi.ai/talent
- group: operate
  title: ''
  type: Support
  url: https://fonzi.ai/support
coverage:
  checked: '2026-10-30'
  detail: The site provides a hiring community platform with no public API.
  evidence:
  - status: 200
    url: https://fonzi.ai
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: Fonzi AI is a talent hiring community that connects top AI engineers with fast‑growing startups. The platform enables engineers to discover high‑impact roles, apply quickly, and interview within 24 hours, while startups gain access to a curated pool of AI talent backed by leading investors. Fonzi AI also offers community features, AI‑driven matching, and resources for both candidates and companies.
image: https://fonzi.ai/seo/og-image.png
layout: provider
modified: '2026-10-30'
name: fonzi-ai
nav: Providers
network: true
overview: 'fonzi-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Hiring, TalentMarketplace, and Startup.


  fonzi-ai''s developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fonzi Ai Domain Security
  slug: fonzi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fonzi-ai
tags:
- Company
- AI
- Hiring
- TalentMarketplace
- Startup
website: https://fonzi.ai/
---
