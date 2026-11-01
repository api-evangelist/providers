---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 29
  human_in_the_loop: 4
  name: Getsmileapi Agentic Access
  operation_count: 92
  slug: getsmileapi-agentic-access
  summary_line: 92 operations · 29 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Accounts API from Smile — 5 operation(s) for accounts.
  name: Smile Accounts API
  slug: getsmileapi-accounts-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Archives API from Smile — 3 operation(s) for archives.
  name: Smile Archives API
  slug: getsmileapi-archives-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Blacklists (Alpha) API from Smile — 2 operation(s) for blacklists (alpha).
  name: Smile Blacklists (Alpha) API
  slug: getsmileapi-blacklists-alpha-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Consent Templates API from Smile — 2 operation(s) for consent templates.
  name: Smile Consent Templates API
  slug: getsmileapi-consent-templates-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Contributions API from Smile — 2 operation(s) for contributions.
  name: Smile Contributions API
  slug: getsmileapi-contributions-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Documents API from Smile — 2 operation(s) for documents.
  name: Smile Documents API
  slug: getsmileapi-documents-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Employments API from Smile — 2 operation(s) for employments.
  name: Smile Employments API
  slug: getsmileapi-employments-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Estimated Incomes API from Smile — 2 operation(s) for estimated incomes.
  name: Smile Estimated Incomes API
  slug: getsmileapi-estimated-incomes-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The File Types API from Smile — 1 operation(s) for file types.
  name: Smile File Types API
  slug: getsmileapi-file-types-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Footprints (Alpha) API from Smile — 2 operation(s) for footprints (alpha).
  name: Smile Footprints (Alpha) API
  slug: getsmileapi-footprints-alpha-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Forms (Alpha) API from Smile — 2 operation(s) for forms (alpha).
  name: Smile Forms (Alpha) API
  slug: getsmileapi-forms-alpha-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Identities API from Smile — 2 operation(s) for identities.
  name: Smile Identities API
  slug: getsmileapi-identities-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Income Estimators (Alpha) API from Smile — 2 operation(s) for income estimators (alpha).
  name: Smile Income Estimators (Alpha) API
  slug: getsmileapi-income-estimators-alpha-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Incomes API from Smile — 2 operation(s) for incomes.
  name: Smile Incomes API
  slug: getsmileapi-incomes-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Insights API from Smile — 2 operation(s) for insights.
  name: Smile Insights API
  slug: getsmileapi-insights-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Invite Templates API from Smile — 2 operation(s) for invite templates.
  name: Smile Invite Templates API
  slug: getsmileapi-invite-templates-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Invites API from Smile — 3 operation(s) for invites.
  name: Smile Invites API
  slug: getsmileapi-invites-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Liabilities API from Smile — 2 operation(s) for liabilities.
  name: Smile Liabilities API
  slug: getsmileapi-liabilities-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Links API from Smile — 2 operation(s) for links.
  name: Smile Links API
  slug: getsmileapi-links-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Maws (Alpha) API from Smile — 2 operation(s) for maws (alpha).
  name: Smile Maws (Alpha) API
  slug: getsmileapi-maws-alpha-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Maws (Beta) API from Smile — 4 operation(s) for maws (beta).
  name: Smile Maws (Beta) API
  slug: getsmileapi-maws-beta-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Providers API from Smile — 2 operation(s) for providers.
  name: Smile Providers API
  slug: getsmileapi-providers-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Ratings API from Smile — 2 operation(s) for ratings.
  name: Smile Ratings API
  slug: getsmileapi-ratings-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Signals (Alpha) API from Smile — 2 operation(s) for signals (alpha).
  name: Smile Signals (Alpha) API
  slug: getsmileapi-signals-alpha-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Signals (Beta) API from Smile — 4 operation(s) for signals (beta).
  name: Smile Signals (Beta) API
  slug: getsmileapi-signals-beta-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Social Securities (Beta) API from Smile — 2 operation(s) for social securities (beta).
  name: Smile Social Securities (Beta) API
  slug: getsmileapi-social-securities-beta-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Tasks API from Smile — 2 operation(s) for tasks.
  name: Smile Tasks API
  slug: getsmileapi-tasks-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Tokens API from Smile — 1 operation(s) for tokens.
  name: Smile Tokens API
  slug: getsmileapi-tokens-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Transactions API from Smile — 2 operation(s) for transactions.
  name: Smile Transactions API
  slug: getsmileapi-transactions-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Users API from Smile — 4 operation(s) for users.
  name: Smile Users API
  slug: getsmileapi-users-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Verification API from Smile — 2 operation(s) for verification.
  name: Smile Verification API
  slug: getsmileapi-verification-api
