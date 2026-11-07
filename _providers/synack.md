---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 75
  human_in_the_loop: 1
  name: Synack Agentic Access
  operation_count: 143
  slug: synack-agentic-access
  summary_line: 143 operations · 75 acting · 1 human-in-the-loop
api_count: 9
apis:
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Users assigned to an Assessment Group, with their roles.
  name: Synack Assessment Groups API
  slug: synack-assessment-groups-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Lifecycle state transitions for an individual assessment.
  name: Synack Assessment Lifecycle API
  slug: synack-assessment-lifecycle-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Assets are associated with listings.
  name: Synack Assessments API
  slug: synack-assessments-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Relationships between assets.
  name: Synack Asset Relationships API
  slug: synack-asset-relationships-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: The assetproviders API from Synack — 1 operation(s) for assetproviders.
  name: Synack Assetproviders API
  slug: synack-assetproviders-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Assets managed by Synack.
  name: Synack Assets API
  slug: synack-assets-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Operations related to comments
  name: Synack Comments API
  slug: synack-comments-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Credentials are restricted to authorized users.
  name: Synack Credentials API
  slug: synack-credentials-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: The external-relationships API from Synack — 2 operation(s) for external-relationships.
  name: Synack External Relationships API
  slug: synack-external-relationships-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: The health API from Synack — 1 operation(s) for health.
  name: Synack Health API
  slug: synack-health-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Host assets.
  name: Synack Hosts API
  slug: synack-hosts-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Access mission information.
  name: Synack Missions API
  slug: synack-missions-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Operations related to patch verifications
  name: Synack Patch Verifications API
  slug: synack-patch-verifications-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Collections of seeds associated with a listing.
  name: Synack Seeds API
  slug: synack-seeds-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Operations related to suspected vulnerabilities
  name: Synack Suspected Vulnerabilities API
  slug: synack-suspected-vulnerabilities-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Tags applied to seeds and seed groups.
  name: Synack Tags API
  slug: synack-tags-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Operations related to security tests
  name: Synack Tests API
  slug: synack-tests-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Users of credentials.
  name: Synack Users API
  slug: synack-users-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Operations related to security vulnerabilities
  name: Synack Vulnerabilities API
  slug: synack-vulnerabilities-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Operations related to vulnerability statuses
  name: Synack Vulnerability Statuses API
  slug: synack-vulnerability-statuses-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Mobile application assets.
  name: Synack Mobile Apps API
  slug: synack-mobile-apps-api
- baseURL: https://api.synack.com
  baseurl_source: declared
  description: Web application assets.
  name: Synack Web Apps API
  slug: synack-web-apps-api
artifact_total: 62
collections:
- collection_type: open
  name: Assessment Service Assessment Groups API
  slug: open-synack-assessment-groups-api
- collection_type: open
  name: Assessment Service Assessment Groups Assessment Lifecycle API
  slug: open-synack-assessment-lifecycle-api
- collection_type: open
  name: Assessment Service Assessment Groups Assessments API
  slug: open-synack-assessments-api
- collection_type: open
  name: Assessment Service Assessment Groups asset-relationships API
  slug: open-synack-asset-relationships-api
- collection_type: open
  name: Assessment Service Assessment Groups assetproviders API
  slug: open-synack-assetproviders-api
- collection_type: open
  name: Assessment Service Assessment Groups Assets API
  slug: open-synack-assets-api
- collection_type: open
  name: Assessment Service Assessment Groups cloudaccounts API
  slug: open-synack-cloudaccounts-api
- collection_type: open
  name: Assessment Service Assessment Groups Comments API
  slug: open-synack-comments-api
- collection_type: open
  name: Assessment Service Assessment Groups credentials API
  slug: open-synack-credentials-api
- collection_type: open
  name: Assessment Service Assessment Groups external-relationships API
  slug: open-synack-external-relationships-api
- collection_type: open
  name: Assessment Service Assessment Groups health API
  slug: open-synack-health-api
- collection_type: open
  name: Assessment Service Assessment Groups Hosts API
  slug: open-synack-hosts-api
- collection_type: open
  name: Assessment Service Assessment Groups Missions API
  slug: open-synack-missions-api
- collection_type: open
  name: Assessment Service Assessment Groups mobileapps API
  slug: open-synack-mobileapps-api
- collection_type: open
  name: Assessment Service Assessment Groups networks API
  slug: open-synack-networks-api
- collection_type: open
  name: Assessment Service Assessment Groups Patch Verifications API
  slug: open-synack-patch-verifications-api
- collection_type: open
  name: Assessment Service Assessment Groups ports API
  slug: open-synack-ports-api
- collection_type: open
  name: Assessment Service Assessment Groups scoperules API
  slug: open-synack-scoperules-api
- collection_type: open
  name: Assessment Service Assessment Groups scripts API
  slug: open-synack-scripts-api
- collection_type: open
  name: Assessment Service Assessment Groups Seeds API
  slug: open-synack-seeds-api
- collection_type: open
  name: Assessment Service Assessment Groups Suspected Vulnerabilities API
  slug: open-synack-suspected-vulnerabilities-api
- collection_type: open
  name: Assessment Service Assessment Groups Tags API
  slug: open-synack-tags-api
