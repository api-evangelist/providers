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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Overleaf provides a private API for project management and integration, documented behind a login.
  name: Overleaf API
  slug: overleaf-api-2
- description: 'Overleaf API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Overleaf API
  slug: overleaf-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/overleaf/vendors/overleaf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/overleaf-vendors.yml
- group: design
  href: https://artifacts.apis.io/overleaf/rules/overleaf-rules.yml
  title: ''
  type: Spectral
  url: rules/overleaf-rules.yml
- group: design
  href: https://artifacts.apis.io/overleaf/json-ld/overleaf-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/overleaf-context.jsonld
- group: design
  href: https://artifacts.apis.io/overleaf/vocabulary/overleaf-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/overleaf-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/overleaf/data-model/overleaf-data-model.yml
  title: ''
  type: DataModel
  url: data-model/overleaf-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.overleaf.com/legal#Security
- group: auth
  href: https://artifacts.apis.io/overleaf/security/overleaf-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/overleaf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/overleaf/authentication/overleaf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/overleaf-authentication.yml
- group: design
  href: https://artifacts.apis.io/overleaf/conformance/overleaf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/overleaf-conformance.yml
- group: agent
  href: https://artifacts.apis.io/overleaf/llms/overleaf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/overleaf-llms.txt
- group: agent
  href: https://artifacts.apis.io/overleaf/well-known/overleaf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/overleaf-well-known.yml
- group: other
  href: https://artifacts.apis.io/overleaf/hosts/overleaf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/overleaf-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.overleaf.com/
- group: auth
  href: https://artifacts.apis.io/overleaf/security/overleaf-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/overleaf-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/overleaf/security/overleaf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/overleaf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/overleaf/security/overleaf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/overleaf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://overleaf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.overleaf.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.overleaf.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.overleaf.com/devs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.overleaf.com/learn
- group: company
  title: ''
  type: Blog
  url: https://www.overleaf.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overleaf
- group: commercial
  title: ''
  type: Pricing
  url: https://www.overleaf.com/user/subscription/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.overleaf.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.overleaf.com/legal
- group: start
  title: ''
  type: SignUp
  url: https://www.overleaf.com/register
coverage:
  checked: '2026-10-28'
  detail: API documentation is only accessible after logging in.
  evidence:
  - status: 200
    url: https://www.overleaf.com/devs
  reason: customer-only-docs
  state: gated
created: '2026-10-28'
description: Overleaf provides an online LaTeX editor that enables real-time collaboration, version control, and seamless project sharing. Used by millions of researchers, students, and professionals, it offers hundreds of templates, integrated reference management, and cloud-based compilation. The platform supports collaborative writing, academic publishing, and technical documentation without any installation.
image: https://cdn.overleaf.com/img/ol-brand/overleaf_og_logo.png
json_schemas:
- name: GetCitingAndReferencesCreatingABibliographyMdResponse
  property_count: 3
  slug: overleaf-get-citing-and-references-creating-abibliography-md-response
- name: GetGettingStartedHowDoIUseOverleafMdResponse
  property_count: 2
  slug: overleaf-get-getting-started-how-do-iuse-overleaf-md-response
- name: GetGroupsGettingStartedHowToCreateAGroupMdResponse
  property_count: 3
  slug: overleaf-get-groups-getting-started-how-to-create-agroup-md-response
- name: GetOnPremisesGettingStartedMicroservicesMdResponse
  property_count: 2
  slug: overleaf-get-on-premises-getting-started-microservices-md-response
- name: GetOnPremisesGettingStartedRequirementsMdResponse
  property_count: 3
  slug: overleaf-get-on-premises-getting-started-requirements-md-response
- name: GetOnPremisesGettingStartedRequirementsSkillsNeededMdRespons
  property_count: 2
  slug: overleaf-get-on-premises-getting-started-requirements-skills-needed-md-respons
jsonld:
- class_count: 8
  name: Overleaf Context
  property_count: 4
  slug: overleaf-context
layout: provider
modified: '2026-10-28'
name: Overleaf
nav: Providers
network: true
overview: 'Overleaf is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, LaTeX, Cloud, Academic, and Writing.


  The Overleaf catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Overleaf''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Overleaf Plans Pricing
  plan_count: 0
  slug: overleaf-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Overleaf Rate Limits
  slug: overleaf-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Overleaf API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: overleaf-rules
scopes:
- name: Overleaf Scopes
  scope_count: 0
  slug: overleaf-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 32.1
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 45.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/overleaf/overleaf-2026-11-03T140827.png
security:
- kind: authentication
  name: Overleaf Authentication
  slug: overleaf-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Overleaf Domain Security
  slug: overleaf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Overleaf Vulnerability Disclosure
  slug: overleaf-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Overleaf Trust Center
  slug: overleaf-trust-center
  summary_line: ISO 27001, GDPR
slug: overleaf
tags:
- Collaboration
- LaTeX
- Cloud
- Academic
- Writing
- Company
website: https://overleaf.com/
---
