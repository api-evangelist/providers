---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Datao provides AI‑powered monitoring of public procurement opportunities in Morocco via a web platform.
  name: Datao API
  slug: datao-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/datao-ma/llms/datao-ma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datao-ma-llms.txt
- group: other
  href: https://artifacts.apis.io/datao-ma/hosts/datao-ma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datao-ma-hosts.yml
- group: other
  href: https://artifacts.apis.io/datao-ma/vendors/datao-ma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datao-ma-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.datao.ma/auth/signup
- group: docs
  title: ''
  type: Documentation
  url: https://datao.ma/blog/guides/
- group: auth
  href: https://artifacts.apis.io/datao-ma/security/datao-ma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datao-ma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datao.ma/
- group: company
  title: ''
  type: Blog
  url: https://datao.ma/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datao.ma/cgu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datao.ma/politique-de-confidentialite/
coverage:
  checked: '2026-11-05'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found despite probing common spec URLs and the guides page.
  evidence:
  - status: 200
    url: https://datao.ma/blog/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Datao provides AI‑powered monitoring of public procurement opportunities in Morocco. Their platform scans official tender publications, extracts key details, and alerts users to relevant contracts, helping businesses save time and increase win rates. Features include customizable alerts, a Claude‑integrated assistant for summarizing tenders, and a dashboard for tracking opportunities across sectors.
image: https://datao.ma/og-image.jpg
layout: provider
modified: '2026-11-05'
name: Datao
nav: Providers
network: true
overview: 'Datao is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Procurement, Morocco, Public Data, and Software-as-a-Service.


  Datao''s developer surface includes signup flow, documentation, engineering blog, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datao Ma Domain Security
  slug: datao-ma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datao-ma
tags:
- Artificial Intelligence
- Procurement
- Morocco
- Public Data
- Software-as-a-Service
- Company
website: https://datao.ma/
---
