---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/properly-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/properly-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/properly-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/properly-llms.txt
- group: company
  title: ''
  type: Website
  url: https://properly.ca/
- group: company
  title: ''
  type: Website
  url: https://www.pine.ca/real-estate
- group: company
  title: ''
  type: Blog
  url: https://www.pine.ca/resources
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/pine-financial
created: '2026-07-26'
description: 'Properly was a Toronto-based Canadian digital real estate brokerage founded in 2018 that began as one of the country''s only iBuyers — making algorithmic cash offers on Calgary homes — before pivoting to Sale Assurance, a guaranteed-purchase backstop that let a seller buy their next home before selling the current one, wrapped around an online listing search and a machine-generated home valuation. It sat in the challenger layer of the Canadian value chain alongside HouseSigma, Wahi, and Zolo, competing on visibility into listing data controlled by CREA, the national cooperative that operates REALTOR.ca and the Data Distribution Facility (DDF) syndicating member boards'' listings, in a market where land registration is provincially privatised and the public record is itself a commercial product. Properly was acquired by Pine Canada Financial Corporation in October 2023 and the brand has since been absorbed: properly.ca and www.properly.ca now answer HTTP 301 from an Amazon S3
  and CloudFront redirect bucket to www.pine.ca, and the word "Properly" no longer appears anywhere on the surviving Pine real estate pages. Its API posture is closed and, as of this profile, non-existent. No developer portal, no API program page, no partner or data licensing page, and no published terms of API use were found. The developer., developers., api., docs., app., and blog. subdomains of properly.ca do not resolve in DNS, and every contract path probed — /openapi.json, /swagger.json, /api-docs, /$metadata, /odata — redirects into a Pine 404. The successor host api.pine.ca resolves to an AWS API Gateway that answers every path with HTTP 403 MissingAuthenticationTokenException: a private first-party backend, not a developer product. RESO is absent, which is the honest Canadian answer — Properly and Pine appear nowhere on RESO''s own Canadian membership roster, and no Web API or Data Dictionary certification, OData $metadata document, or Universal Property Identifier usage was observed.
  No open, unlicensed dataset is published. The underlying listings reach the platform through licensed channels — CREA MLS trademark attribution appears in the site footer and listing media is served from cdn.repliers.io, the CDN of the licensed MLS data vendor Repliers, whose own developer guide names "Pine (formerly Properly)" as a customer — which is a brokerage and vendor licensing posture, not anything a third-party developer can sign up for.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-26'
name: Properly
nav: Providers
network: true
overview: 'Properly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Canada, Property Listings, MLS, and Valuation.


  Properly''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.8
  delta: 1.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 7.2
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Properly Domain Security
  slug: properly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: properly
tags:
- Real Estate
- Canada
- Property Listings
- MLS
- Valuation
- AVM
- PropTech
- Mortgage
website: https://properly.ca/
---
