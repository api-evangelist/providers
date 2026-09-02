---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The customer-authenticated REST API behind ChromaCode Cloud 6.1, the browser application that decodes HDPCR run files. Observed resource surface includes analyses, assays and assay downloads, batch re
  name: ChromaCode Cloud API
  slug: chromacode-cloud
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.chromacode.com/
- group: operate
  title: ''
  type: Support
  url: https://www.chromacode.com/contact/
- group: start
  title: ''
  type: Login
  url: https://chromacodecloud.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChromaCodeINC
- group: company
  title: ''
  type: BlogRSS
  url: https://www.chromacode.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chromacode.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chromacode.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.chromacode.com/cookie-notice/
- group: auth
  title: ''
  type: Compliance
  url: https://www.chromacode.com/chromacode-cloud/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chromacode-inc/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/chromacodeinc
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/chromacodeinc/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/chromacode_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chromacode-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/chromacode-openid-configuration-apps.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/chromacode-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chromacode-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chromacode-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chromacode-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chromacode-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chromacode-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chromacode-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chromacode-llms.txt
created: '2026-08-02'
description: 'ChromaCode, Inc. is a Carlsbad, California molecular diagnostics company that applies digital signal processing and data science to standard PCR chemistry. Its High-Definition PCR (HDPCR) platform multiplexes more than four times the targets of conventional digital PCR on existing qPCR and dPCR instruments, with no new hardware, reagents, or workflow. The chemistry is paired with ChromaCode Cloud, a browser-based analysis platform that decodes raw PCR run files into interpreted variant calls, plate and well-level visualizations, and downloadable PDF reports that can be exported to LIMS and third-party reporting systems. Products span oncology tumor profiling (the HDPCR NSCLC panel), minimal residual disease and disease monitoring, transplant rejection, and previously an FDA EUA high-throughput SARS-CoV-2 assay. ChromaCode Cloud is a closed, customer-authenticated SaaS: it runs a REST API at chromacodecloud.com/api behind a Keycloak OpenID Connect identity provider whose discovery
  documents are publicly readable, but ChromaCode publishes no developer portal, OpenAPI definition, SDKs, or public API documentation.'
image: https://www.chromacode.com/wp-content/uploads/2022/07/CC_logo.png
layout: provider
modified: '2026-08-02'
name: ChromaCode
nav: Providers
network: true
overview: 'ChromaCode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Molecular Diagnostics, Genomics, Oncology, and PCR.


  ChromaCode''s developer surface includes support, authentication, and 21 more developer resources.'
random_paper: 16
scopes:
- name: Chromacode Scopes
  scope_count: 12
  slug: chromacode-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chromacode/refs/heads/main/screenshots/chromacode-2026-08-07T163339.png
security:
- kind: authentication
  name: Chromacode Authentication
  slug: chromacode-authentication
  summary_line: openIdConnect/oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Chromacode Domain Security
  slug: chromacode-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chromacode
tags:
- Company
- Molecular Diagnostics
- Genomics
- Oncology
- PCR
- Life Sciences
- Healthcare
- Bioinformatics
- Clinical Diagnostics
- Cloud Software
website: https://www.chromacode.com/
---
