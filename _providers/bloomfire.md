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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is provided via the Help Center but no machine-readable contract was found.
  name: Bloomfire API
  slug: bloomfire-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bloomfire/well-known/bloomfire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bloomfire-well-known.yml
- group: other
  href: https://artifacts.apis.io/bloomfire/hosts/bloomfire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloomfire-hosts.yml
- group: other
  href: https://artifacts.apis.io/bloomfire/vendors/bloomfire-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloomfire-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomfire.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.bloomfire.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloomfire.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://bloomfire.com/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.bloomfire.com/posts/3492780-getting-started-with-bloomfire
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomfire
- group: auth
  href: https://artifacts.apis.io/bloomfire/security/bloomfire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomfire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloomfire.com
- group: commercial
  title: ''
  type: Pricing
  url: https://bloomfire.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://bloomfire.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://bloomfire.com/resources/
coverage:
  checked: '2026-11-02'
  detail: Help Center pages are rendered via JavaScript, preventing extraction of a machine-readable spec.
  evidence:
  - status: 200
    url: https://help.bloomfire.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bloomfire provides an AI‑first, headless platform for enterprise knowledge management. Their Governed Context for Enterprise AI unifies data, content, and AI models, offering modular services like Universal Connector Framework, Ontology Management, Content Guardrails, and AI‑driven search and summarization. The platform enables organizations to capture, curate, and retrieve enterprise context at scale, supporting use‑cases from conversational AI assistants to analytics and compliance. Bloomfire’s API‑first design lets developers integrate these capabilities into custom applications, driving intelligent insights across the enterprise.
layout: provider
modified: '2026-11-02'
name: Bloomfire
nav: Providers
network: true
overview: 'Bloomfire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Knowledge Management, Enterprise, Platform, and API-First.


  Bloomfire''s developer surface includes support, getting-started guide, pricing, engineering blog, documentation, and 9 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 54.5
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloomfire Domain Security
  slug: bloomfire-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomfire
tags:
- Artificial Intelligence
- Knowledge Management
- Enterprise
- Platform
- API-First
website: https://bloomfire.com
---
