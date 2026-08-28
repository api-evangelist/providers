---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rcs-capital-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rcs-capital-inc
- group: company
  title: ''
  type: Website
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001568832&type=&dateb=&owner=include&count=40
- group: company
  title: ''
  type: Website
  url: https://www.cetera.com
- group: docs
  title: ''
  type: Documentation
  url: https://cases.ra.kroll.com/rcscapital/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-schema/rcs-capital-financial-advisor-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-schema/rcs-capital-broker-dealer-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-structure/rcs-capital-financial-advisor-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/json-ld/rcs-capital-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/examples/rcs-capital-financial-advisor-example.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/vocabulary/rcs-capital-vocabulary.yml
created: '2025-01-01'
description: RCS Capital Corporation (RCAP) was a publicly traded holding company focused on the financial services industry, founded by Nicholas Schorsch and taken public in June 2013. The firm owned a diversified group of businesses including independent broker-dealers, investment banking, capital markets, and transaction management services. It assembled Cetera Financial Group to become the second largest network of independent broker-dealers in the United States, with approximately 9,100 financial advisors managing $220 billion in assets under administration for 2.5 million clients. RCS Capital filed for Chapter 11 bankruptcy protection in January 2016, citing $1.39 billion in debts, and emerged in May 2016 as Aretec Group, Inc., the holding company of Cetera Financial Group. No public developer APIs were offered under the RCS Capital brand.
examples:
- key_count: 16
  name: Rcs Capital Financial Advisor Example
  slug: rcs-capital-financial-advisor-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rcs-capital.png
json_schemas:
- name: Broker-Dealer Entity
  property_count: 11
  slug: rcs-capital-broker-dealer
- name: Financial Advisor
  property_count: 14
  slug: rcs-capital-financial-advisor
json_structures:
- name: Rcs Capital Financial Advisor Structure
  property_count: 0
  slug: rcs-capital-financial-advisor-structure
jsonld:
- class_count: 17
  name: Rcs Capital Context
  property_count: 9
  slug: rcs-capital-context
layout: provider
modified: '2026-05-02'
name: RCS Capital
nav: Providers
network: true
overview: 'RCS Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Broker-Dealer, Cetera Financial Group, Defunct, Financial-Services, and Independent Advisor.


  The RCS Capital catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RCS Capital''s developer surface includes documentation, code examples, and 9 more developer resources.'
press:
- date: '2026-05-25'
  title: RCS Capital Sells Wholesale Unit to Apollo for $25M
  url: https://www.wealthmanagement.com/ibd-news/rcs-capital-sells-wholesale-unit-to-apollo-for-25m
- date: '2026-05-25'
  title: Brokerage RCS Capital bankruptcy to take Cetera private
  url: https://www.reuters.com/article/breakingviews/brokerage-rcs-capital-bankruptcy-to-take-cetera-private-idUSKCN0VA3EZ/
- date: '2026-05-25'
  title: C. Thomas McMillen
  url: https://www.nexstar.tv/c-thomas-mcmillen/
- date: '2026-05-25'
  title: RCS Capital Corporation Completes Acquisition of Cetera ...
  url: https://www.prnewswire.com/news-releases/rcs-capital-corporation-completes-acquisition-of-cetera-financial-group-257218501.html
- date: '2026-05-25'
  title: 'Rcs: capital increase from 27 June to 5 July - FIRSTonline'
  url: https://www.firstonline.info/en/rcs-capital-increase-from-27-June-to-5-July/
random_paper: 15
rules:
- effective_rule_count: 5
  extends: []
  name: RCS Capital API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rcs-capital-jsonschema-spectral-rules
score:
  band: emerging
  composite: 11.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 17.3
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 18.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rcs-capital/refs/heads/main/screenshots/rcs-capital-2026-06-20T192624.png
security:
- kind: domain-security
  name: Rcs Capital Domain Security
  slug: rcs-capital-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rcs-capital
tags:
- Broker-Dealer
- Cetera Financial Group
- Defunct
- Financial-Services
- Independent Advisor
- Investment Banking
- Wealth Management
website: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001568832&type=&dateb=&owner=include&count=40
---
