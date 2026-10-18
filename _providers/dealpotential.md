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
api_count: 1
apis:
- description: DealPotential provides a platform for managing sales pipelines and deals.
  name: DealPotential API
  slug: dealpotential-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealpotential/refs/heads/main/hosts/dealpotential-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealpotential-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealpotential/refs/heads/main/vendors/dealpotential-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealpotential-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealpotential.com/terms-conditions/
- group: start
  title: ''
  type: SignUp
  url: https://dealpotential.com/register/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealpotential.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealpotential/refs/heads/main/security/dealpotential-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealpotential-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealpotential.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dealpotential.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://dealpotential.com/blog/
coverage:
  checked: '2026-10-15'
  detail: The provider's website offers HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://dealpotential.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: DealPotential is a company data aggregator created for faster deal sourcing and efficient due diligence. It provides comprehensive company information for private equity, venture capital, and investment banks, helping streamline deal evaluation and research processes.
image: https://dealpotential.com/wp-content/uploads/2024/01/dealpotential-featured-image-1-scaled.jpg
layout: provider
modified: '2026-10-15'
name: DealPotential
nav: Providers
network: true
overview: 'DealPotential is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Aggregator, Private Equity, and Venture Capital.


  DealPotential''s developer surface includes signup flow, pricing, engineering blog, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dealpotential Domain Security
  slug: dealpotential-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dealpotential
tags:
- Company
- Data
- Aggregator
- Private Equity
- Venture Capital
website: https://dealpotential.com/
---
