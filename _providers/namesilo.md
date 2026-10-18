---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: 'The NameSilo Domain API allows developers to search, register, transfer, renew, and manage domains programmatically. All API calls use HTTPS GET requests and return XML or JSON. A sandbox environment '
  name: NameSilo Domain API
  slug: namesilo
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/plans/namesilo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/namesilo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/rate-limits/namesilo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/namesilo-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/finops/namesilo-finops.yml
  title: ''
  type: FinOps
  url: finops/namesilo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.namesilo.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/security/namesilo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/namesilo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/namesilo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/namesilo
- group: company
  title: ''
  type: Website
  url: https://www.namesilo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.namesilo.com/api-reference
- group: start
  title: ''
  type: Signup
  url: https://www.namesilo.com/account/api-manager
- group: commercial
  title: ''
  type: Pricing
  url: https://www.namesilo.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.namesilo.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.namesilo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.namesilo.com/privacy-policy
created: '2025-02-09'
description: NameSilo is a domain registrar and web services provider offering domain registration, hosting, email, and SSL solutions. NameSilo exposes a Domain API enabling programmatic domain search, registration, and management via HTTPS GET requests with XML or JSON responses, plus an MCP server for AI agents.
finops:
- has_sources: false
  method: generated
  name: Namesilo Finops
  primary_unit: ''
  service_category: API
  slug: namesilo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/namesilo.png
layout: provider
modified: '2026-10-06'
name: NameSilo
nav: Providers
network: true
overview: 'NameSilo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domains, Domain Registrar, DNS, Hosting, and SSL.


  NameSilo''s developer surface includes engineering blog, documentation, signup flow, pricing, support, and 9 more developer resources.'
plans:
- name: Namesilo Plans Pricing
  plan_count: 3
  slug: namesilo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Namesilo Rate Limits
  slug: namesilo-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/screenshots/namesilo-2026-08-07T184613.png
security:
- kind: domain-security
  name: Namesilo Domain Security
  slug: namesilo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: namesilo
tags:
- Domains
- Domain Registrar
- DNS
- Hosting
- SSL
- Email
website: https://www.namesilo.com/
---
