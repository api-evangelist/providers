---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Equilibria provides premium CBD and wellness supplements specifically formulated for women.
  name: Equilibria API
  slug: equilibria-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equilibria/refs/heads/main/llms/equilibria-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/equilibria-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equilibria/refs/heads/main/well-known/equilibria-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/equilibria-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/equilibria/refs/heads/main/hosts/equilibria-hosts.yml
  title: ''
  type: Hosts
  url: hosts/equilibria-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/equilibria/refs/heads/main/vendors/equilibria-vendors.yml
  title: ''
  type: Vendors
  url: vendors/equilibria-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.myeq.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.myeq.com/policies/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.myeq.com/blogs/home/price-reduction-to-make-your-wellness-a-priority
- group: company
  title: ''
  type: Newsroom
  url: https://shop.myeq.com/pages/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myeq
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/equilibria/refs/heads/main/security/equilibria-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/equilibria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myeq.com
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract could be retrieved despite accessible docs.
  evidence:
  - status: 200
    url: https://myeq.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Equilibria provides premium CBD and wellness supplements specifically formulated for women. The brand focuses on natural, high-quality ingredients to support relaxation, sleep, hormone balance, and overall wellbeing. Their product line includes oils, gummies, topicals, and personalized wellness kits, sold through an online shop and supported by educational resources and a community focused on health and self-care.
image: http://shop.myeq.com/cdn/shop/files/EquilibriaWomen.png?v=1774545208
layout: provider
modified: '2026-10-12'
name: Equilibria
nav: Providers
network: true
overview: 'Equilibria is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Wellness, CBD, and Women.


  Equilibria''s developer surface includes pricing and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Equilibria Domain Security
  slug: equilibria-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equilibria
tags:
- Company
- Health
- Wellness
- CBD
- Women
website: https://myeq.com
---
