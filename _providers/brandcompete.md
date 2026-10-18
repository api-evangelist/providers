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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brandcompete/refs/heads/main/llms/brandcompete-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandcompete-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brandcompete/refs/heads/main/hosts/brandcompete-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandcompete-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brandcompete/refs/heads/main/packages/brandcompete-packages.yml
  title: ''
  type: SDKs
  url: packages/brandcompete-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brandcompete/refs/heads/main/packages/brandcompete-packages.yml
  title: ''
  type: Packages
  url: packages/brandcompete-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandcompete
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brandcompete/refs/heads/main/security/brandcompete-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandcompete-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandcompete.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.brandcompete.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.brandcompete.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.brandcompete.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.brandcompete.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.brandcompete.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brandcompete.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brandcompete.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brandcompete.com/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://brandcompete.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Brandcompete provides competitive intelligence tools that help businesses monitor and analyze brand performance across various digital channels. The platform aggregates data from social media, search trends, and market research to deliver actionable insights, enabling companies to benchmark against competitors, track sentiment, and identify emerging opportunities. With customizable dashboards and reporting features, Brandcompete supports strategic decision‑making for marketing, product development, and executive leadership.
layout: provider
modified: '2026-10-16'
name: Brandcompete
nav: Providers
network: true
overview: 'Brandcompete is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Consulting, Data Intelligence, Process Automation, Enterprise Software, and Artificial Intelligence.


  Brandcompete''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brandcompete Domain Security
  slug: brandcompete-domain-security
  summary_line: TLSv1.2 · HSTS
slug: brandcompete
tags:
- Cloud Consulting
- Data Intelligence
- Process Automation
- Enterprise Software
- Artificial Intelligence
- GDPR Compliance
website: https://brandcompete.com/
---
