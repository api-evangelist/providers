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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Mendix Agentic Access
  operation_count: 20
  slug: mendix-agentic-access
  summary_line: 20 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: REST API for managing app projects, branches, revisions, and build packages in Mendix Team Server. Uses Mendix API key authentication.
  name: Mendix Build API
  slug: build-api
- description: REST API for managing apps, members, and repository metadata in the Mendix platform. Uses PAT or Mendix API key authentication.
  name: Mendix App Repository API
  slug: app-repository-api
- baseURL: https://deploy.mendix.com/api/1
  baseurl_source: declared
  description: The Apps API from Mendix — 2 operation(s) for apps.
  name: Mendix Apps API
  slug: mendix-apps-api
- baseURL: https://deploy.mendix.com/api/1
  baseurl_source: declared
  description: The Environments API from Mendix — 8 operation(s) for environments.
  name: Mendix Environments API
  slug: mendix-environments-api
- baseURL: https://deploy.mendix.com/api/1
  baseurl_source: declared
  description: The Logs API from Mendix — 2 operation(s) for logs.
  name: Mendix Logs API
  slug: mendix-logs-api
- baseURL: https://deploy.mendix.com/api/1
  baseurl_source: declared
  description: The Packages API from Mendix — 3 operation(s) for packages.
  name: Mendix Packages API
  slug: mendix-packages-api
- baseURL: https://deploy.mendix.com/api/1
  baseurl_source: declared
  description: The Tags API from Mendix — 1 operation(s) for tags.
  name: Mendix Tags API
  slug: mendix-tags-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mendix Deploy API v1 Apps API
  slug: open-mendix-apps-api
- collection_type: open
  name: Mendix Deploy API v1 Apps Environments API
  slug: open-mendix-environments-api
- collection_type: open
  name: Mendix Deploy API v1 Apps Logs API
  slug: open-mendix-logs-api
- collection_type: open
  name: Mendix Deploy API v1 Apps Packages API
  slug: open-mendix-packages-api
- collection_type: open
  name: Mendix Deploy API v1 Apps Tags API
  slug: open-mendix-tags-api
- collection_type: open
  name: Mendix Deploy API v1
  slug: open-mendix
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/well-known/mendix-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mendix-status-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/plans/mendix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mendix-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/rules/mendix-rules.yml
  title: ''
  type: Spectral
  url: rules/mendix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/json-ld/mendix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mendix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/vocabulary/mendix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mendix-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/data-model/mendix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mendix-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mendix.com/trust/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/errors/mendix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mendix-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/conformance/mendix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mendix-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/overlays/mendix-apps-api-overlay.yml
  title: ''
  type: Overlay
  url: overlays/mendix-apps-api-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/llms/mendix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mendix-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/well-known/mendix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mendix-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/well-known/mendix-mendix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mendix-mendix-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/well-known/mendix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mendix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/hosts/mendix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mendix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/vendors/mendix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mendix-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/packages/mendix-packages.yml
  title: ''
  type: SDKs
  url: packages/mendix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/packages/mendix-packages.yml
  title: ''
  type: Packages
  url: packages/mendix-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.mendix.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mendix.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.mendix.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mendix.com/
- group: start
  title: ''
  type: SignUp
  url: https://signup.mendix.com/link/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mendix.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.mendix.com/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mendix.com/releases/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mendix.com/apidocs-mxsdk/apidocs/deploy-api
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/agentic-access/mendix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mendix-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/security/mendix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mendix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/security/mendix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mendix-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/authentication/mendix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mendix-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mendix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mendix
- group: company
  title: ''
  type: Website
  url: https://www.mendix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mendix.com/apidocs-mxsdk/apidocs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mendix.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://signup.mendix.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://mendix.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.mendix.com/feed/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/capabilities/mendix-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mendix-capability-edges.yml
created: '2026-05-11'
description: Mendix, a Siemens company, is an enterprise low-code application development platform for designing, building, deploying, and operating multi-experience applications across web, mobile, and conversational interfaces. The platform spans Studio Pro modeling, the Mendix Cloud and private cloud runtimes, and governance and operational tooling for the full application lifecycle. Mendix exposes a suite of platform APIs (Deploy, Build, App Repository, User Management, Content, Studio Pro, and Apps APIs) secured by API keys or personal access tokens (PATs).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mendix.png
json_schemas:
- name: ConfigurationDeleteRequest
  property_count: 5
  slug: mendix-configuration-delete-request
- name: ConfigurationPatchRequest
  property_count: 20
  slug: mendix-configuration-patch-request
- name: EnvironmentCreateRequest
  property_count: 10
  slug: mendix-environment-create-request
jsonld:
- class_count: 7
  name: Mendix Context
  property_count: 60
  slug: mendix-context
layout: provider
modified: '2026-05-11'
name: Mendix
nav: Providers
network: true
overview: 'Mendix publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Environments API, Logs API, and 4 more. Tagged areas include Low-Code, Application Development, Enterprise Platform, Application Lifecycle, and Deployment.


  The Mendix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mendix''s developer surface includes support, signup flow, changelog, API reference, authentication, documentation, pricing, and 34 more developer resources.'
plans:
- name: Mendix Plans Pricing
  plan_count: 4
  slug: mendix-plans-pricing
random_paper: 7
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Mendix API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: mendix-rules
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.0
    catalog_earned_first_party: 12.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 28.4
  facets:
    access_clarity: 84.2
    contract_governance: 19.7
    contract_quality: 55.9
    developer_ergonomics: 44.6
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/mendix/refs/heads/main/screenshots/mendix-2026-06-20T185144.png
security:
- kind: authentication
  name: Mendix Authentication
  slug: mendix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mendix Domain Security
  slug: mendix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mendix Vulnerability Disclosure
  slug: mendix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mendix
tags:
- Low-Code
- Application Development
- Enterprise Platform
- Application Lifecycle
- Deployment
- Governance
website: https://www.mendix.com
---
