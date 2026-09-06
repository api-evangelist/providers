---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Signal Sciences Core API (now the Fastly Next-Gen WAF control-plane API) is a REST API served at https://dashboard.signalsciences.net/api/v0 that lets developers manage the Next-Gen WAF programmat
  name: Signal Sciences Core API
  slug: core-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.signalsciences.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fastly.com/documentation/signalsciences/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fastly.com/documentation/signalsciences/
- group: docs
  title: ''
  type: APIReference
  url: https://www.fastly.com/documentation/reference/api/ngwaf/
- group: auth
  title: ''
  type: Authentication
  url: authentication/signal-sciences-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/signal-sciences-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/signal-sciences-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signal-sciences-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signal-sciences-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signal-sciences-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signalsciences
created: '2026-07-17'
description: Signal Sciences is a web application and API protection (WAAP) company whose Next-Gen Web Application Firewall (WAF) and Runtime Application Self-Protection (RASP) defend web apps, APIs, and microservices against the OWASP Top 10, account takeover, and malicious bots without the tuning burden of legacy WAFs. Founded in 2014 by Andrew Peterson, Nick Galbreath, and Zane Lackey and backed by CRV, Index Ventures, and others, Signal Sciences was acquired by Fastly in October 2020 for approximately $775M and is now sold as the Fastly Next-Gen WAF. The product retains its own control plane and REST API at dashboard.signalsciences.net/api/v0, which remains live for existing customers and lets developers programmatically manage corps, sites, requests, events, custom signals, rules, redactions, lists, rate-limited sources, thresholds, virtual patches, and workspace alerts. Product documentation now lives on the Fastly developer documentation site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signal-sciences.png
layout: provider
modified: '2026-07-21'
name: Signal Sciences
nav: Providers
network: true
overview: 'Signal Sciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Web Application Firewall, WAF, and API Security.


  Signal Sciences'' developer surface includes documentation, API reference, authentication, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Signal Sciences Authentication
  slug: signal-sciences-authentication
  summary_line: token · 2 schemes
- kind: domain-security
  name: Signal Sciences Domain Security
  slug: signal-sciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: signal-sciences
tags:
- Company
- Security
- Web Application Firewall
- WAF
- API Security
- RASP
- Application Security
- Bot Protection
website: https://www.signalsciences.com/
---
