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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cirrus Identity Agentic Access
  operation_count: 2
  slug: cirrus-identity-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The endpoints API from Cirrus Identity — 2 operation(s) for endpoints.
  name: Cirrus Identity endpoints API
  slug: cirrus-identity-endpoints-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cirrus Identity Log endpoints API
  slug: open-cirrus-identity-endpoints-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cirrusidentity.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://cirrusidentity.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.cirrusidentity.com/logs/v1/docs
- group: company
  title: ''
  type: Blog
  url: https://www.cirrusidentity.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.cirrusidentity.com/resources/support-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cirrusidentity
- group: start
  title: ''
  type: Login
  url: https://apps.cirrusidentity.com/console/auth/index
- group: start
  title: ''
  type: SignUp
  url: https://www.cirrusidentity.com/talk-to-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cirrusidentity.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cirrusidentity.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.cirrusidentity.com/resources/trust-and-compliance-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.cirrusidentity.com/resources/trust-and-compliance-center
- group: auth
  title: ''
  type: Security
  url: https://www.cirrusidentity.com/resources/trust-and-compliance-center
- group: auth
  title: ''
  type: Authentication
  url: authentication/cirrus-identity-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cirrus-identity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cirrus-identity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cirrus-identity-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cirrus-identity-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cirrus-identity-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cirrus-identity-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cirrus-identity-log-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cirrus-identity-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cirrus-identity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cirrus-identity-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cirrus-identity-log-vocabulary.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/cirrus-identity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cirrus-identity-llms.txt
- group: company
  title: ''
  type: Website
  url: https://cirrusidentity.com
created: '2026-07-17'
description: Cirrus Identity provides managed identity and access management for higher education, connecting modern identity providers, federations, and legacy systems to standardize authentication across campus environments without replacing existing infrastructure. Its products include Cirrus Bridge (multilateral SAML & CAS for Entra ID, Okta, and Duo SSO), External User Sign-In, Trusted Federation & Affiliates Sign-In, a Slate applicant sign-in extension, and an Admin Console with event logs. Cirrus also publishes a REST Log API for programmatically retrieving authentication and service event logs, and maintains a suite of open-source SimpleSAMLphp modules on GitHub and Packagist.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cirrus-identity.png
layout: provider
mcp_servers:
- description: ''
  name: Cirrus Identity MCP Server
  slug: cirrus-identity-mcp-server
modified: '2026-07-18'
name: Cirrus Identity
nav: Providers
network: true
overview: 'Cirrus Identity publishes 1 API on the [APIs.io](https://apis.io/) network: endpoints API. Tagged areas include Company, Identity, Authentication, Single Sign-On, and SAML.


  Cirrus Identity''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 23 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 76.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 8.3
    contract_quality: 55.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 13.2
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cirrus-identity/refs/heads/main/screenshots/cirrus-identity-2026-07-25T205419.png
security:
- kind: authentication
  name: Cirrus Identity Authentication
  slug: cirrus-identity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cirrus Identity Domain Security
  slug: cirrus-identity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cirrus Identity Vulnerability Disclosure
  slug: cirrus-identity-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cirrus Identity Trust Center
  slug: cirrus-identity-trust-center
  summary_line: SOC 2 Type 2, TX-RAMP Level 1
slug: cirrus-identity
tags:
- Company
- Identity
- Authentication
- Single Sign-On
- SAML
- OIDC
- Higher Education
- Identity Management
- Federation
- Logs
website: https://cirrusidentity.com
---