- collection_type: open
  name: Assessment Service Assessment Groups Tests API
  slug: open-synack-tests-api
- collection_type: open
  name: Assessment Service Assessment Groups userroles API
  slug: open-synack-userroles-api
- collection_type: open
  name: Assessment Service Assessment Groups users API
  slug: open-synack-users-api
- collection_type: open
  name: Assessment Service Assessment Groups Vulnerabilities API
  slug: open-synack-vulnerabilities-api
- collection_type: open
  name: Assessment Service Assessment Groups Vulnerability Statuses API
  slug: open-synack-vulnerability-statuses-api
- collection_type: open
  name: Assessment Service Assessment Groups webapps API
  slug: open-synack-webapps-api
common:
- group: commercial
  href: https://artifacts.apis.io/synack/plans/synack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synack-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.synack.com/feed/
- group: other
  href: https://artifacts.apis.io/synack/capabilities/synack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/synack-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/synack/overlays/synack-assessment-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/synack-assessment-v1-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synack.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.synack.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synack.com/
- group: auth
  href: https://artifacts.apis.io/synack/authentication/synack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/synack-authentication.yml
- group: auth
  href: https://artifacts.apis.io/synack/scopes/synack-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/synack-scopes.yml
- group: design
  href: https://artifacts.apis.io/synack/errors/synack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/synack-problem-types.yml
- group: design
  href: https://artifacts.apis.io/synack/conventions/synack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/synack-conventions.yml
- group: design
  href: https://artifacts.apis.io/synack/data-model/synack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/synack-data-model.yml
- group: design
  href: https://artifacts.apis.io/synack/lifecycle/synack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/synack-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/synack/conformance/synack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.synack.com/
- group: auth
  href: https://artifacts.apis.io/synack/security/synack-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/synack-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/synack/security/synack-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/synack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.synack.com/vdp/synack/
- group: auth
  href: https://artifacts.apis.io/synack/security/synack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synack-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/synack/mcp/synack-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/synack-mcp.yml
- group: agent
  href: https://artifacts.apis.io/synack/agentic-access/synack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/synack-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/synack/llms/synack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synack-llms.txt
- group: build
  href: https://artifacts.apis.io/synack/packages/synack-packages.yml
  title: ''
  type: Packages
  url: packages/synack-packages.yml
- group: agent
  href: https://artifacts.apis.io/synack/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synack
- group: company
  title: ''
  type: Blog
  url: https://www.synack.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synack.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://login.synack.com/
- group: start
  title: ''
  type: Login
  url: https://login.synack.com/
- group: operate
  title: ''
  type: Support
  url: https://www.synack.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synack.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synack.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.synack.com/
created: '2026-07-17'
description: Synack is a crowdsourced security testing platform that pairs the Synack Red Team — a global community of vetted security researchers — with AI-enabled attack-surface discovery to deliver continuous penetration testing, vulnerability management, and compliance-grade assessments. The Synack Enterprise API exposes assessments, assets, asset discovery (seed groups and seeds), vulnerabilities and suspected vulnerabilities, missions and campaigns, tagging, tests, users, and streaming analytics across nine REST services, secured with OAuth2 scopes and JWT bearer tokens.
finops:
- has_sources: true
  method: derived
  name: Synack Finops
  primary_unit: pentest
  service_category: ''
  slug: synack-finops
  template: false
image: https://www.synack.com/wp-content/uploads/2024/08/synack-meta-card-home-page-PTaaS-1.jpg
layout: provider
modified: '2026-10-06'
name: Synack
nav: Providers
network: true
overview: 'Synack publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assessment Groups API, Assessment Lifecycle API, Assessments API, and 19 more. Tagged areas include Company, Security, Penetration Testing, Vulnerability Management, and Attack Surface Management.


  The Synack catalog on APIs.io includes 1 Spectral governance ruleset.


  Synack''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Synack Plans Pricing
  plan_count: 4
  slug: synack-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Synack API Rules
  rule_count: 67
  severity_counts:
    error: 38
    hint: 0
    info: 8
    warn: 21
  slug: synack-rules
scopes:
- name: Synack Scopes
  scope_count: 21
  slug: synack-scopes
  summary_line: 21 scopes · implicit
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 13.2
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 68.2
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/synack/synack-2026-08-17T082224.png
security:
- kind: authentication
  name: Synack Authentication
  slug: synack-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Synack Domain Security
  slug: synack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Synack Vulnerability Disclosure
  slug: synack-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Synack Trust Center
  slug: synack-trust-center
  summary_line: ISO 27001:2022, FedRAMP Moderate, TX-RAMP Level 2, IASME Cyber Essentials, CREST, Privacy Shield
skill_count: 3
skills:
- name: Discover and inventory Synack assets
  slug: synack-discover-and-inventory-assets
- name: Manage Synack assessment lifecycle
  slug: synack-manage-assessment-lifecycle
- name: Triage Synack vulnerabilities
  slug: synack-triage-vulnerabilities
slug: synack
tags:
- Company
- Security
- Penetration Testing
- Vulnerability Management
- Attack Surface Management
- Crowdsourced Security
- Compliance
website: https://www.synack.com/
---
