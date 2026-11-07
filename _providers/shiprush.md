---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/shiprush/rules/shiprush-rules.yml
  title: ''
  type: Spectral
  url: rules/shiprush-rules.yml
- group: design
  href: https://artifacts.apis.io/shiprush/vocabulary/shiprush-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shiprush-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shiprush/conformance/shiprush-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shiprush-conformance.yml
- group: auth
  href: https://artifacts.apis.io/shiprush/well-known/shiprush-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shiprush-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/shiprush/plans/shiprush-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shiprush-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/shiprush/changelog/shiprush-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shiprush-changelog.yml
- group: agent
  href: https://artifacts.apis.io/shiprush/well-known/shiprush-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shiprush-well-known.yml
- group: other
  href: https://artifacts.apis.io/shiprush/hosts/shiprush-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shiprush-hosts.yml
- group: other
  href: https://artifacts.apis.io/shiprush/vendors/shiprush-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shiprush-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shiprush.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://my.shiprush.com/pageblobs/PrivacyPolicy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shiprush.com/developer/sql/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shiprush.com/en/introduction-to-descartes-shiprush-web/the-basics/getting-started-links
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shiprush.com/
- group: auth
  href: https://artifacts.apis.io/shiprush/security/shiprush-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiprush-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shiprush.com/
- group: company
  title: ''
  type: Blog
  url: https://shiprush.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://shiprush.com/pricing/
- group: company
  title: ''
  type: AboutUs
  url: https://shiprush.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://shiprush.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://my.shiprush.com/SignUp/SignUp
coverage:
  checked: '2026-10-27'
  detail: The ShipRush documentation site provides only HTML pages without a downloadable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specification.
  evidence:
  - status: 200
    url: https://docs.shiprush.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ShipRush provides multi‑carrier shipping software for growing ecommerce businesses, offering features such as rate shopping, automation, white‑label branding, and integrations with major platforms like Shopify, Amazon, eBay, and Netsuite. The solution helps merchants ship faster, reduce costs, and streamline order fulfillment across multiple carriers.
image: https://shiprush.com/wp-content/uploads/2023/09/shiprush-share-logo-1.png
layout: provider
modified: '2026-10-27'
name: ShipRush
nav: Providers
network: true
overview: 'ShipRush is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, E-Commerce, Multi-Carrier, Software-as-a-Service, and Company.


  The ShipRush catalog on APIs.io includes 1 Spectral governance ruleset.


  ShipRush''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Shiprush Plans Pricing
  plan_count: 4
  slug: shiprush-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: ShipRush API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: shiprush-rules
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 34.2
  previous_composite: 30.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/shiprush/shiprush-2026-11-03T143125.png
security:
- kind: domain-security
  name: Shiprush Domain Security
  slug: shiprush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shiprush
tags:
- Shipping
- E-Commerce
- Multi-Carrier
- Software-as-a-Service
- Company
website: https://shiprush.com/
---
