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
  scored_at: '2026-08-30'
api_count: 8
apis:
- description: The Assistant API from Metabolon — 2 operation(s) for assistant.
  name: Metabolon Assistant API
  slug: metabolon-assistant-api
- description: The Auth API from Metabolon — 10 operation(s) for auth.
  name: Metabolon Auth API
  slug: metabolon-auth-api
- description: The Decentralization API from Metabolon — 4 operation(s) for decentralization.
  name: Metabolon Decentralization API
  slug: metabolon-decentralization-api
- description: The Eula API from Metabolon — 12 operation(s) for eula.
  name: Metabolon Eula API
  slug: metabolon-eula-api
- description: The Files API from Metabolon — 34 operation(s) for files.
  name: Metabolon Files API
  slug: metabolon-files-api
- description: The Health API from Metabolon — 10 operation(s) for health.
  name: Metabolon Health API
  slug: metabolon-health-api
- description: The LabVantageFiles API from Metabolon — 6 operation(s) for labvantagefiles.
  name: Metabolon Lab Vantage Files API
  slug: metabolon-labvantagefiles-api
- description: The PipelineStatus API from Metabolon — 8 operation(s) for pipelinestatus.
  name: Metabolon Pipeline Status API
  slug: metabolon-pipelinestatus-api
- description: The Projects API from Metabolon — 18 operation(s) for projects.
  name: Metabolon Projects API
  slug: metabolon-projects-api
- description: The Reports API from Metabolon — 1 operation(s) for reports.
  name: Metabolon Reports API
  slug: metabolon-reports-api
- description: The SampleSets API from Metabolon — 2 operation(s) for samplesets.
  name: Metabolon Sample Sets API
  slug: metabolon-samplesets-api
- description: The SampleSetsInfo API from Metabolon — 6 operation(s) for samplesetsinfo.
  name: Metabolon Sample Sets Info API
  slug: metabolon-samplesetsinfo-api
- description: The Search API from Metabolon — 1 operation(s) for search.
  name: Metabolon Search API
  slug: metabolon-search-api
- description: The SharedFile API from Metabolon — 12 operation(s) for sharedfile.
  name: Metabolon Shared File API
  slug: metabolon-sharedfile-api
- description: The SpectralData API from Metabolon — 4 operation(s) for spectraldata.
  name: Metabolon Spectral Data API
  slug: metabolon-spectraldata-api
- description: The Status API from Metabolon — 16 operation(s) for status.
  name: Metabolon Status API
  slug: metabolon-status-api
- description: The StudyBuilder API from Metabolon — 6 operation(s) for studybuilder.
  name: Metabolon Study Builder API
  slug: metabolon-studybuilder-api
- description: The Users API from Metabolon — 90 operation(s) for users.
  name: Metabolon Users API
  slug: metabolon-users-api
artifact_total: 23
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/metabolon-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/metabolon-portal-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/metabolon-discovery-panels-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/metabolon-pathway-explorer-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/metabolon-heatmap-api-overlay.yaml
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
overview: 'Metabolon publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Assistant API, Auth API, Decentralization API, and 15 more. Tagged areas include Company, Metabolomics, Life Sciences, Bioinformatics, and Multiomics.


  Metabolon''s developer surface includes documentation, getting-started guide, support, engineering blog, authentication, and 22 more developer resources.'
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
  composite: 42.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 43.0
    developer_ergonomics: 42.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 42.7
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
