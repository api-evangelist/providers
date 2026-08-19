---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-19'
api_count: 12
apis:
- description: The Auth API from Wayflyer — 2 operation(s) for auth.
  name: Wayflyer Auth API
  slug: wayflyer-auth-api
- description: The Company Details API from Wayflyer — 3 operation(s) for company details.
  name: Wayflyer Company Details API
  slug: wayflyer-company-details-api
- description: The Company Search API from Wayflyer — 1 operation(s) for company search.
  name: Wayflyer Company Search API
  slug: wayflyer-company-search-api
- description: The CTA API from Wayflyer — 4 operation(s) for cta.
  name: Wayflyer CTA API
  slug: wayflyer-cta-api
- description: The Data Upload API from Wayflyer — 3 operation(s) for data upload.
  name: Wayflyer Data Upload API
  slug: wayflyer-data-upload-api
- description: The Documents API from Wayflyer — 3 operation(s) for documents.
  name: Wayflyer Documents API
  slug: wayflyer-documents-api
- description: The Embedded Application API from Wayflyer — 3 operation(s) for embedded application.
  name: Wayflyer Embedded Application API
  slug: wayflyer-embedded-application-api
- description: The Handover API from Wayflyer — 1 operation(s) for handover.
  name: Wayflyer Handover API
  slug: wayflyer-handover-api
- description: The Industry Classification API from Wayflyer — 1 operation(s) for industry classification.
  name: Wayflyer Industry Classification API
  slug: wayflyer-industry-classification-api
- description: The Simulation API from Wayflyer — 1 operation(s) for simulation.
  name: Wayflyer Simulation API
  slug: wayflyer-simulation-api
- description: The Tracked Login API from Wayflyer — 1 operation(s) for tracked login.
  name: Wayflyer Tracked Login API
  slug: wayflyer-tracked-login-api
- description: The User Details API from Wayflyer — 4 operation(s) for user details.
  name: Wayflyer User Details API
  slug: wayflyer-user-details-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Embedded Finance Auth API
  slug: open-wayflyer-auth-api
- collection_type: open
  name: Embedded Finance Auth Company Details API
  slug: open-wayflyer-company-details-api
- collection_type: open
  name: Embedded Finance Auth Company Search API
  slug: open-wayflyer-company-search-api
- collection_type: open
  name: Embedded Finance Auth CTA API
  slug: open-wayflyer-cta-api
- collection_type: open
  name: Embedded Finance Auth Data Upload API
  slug: open-wayflyer-data-upload-api
- collection_type: open
  name: Embedded Finance Auth Documents API
  slug: open-wayflyer-documents-api
- collection_type: open
  name: Embedded Finance Auth Embedded Application API
  slug: open-wayflyer-embedded-application-api
- collection_type: open
  name: Embedded Finance Auth Handover API
  slug: open-wayflyer-handover-api
- collection_type: open
  name: Embedded Finance Auth Industry Classification API
  slug: open-wayflyer-industry-classification-api
- collection_type: open
  name: Embedded Finance Auth Simulation API
  slug: open-wayflyer-simulation-api
- collection_type: open
  name: Embedded Finance Auth Tracked Login API
  slug: open-wayflyer-tracked-login-api
- collection_type: open
  name: Embedded Finance Auth User Details API
  slug: open-wayflyer-user-details-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wayflyer-embedded-finance-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://wayflyer.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wayflyer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wayflyer.com/embedded-journey-v5-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wayflyer.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wayflyer.com/embedded-journey-v5-overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/wayflyer-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.wayflyer.com/embedded-journey-v5-overview/shared/rate-limiting
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wayflyer-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/wayflyer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wayflyer-packages.yml
- group: design
  title: ''
  type: Components
  url: components/wayflyer-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wayflyer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wayflyer-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wayflyer-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wayflyer.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/wayflyer-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wayflyer-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wayflyer-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wayflyer-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wayflyer-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wayflyer-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://help-center.wayflyer.com/
- group: company
  title: ''
  type: Blog
  url: https://wayflyer.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wayflyer
- group: commercial
  title: ''
  type: Pricing
  url: https://wayflyer.com/how-our-financing-offers-work
- group: start
  title: ''
  type: SignUp
  url: https://app.wayflyer.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wayflyer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wayflyer.com/privacy-notice
- group: company
  title: ''
  type: PartnerProgram
  url: https://wayflyer.com/hosted-capital
created: '2026-07-17'
description: Wayflyer provides revenue-based financing and growth capital for e-commerce businesses, and exposes its funding products to software platforms through the Hosted Capital / Embedded Finance API. Partners upload anonymized merchant revenue data to generate personalised indicative offers, render a Wayflyer CTA banner in their own UI, and run the full funding application as an embedded (v5) or hosted (v4 legacy) journey — with JavaScript UI and headless SDKs on npm, a production-parity sandbox with application-state simulation, and OpenAPI 3.1 contracts published on a Kong Konnect developer portal at docs.wayflyer.com.
image: https://avatars.githubusercontent.com/u/56260407
layout: provider
mcp_servers:
- description: ''
  name: wayflyer-mcp.yml
  slug: wayflyer-mcpyml
modified: '2026-07-21'
name: Wayflyer
nav: Providers
network: true
overview: 'Wayflyer publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Company Details API, Company Search API, and 9 more. Tagged areas include Company, Ecommerce, Fintech, Embedded Finance, and Lending.


  Wayflyer''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 24 more developer resources.'
random_paper: 138
score:
  band: developing
  composite: 50.8
  delta: -1.5
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 56.3
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 52.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wayflyer/refs/heads/main/screenshots/wayflyer-2026-08-17T082841.png
security:
- kind: authentication
  name: Wayflyer Authentication
  slug: wayflyer-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Wayflyer Domain Security
  slug: wayflyer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wayflyer Trust Center
  slug: wayflyer-trust-center
  summary_line: trust center published
slug: wayflyer
tags:
- Company
- Ecommerce
- Fintech
- Embedded Finance
- Lending
- Revenue-Based Financing
- Financing
website: https://wayflyer.com
---
