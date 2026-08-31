---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Bi-directional API for technology platforms to request insurance coverage for their customers' suppliers and receive real-time, source-verified policy data, PDF certificates of insurance and endorseme
  name: Certificial Insurance Tracking API
  slug: certificial-insurance-tracking-api
- description: API for InsurTech platforms and agency-management systems to automate certificate of insurance distribution — generating ACORD 24, 25, 27, 28 and 101 forms, automatically reissuing certificates when t
  name: Certificial COI Issuance API
  slug: certificial-coi-issuance-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.certificial.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.certificial.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.certificial.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certificial.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certificial.com/user-eula
- group: operate
  title: ''
  type: Support
  url: https://support.certificial.com/portal/en/home
- group: company
  title: ''
  type: Blog
  url: https://www.certificial.com/news
- group: auth
  title: ''
  type: Authentication
  url: authentication/certificial-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/certificial-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certificial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/certificial-llms.txt
coverage:
  checked: '2026-08-09'
  detail: Certificial markets two APIs (Insurance Tracking and COI Issuance) but publishes no reference for either — both product pages end at a Calendly "Setup a Call to Discuss our API" reseller booking, the 130-URL sitemap contains no developer or docs page, and the live platform API root at my.certificial.com/api/ answers 401 with a WWW-Authenticate Token challenge.
  evidence:
  - status: 200
    url: https://www.certificial.com/insurance-tracking-api
  - status: 401
    url: https://my.certificial.com/api/
  - status: 404
    url: https://www.certificial.com/openapi.json
  - status: 404
    url: https://www.certificial.com/.well-known/security.txt
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: Certificial operates the Smart COI Network, a real-time certificate of insurance (COI) tracking, issuance and compliance platform used by requestors, insureds, and insurance agents and brokers. Instead of a static PDF certificate that goes stale the moment a policy changes, Certificial maintains a continuously monitored Smart COI that reflects policy-level changes as they happen and notifies every party to the relationship. The company sells two API products to software platforms — an Insurance Tracking API for pulling real-time, source-verified coverage data and COI documents into a host platform, and a COI Issuance API for InsurTech and agency-management vendors that need to generate and automatically reissue ACORD-form certificates. The platform API is live at my.certificial.com/api/ but is credential-gated, and no public API reference, OpenAPI definition, or developer portal is published — API access is arranged through a sales/reseller conversation.
image: https://cdn.prod.website-files.com/61da5f835921f2d8534e64ee/61da631ef7dad474183c7474_certificial_logo.svg
layout: provider
modified: '2026-08-09'
name: Certificial
nav: Providers
network: true
overview: 'Certificial publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, InsurTech, Certificate of Insurance, Risk Management, and Compliance.


  Certificial''s developer surface includes pricing, signup flow, support, engineering blog, authentication, and 6 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Certificial Authentication
  slug: certificial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Certificial Domain Security
  slug: certificial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: certificial
tags:
- Insurance
- InsurTech
- Certificate of Insurance
- Risk Management
- Compliance
- Supplier Management
- Insurance Verification
- ACORD
- Company
website: https://www.certificial.com/
---
