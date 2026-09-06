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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/built-robotics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.builtrobotics.com/security-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/built-robotics-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/built-robotics-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/built-robotics-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/built-robotics-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/built-robotics-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/built-robotics-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.builtrobotics.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/built-robotics_stock/
- group: other
  title: ''
  type: Technology
  url: https://www.builtrobotics.com/technology
- group: company
  title: ''
  type: About
  url: https://www.builtrobotics.com/about/company
- group: company
  title: ''
  type: Press
  url: https://www.builtrobotics.com/about/press
- group: operate
  title: ''
  type: Support
  url: https://www.builtrobotics.com/contact/general
- group: company
  title: ''
  type: Careers
  url: https://www.builtrobotics.com/careers/work
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/builtrobotics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.builtrobotics.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.builtrobotics.com/legal/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.builtrobotics.com/legal/cookie-policy
- group: company
  title: ''
  type: Newsletter
  url: https://www.builtrobotics.com/contact/newsletter
- group: other
  title: ''
  type: Media
  url: https://www.builtrobotics.com/about/downloads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/builtrobotics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@builtrobotics
- group: other
  title: ''
  type: X
  url: https://x.com/builtrobotics
created: '2026-08-01'
description: Built Robotics is a San Francisco robotics company, founded in 2016 by Noah Ready-Campbell and Andrew Liang, that turns conventional heavy construction equipment into AI-powered autonomous robots. Its Exosystem retrofit kit converts excavators and other earthmoving machines into self-operating robots for trenching, foundation excavation and pad grading, while the RPD 35 and RPS 25 autonomous pile drivers install foundations for utility-scale solar farms. Machines are supervised from the Everest command center, and field deployment is run through its Built Solar Technologies (built.solar) division. The company reports $114M raised and 25+ commercial deployments across the United States and Australia. Built Robotics publishes no public developer API, SDK or machine-readable API contract; its only public developer artifact is the open-source rsplan Reeds-Shepp path-planning library on PyPI and GitHub.
image: https://assets.builtrobotics.com/production/public/download/built_robotics_stacked.png
layout: provider
modified: '2026-08-01'
name: Built Robotics
nav: Providers
network: true
overview: 'Built Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Construction, Autonomous Systems, and Heavy Equipment.


  Built Robotics'' developer surface includes support, YouTube channel, and 22 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 15.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/built-robotics/refs/heads/main/screenshots/built-robotics-2026-08-07T162842.png
security:
- kind: domain-security
  name: Built Robotics Domain Security
  slug: built-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Built Robotics Vulnerability Disclosure
  slug: built-robotics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: built-robotics
tags:
- Company
- Robotics
- Construction
- Autonomous Systems
- Heavy Equipment
- Solar Energy
- Artificial Intelligence
- Industrial Automation
website: https://www.builtrobotics.com/
---
