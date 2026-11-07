---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cavco-industries/plans/cavco-industries-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cavco-industries-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cavco-industries/rate-limits/cavco-industries-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cavco-industries-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cavco-industries/finops/cavco-industries-finops.yml
  title: ''
  type: FinOps
  url: finops/cavco-industries-finops.yml
- group: auth
  href: https://artifacts.apis.io/cavco-industries/security/cavco-industries-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cavco-industries-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cavco-industries-inc-
- group: company
  title: ''
  type: Website
  url: https://www.cavco.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cavcohomes.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cavcohomes.com/contact
- group: company
  title: ''
  type: Newsroom
  url: https://investor.cavco.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://investor.cavco.com/management/
- group: agent
  href: https://artifacts.apis.io/cavco-industries/llms/cavco-industries-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cavco-industries-llms.txt
- group: other
  href: https://artifacts.apis.io/cavco-industries/regulatory/cavco-industries-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/cavco-industries-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/cavco-industries/regulatory/cavco-industries-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/cavco-industries-regulatory-posture.yml
coverage:
  checked: '2026-09-19'
  detail: 'Cavco Industries builds and sells factory-built homes, and software is not a product it sells: the developer.cavco.com and api.cavco.com hosts a prior profile recorded are NXDOMAIN, no api./docs./dev. host, OpenAPI, GraphQL, MCP, agent card, llms.txt, well-known document, GitHub organization or package exists on any of its seven live hosts, and its only integration property is the login-gated CavConnect Angular retailer portal whose backend host cavconnectdata.cavco.com (named in the portal''s public bundle) does not resolve from the public internet — the one open JSON surface, www.cavcohomes.com/resourceapi/*, is the stock Bloomreach CMS page-delivery API the site''s SPA renders from, not a Cavco-designed API.'
  evidence:
  - status: 0
    url: https://developer.cavco.com/docs
  - status: 0
    url: https://api.cavco.com/openapi.json
  - status: 301
    url: https://www.cavco.com
  - status: 404
    url: https://www.cavcohomes.com/openapi.json
  - status: 404
    url: https://www.cavcohomes.com/.well-known/agent-card.json
  - status: 404
    url: https://www.cavcohomes.com/llms.txt
  - status: 200
    url: https://cavconnect.cavco.com/
  - status: 0
    url: https://cavconnectdata.cavco.com/rest/api
  - status: 200
    url: https://www.cavcohomes.com/resourceapi/
  - status: 200
    url: https://api.github.com/users/cavcoindustries
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Cavco Industries, Inc. (Nasdaq: CVCO), founded in Phoenix, Arizona in 1965, designs and builds factory-built housing — manufactured homes, modular homes, park model RVs and vacation cabins — at more than twenty plants across the United States, sold through independent and company-owned retailers under the Cavco family of brands (including Fleetwood Homes and Palm Harbor Homes), with financing through its CountryPlace Mortgage subsidiary and homeowner insurance through Standard Casualty. It is a Fortune 1000 home builder, not a software vendor: it publishes no developer program, API reference, OpenAPI, SDK or webhook surface. Its only integration property is a login-gated Angular retailer portal (CavConnect, cavconnect.cavco.com) whose backend host is not publicly resolvable. The developer.cavco.com and api.cavco.com hosts an earlier profile scaffolded do not exist in DNS and were removed from this record.'
finops:
- has_sources: true
  method: generated
  name: Cavco Industries Finops
  primary_unit: ''
  service_category: Manufactured Housing
  slug: cavco-industries-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cavco-industries.png
layout: provider
modified: '2026-09-19'
name: Cavco Industries
nav: Providers
network: true
overview: 'Cavco Industries is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufactured Homes, Housing, Modular Homes, Park Model RVs, and Homebuilding.


  Cavco Industries'' developer surface includes support and 12 more developer resources.'
plans:
- name: Cavco Industries Plans Pricing
  plan_count: 1
  slug: cavco-industries-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Cavco Industries Rate Limits
  slug: cavco-industries-rate-limits
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cavco-industries/cavco-industries-2026-06-20T174054.png
security:
- kind: domain-security
  name: Cavco Industries Domain Security
  slug: cavco-industries-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cavco-industries
tags:
- Manufactured Homes
- Housing
- Modular Homes
- Park Model RVs
- Homebuilding
- Manufacturing
- Mortgage Lending
- Insurance
- Real Estate
website: https://www.cavco.com
---
