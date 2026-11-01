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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/skuplugs/plans/skuplugs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skuplugs-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/skuplugs/llms/skuplugs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skuplugs-llms.txt
- group: agent
  href: https://artifacts.apis.io/skuplugs/well-known/skuplugs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skuplugs-well-known.yml
- group: other
  href: https://artifacts.apis.io/skuplugs/hosts/skuplugs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skuplugs-hosts.yml
- group: other
  href: https://artifacts.apis.io/skuplugs/vendors/skuplugs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skuplugs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skuplugs.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skuplugs.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://skuplugs.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://skuplugs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skuplugs
- group: auth
  href: https://artifacts.apis.io/skuplugs/security/skuplugs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skuplugs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skuplugs.com/
coverage:
  checked: '2026-10-27'
  detail: The provider's website is a JavaScript‑rendered site with no publicly available OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://skuplugs.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: SKUPlugs provides a no‑code solution to sync inventory, products and orders across major POS and e‑commerce platforms such as Lightspeed, Square, Loyverse, Zoho, Shopify, WooCommerce, Amazon and Walmart. Users can connect their POS, configure mappings, and automate inventory synchronization without writing code, benefiting from a 15‑day free trial and multi‑channel support.
image: https://skuplugs.com/wp-content/uploads/2026/06/SKUPlugs-homepage.jpg
layout: provider
modified: '2026-10-27'
name: SKUPLUGS
nav: Providers
network: true
overview: 'SKUPLUGS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include eCommerce, InventorySync, NoCode, POSIntegration, and MultiChannel.


  SKUPLUGS''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Skuplugs Plans Pricing
  plan_count: 4
  slug: skuplugs-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Skuplugs Domain Security
  slug: skuplugs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: skuplugs
tags:
- eCommerce
- InventorySync
- NoCode
- POSIntegration
- MultiChannel
website: https://skuplugs.com/
---
