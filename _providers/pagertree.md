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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: PagerTree provides an incident management platform with APIs for managing on‑call schedules, alerts, and integrations. Documentation is hosted at the /docs/ site.
  name: PagerTree API
  slug: pagertree-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://pagertree.com/security
- group: agent
  href: https://artifacts.apis.io/pagertree/llms/pagertree-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pagertree-llms.txt
- group: other
  href: https://artifacts.apis.io/pagertree/hosts/pagertree-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pagertree-hosts.yml
- group: other
  href: https://artifacts.apis.io/pagertree/vendors/pagertree-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pagertree-vendors.yml
- group: build
  href: https://artifacts.apis.io/pagertree/packages/pagertree-packages.yml
  title: ''
  type: SDKs
  url: packages/pagertree-packages.yml
- group: build
  href: https://artifacts.apis.io/pagertree/packages/pagertree-packages.yml
  title: ''
  type: Packages
  url: packages/pagertree-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pagertree.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pagertree.com/
- group: auth
  title: ''
  type: Security
  url: https://pagertree.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pagertree.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://pagertree.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.pagertree.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PagerTree
- group: company
  title: ''
  type: Blog
  url: https://pagertree.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://pagertree.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagertree.com/
- group: auth
  href: https://artifacts.apis.io/pagertree/security/pagertree-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pagertree-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pagertree/security/pagertree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagertree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pagertree.com/
coverage:
  checked: '2026-10-27'
  detail: Documentation is served via Docusaurus with a JavaScript‑rendered site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://pagertree.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: PagerTree provides an incident management platform that aggregates alerts from various monitoring tools and routes them to on‑call responders via multiple channels such as email, SMS, phone, and mobile push. The service offers customizable escalation policies, integrations with popular services like PagerDuty, Opsgenie, Slack, and supports webhook endpoints for automated incident creation. It aims to improve reliability and response times for engineering teams handling production incidents.
image: https://pagertree.com/lib_yteZXpJQdUuJWoOB/kjk5nze8tj0eenxe.svg?w=1200&h=630&fit=crop
layout: provider
modified: '2026-10-26'
name: PagerTree
nav: Providers
network: true
overview: 'PagerTree is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  PagerTree''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 15.8
  previous_composite: 28.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pagertree/pagertree-2026-11-03T140849.png
security:
- kind: domain-security
  name: Pagertree Domain Security
  slug: pagertree-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pagertree Trust Center
  slug: pagertree-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: pagertree
tags:
- Company
website: https://pagertree.com/
---
