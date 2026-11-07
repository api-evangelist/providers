---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SendFaxFast API allows sending faxes via a POST /send-fax.php endpoint.
  name: SendFaxFast API
  slug: sendfaxfast-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/sendfaxfast-com/plans/sendfaxfast-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendfaxfast-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/sendfaxfast-com/authentication/sendfaxfast-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendfaxfast-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/sendfaxfast-com/errors/sendfaxfast-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendfaxfast-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/sendfaxfast-com/llms/sendfaxfast-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendfaxfast-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/sendfaxfast-com/well-known/sendfaxfast-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sendfaxfast-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sendfaxfast-com/hosts/sendfaxfast-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendfaxfast-com-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://sendfaxfast.com/plans.html
- group: auth
  href: https://artifacts.apis.io/sendfaxfast-com/security/sendfaxfast-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendfaxfast-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendfaxfast.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sendfaxfast.com/api-docs
- group: company
  title: ''
  type: Blog
  url: https://sendfaxfast.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendfaxfast.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendfaxfast.com/privacy-policy.html
coverage:
  checked: '2026-10-30'
  detail: API documentation is public HTML but provides no machine‑readable OpenAPI/Swagger/GraphQL spec.
  evidence:
  - status: 200
    url: https://sendfaxfast.com/api-docs.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: SendFaxFast provides an online fax service that allows users to send faxes to the IRS, Social Security Administration, Veterans Affairs, Canada Revenue Agency, and medical providers without a physical fax machine. Operating from Germany and run by Alexander Mäding, the platform offers low-cost pricing starting at $2.89 per fax, includes proof of delivery, and guarantees a full refund if a fax is not delivered. The service supports PDF, JPG, and PNG files up to 10 MB and integrates via a public API documented at /api-docs.
image: https://sendfaxfast.com/sendfaxfast-og.png
layout: provider
modified: '2026-10-30'
name: sendfaxfast-com
nav: Providers
network: true
overview: 'sendfaxfast-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fax, Payments, Healthcare, Government, and Germany.


  sendfaxfast-com''s developer surface includes authentication, pricing, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Sendfaxfast Com Plans Pricing
  plan_count: 6
  slug: sendfaxfast-com-plans-pricing
random_paper: 3
scopes:
- name: Sendfaxfast Com Scopes
  scope_count: 0
  slug: sendfaxfast-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sendfaxfast-com/sendfaxfast-com-2026-11-03T143023.png
security:
- kind: authentication
  name: Sendfaxfast Com Authentication
  slug: sendfaxfast-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sendfaxfast Com Domain Security
  slug: sendfaxfast-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sendfaxfast-com
tags:
- Fax
- Payments
- Healthcare
- Government
- Germany
website: https://sendfaxfast.com/
---