- baseURL: https://open.smileapi.io/v1
  baseurl_source: declared
  description: The Webhooks API from Smile — 2 operation(s) for webhooks.
  name: Smile Webhooks API
  slug: getsmileapi-webhooks-api
artifact_total: 47
asyncapis:
- description: ''
  name: Getsmileapi Webhooks
  slug: getsmileapi-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/getsmileapi/agentic-access/getsmileapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getsmileapi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/getsmileapi/rules/getsmileapi-rules.yml
  title: ''
  type: Spectral
  url: rules/getsmileapi-rules.yml
- group: design
  href: https://artifacts.apis.io/getsmileapi/json-ld/getsmileapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getsmileapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/getsmileapi/vocabulary/getsmileapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getsmileapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/getsmileapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/getsmileapi/asyncapi/getsmileapi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/getsmileapi-webhooks.yml
- group: design
  href: https://artifacts.apis.io/getsmileapi/data-model/getsmileapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getsmileapi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/getsmileapi/authentication/getsmileapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getsmileapi-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getsmileapi.com/
- group: design
  href: https://artifacts.apis.io/getsmileapi/lifecycle/getsmileapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getsmileapi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/getsmileapi/errors/getsmileapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getsmileapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getsmileapi/conformance/getsmileapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getsmileapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getsmileapi/llms/getsmileapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getsmileapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/getsmileapi/well-known/getsmileapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getsmileapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/getsmileapi/hosts/getsmileapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getsmileapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/getsmileapi/vendors/getsmileapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getsmileapi-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.getsmileapi.com/
- group: operate
  title: ''
  type: Support
  url: https://support.getsmileapi.com/portal/en/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SmileAPI
- group: operate
  title: ''
  type: ChangeLog
  url: https://roadmap.getsmileapi.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getsmileapi.com/docs/onboarding-faqs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getsmileapi.com/
- group: auth
  href: https://artifacts.apis.io/getsmileapi/security/getsmileapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getsmileapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getsmileapi.com/
created: '2026-10-20'
description: Smile API provides consent-driven employment and income verification services for credit decisioning, credit scoring, KYC, fraud prevention, and pre‑employment screening in the Philippines. It offers APIs for real‑time risk assessment, digital onboarding, document processing, and seamless integration with lending, financing, recruitment, and property rental platforms. The platform emphasizes data privacy, secure account linking, and AI‑powered document extraction to streamline verification workflows for financial institutions and enterprises.
image: https://cloud-1de12d.becdn.net/media/iW=1200&iH=630/3450f2162d2c4ca8573b24d0679dd68e.png
json_schemas:
- name: InvitePostRequest
  property_count: 6
  slug: getsmileapi-invite-post-request
- name: InviteTemplatePostRequest
  property_count: 5
  slug: getsmileapi-invite-template-post-request
- name: InviteTemplateUpdateRequest
  property_count: 5
  slug: getsmileapi-invite-template-update-request
- name: schemas-SocialSecurityPostRequest
  property_count: 7
  slug: getsmileapi-schemas-social-security-post-request
- name: VerificationCreateRequest
  property_count: 7
  slug: getsmileapi-verification-create-request
- name: WebhookPostRequest
  property_count: 6
  slug: getsmileapi-webhook-post-request
jsonld:
- class_count: 120
  name: Getsmileapi Context
  property_count: 247
  slug: getsmileapi-context
layout: provider
modified: '2026-10-20'
name: Smile
nav: Providers
network: true
overview: 'Smile publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Archives API, Blacklists (Alpha) API, and 29 more. Tagged areas include Company, Employment Verification, Credit Scoring, KYC, and Fraud Prevention.


  The Smile catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Smile''s developer surface includes authentication, support, changelog, getting-started guide, documentation, and 19 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Smile API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: getsmileapi-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 22.0
    contract_quality: 72.7
    developer_ergonomics: 39.9
    discoverability: 66.1
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - philippines
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 32
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getsmileapi Authentication
  slug: getsmileapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Getsmileapi Domain Security
  slug: getsmileapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: getsmileapi-create-and-view-user
  slug: getsmileapi-create-and-view-user
- name: getsmileapi-manage-consent-templates
  slug: getsmileapi-manage-consent-templates
- name: getsmileapi-manage-webhooks
  slug: getsmileapi-manage-webhooks
slug: getsmileapi
tags:
- Company
- Employment Verification
- Credit Scoring
- KYC
- Fraud Prevention
- Philippines
website: https://getsmileapi.com/
---
