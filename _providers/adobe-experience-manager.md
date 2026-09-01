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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Adobe Experience Manager Agentic Access
  operation_count: 14
  slug: adobe-experience-manager-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 1
apis:
- description: Collection of REST and GraphQL APIs for AEM as a Cloud Service covering Content Fragment delivery and management, Sites authoring, Dynamic Media asset delivery, Forms, and infrastructure. Authenticati
  name: Adobe Experience Manager APIs
  slug: apis
- description: AEM Launches for Content Fragments (experimental)
  name: Adobe Experience Manager Launches API
  slug: adobe-experience-manager-launches-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Experience Manager APIs Launches API
  slug: open-adobe-experience-manager-launches-api
- collection_type: open
  name: Adobe Experience Manager APIs
  slug: open-adobe-experience-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-experience-manager-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-experience-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-experience-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-experience-manager-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adobe-experience-manager-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aemsites
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/adobe-experience-manager
- group: company
  title: ''
  type: Website
  url: https://business.adobe.com/products/experience-manager/adobe-experience-manager.html
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/experience-manager/adobe-experience-manager.html
- group: start
  title: ''
  type: Signup
  url: https://business.adobe.com/request-consultation/experience-cloud.html
created: '2026-05-11'
description: Adobe Experience Manager (AEM) is an enterprise content management solution for building websites, mobile apps, and forms, combining a digital asset management system, content fragment authoring, and adaptive forms in a single platform delivered as a cloud service. AEM provides REST APIs, GraphQL endpoints, and Java/JavaScript SDKs for content delivery, authoring, asset management, and infrastructure operations. Authentication for AEM as a Cloud Service uses Adobe IMS OAuth 2.0 service tokens.
graphqls:
- description: Collection of REST and GraphQL APIs for AEM as a Cloud Service covering Content Fragment delivery and management, Sites authoring, Dynamic Media asset delivery, Forms, and infrastructure. Authenticati
  name: Adobe Experience Manager GraphQL API
  slug: adobe-experience-manager-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adobe-experience-manager.png
layout: provider
modified: '2026-05-11'
name: Adobe Experience Manager
nav: Providers
network: true
overview: 'Adobe Experience Manager publishes 1 API on the [APIs.io](https://apis.io/) network: Launches API. Tagged areas include Content Management, Enterprise CMS, Digital Asset Management, Headless CMS, and Content Fragments.


  Adobe Experience Manager''s developer surface includes authentication, documentation, pricing, signup flow, and 7 more developer resources.'
random_paper: 19
scopes:
- name: Adobe Experience Manager Scopes
  scope_count: 6
  slug: adobe-experience-manager-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 39.5
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-experience-manager/refs/heads/main/screenshots/adobe-experience-manager-2026-06-20T164924.png
security:
- kind: authentication
  name: Adobe Experience Manager Authentication
  slug: adobe-experience-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Adobe Experience Manager Domain Security
  slug: adobe-experience-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Experience Manager Vulnerability Disclosure
  slug: adobe-experience-manager-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-experience-manager
tags:
- Content Management
- Enterprise CMS
- Digital Asset Management
- Headless CMS
- Content Fragments
- Adaptive Forms
website: https://business.adobe.com/products/experience-manager/adobe-experience-manager.html
---
