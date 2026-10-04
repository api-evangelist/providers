---
access_model:
  confidence: high
  label: No public API access path
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.amedisys.com/
- group: company
  title: ''
  type: About
  url: https://www.amedisys.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.amedisys.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.amedisys.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://resources.amedisys.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amedisys.com/terms-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amedisys.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.amedisys.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.amedisys.com/careers-home/
- group: other
  title: ''
  type: Locations
  url: https://www.amedisys.com/locations/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amedisys
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amedisys/refs/heads/main/security/amedisys-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amedisys-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amedisys/refs/heads/main/llms/amedisys-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amedisys-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amedisys/refs/heads/main/plans/amedisys-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amedisys-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amedisys/refs/heads/main/rate-limits/amedisys-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amedisys-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: Amedisys is a home health, hospice and palliative care-delivery organization — now an Optum subsidiary — whose product is nursing care in patients' homes, not software; the two hosts this profile previously claimed, developer.amedisys.com and api.amedisys.com, have no DNS record at all and never resolved, and on the real corporate site every discovery path probed (/developers, /api, /api-docs, /openapi.json, /swagger.json, /graphql, /wp-json/, /mcp, /llms.txt and nine /.well-known/* paths) returns a genuine 404 — verified genuine by a control path that also 404s — while npm, PyPI and RubyGems return zero packages and the only Amedisys GitHub accounts are empty shells with no public repositories.
  evidence:
  - status: 0
    url: https://developer.amedisys.com/
  - status: 0
    url: https://api.amedisys.com/
  - status: 404
    url: https://www.amedisys.com/openapi.json
  - status: 404
    url: https://www.amedisys.com/developers
  - status: 404
    url: https://www.amedisys.com/llms.txt
  - status: 404
    url: https://www.amedisys.com/.well-known/agent-card.json
  - status: 404
    url: https://www.amedisys.com/.well-known/security.txt
  - status: 404
    url: https://www.amedisys.com/zz-api-evangelist-control
  - status: 200
    url: https://api.github.com/orgs/amedisys-appdev
  - status: 200
    url: https://www.amedisys.com/
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Amedisys, Inc. is a United States home health, hospice, palliative and high-acuity in-home care company headquartered in Baton Rouge, Louisiana. Founded in 1982, it delivers skilled nursing, physical and occupational therapy, medical social work, hospice and palliative care through a nationwide network of care centers, and — through Contessa, an Amedisys company — hospital-level and skilled-nursing-level care delivered in the patient''s home in partnership with health systems and payers. Formerly listed on Nasdaq as AMED, Amedisys was acquired by UnitedHealth Group''s Optum in a $3.3 billion all-cash transaction that closed in August 2025 after a Department of Justice settlement requiring the divestiture of 164 home health and hospice locations; it continues to operate under the Amedisys brand. Amedisys publishes no public API: there is no developer portal, no API reference, no OpenAPI, GraphQL, AsyncAPI, gRPC or SOAP contract, no SDK on any package registry, no MCP server
  and no A2A agent card. Clinical data moves between Amedisys, its referral sources, its EHR vendors and payers under HIPAA business-associate agreements and bilateral integration contracts rather than through a documented public interface.'
finops:
- name: Amedisys Finops
  service_category: Healthcare
  slug: amedisys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amedisys.png
layout: provider
modified: '2026-09-02'
name: Amedisys
nav: Providers
network: true
overview: 'Amedisys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Home Health, Hospice, and Palliative Care.


  Amedisys'' developer surface includes support, FAQ, engineering blog, and 12 more developer resources.'
plans:
- name: Amedisys Plans Pricing
  plan_count: 0
  slug: amedisys-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Amedisys Rate Limits
  slug: amedisys-rate-limits
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/amedisys/refs/heads/main/screenshots/amedisys-2026-06-20T171900.png
security:
- kind: domain-security
  name: Amedisys Domain Security
  slug: amedisys-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: amedisys
tags:
- Company
- Healthcare
- Home Health
- Hospice
- Palliative Care
- Home Care
- Health Systems
- Care Delivery
- Post-Acute Care
- Hospital at Home
website: https://www.amedisys.com/
---
