---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Interfolio Agentic Access
  operation_count: 56
  slug: interfolio-agentic-access
  summary_line: 56 operations · 20 acting
api_count: 1
apis:
- description: REST and GraphQL APIs for the Interfolio Faculty Information System covering core Units, Faculty Search (Positions, Position Types/Status, Applications, Application Documents, Reports), and Review, Pr
  name: Interfolio Core, Search & RPT API
  slug: interfolio-core-search-rpt-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of Activities.
  name: Interfolio Activities API
  slug: interfolio-activities-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieves details regarding activity classifications.
  name: Interfolio Activity Classifications API
  slug: interfolio-activity-classifications-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: The Activity Input API from Interfolio — 2 operation(s) for activity input.
  name: Interfolio Activity Input API
  slug: interfolio-activity-input-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of Courses (Prefixes, Courses Taught, Attachments).
  name: Interfolio Courses API
  slug: interfolio-courses-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieves an attachment.
  name: Interfolio Download Attachments API
  slug: interfolio-download-attachments-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Email requests.
  name: Interfolio Emails API
  slug: interfolio-emails-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of users' evaluations.
  name: Interfolio Evaluations API
  slug: interfolio-evaluations-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of Faculty Classifications.
  name: Interfolio Faculty Classifications API
  slug: interfolio-faculty-classifications-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieves frequently asked questions.
  name: Interfolio FAQ API
  slug: interfolio-faq-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of users' permissions.
  name: Interfolio Permissions API
  slug: interfolio-permissions-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of Sections.
  name: Interfolio Sections API
  slug: interfolio-sections-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: The SSO API from Interfolio — 1 operation(s) for sso.
  name: Interfolio SSO API
  slug: interfolio-sso-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of academic terms.
  name: Interfolio Terms API
  slug: interfolio-terms-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Create & retrieve details of academic units.
  name: Interfolio Units API
  slug: interfolio-units-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieves a users activity information.
  name: Interfolio User Data API
  slug: interfolio-user-data-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Create, update and retreive details of users.
  name: Interfolio Users API
  slug: interfolio-users-api
- baseURL: https://faculty180.interfolio.com/api.php
  baseurl_source: declared
  description: Retrieve details of users' vitaes.
  name: Interfolio Vitas API
  slug: interfolio-vitas-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/interfolio/capabilities/interfolio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/interfolio-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/interfolio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/interfolio/overlays/interfolio-faculty180-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/interfolio-faculty180-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/interfolio/agentic-access/interfolio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/interfolio-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/interfolio/rules/interfolio-rules.yml
  title: ''
  type: Spectral
  url: rules/interfolio-rules.yml
- group: design
  href: https://artifacts.apis.io/interfolio/vocabulary/interfolio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/interfolio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/interfolio/data-model/interfolio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/interfolio-data-model.yml
- group: operate
  href: https://artifacts.apis.io/interfolio/lifecycle/interfolio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/interfolio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/interfolio/errors/interfolio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/interfolio-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/interfolio/well-known/interfolio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/interfolio-well-known.yml
- group: other
  href: https://artifacts.apis.io/interfolio/hosts/interfolio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/interfolio-hosts.yml
- group: build
  href: https://artifacts.apis.io/interfolio/integrations/interfolio-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/interfolio-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/interfolio/vendors/interfolio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/interfolio-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://product-help.interfolio.com/en_US/about-dossier-accounts/dossier-quick-start-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Interfolio
- group: company
  title: ''
  type: Website
  url: https://www.interfolio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.faculty180.com/api_docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.faculty180.com/api_docs
- group: docs
  title: ''
  type: APIReference
  url: https://faculty180.interfolio.com/swagger/ui/
- group: operate
  title: ''
  type: Support
  url: https://product-help.interfolio.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.interfolio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.interfolio.com/resources/
- group: start
  title: ''
  type: SignUp
  url: https://account.interfolio.com/login
- group: start
  title: ''
  type: Login
  url: https://account.interfolio.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elsevier.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elsevier.com/legal/elsevier-website-terms-and-conditions
- group: auth
  href: https://artifacts.apis.io/interfolio/authentication/interfolio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/interfolio-authentication.yml
- group: design
  href: https://artifacts.apis.io/interfolio/conventions/interfolio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/interfolio-conventions.yml
- group: design
  href: https://artifacts.apis.io/interfolio/conformance/interfolio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/interfolio-conformance.yml
- group: design
  href: https://artifacts.apis.io/interfolio/lifecycle/interfolio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/interfolio-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/interfolio/security/interfolio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/interfolio-domain-security.yml
created: '2026-07-17'
description: 'Interfolio is a Faculty Information System (now an Elsevier product) that helps colleges and universities manage the full faculty lifecycle: recruiting and hiring (Faculty Search), activity reporting and reviews (Faculty180 / Faculty Activity Reporting), review, promotion and tenure (RPT), lifecycle management, faculty web profiles, and the Dossier application service for individual academics. Interfolio exposes REST and GraphQL APIs for integrating faculty, activity, position, and review data with campus systems, secured with an HMAC public/private key mechanism scoped by tenant. Surfaced as a portfolio company of Insight Partners and enriched with real developer-surface artifacts.'
image: https://assets.interfolio.com/public/images/favicons/apple-touch-icon.png
layout: provider
modified: '2026-10-20'
name: Interfolio
nav: Providers
network: true
overview: 'Interfolio publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Activity Classifications API, Activity Input API, and 15 more. Tagged areas include Company, Education, Higher Education, Faculty Information System, and Faculty Activity Reporting.


  The Interfolio catalog on APIs.io includes 1 Spectral governance ruleset.


  Interfolio''s developer surface includes getting-started guide, documentation, API reference, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Interfolio Plans Pricing
  plan_count: 0
  slug: interfolio-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Interfolio Rate Limits
  slug: interfolio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Interfolio API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: interfolio-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 43.0
    developer_ergonomics: 53.0
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/interfolio/interfolio-2026-07-25T222701.png
security:
- kind: authentication
  name: Interfolio Authentication
  slug: interfolio-authentication
  summary_line: hmac · 2 schemes
- kind: domain-security
  name: Interfolio Domain Security
  slug: interfolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: faculty-activity-export
  slug: interfolio-faculty-activity-export
- name: manage-courses-taught
  slug: interfolio-manage-courses-taught
slug: interfolio
tags:
- Company
- Education
- Higher Education
- Faculty Information System
- Faculty Activity Reporting
- Review Promotion Tenure
- Academic
- Research
website: https://www.interfolio.com/
---
