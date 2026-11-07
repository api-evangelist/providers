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
api_count: 1
apis:
- description: The JDownloader service provides a download manager with a web interface and API endpoints for managing downloads, plugins, and account information. Documentation is available on the website but no ma
  name: JDownloader API
  slug: jdownloader-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/jdownloader/security/jdownloader-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jdownloader-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/jdownloader/hosts/jdownloader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jdownloader-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://my.jdownloader.org/legal/terms.html
- group: operate
  title: ''
  type: Support
  url: https://support.jdownloader.org/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.jdownloader.org/en/knowledgebase/article/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://jdownloader.org/news/index
- group: company
  title: ''
  type: Blog
  url: https://jdownloader.org/news/blog/dlc-limit
- group: auth
  href: https://artifacts.apis.io/jdownloader/security/jdownloader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jdownloader-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jdownloader/security/jdownloader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jdownloader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jdownloader.org/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known hosts.
  evidence:
  - status: 200
    url: https://jdownloader.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: JDownloader provides a popular download manager application that simplifies downloading files from the internet. It supports multiple hosters, automatic extraction, captcha solving, and bandwidth management. The company offers both a free version and premium subscriptions, with a focus on user-friendly features and extensive plugin support for various services.
layout: provider
modified: '2026-10-28'
name: JDownloader
nav: Providers
network: true
overview: 'JDownloader is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Download-Manager, File Transfer, Java, and Freemium.


  JDownloader''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 54.5
    operational_transparency: 10.5
  previous_composite: 13.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jdownloader/jdownloader-2026-11-03T134130.png
security:
- kind: domain-security
  name: Jdownloader Domain Security
  slug: jdownloader-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jdownloader Vulnerability Disclosure
  slug: jdownloader-vulnerability-disclosure
  summary_line: no policy recorded
slug: jdownloader
tags:
- Company
- Download-Manager
- File Transfer
- Java
- Freemium
website: https://jdownloader.org/
---
