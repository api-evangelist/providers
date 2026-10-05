---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Braintrust platform
  name: Braintrust API
  slug: braintrust-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braintrustbac9/refs/heads/main/llms/braintrustbac9-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/braintrustbac9-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braintrustbac9/refs/heads/main/well-known/braintrustbac9-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/braintrustbac9-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braintrustbac9/refs/heads/main/hosts/braintrustbac9-hosts.yml
  title: ''
  type: Hosts
  url: hosts/braintrustbac9-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braintrustbac9/refs/heads/main/vendors/braintrustbac9-vendors.yml
  title: ''
  type: Vendors
  url: vendors/braintrustbac9-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.usebraintrust.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usebraintrust.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.usebraintrust.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usebraintrust.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braintrustbac9/refs/heads/main/security/braintrustbac9-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braintrustbac9-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usebraintrust.com
- group: company
  title: ''
  type: Blog
  url: https://www.usebraintrust.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usebraintrust.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usebraintrust.com/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.usebraintrust.com/about
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/braintrustbac9
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Braintrust is an AI infrastructure company offering a talent marketplace, AI interview software (AIR), and workflow automation (Nexus). It connects enterprises with 2M+ vetted professionals, provides AI‑powered recruiting, and builds AI tools for enterprise work. Founded in 2018, Braintrust delivers transparent pricing and compliance solutions for modern talent acquisition.
image: https://www.usebraintrust.com/og-image.png
layout: provider
modified: '2026-10-03'
name: Braintrustbac9
nav: Providers
network: true
overview: 'Braintrustbac9 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Marketplace, AI Recruiting, Enterprise Hiring, Workflow Automation, and Human Data Infrastructure.


  Braintrustbac9''s developer surface includes support, pricing, documentation, engineering blog, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Braintrustbac9 Domain Security
  slug: braintrustbac9-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: braintrustbac9
tags:
- Talent Marketplace
- AI Recruiting
- Enterprise Hiring
- Workflow Automation
- Human Data Infrastructure
website: https://www.usebraintrust.com
---
