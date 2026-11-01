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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/weareocta-com/plans/weareocta-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weareocta-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://weareocta.com/security
- group: design
  href: https://artifacts.apis.io/weareocta-com/conformance/weareocta-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weareocta-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/weareocta-com/llms/weareocta-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weareocta-com-llms.txt
- group: other
  href: https://artifacts.apis.io/weareocta-com/hosts/weareocta-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weareocta-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weareocta.com/lps/terms
- group: operate
  title: ''
  type: Support
  url: https://weareocta.com/support
- group: auth
  title: ''
  type: Security
  url: https://weareocta.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weareocta.com/lps/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://weareocta.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://weareocta.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://weareocta.com/resources/blog/will-ai-replace-cpas/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WeAreOcta
- group: auth
  href: https://artifacts.apis.io/weareocta-com/security/weareocta-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/weareocta-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/weareocta-com/security/weareocta-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weareocta-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weareocta.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://weareocta.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Octa provides an AI-powered workforce for accounting firms, automating client work, relationship management, and practice growth. The platform leverages artificial intelligence to streamline accounting processes, improve efficiency, and enable firms to scale services while maintaining high-quality client interactions.
image: https://weareocta.com/og-image.png
layout: provider
modified: '2026-10-25'
name: Octa
nav: Providers
network: true
overview: 'Octa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Accounting, SaaS, and Workforce.


  Octa''s developer surface includes support, pricing, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Weareocta Com Plans Pricing
  plan_count: 3
  slug: weareocta-com-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Weareocta Com Domain Security
  slug: weareocta-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Weareocta Com Trust Center
  slug: weareocta-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: weareocta-com
tags:
- Company
- AI
- Accounting
- SaaS
- Workforce
website: https://weareocta.com
---
