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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/iffco-tokio/llms/iffco-tokio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iffco-tokio-llms.txt
- group: other
  href: https://artifacts.apis.io/iffco-tokio/hosts/iffco-tokio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iffco-tokio-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iffcotokio.co.in/about-us/terms-use
- group: start
  title: ''
  type: SignUp
  url: https://www.iffcotokio.co.in/claims/register-a-claim
- group: auth
  href: https://artifacts.apis.io/iffco-tokio/security/iffco-tokio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iffco-tokio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iffcotokio.co.in/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iffcotokio.co.in/about-us/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.iffcotokio.co.in/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.iffcotokio.co.in/blog
coverage:
  checked: '2026-10-28'
  detail: The provider's website returns HTML error pages for typical OpenAPI spec URLs and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.iffcotokio.co.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: IFFCO‑TOKIO General Insurance Company Limited, incorporated in 2000 as a joint venture between Indian Farmers Fertiliser Co‑operative Limited (IFFCO) and Tokio Marine Group, offers a comprehensive portfolio of general insurance products in India, including motor, health, travel, home, and corporate policies such as property and liability insurance. The company also provides niche solutions like cyber, credit, fine arts, and errors & omissions insurance, and runs rural‑centric initiatives such as Sankat Haran Bima Yojana and Mahila Suraksha Bima Yojana to increase insurance penetration.
image: https://www.iffcotokio.co.in/content/dam/iffcotokio/iffco-images/logo.jpg
layout: provider
modified: '2026-10-28'
name: IFFCO-Tokio General Insurance
nav: Providers
network: true
overview: 'IFFCO-Tokio General Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, GeneralInsurance, India, JointVenture, and FinancialServices.


  IFFCO-Tokio General Insurance''s developer surface includes signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 10
scopes:
- name: Iffco Tokio Scopes
  scope_count: 0
  slug: iffco-tokio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 27.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Iffco Tokio Authentication
  slug: iffco-tokio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Iffco Tokio Domain Security
  slug: iffco-tokio-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: iffco-tokio
tags:
- Insurance
- GeneralInsurance
- India
- JointVenture
- FinancialServices
website: https://iffcotokio.co.in/
---
