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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intact-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.intactfc.com/
- group: company
  title: ''
  type: Website
  url: https://www.intact.ca/
- group: company
  title: ''
  type: Website
  url: https://www.intactspecialty.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.intactinsurance.com/
- group: company
  title: ''
  type: Blog
  url: https://www.intact.ca/en/blog
- group: company
  title: ''
  type: News
  url: https://www.intactfc.com/news
- group: company
  title: ''
  type: About
  url: https://www.intactfc.com/about-us/who-we-are
- group: other
  title: ''
  type: Company
  url: https://www.intactfc.com/investors/company-overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intactfc.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intactfc.com/terms-and-conditions-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intact
- group: operate
  title: ''
  type: Support
  url: https://www.intact.ca/en/contact-us
- group: company
  title: ''
  type: Careers
  url: https://careers.intactfc.com/
- group: company
  title: ''
  type: Website
  url: https://www.belairdirect.com/
- group: company
  title: ''
  type: Website
  url: https://www.123.ie/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intact-financial-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intact-financial-belairdirect-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intact-financial-123ie-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/intact-financial-conformance.yml
created: '2026-07-25'
description: Intact Financial Corporation is the largest provider of property and casualty insurance in Canada, headquartered in Toronto and trading on the TSX as IFC. It underwrites personal auto, personal property, and commercial P&C lines through the Intact Insurance, belairdirect, BrokerLink, Intact Prestige, Intact Public Entities, and On Side Restoration brands in Canada, through Intact Insurance Specialty Solutions in the United States, and through Intact Insurance UK, EU, IE and 123.ie internationally following the 2021 acquisition of RSA. Distribution runs through a network of more than 6,000 independent broker offices plus direct-to-consumer channels. Its API posture is partner-gated and closed. There is no public, self-serve developer portal, no published API reference, and no downloadable OpenAPI, Swagger, GraphQL, or AsyncAPI artifact on any Intact domain probed. developer/developers/docs/api subdomains on intactfc.com and intact.ca do not resolve; /developers, /api, /developer
  and /partners return 404. The only integration surfaces are login walls — the Intact Portal for brokers at portal.intactinsurance.com (brokers.intact.ca redirects there) and the customer Client Centre behind IBM Security WebSEAL at apps.intactinsurance.com. Broker connectivity in Canada is mediated by CSIO, the industry standards body whose EDI, XML, eDocs and JSON API standards are the Canadian analogue of ACORD. Intact Insurance is listed in the CSIO member directory but appears on none of CSIO's certified-member lists (eDocs, CL Data, Compliance/Z-code, API Security Standards, JSON API Standards) and is recorded as "Not Yet Rated" on both the personal and commercial tracks of CSIO's 2026 Standards Certification Ratings. No ACORD reference was found anywhere on the company's public web properties.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Intact Financial
nav: Providers
network: true
overview: 'Intact Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Carrier, and Underwriting.


  Intact Financial''s developer surface includes developer portal, engineering blog, product news, support, and 16 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 22.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Intact Financial Domain Security
  slug: intact-financial-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: intact-financial
tags:
- Insurance
- Canada
- Property and Casualty
- Carrier
- Underwriting
- Claims
- Brokers
- Partner Gated
- No Public API
- CSIO
website: https://www.intactfc.com/
---
