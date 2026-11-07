---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/catalent/finops/catalent-finops.yml
  title: ''
  type: FinOps
  url: finops/catalent-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.catalent.com
- group: company
  title: ''
  type: Blog
  url: https://www.catalent.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.catalent.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.catalent.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.catalent.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/catalent-data-science-community
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/catalent
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Catalent_
- group: agent
  href: https://artifacts.apis.io/catalent/llms/catalent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catalent-llms.txt
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.catalent.com/privacy-request
- group: other
  href: https://artifacts.apis.io/catalent/regulatory/catalent-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/catalent-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/catalent/plans/catalent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/catalent-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/catalent/rate-limits/catalent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/catalent-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/catalent/security/catalent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalent-domain-security.yml
coverage:
  checked: '2026-09-19'
  detail: Catalent is a pharmaceutical CDMO whose only software surface is the login-gated OneHub clinical-supply portal on Salesforce Experience Cloud; the developer.catalent.com and api.catalent.com hosts the prior record named do not exist in DNS, the 1,352-URL sitemap and first-party llms.txt list no developer, API or integration page, every OpenAPI, .well-known, agent-card and APIs.json discovery path 404s on www, apex and clinical.catalent.com, and no package registry or first-party GitHub repo ships a client library.
  evidence:
  - status: 0
    url: https://developer.catalent.com/docs
  - status: 0
    url: https://api.catalent.com
  - status: 404
    url: https://www.catalent.com/developers
  - status: 404
    url: https://www.catalent.com/openapi.json
  - status: 404
    url: https://www.catalent.com/.well-known/api-catalog
  - status: 404
    url: https://www.catalent.com/.well-known/agent-card.json
  - status: 200
    url: https://www.catalent.com/llms.txt
  - status: 200
    url: https://catalent.my.site.com/onehub/s/login/
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Catalent is a global pharmaceutical contract development and manufacturing organization (CDMO) headquartered in Somerset, New Jersey, and owned by Novo Holdings since December 2024. It develops, manufactures and supplies medicines and consumer health products for biopharma, biotech and self-care brands across biologics, cell and gene therapy, oral and injectable dose forms, clinical supply and consumer health, from roughly forty facilities. Catalent has no developer program: it publishes no API, OpenAPI, SDK, package, MCP server or agent card, and the developer.catalent.com and api.catalent.com hosts an earlier catalog record assumed do not exist in DNS. Its only customer-facing software surface is the OneHub clinical-supply portal, a login-gated Salesforce Experience Cloud site. It does publish a first-party llms.txt index of its corporate site and a working privacy-request form; both are captured here, and nothing has been authored on its behalf.'
finops:
- has_sources: true
  method: generated
  name: Catalent Finops
  primary_unit: ''
  service_category: Pharmaceutical Services
  slug: catalent-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catalent.png
layout: provider
modified: '2026-09-19'
name: Catalent
nav: Providers
network: true
overview: 'Catalent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceutical Services, Drug Delivery, CDMO, Biologics, and Cell and Gene Therapy.


  Catalent''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Catalent Plans Pricing
  plan_count: 0
  slug: catalent-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Catalent Rate Limits
  slug: catalent-rate-limits
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/catalent/catalent-2026-06-20T174043.png
security:
- kind: domain-security
  name: Catalent Domain Security
  slug: catalent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catalent
tags:
- Pharmaceutical Services
- Drug Delivery
- CDMO
- Biologics
- Cell and Gene Therapy
- Clinical Supply
- Consumer Health
- No Developer Program
website: https://www.catalent.com
---
