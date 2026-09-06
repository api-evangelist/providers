---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/86repairs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.86repairs.com/
- group: build
  title: ''
  type: Packages
  url: packages/86repairs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/86repairs-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/86repairs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/86repairs-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.86repairs.com/
- group: operate
  title: ''
  type: Support
  url: https://www.86repairs.com/customer-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://intercom.help/86-repairs-customer-service/en/
- group: start
  title: ''
  type: Login
  url: https://portal.86repairs.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.86repairs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.86repairs.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/86repairs
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@86Repairs
coverage:
  checked: '2026-09-05'
  detail: 86 Repairs ships its repair-management product only as an end-user web portal and mobile apps — no developer subdomain resolves (docs., developer., developers.86repairs.com all fail DNS), the sitemap lists no API, developer or integrations page, and the private portal backend at eightysix-api.86repairs.com returns a real JSON 404 for /openapi.json, /swagger.json, /graphql and every .well-known path while serving only /health.
  evidence:
  - status: 404
    url: https://eightysix-api.86repairs.com/openapi.json
  - status: 404
    url: https://eightysix-api.86repairs.com/graphql
  - status: 200
    url: https://eightysix-api.86repairs.com/health
  - status: 0
    url: https://docs.86repairs.com/
  - status: 0
    url: https://developer.86repairs.com/
  - status: 403
    url: https://api.86repairs.com/
  - status: 200
    url: https://www.86repairs.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '86 Repairs is a restaurant equipment repair and maintenance (R&M) management platform founded in 2018 in Chicago by Daniel Estrada and Joe Gallagher. It manages the repair lifecycle for restaurant operators — 24/7 intake and troubleshooting, warranty verification, dispatch to a vetted service provider network, preventative maintenance scheduling, equipment and asset inventory, invoice assurance and R&M spend analytics — and is used by operators and franchisees of brands including McDonald''s, Wendy''s, Taco Bell, Jersey Mike''s, Five Guys and Wingstop. The product is delivered as an end-user web portal (portal.86repairs.com) and iOS/Android mobile apps, backed by a private NestJS service at eightysix-api.86repairs.com; it is not offered as a developer platform. Parts Town, the Addison, Illinois OEM foodservice parts distributor, acquired 86 Repairs in June 2026 to connect parts availability with repair and service workflows. As of this profile 86 Repairs publishes no public
  API: no developer portal, no API reference, no OpenAPI/AsyncAPI/GraphQL contract, no SDK or package on any public registry, no webhook catalog, no MCP server and no A2A agent card were found on any host it controls.'
image: https://www.86repairs.com/hubfs/86%20Repairs%20for%20Facilities%20Managers%20%281200%20x%20630%20px%29%20%281%29.png
layout: provider
modified: '2026-09-05'
name: 86 Repairs
nav: Providers
network: true
overview: '86 Repairs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Foodservice, Facilities Management, Maintenance, and Field Service Management.


  86 Repairs'' developer surface includes engineering blog, support, YouTube channel, and 11 more developer resources.'
plans:
- name: 86Repairs Plans Pricing
  plan_count: 0
  slug: 86repairs-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 86Repairs Rate Limits
  slug: 86repairs-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 86Repairs Domain Security
  slug: 86repairs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 86repairs
tags:
- Restaurants
- Foodservice
- Facilities Management
- Maintenance
- Field Service Management
- Equipment
- Asset Management
- Hospitality
- Vendor Management
- No Developer Program
website: https://www.86repairs.com/
---
