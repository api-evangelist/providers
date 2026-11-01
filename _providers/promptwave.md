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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/promptwave/security/promptwave-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/promptwave-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/promptwave/hosts/promptwave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptwave-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://promptwave.ai/Identity/Account/Register
- group: commercial
  title: ''
  type: Pricing
  url: https://promptwave.ai/prompts/1220/pricing-strategies
- group: auth
  href: https://artifacts.apis.io/promptwave/security/promptwave-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/promptwave-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/promptwave/security/promptwave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptwave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptwave.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://promptwave.ai/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://promptwave.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promptwave.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://promptwave.ai/contact
created: '2026-10-18'
description: PromptWave AI is a web platform that enables users to save, organize, share, and explore AI prompts across various models. It offers a community-driven marketplace where creators can publish prompts, discover new ideas, and collaborate. Features include prompt collections, AI‑generated content, and tools for customizing prompts for scientific papers, image generation, and more. The service aims to boost AI productivity by simplifying prompt management and fostering a vibrant ecosystem of prompt engineers and enthusiasts.
image: https://promptwave.ai/img/presentation-promptwave-ai-1920-1080-light.png
layout: provider
modified: '2026-10-18'
name: PromptWave AI
nav: Providers
network: true
overview: 'PromptWave AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Prompt Engineering, Community, and Productivity.


  PromptWave AI''s developer surface includes signup flow, pricing, documentation, support, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Promptwave Domain Security
  slug: promptwave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Promptwave Vulnerability Disclosure
  slug: promptwave-vulnerability-disclosure
  summary_line: no policy recorded
slug: promptwave
tags:
- Company
- Artificial Intelligence
- Prompt Engineering
- Community
- Productivity
website: https://promptwave.ai/
---
