---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A live, remotely-callable Model Context Protocol server for Wyatt's Dr.FORHAIR direct-to-consumer storefront. Six tools cover catalog search, product detail, checkout-URL creation, customer order hist
  name: Dr.FORHAIR Storefront MCP Server
  slug: drforhair-storefront-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wyatt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wyatt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wyattcorp.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wyatt-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wyatt-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wyatt-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/wyatt-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wyatt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wyatt-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wyatt-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drforhair.co.kr/member/agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drforhair.co.kr/member/privacy.html
- group: start
  title: ''
  type: SignUp
  url: https://drforhair.co.kr/member/join.html
- group: operate
  title: ''
  type: Support
  url: https://drforhair.co.kr/shopinfo/guide.html
created: '2026-09-04'
description: 'Wyatt Corp. (주식회사 와이어트) is a South Korean beauty and personal-care company headquartered in Gangnam, Seoul. It owns and operates the Dr.FORHAIR scalp and hair-care brand — ranked first in the Korea Consumer Satisfaction Index shampoo category for twelve consecutive years — alongside the UNOVE and Tangle Angel brands, and it built and operated Kakao Hair Shop, the salon-booking service inside KakaoTalk. Wyatt is a consumer-products company rather than a software vendor: it publishes no developer portal, no public API program and no OpenAPI. Its only machine-readable, agent-callable surface is the Model Context Protocol endpoint attached to its Dr.FORHAIR direct-to-consumer storefront, which is operated on its behalf by the Cafe24 commerce platform and advertised from Wyatt''s own domain via RFC 9728 protected-resource metadata.'
image: https://drforhair.co.kr/web/upload/share-image-1-2b0d3336e497f1cc904d314e5eed16c8.png
layout: provider
mcp_servers:
- description: ''
  name: Dr.FORHAIR Storefront MCP Server
  slug: drforhair-storefront-mcp-server
modified: '2026-09-04'
name: Wyatt
nav: Providers
network: true
overview: 'Wyatt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Personal Care, Haircare, and Consumer Products.


  Wyatt''s developer surface includes signup flow, support, and 13 more developer resources.'
plans:
- name: Wyatt Plans Pricing
  plan_count: 0
  slug: wyatt-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Wyatt Rate Limits
  slug: wyatt-rate-limits
scopes:
- name: Wyatt Scopes
  scope_count: 0
  slug: wyatt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 1.9
    developer_ergonomics: 18.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 20.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Wyatt Authentication
  slug: wyatt-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Wyatt Domain Security
  slug: wyatt-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wyatt Vulnerability Disclosure
  slug: wyatt-vulnerability-disclosure
  summary_line: Hackerone
slug: wyatt
tags:
- Company
- Beauty
- Personal Care
- Haircare
- Consumer Products
- E-Commerce
- Retail
- Agentic Commerce
- Model Context Protocol
- South Korea
website: https://wyattcorp.com/
---
