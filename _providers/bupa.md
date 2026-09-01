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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Bupa Australia API estate, published through an Azure API Management managed developer portal at portal.api.bupa.com.au and served from the api.bupa.com.au gateway host. The portal is publicly rea
  name: Bupa Australia APIs (Integration Fabric)
  slug: bupa-australia-apis-integration-fabric
- description: The Bupa Chile API portal at apidoc.bupa.cl — an Angular single-page application that ships Swagger UI and renders API definitions fetched from the backend controller at https://api.bupa.cl/portal/ms-
  name: Portal de APIs Bupa (Bupa Chile)
  slug: portal-de-apis-bupa-bupa-chile
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.bupa.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bupa.com/news-and-press/news-and-stories
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bupa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bupa-digital
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.api.bupa.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.api.bupa.com.au/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.api.bupa.com.au/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://portal.api.bupa.com.au/api-details
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bupa-changelog.yml
- group: start
  title: ''
  type: SignUp
  url: https://portal.api.bupa.com.au/signin
- group: operate
  title: ''
  type: Support
  url: https://www.bupa.com/contacts
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bupa.com.au/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bupa.com/important-notices/privacy-notices
- group: auth
  title: ''
  type: Authentication
  url: authentication/bupa-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bupa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bupa-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/bupa-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bupa-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bupa-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bupa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/bupa-aus-vdp-pro
created: '2026-07-25'
description: 'Bupa is a United Kingdom headquartered international healthcare group that writes private medical insurance and also runs the clinics, dental practices, hospitals and aged-care homes that deliver the care it funds. It has no shareholders, is owned by the British United Provident Association Limited and reinvests its profits, and operates market units across the UK, Australia and New Zealand, Spain and Latin America (Sanitas, Bupa Chile), Turkiye, Poland, Hong Kong SAR, India and the Middle East, plus the Bupa Global international private medical insurance business. Its lines of business are health insurance, health provision and aged care rather than property and casualty or life, so the ACORD data standards that shape the rest of the insurance sector are absent from its published surface. Bupa''s API posture is partner-gated: the group site bupa.com publishes no developer portal at all (developer, developers, docs and api subdomains do not resolve, and /developers, /api and
  /developer return 404), and the only first-party developer surfaces belong to market units. Bupa Australia runs a real Azure API Management developer portal at portal.api.bupa.com.au that returns HTTP 200 but lists no APIs publicly, instructing prospective consumers to contact the Bupa Integration Fabric Team to get access to API specifications; Bupa Chile runs apidoc.bupa.cl behind a Microsoft Entra ID login wall whose backend returns HTTP 401 to anonymous callers; and the Bupa Global portal host api-portal.bupaglobal.com no longer resolves. No public OpenAPI or Swagger definition, no Postman collection, no GraphQL or gRPC surface, and no event or webhook catalog could be confirmed anywhere on Bupa''s public web estate as of 2026-07-25, and none of the four insurance API verbs — quote, bind, issue or FNOL — is exposed to unauthenticated developers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Bupa
nav: Providers
network: true
overview: 'Bupa publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Health Insurance, Life and Health, and Carrier.


  Bupa''s developer surface includes engineering blog, documentation, getting-started guide, API reference, changelog, signup flow, support, and 14 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 31.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 40.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bupa/refs/heads/main/screenshots/bupa-2026-07-25T204111.png
security:
- kind: authentication
  name: Bupa Authentication
  slug: bupa-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Bupa Domain Security
  slug: bupa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bupa Vulnerability Disclosure
  slug: bupa-vulnerability-disclosure
  summary_line: Hackerone
slug: bupa
tags:
- Insurance
- United Kingdom
- Health Insurance
- Life and Health
- Carrier
- Healthcare
- Aged Care
- Claims
- Policy Administration
- Partner Gated
website: https://www.bupa.com/
---
