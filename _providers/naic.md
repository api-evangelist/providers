---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Naic Agentic Access
  operation_count: 569
  slug: naic-agentic-access
  summary_line: 569 operations
api_count: 2
apis:
- description: The NAIC-operated SERFF (System for Electronic Rates & Forms Filing) platform exposes machine integration services to filers, state regulators and filing vendors. The SERFF Technical Support Checklist
  name: SERFF Web Services
  slug: serff-web-services
- description: A live, anonymously readable JSON:API v1.1 surface over the NAIC's public regulatory content estate, served by Drupal 11 at content.naic.org/jsonapi. The NAIC neither documents nor advertises it - the
  name: NAIC Content JSON:API
  slug: content-jsonapi
artifact_total: 12
collections:
- collection_type: open
  name: NAIC Content JSON:API
  slug: open-naic-content-jsonapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/naic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/naic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/naic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/naic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/naic-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/naic-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/naic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/naic-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/naic-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://content.naic.org/
- group: company
  title: ''
  type: About
  url: https://content.naic.org/about
- group: company
  title: ''
  type: Blog
  url: https://content.naic.org/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/insurance-topics
- group: other
  title: ''
  type: Publications
  url: https://content.naic.org/publications
- group: start
  title: ''
  type: Portal
  url: https://www.serff.com/
- group: start
  title: ''
  type: Portal
  url: https://sbs.naic.org/
- group: start
  title: ''
  type: Portal
  url: https://isiteplus.naic.org/iSiteUI/faces/pages/Home.xhtml
- group: start
  title: ''
  type: Portal
  url: https://insdata.naic.org/
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/insurance-topics/financial-data-repository
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/cis_consumer_information.htm
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/sites/default/files/naic-technology-services-products-catalog.pdf
- group: operate
  title: ''
  type: Support
  url: https://content.naic.org/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://content.naic.org/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://content.naic.org/application/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://content.naic.org/privacy_statement.htm
created: '2026-07-25'
description: 'The National Association of Insurance Commissioners (NAIC) is the U.S. standard-setting and regulatory support organization created and governed by the chief insurance regulators of the 50 states, the District of Columbia and five territories. It is not a carrier and not a federal regulator - under the McCarran-Ferguson settlement the United States has no national insurance supervisor, so the NAIC is the coordinating body through which state-based regulation is made uniform. It writes the model laws, accounting practices and Annual Statement Blanks that every admitted insurer files against, operates the Financial Data Repository behind those filings, and runs the market infrastructure the industry actually transacts on: SERFF for electronic rate and form filing, State Based Systems (SBS) for producer and company licensing in roughly thirty jurisdictions, iSite+ and myNAIC for regulator analytics, OPTins for premium tax, and consumer-facing lookups such as the Consumer Information
  Source and the Life Insurance Policy Locator. Its lines of business span property and casualty, life and annuity, health, title and fraternal across the United States. Its API posture is partner-gated and closed: there is no developer portal at developer/developers/docs.naic.org (all NXDOMAIN), no documented self-serve API, and no downloadable OpenAPI anywhere on naic.org or serff.com. SERFF does operate real integration services - Legacy SPI (two-way PUSH/PULL), Legacy SIS (one-way PULL) and a Modernized Data API (one-way PULL), in PROD and BETA - but they are named only on a support checklist, provisioned by emailing wsrequest@naic.org, and fronted by Okta login walls. Bulk regulatory data is licensed by contract through idp@naic.org rather than served over an API. There is, however, one real and entirely undocumented public machine surface: content.naic.org runs Drupal 11 and serves a live, anonymously readable JSON:API v1.1 at /jsonapi, whose resource index enumerates 284 resource
  types and exposes the model law corpus with its MDL numbers, the state insurance department regulator directory, committees, insurance topics, publications, CIPR research and the newsroom. The NAIC also publishes a first-party llms.txt declaring AI usage preferences, attribution requirements and crawl limits - so its stated contract with automated consumers is more explicit than its contract with API developers.'
examples:
- key_count: 3
  name: Naic Jsonapi Resource Index
  slug: naic-jsonapi-resource-index
- key_count: 5
  name: Naic Node Article Example
  slug: naic-node-article-example
- key_count: 5
  name: Naic Node State Department Contact Example
  slug: naic-node-state-department-contact-example
- key_count: 5
  name: Naic Taxonomy Model Law Example
  slug: naic-taxonomy-model-law-example
- key_count: 3
  name: Naic Taxonomy States Alabama Example
  slug: naic-taxonomy-states-alabama-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: naic-mcp.yml
  slug: naic-mcpyml
modified: '2026-07-25'
name: NAIC
nav: Providers
network: true
overview: 'NAIC publishes 1 API on the [APIs.io](https://apis.io/) network: Content JSON:API. Tagged areas include Insurance, United States, Regulator, Market Infrastructure, and Insurance Regulation.


  NAIC''s developer surface includes authentication, code examples, engineering blog, documentation, developer portal, support, and 22 more developer resources.'
random_paper: 113
score:
  band: emerging
  composite: 26.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 14.4
    developer_ergonomics: 38.6
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/naic/refs/heads/main/screenshots/naic-2026-08-07T184609.png
security:
- kind: authentication
  name: Naic Authentication
  slug: naic-authentication
  summary_line: none/cookie/saml-oidc-sso · 0 schemes
- kind: domain-security
  name: Naic Domain Security
  slug: naic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: naic
tags:
- Insurance
- United States
- Regulator
- Market Infrastructure
- Insurance Regulation
- Property and Casualty
- Life Insurance
- Health Insurance
- Producer Licensing
- Rate and Form Filing
- Regulatory Reporting
- Standards Body
- Model Laws
- Regulatory Data
- Open Data
website: https://content.naic.org/
---
