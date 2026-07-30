---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Open Technology Fund (OTF) is a U.S. government-funded independent nonprofit that supports the development of open-source internet freedom technologies to advance human rights and open societies. '
  name: Open Technology Fund
  slug: open-technology-fund
artifact_total: 21
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/u-s-agency-for-global-media-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/u-s-agency-for-global-media-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-states-agency-for-global-media
- group: company
  title: ''
  type: Website
  url: https://www.usagm.gov/
- group: company
  title: ''
  type: About
  url: https://www.usagm.gov/who-we-are/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usagm
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/u-s-agency-for-global-media/refs/heads/main/vocabulary/u-s-agency-for-global-media-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/u-s-agency-for-global-media/refs/heads/main/json-ld/u-s-agency-for-global-media-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.usagm.gov/feed/
- group: company
  title: ''
  type: News
  url: https://github.com/usagm/usagm-press-freedom
created: '2024-11-21'
description: The U.S. Agency for Global Media (USAGM) is an independent federal agency that oversees a network of international media organizations aimed at providing news and information to audiences around the world in support of freedom and democracy. These media outlets include Voice of America (VOA), Radio Free Europe/Radio Liberty (RFE/RL), Radio Free Asia (RFA), Office of Cuba Broadcasting (OCB), Middle East Broadcasting Networks (MBN), and the Open Technology Fund (OTF). Together these entities operate in over 64 languages and reach approximately 427 million people weekly, producing more than 3,000 hours of original programming per week in regions where access to a free press is limited.
features:
- description: The largest U.S. international broadcaster, providing news and information in 47 languages to audiences in regions underserved by free press, including sub-Saharan Africa, Latin America, and Asia.
  name: Voice of America (VOA)
- description: Broadcasts domestic news coverage to audiences in Central and Eastern Europe, Russia, the Caucasus, Central Asia, and the Middle East in 27 languages.
  name: Radio Free Europe/Radio Liberty (RFE/RL)
- description: Provides uncensored news and information in nine languages to audiences across East and Southeast Asia, including China, North Korea, Vietnam, and Burma.
  name: Radio Free Asia (RFA)
- description: Delivers Arabic-language television and digital content across the Middle East and North Africa, including Alhurra TV and Radio Sawa.
  name: Middle East Broadcasting Networks (MBN)
- description: Funds the development of open-source internet freedom tools and technologies that help individuals in repressive environments access a free and open internet.
  name: Open Technology Fund (OTF)
- description: Anti-censorship, circumvention, and digital safety programs supporting journalists, activists, and ordinary citizens operating in restricted environments.
  name: Internet Freedom Programs
finops:
- name: U S Agency For Global Media Finops
  service_category: API
  slug: u-s-agency-for-global-media-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/u-s-agency-for-global-media.png
integrations:
- description: OTF-funded privacy and anonymity network enabling secure communication for users in censored or surveilled environments.
  name: Tor Project
- description: End-to-end encrypted messaging platform supported by OTF for secure communications by journalists and activists.
  name: Signal
- description: Developer of Signal protocol providing encrypted messaging and calling for vulnerable populations worldwide.
  name: Open Whisper Systems
jsonld:
- class_count: 5
  name: U S Agency For Global Media Context
  property_count: 19
  slug: u-s-agency-for-global-media-context
layout: provider
modified: '2026-07-25'
name: U.S. Agency for Global Media
nav: Providers
network: true
overview: 'U.S. Agency for Global Media publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Media, Broadcasting, International, and Press Freedom.


  The U.S. Agency for Global Media catalog on APIs.io includes 1 JSON-LD context.


  U.S. Agency for Global Media''s developer surface includes engineering blog, product news, and 8 more developer resources.'
plans:
- name: U S Agency For Global Media Plans Pricing
  plan_count: 3
  slug: u-s-agency-for-global-media-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: U S Agency For Global Media Rate Limits
  slug: u-s-agency-for-global-media-rate-limits
score:
  band: emerging
  composite: 24.7
  delta: -3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 27.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/u-s-agency-for-global-media/refs/heads/main/screenshots/u-s-agency-for-global-media-2026-06-20T195915.png
security:
- kind: domain-security
  name: U S Agency For Global Media Domain Security
  slug: u-s-agency-for-global-media-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: U S Agency For Global Media Vulnerability Disclosure
  slug: u-s-agency-for-global-media-vulnerability-disclosure
  summary_line: Bugcrowd
slug: u-s-agency-for-global-media
tags:
- Federal Government
- Media
- Broadcasting
- International
- Press Freedom
- Internet Freedom
use_cases:
- description: Delivering independent, accurate news and information to audiences in countries that lack a free press or face government-controlled media.
  name: International News Delivery
- description: Supporting journalists and media organizations operating in repressive environments by providing training, tools, and reporting support.
  name: Press Freedom Advocacy
- description: Enabling internet users in censored environments to bypass restrictions and access uncensored online content through funded circumvention tools.
  name: Internet Circumvention
- description: Protecting journalists and activists with digital security tools and training through Open Technology Fund-supported projects.
  name: Digital Safety
- description: Supporting the development of independent media ecosystems in transitioning democracies through training, technology, and partnerships.
  name: Media Development
website: https://www.usagm.gov/
---
