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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/getphyllo/well-known/getphyllo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getphyllo-status-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.getphyllo.com/security
- group: agent
  href: https://artifacts.apis.io/getphyllo/llms/getphyllo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getphyllo-llms.txt
- group: agent
  href: https://artifacts.apis.io/getphyllo/well-known/getphyllo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getphyllo-well-known.yml
- group: other
  href: https://artifacts.apis.io/getphyllo/hosts/getphyllo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getphyllo-hosts.yml
- group: other
  href: https://artifacts.apis.io/getphyllo/vendors/getphyllo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getphyllo-vendors.yml
- group: build
  href: https://artifacts.apis.io/getphyllo/packages/getphyllo-packages.yml
  title: ''
  type: SDKs
  url: packages/getphyllo-packages.yml
- group: build
  href: https://artifacts.apis.io/getphyllo/packages/getphyllo-packages.yml
  title: ''
  type: Packages
  url: packages/getphyllo-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.getphyllo.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getphyllo.com/
- group: auth
  title: ''
  type: Security
  url: https://www.getphyllo.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getphyllo.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.getphyllo.com/whats-new
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getphyllo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getphyllo
- group: auth
  href: https://artifacts.apis.io/getphyllo/security/getphyllo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getphyllo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/getphyllo/security/getphyllo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getphyllo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getphyllo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.getphyllo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getphyllo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.getphyllo.com/signup/advanced
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getphyllo.com/end-user-agreement
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://getphyllo.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Phyllo provides APIs that give developers access to public and consented social data across 25+ platforms, enabling influencer discovery, brand safety vetting, social listening, background verification, and financial services such as income assessment and visa checks. Their platform consolidates multiple social media sources into a single API, offering tools for creator tools, identity verification, content publishing, and AI-driven insights, aimed at influencer marketing, PR agencies, and financial institutions.
image: https://cdn.prod.website-files.com/624eb8b8eb3aed6e1e68a7d2/626aa9c4370e6db24d09054a_Frame%2048096716%20(1)%20(1).jpg
layout: provider
modified: '2026-10-20'
name: Phyllo
nav: Providers
network: true
overview: 'Phyllo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Data, Influencer Marketing, and Fintech.


  Phyllo''s developer surface includes support, changelog, documentation, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 46.4
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.1
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
screenshot: https://apis.io/screenshots/getphyllo/getphyllo-2026-11-03T132742.png
security:
- kind: domain-security
  name: Getphyllo Domain Security
  slug: getphyllo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getphyllo Trust Center
  slug: getphyllo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: getphyllo
tags:
- Company
- Social Data
- Influencer Marketing
- Fintech
website: https://www.getphyllo.com/
---
