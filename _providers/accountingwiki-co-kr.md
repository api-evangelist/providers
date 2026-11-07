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
- description: AccountingWiki provides a knowledge base for Korean accounting standards and offers an MCP endpoint for AI‑assisted queries. Documentation is available at the guides page. No public OpenAPI or other m
  name: AccountingWiki API
  slug: accountingwiki-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/accountingwiki-co-kr/llms/accountingwiki-co-kr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accountingwiki-co-kr-llms.txt
- group: other
  href: https://artifacts.apis.io/accountingwiki-co-kr/hosts/accountingwiki-co-kr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accountingwiki-co-kr-hosts.yml
- group: other
  href: https://artifacts.apis.io/accountingwiki-co-kr/vendors/accountingwiki-co-kr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accountingwiki-co-kr-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://accountingwiki.co.kr/guides
- group: auth
  href: https://artifacts.apis.io/accountingwiki-co-kr/security/accountingwiki-co-kr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accountingwiki-co-kr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accountingwiki.co.kr/
- group: company
  title: ''
  type: About
  url: https://accountingwiki.co.kr/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accountingwiki.co.kr/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accountingwiki.co.kr/privacy
- group: other
  title: ''
  type: Disclaimer
  url: https://accountingwiki.co.kr/disclaimer
- group: operate
  title: ''
  type: Contact
  url: https://accountingwiki.co.kr/contact
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered.
  evidence:
  - status: 200
    url: https://accountingwiki.co.kr/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AccountingWiki is an open-source knowledge wiki for accounting and finance professionals in Korea, providing K‑IFRS, K‑GAAP, audit, internal accounting standards, and practical guides. The site aggregates official standards, Q&A responses, and expert commentary written by certified Korean accountants, offering searchable, paragraph‑linked content and AI‑assisted query capabilities via its MCP endpoint.
image: https://accountingwiki.co.kr/og-default.png?v=20260713
layout: provider
modified: '2026-10-31'
name: AccountingWiki
nav: Providers
network: true
overview: 'AccountingWiki is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Finance, Knowledge Base, Open Source, and South Korea.


  AccountingWiki''s developer surface includes documentation and 10 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 11.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accountingwiki Co Kr Domain Security
  slug: accountingwiki-co-kr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accountingwiki-co-kr
tags:
- Accounting
- Finance
- Knowledge Base
- Open Source
- South Korea
website: https://accountingwiki.co.kr/
---
