---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: The backend REST API for the MyMetabolon customer portal (portal.metabolon.com). 248 operations across 18 tags — Users, Auth, Projects, Files, SampleSetsInfo, SpectralData, StudyBuilder, Reports, Sear
  name: Metabolon Portal API
  slug: metabolon-portal-api
- description: ASP.NET service backing the Discovery Panel views of the Metabolon Integrated Bioinformatics Platform. Its public NSwag OpenAPI document (DiscoveryPanelsApi v1) exposes only the ten health, ping, deep
  name: Metabolon Discovery Panels API
  slug: metabolon-discovery-panels-api
- description: ASP.NET service backing the Pathway Explorer visualization in the Metabolon Integrated Bioinformatics Platform. Its public NSwag OpenAPI document (PathwayExplorerApi v1) exposes only the ten health, p
  name: Metabolon Pathway Explorer API
  slug: metabolon-pathway-explorer-api
- description: 'ASP.NET service backing the heatmap visualization in the Metabolon Integrated Bioinformatics Platform. Its public NSwag OpenAPI document carries the NSwag default title "ServiceName" and exposes only '
  name: Metabolon Heatmap API
  slug: metabolon-heatmap-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.metabolon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.metabolon.com/support/portal/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.metabolon.com/support/portal/how-to/
- group: operate
  title: ''
  type: Support
  url: https://www.metabolon.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.metabolon.com/blog/
- group: start
  title: ''
  type: Login
  url: https://portal.metabolon.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metabolon.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metabolon.com/legal/
- group: auth
  title: ''
  type: Compliance
  url: https://www.metabolon.com/quality-assurance/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metabolon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metabolon-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metabolon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/metabolon-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metabolon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metabolon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metabolon-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metabolon-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metabolon-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metabolon-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metabolon-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/metabolon-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: Metabolon, Inc. is the metabolomics contract research and software company headquartered in Morrisville, North Carolina. It runs the Global Discovery Panel and a family of targeted and untargeted metabolomics, lipidomics and microbiome panels for pharma, biotech, academic and clinical-research customers, and delivers the resulting biochemical data through MyMetabolon — a customer portal fronting an Integrated Bioinformatics Platform of pathway, heatmap, discovery-panel and multiomics analysis tools. Metabolon publishes no public developer program or API reference, but the portal is a React single-page app backed by four publicly reachable ASP.NET services on *.prod.metabolon.com whose NSwag-generated OpenAPI 3.0 documents are served unauthenticated at /swagger/v1/swagger.json, and customer sign-in runs on a Metabolon-branded Auth0 tenant at auth0.metabolon.com with full OIDC discovery.
image: https://www.metabolon.com/wp-content/uploads/2022/11/Metabolon-logo-peak@2x.webp
layout: provider
modified: '2026-08-25'
name: Metabolon
nav: Providers
network: true
overview: 'Metabolon publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Portal API, Discovery Panels API, Pathway Explorer API, and 1 more. Tagged areas include Company, Metabolomics, Life Sciences, Bioinformatics, and Multiomics.


  Metabolon''s developer surface includes documentation, getting-started guide, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Metabolon Plans Pricing
  plan_count: 0
  slug: metabolon-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Metabolon Rate Limits
  slug: metabolon-rate-limits
scopes:
- name: Metabolon Scopes
  scope_count: 0
  slug: metabolon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.8
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 41.5
    developer_ergonomics: 42.3
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Metabolon Authentication
  slug: metabolon-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Metabolon Domain Security
  slug: metabolon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metabolon
tags:
- Company
- Metabolomics
- Life Sciences
- Bioinformatics
- Multiomics
- Biotechnology
- Drug Discovery
- Precision Medicine
- Microbiome
- Biomarkers
- Contract Research
- Laboratory
website: https://www.metabolon.com/
---
