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
- description: Nomad provides AI-driven data insights platform; API details are not publicly documented.
  name: Nomad Data API
  slug: nomad-data-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.nomad-data.com/security
- group: agent
  href: https://artifacts.apis.io/nomad-data-com/llms/nomad-data-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nomad-data-com-llms.txt
- group: other
  href: https://artifacts.apis.io/nomad-data-com/hosts/nomad-data-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nomad-data-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/nomad-data-com/vendors/nomad-data-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nomad-data-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.nomad-data.com/_hcms/mem/saml?redirect_url=https%3A%2F%2Fhelp.nomad-data.com%2F
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nomad-data.com/
- group: auth
  title: ''
  type: Security
  url: https://www.nomad-data.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nomad-data.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nomad-data.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.nomad-data.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.nomad-data.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.nomad-data.com/
- group: auth
  href: https://artifacts.apis.io/nomad-data-com/security/nomad-data-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nomad-data-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/nomad-data-com/security/nomad-data-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nomad-data-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nomad-data.com/
coverage:
  checked: '2026-10-25'
  detail: Provider docs are rendered via JavaScript and no machine‑readable spec could be retrieved.
  evidence:
  - status: 200
    url: https://www.nomad-data.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Nomad provides a platform that lets organizations query and extract insights from unstructured text across thousands of documents and centralize data relationships like a CRM. It offers access to over 5,600 external data providers and tools for data spend audit, request routing, and AI‑powered search, enabling knowledge workers to obtain instant, source‑linked answers and manage data subscriptions in one system.
image: https://cdn.prod.website-files.com/60b79cb8dcca8ad97d2ba9ab/66c49eaeebca4d44bcaf068f_Nomad-Data-Logo.png
layout: provider
modified: '2026-10-25'
name: Nomad
nav: Providers
network: true
overview: 'Nomad is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Catalog, Document Insights, Data Relationship Manager, AI Search, and Data Spend Management.


  Nomad''s developer surface includes support, pricing, changelog, engineering blog, documentation, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 22.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nomad-data-com/nomad-data-com-2026-11-03T140254.png
security:
- kind: domain-security
  name: Nomad Data Com Domain Security
  slug: nomad-data-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nomad Data Com Trust Center
  slug: nomad-data-com-trust-center
  summary_line: SOC 2, HIPAA
slug: nomad-data-com
tags:
- Data Catalog
- Document Insights
- Data Relationship Manager
- AI Search
- Data Spend Management
website: https://www.nomad-data.com/
---
