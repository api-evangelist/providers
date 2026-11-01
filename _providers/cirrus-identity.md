---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cirrus Identity Agentic Access
  operation_count: 2
  slug: cirrus-identity-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://api.cirrusidentity.com/logs/v1
  baseurl_source: declared
  description: The endpoints API from Cirrus Identity — 2 operation(s) for endpoints.
  name: Cirrus Identity Endpoints API
  slug: cirrus-identity-endpoints-api
artifact_total: 8
collections:
- collection_type: open
  name: Cirrus Identity Log endpoints API
  slug: open-cirrus-identity-endpoints-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cirrusidentity.com/blog/rss.xml
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
  href: https://artifacts.apis.io/cirrus-identity/authentication/cirrus-identity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cirrus-identity-authentication.yml
- group: agent
  href: https://artifacts.apis.io/cirrus-identity/agentic-access/cirrus-identity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cirrus-identity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cirrus-identity/security/cirrus-identity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cirrus-identity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cirrus-identity/security/cirrus-identity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cirrus-identity-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/cirrus-identity/errors/cirrus-identity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cirrus-identity-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cirrus-identity/conventions/cirrus-identity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cirrus-identity-conventions.yml
- group: design
  href: https://artifacts.apis.io/cirrus-identity/data-model/cirrus-identity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cirrus-identity-data-model.yml
- group: other
  href: https://artifacts.apis.io/cirrus-identity/overlays/cirrus-identity-log-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cirrus-identity-log-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cirrus-identity/mcp/cirrus-identity-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cirrus-identity-mcp.yml
- group: design
  href: https://artifacts.apis.io/cirrus-identity/lifecycle/cirrus-identity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cirrus-identity-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cirrus-identity/conformance/cirrus-identity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cirrus-identity-conformance.yml
- group: design
  href: https://artifacts.apis.io/cirrus-identity/vocabulary/cirrus-identity-log-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cirrus-identity-log-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cirrus-identity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/cirrus-identity/packages/cirrus-identity-packages.yml
  title: ''
  type: Packages
  url: packages/cirrus-identity-packages.yml
- group: agent
  href: https://artifacts.apis.io/cirrus-identity/llms/cirrus-identity-llms.txt
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
modified: '2026-10-06'
name: Cirrus Identity
nav: Providers
network: true
overview: 'Cirrus Identity publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Endpoints API. Tagged areas include Company, Identity, Authentication, SSO, and SAML.


  Cirrus Identity''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
random_paper: 23
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 8.3
    contract_quality: 50.2
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 44.1
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
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cirrus-identity/cirrus-identity-2026-07-25T205419.png
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
skill_count: 1
skills:
- name: Export Cirrus Identity org logs
  slug: cirrus-identity-export-org-logs
slug: cirrus-identity
tags:
- Company
- Identity
- Authentication
- SSO
- SAML
- OpenID Connect
- Higher Education
- Identity and Access Management
- Federation
- Logs
- Identity Federation
website: https://cirrusidentity.com
---
