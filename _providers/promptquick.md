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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/promptquick/llms/promptquick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptquick-llms.txt
- group: other
  href: https://artifacts.apis.io/promptquick/hosts/promptquick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptquick-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptquick/vendors/promptquick-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptquick-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TechNomadCode
- group: auth
  href: https://artifacts.apis.io/promptquick/security/promptquick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptquick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptquick.ai/
- group: company
  title: ''
  type: Blog
  url: https://promptquick.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://promptquick.ai/about
- group: start
  title: ''
  type: GettingStarted
  url: https://promptquick.ai/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://promptquick.ai/buy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://promptquick.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promptquick.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://promptquick.ai/faq
coverage:
  checked: '2026-10-18'
  detail: No developer documentation or machine-readable API contract was found on the provider's sites.
  evidence:
  - status: 404
    url: https://api.promptquick.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: PromptQuick provides simple prompt rules and toolkits to help developers get better AI results. Founded in 2024, it offers a free Prompt Rulebook, a paid full version, and an AI Product Development Toolkit that generates product requirements, user journeys, and starter code for Next.js, Supabase, and Vercel. The platform includes a blog, documentation, and a signup portal, aiming to streamline AI‑assisted product creation for developers and teams.
image: https://promptquick.ai/og/home.png
layout: provider
modified: '2026-10-18'
name: PromptQuick
nav: Providers
network: true
overview: 'PromptQuick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Toolkit, Prompt Engineering, and Product Development.


  PromptQuick''s developer surface includes engineering blog, documentation, getting-started guide, pricing, support, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Promptquick Domain Security
  slug: promptquick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: promptquick
tags:
- Company
- Artificial Intelligence
- Toolkit
- Prompt Engineering
- Product Development
website: https://promptquick.ai/
---
