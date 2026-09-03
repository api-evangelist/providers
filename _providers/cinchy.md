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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://cinchy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cinchy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cinchy.com/api-guide/
- group: operate
  title: ''
  type: Support
  url: https://support.cinchy.com
- group: company
  title: ''
  type: Blog
  url: https://cinchy.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cinchy-co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cinchy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cinchy.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.cinchy.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cinchy.com/category/release-notes/
- group: build
  title: ''
  type: Packages
  url: packages/cinchy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cinchy-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cinchy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cinchy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cinchy-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cinchy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cinchy-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cinchy-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/cinchy-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cinchy-domain-security.yml
created: '2026-07-17'
description: Cinchy is a data collaboration ("dataware") platform whose network-based data architecture lets enterprise applications share live, governed data without making copies or building point-to-point integrations. Its current focus, PeriMind, is an enterprise control plane for AI that secures, governs, and audits every interaction between AI agents and enterprise systems, data, and applications. Cinchy exposes a REST API for executing Cinchy Query Language (CQL), calling versioned saved queries, triggering data-sync jobs, and managing secrets, with authentication via bearer tokens, personal access tokens, HTTP Basic, and an embedded OAuth2/OIDC IdentityServer. Official Angular and JavaScript SDKs and embeddable app experiences are published on GitHub. Cinchy was surfaced as a Techstars portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cinchy.png
layout: provider
modified: '2026-07-18'
name: Cinchy
nav: Providers
network: true
overview: 'Cinchy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Collaboration, Dataware, and Data Integration.


  Cinchy''s developer surface includes documentation, API reference, support, engineering blog, changelog, authentication, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 20.7
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cinchy/refs/heads/main/screenshots/cinchy-2026-07-25T205348.png
security:
- kind: authentication
  name: Cinchy Authentication
  slug: cinchy-authentication
  summary_line: http/oauth2/apiKey · 4 schemes
- kind: domain-security
  name: Cinchy Domain Security
  slug: cinchy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cinchy Trust Center
  slug: cinchy-trust-center
  summary_line: trust center published
slug: cinchy
tags:
- Company
- Data
- Data Collaboration
- Dataware
- Data Integration
- Data Governance
- AI Governance
website: https://cinchy.com/
---
