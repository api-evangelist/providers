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
- group: commercial
  href: https://artifacts.apis.io/lifelock-com/plans/lifelock-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lifelock-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/lifelock-com/llms/lifelock-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lifelock-com-llms.txt
- group: other
  href: https://artifacts.apis.io/lifelock-com/hosts/lifelock-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lifelock-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lifelock-com/vendors/lifelock-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lifelock-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.norton.com/terms-of-sale
- group: operate
  title: ''
  type: StatusPage
  url: https://status.norton.com
- group: auth
  title: ''
  type: Security
  url: https://us.norton.com/blog/security
- group: commercial
  title: ''
  type: Pricing
  url: https://us.norton.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://us.norton.com/blog
- group: auth
  href: https://artifacts.apis.io/lifelock-com/security/lifelock-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifelock-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lifelock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lifelock.norton.com/learn
- group: operate
  title: ''
  type: Support
  url: https://support.norton.com/lifelock/en/us/home/current/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.norton.com/privacy/general-privacy-notice
coverage:
  checked: '2026-10-25'
  detail: Documentation pages are HTML without any OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://lifelock.norton.com/learn
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: LifeLock provides identity theft protection services, offering plans that safeguard personal and financial information for individuals and families. The company delivers monitoring, alerts, and recovery assistance to prevent and address identity fraud. Through its platform, users can manage protection levels, receive real‑time notifications, and access resources on credit, fraud, and personal data security. LifeLock’s services are integrated with Norton, extending its reach in consumer security solutions.
image: https://lifelock.norton.com/media_1e614c5b12803b36eb69ce75e0b3e4fd19616f376.jpg?width=1200&format=pjpg&optimize=medium
layout: provider
modified: '2026-10-25'
name: LifeLock
nav: Providers
network: true
overview: 'LifeLock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Identity Protection, Consumer Security, Credit Monitoring, Fraud Prevention, and Family Plans.


  LifeLock''s developer surface includes pricing, engineering blog, documentation, support, and 10 more developer resources.'
plans:
- name: Lifelock Com Plans Pricing
  plan_count: 5
  slug: lifelock-com-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lifelock Com Domain Security
  slug: lifelock-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lifelock-com
tags:
- Identity Protection
- Consumer Security
- Credit Monitoring
- Fraud Prevention
- Family Plans
website: https://www.lifelock.com/
---
