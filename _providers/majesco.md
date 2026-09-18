---
access_model:
  confidence: high
  label: Enterprise · Contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Majesco Agentic Access
  operation_count: 12
  slug: majesco-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.majesco.example.com
  baseurl_source: declared
  description: Premium billing and payment operations
  name: majesco Billing API
  slug: majesco-billing-api
- baseURL: https://api.majesco.example.com
  baseurl_source: declared
  description: Claims intake and management
  name: majesco Claims API
  slug: majesco-claims-api
- baseURL: https://api.majesco.example.com
  baseurl_source: declared
  description: Quote and bind operations for distribution channels
  name: majesco Distribution API
  slug: majesco-distribution-api
- baseURL: https://api.majesco.example.com
  baseurl_source: declared
  description: Insurance policy lifecycle management
  name: majesco Policies API
  slug: majesco-policies-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Majesco Insurance Policy Administration Billing API
  slug: open-majesco-billing-api
- collection_type: open
  name: Majesco Insurance Policy Administration Billing Claims API
  slug: open-majesco-claims-api
- collection_type: open
  name: Majesco Insurance Policy Administration Billing Distribution API
  slug: open-majesco-distribution-api
- collection_type: open
  name: Majesco Insurance Policy Administration Billing Policies API
  slug: open-majesco-policies-api
- collection_type: open
  name: Majesco Insurance Policy Administration API
  slug: open-majesco-policy
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/agentic-access/majesco-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/majesco-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/security/majesco-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/majesco-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/security/majesco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/majesco-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/authentication/majesco-authentication.yml
  title: ''
  type: Authentication
  url: authentication/majesco-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/scopes/majesco-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/majesco-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/majesco
- group: start
  title: ''
  type: Portal
  url: https://www.majesco.com/
- group: company
  title: ''
  type: Website
  url: https://www.majesco.com/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/json-schema/majesco-policy-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/json-ld/majesco-context.jsonld
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/llms/majesco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/majesco-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/changelog/majesco-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/majesco-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/lifecycle/majesco-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/majesco-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/conformance/majesco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/majesco-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/security/majesco-trust-center.yml
  title: ''
  type: Compliance
  url: security/majesco-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/json-ld/majesco-ai-schema.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/majesco-ai-schema.jsonld
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.majesco.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.majesco.com/majesco-support/
- group: company
  title: ''
  type: Blog
  url: https://www.majesco.com/blog/
coverage:
  checked: '2026-09-17'
  detail: Majesco markets "thousands of APIs" through its APIM product but runs the gateway inside each carrier's own tenant, so there is no developer.majesco.com, api.majesco.com or docs.majesco.com (none of them resolve in DNS) and the API reference and release notes are delivered through the customer support portal at majescoprod.service-now.com/csm, which requires a signed-carrier login.
  evidence:
  - status: 200
    url: https://www.majesco.com/ecosystem-insurance-solutions/api-management/
  - status: 0
    url: https://developer.majesco.com/
  - status: 200
    url: https://support.majesco.com/
  - status: 200
    url: https://www.majesco.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2026-05-04'
description: Majesco is a global provider of cloud-native insurance software for Property & Casualty and Life, Annuity & Health carriers, serving 130+ insurers worldwide from its Morristown, New Jersey headquarters. Founded in 1989, it unifies Policy, Billing and Claims administration on a single platform alongside digital engagement, distribution, analytics and risk & compliance products, with GenAI (Majesco Copilot) and agentic AI embedded across the core suites. Its ClaimVantage line covers L&H claims, disability and absence management. Majesco sells API Management (APIM) as a component of those suites rather than as a public developer program, so its API surface is provisioned per carrier tenant and is not publicly documented.
finops:
- name: Majesco Finops
  service_category: API
  slug: majesco-finops
graphqls:
- description: Majesco provides cloud insurance software. The API covers policy administration, billing, claims, underwriting, agency management, product configuration, and analytics for life, annuity, P&C, and grou
  name: Majesco GraphQL API
  slug: majesco-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/majesco.png
json_schemas:
- name: Majesco Insurance Policy
  property_count: 14
  slug: majesco-policy
jsonld:
- class_count: 0
  name: Majesco Ai Schema Context
  property_count: 0
  slug: majesco-ai-schema
- class_count: 24
  name: Majesco Context
  property_count: 11
  slug: majesco-context
layout: provider
modified: '2026-09-17'
name: Majesco
nav: Providers
network: true
overview: 'Majesco publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Claims API, Distribution API, and 1 more. Tagged areas include Insurance, Insurtech, Policy Administration, Claims, and Billing.


  The Majesco catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Majesco''s developer surface includes authentication, developer portal, changelog, support, engineering blog, and 14 more developer resources.'
plans:
- name: Majesco Plans Pricing
  plan_count: 0
  slug: majesco-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Majesco Rate Limits
  slug: majesco-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Majesco API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: majesco-jsonschema-spectral-rules
scopes:
- name: Majesco Scopes
  scope_count: 2
  slug: majesco-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.6
  facets:
    access_clarity: 34.2
    contract_governance: 28.0
    contract_quality: 67.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    operational_transparency: 15.8
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 65.2
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/screenshots/majesco-2026-06-20T184906.png
security:
- kind: authentication
  name: Majesco Authentication
  slug: majesco-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Majesco Domain Security
  slug: majesco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Majesco Trust Center
  slug: majesco-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: majesco
tags:
- Insurance
- Insurtech
- Policy Administration
- Claims
- Billing
- Underwriting
- Life and Annuity
- Property and Casualty
- Absence Management
- Enterprise Software
website: https://www.majesco.com/
---
